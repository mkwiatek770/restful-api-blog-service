from rest_framework import serializers
from mturk_manager.models import Worker


class SerializerWorker(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = (
            "id_worker",
            "global_block",
        )
