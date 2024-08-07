import json

from channels.generic.websocket import AsyncWebsocketConsumer


class PushNotificationsConsumer(AsyncWebsocketConsumer):
    group_name = "push_notifications"

    async def connect(self):
        # Join group
        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["display_title"]

        # Send message to group
        await self.channel_layer.group_send(
            self.group_name, {"type": "send.notification", "message": "The following Data object has been updated "
                                                                      "on the TSD side: " + message}
        )

    # Receive message from group
    async def send_notification(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
