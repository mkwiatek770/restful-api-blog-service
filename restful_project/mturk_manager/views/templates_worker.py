from rest_framework.viewsets import ModelViewSet
from mturk_manager.models import TemplateWorker
from mturk_manager.serializers import SerializerTemplateWorker


class TemplatesWorker(ModelViewSet):
    queryset = TemplateWorker.objects.all()
    serializer_class = SerializerTemplateWorker
