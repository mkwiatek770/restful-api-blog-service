from rest_framework import serializers
from mturk_manager.models import Batch
from mturk_manager.serializers import SerializerProject


class SerializerBatch(serializers.ModelSerializer):

    project = SerializerProject()

    class Meta:
        model = Batch
        fields = (
            "project",
            "name",
            "use_sandbox",
            "datetime_created",
        )
