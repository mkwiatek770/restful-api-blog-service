from rest_framework import serializers
from mturk_manager.models import HIT
from mturk_manager.serializers import SerializerBatch


class SerializerHIT(serializers.ModelSerializer):

    batch = SerializerBatch()

    class Meta:
        model = HIT
        fields = (
            "id_hit",
            "batch",
            "datetime_created",
            "datetime_expiration",
            "status",
            "count_assignments_additional",
            "count_assignments_dead"
        )
