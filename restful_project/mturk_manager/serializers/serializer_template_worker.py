from rest_framework import serializers
from mturk_manager.models import Batch


class SerializerBatch(serializers.ModelSerializer):

    class Meta:
        model = Batch
        fields = (
            "height_frame",
            "content",
            "json_dict_parameters",
        )
