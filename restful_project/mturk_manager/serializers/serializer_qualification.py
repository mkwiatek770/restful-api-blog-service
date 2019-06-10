from rest_framework import serializers
from mturk_manager.models import Qualification, Keyword
from mturk_manager.serializers import SerializerKeyword


class SerializerQualification(serializers.ModelSerializer):

    # keywords = SerializerKeyword(many=True)
    keywords = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Keyword.objects.all())

    class Meta:
        model = Qualification
        fields = (
            "url",
            "name",
            "keywords",
            "description",
            "test",
            "answer_key",
        )
