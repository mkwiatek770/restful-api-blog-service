from rest_framework import serializers
from mturk_manager.models import MessageReject


class SerializerMessageReject(serializers.ModelSerializer):

    class Meta:
        model = MessageReject
        fields = (
            "name",
            "message",
        )
