from rest_framework import serializers
from mturk_manger.models import Qualification
from mturk_manager.serializers import SerializerKeyword


class SerializerQualification(serializers.ModelSerializer):

    keywords = SerializerKeyword()

    class Meta:
        model = Qualification
        fields = (
            "name",
            "keywords",
            "description",
            "test",
            "answer_key",
        )
