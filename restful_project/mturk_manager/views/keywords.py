from rest_framework.viewsets import ModelViewSet
from mturk_manager.models import Keyword
from mturk_manager.serializers import SerializerKeyword


class Keywords(ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = SerializerKeyword
