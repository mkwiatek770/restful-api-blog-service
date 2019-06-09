from mturk_manager.serializers import SerializerHIT, SerializerWorker
from mturk_manager.models import Assignment
from rest_framework import serializers


class SerializerAssignment(serializers.ModelSerializer):
    """
    Serializer for Assignment model
    """
    hit = SerializerHIT()
    worker = SerializerWorker()

    class Meta:
        model = Assignment
        fields = (
            "id_assignment",
            "hit",
            "worker",
            "status",
            "datetime_created",
            "datetime_submit",
            "datetime_accept",
            "answer"
        )
