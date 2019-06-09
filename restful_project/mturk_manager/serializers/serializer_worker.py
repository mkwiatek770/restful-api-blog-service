from rest_framework import serializers
from mturk_manager.models import Worker
from mturk_manager.serializers import SerializerProject


class SerializerWorker(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = (
            "id_worker",
            "global_block",
        )
