import mimetypes
import os

from django.core.mail import EmailMultiAlternatives
from rest_framework import serializers

from configs.app_settings import EMAIL_MAIN_RECIPIENT


class EmailMessageClass:
    subject: str
    message: str
    sender: str
    cv: str
    cc: str

    def __init__(self, subject: str, message: str, sender: str, cc: str, *args, **kwargs):
        self.subject = subject
        self.message = message
        self.sender = sender
        self.cv = kwargs.get('cv', None)
        self.cc = cc


class MailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=100)
    message = serializers.CharField()
    sender = serializers.EmailField()
    cv = serializers.CharField(required=False, allow_blank=True)
    cc = serializers.CharField()

    def create(self, validated_data):
        email = EmailMessageClass(**validated_data)

        message = EmailMultiAlternatives(
            subject=email.subject,
            body=email.message,
            from_email=email.sender,
            to=[EMAIL_MAIN_RECIPIENT],
            cc=email.cc.split(','),
            reply_to=[email.sender]
        )
        message.attach_alternative(email.message, "text/html")

        if email.cv:    # TODO: verify that this is the proper check
            # Open the file in binary mode
            file_path = ('.' + email.cv)
            with open(file_path, 'rb') as f:
                file_content = f.read()

                # Extract the filename from the file path
                file_name = os.path.basename(file_path)

                # Guess the MIME type of the file (fallback to application/octet-stream)
                mime_type, _ = mimetypes.guess_type(file_path)
                if mime_type is None:
                    mime_type = 'application/octet-stream'

                message.attach(file_name, file_content, mime_type)

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
