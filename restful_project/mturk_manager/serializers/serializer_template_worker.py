from rest_framework import serializers
from mturk_manager.models import TemplateWorker


class SerializerTemplateWorker(serializers.ModelSerializer):

    class Meta:
        model = TemplateWorker
        fields = (
            "height_frame",
            "content",
            "json_dict_parameters",
        )
