from rest_framework import serializers
from mturk_manager.models import SettingsBatch
from mturk_manager.serializers import (
    SerializerTemplateWorker,
    SerializerKeyword,
    SerializerQualification,
    SerializerMessageReject,
)


class SerializerSettingsBatch(serializers.ModelSerializer):

    template_worker = SerializerTemplateWorker()
    keywords = SerializerKeyword(many=True)
    qualifications = SerializerQualification(many=True)
    message_reject = SerializerMessageReject()

    class Meta:
        model = SettingsBatch
        fields = (
            "name",
            "title",
            "description",
            "reward",
            "count_assignments",
            "count_assignments_max_per_worker",
            "lifetime",
            "duration",
            "amount_budget_max",
            "template_worker",
            "keywords",
            "qualifications",
            "message_reject",
        )
