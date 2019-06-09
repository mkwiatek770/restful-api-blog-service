from rest_framework import serializers
from mturk_manager.models import AccountMturk


class SerializerAccountMturk(serializers.ModelSerializer):
    class Meta:
        model = AccountMturk
        fields = (
            "name",
            "key_access",
            "key_secret",
        )
