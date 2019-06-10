from rest_framework import serializers
from mturk_manager.models import Keyword


class SerializerKeyword(serializers.ModelSerializer):

    class Meta:
        model = Keyword
        fields = ("url", "name")
