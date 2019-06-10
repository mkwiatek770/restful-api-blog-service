from rest_framework.viewsets import ModelViewSet
from mturk_manager.models import HIT
from mturk_manager.serializers import SerializerHIT


class HITs(ModelViewSet):
    queryset = HIT.objects.all()
    serializer_class = SerializerHIT
