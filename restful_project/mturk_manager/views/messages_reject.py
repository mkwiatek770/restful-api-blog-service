from rest_framework.viewsets import ModelViewSet
from mturk_manager.models import MessageReject
from mturk_manager.serializers import SerializerMessageReject


class MessagesReject(ModelViewSet):
    queryset = MessageReject.objects.all()
    serializer_class = SerializerMessageReject
