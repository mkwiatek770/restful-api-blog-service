from rest_framework import serializers
from mturk_manager.models import Project
from mturk_manager.serializers import (
    SerializerAccountMturk,
    SerializerSettingsBatch,
    SerializerWorker
)


class SerializerProject(serializers.ModelSerializer):

    account_mturk = SerializerAccountMturk()
    settings_batch = SerializerSettingsBatch()
    blocked_workers = SerializerWorker(many=True)

    class Meta:
        model = Project
        fields = (
            "version",
            "name",
            "slug",
            "account_mturk",
            "datetime_visited",
            "datetime_created",
            "settings_batch",
            "blocked_workers",
        )
