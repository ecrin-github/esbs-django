from django.core.mail import EmailMultiAlternatives
from rest_framework import serializers


class EmailMessageClass:
    subject: str
    message: str
    recipients: str
    sender: str
    cc: str

    def __init__(self, subject: str, message: str, recipients: str, sender: str, cc: str):
        self.subject = subject
        self.message = message
        self.recipients = recipients
        self.sender = sender
        self.cc = cc


class MailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=100)
    message = serializers.CharField()
    recipients = serializers.CharField()
    sender = serializers.EmailField()
    cc = serializers.EmailField()

    def create(self, validated_data):
        email = EmailMessageClass(**validated_data)

        message = EmailMultiAlternatives(
            subject=email.subject,
            body=email.message,
            from_email=email.sender,
            to=email.recipients.split(','),
            cc=[email.cc],
            reply_to=[email.sender]
        )
        message.attach_alternative(email.message, "text/html")

        message.send()

        return email

    def update(self, instance, validated_data):
        instance.subject = validated_data.get('subject', instance.subject)
        instance.message = validated_data.get('message', instance.message)
        instance.recipients = validated_data.get('recipients', instance.recipients)
        instance.sender = validated_data.get('sender', instance.sender)
        instance.cc = validated_data.get('cc', instance.cc)

        message = EmailMultiAlternatives(
            subject=instance.subject,
            body=instance.message,
            from_email=instance.sender,
            to=instance.recipients.split(','),
            cc=[instance.cc],
            reply_to=[instance.sender]
        )

        message.send()

        return instance
