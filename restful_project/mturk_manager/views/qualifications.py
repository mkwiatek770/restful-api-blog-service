from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from mturk_manager.models import Qualification
from mturk_manager.serializers import SerializerQualification


class Qualifications(ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = SerializerQualification
