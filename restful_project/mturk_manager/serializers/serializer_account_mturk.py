from rest_framework import serializers
from mturk_manager.models import AccountMturk


class SerializerAccountMturk(serializers.HyperlinkedModelSerializer):

    # url = serializers.HyperlinkedIdentityField(
    #     view_name="Accounts.retrieve", read_only=True)
    # TODO w przyszłości zmienić link żeby nie było /accounts/<id>/ tylko żeby zamiast id było użytę pole name

    class Meta:
        model = AccountMturk
        fields = (
            "url",
            "name",
            "key_access",
            "key_secret",
        )
