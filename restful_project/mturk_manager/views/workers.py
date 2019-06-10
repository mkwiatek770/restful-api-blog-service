from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from mturk_manager.models import Worker
from mturk_manager.serializers import SerializerWorker


# class Workers(APIView):

#     def get(self, request, format=None):
#         queryset = Worker.objects.all()
#         serializer = SerializerWorker(queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SerializerWorker(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Workers(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = SerializerWorker
