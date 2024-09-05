import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from django.db.models import F
from users.models import Users, Notifications

import logging
LOGGER = logging.getLogger('django')


# Note: both of these methods are run synchronously because the site doesn't have a lot of traffic
def update_user_incr(uuid):
    Users.objects.filter(id=uuid).update(online=F('online') + 1)

def update_user_decr(uuid):
    Users.objects.filter(id=uuid).update(online=F('online') - 1)


class PushNotificationsConsumer(WebsocketConsumer):
    def send_stored_messages(self):
        LOGGER.debug("NOTIFICATIONS - send_stored_messages")

        notifications = Notifications.objects.filter(user=self.id)
        for notif in notifications:
            self.send_notification({"id": notif.id, "time": notif.datetime.timestamp(), "message": notif.message})

    def connect(self):
        if "error" in self.scope and self.scope["error"]:
            LOGGER.debug("NOTIFICATIONS - connect - error")

            self.accept()
            self.send(text_data=json.dumps({'error': str(self.scope['error'])}))
            self.close()
        else:
            LOGGER.debug("NOTIFICATIONS - connect - no error")

            self.id = self.scope['user_id']
            self.group_name = f"push_notifications_{self.id}"
            async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

            # Need to communicate on token subprotocol for Chromium browsers to accept connection
            self.accept(self.scope["token"])
            
            # Logging number of connections for a user
            update_user_incr(self.id)
            
            # Checking and sending stored messages (if any)
            self.send_stored_messages()
            LOGGER.debug("NOTIFICATIONS - connect - after send stored messages")

    def disconnect(self, close_code):
        LOGGER.debug("NOTIFICATIONS - disconnect")

        # Leave group
        update_user_decr(self.id)
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)
        self.close()

    # Receive message from WebSocket
    def receive(self, text_data):
        LOGGER.debug("NOTIFICATIONS - receive")

        # Receiving the confirmation that the stored notification was delivered, deleting it from the DB
        data = json.loads(text_data)
        if "consumed" in data and "id" in data:
            Notifications.objects.filter(id=data["id"]).delete()

    # Receive message from group
    def send_notification(self, event):
        LOGGER.debug(f"NOTIFICATIONS - send_notification: {event['time']} {event['message']}")

        # Send message to WebSocket
        self.send(text_data=json.dumps({"id": str(event["id"]) if "id" in event else None,
                                        "time": event["time"],
                                        "message": event["message"]}))
