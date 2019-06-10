from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from mturk_manager.serializers import SerializerAccountMturk
from mturk_manager.models import AccountMturk


# class Accounts(APIView):

#     def get(self, request, format=None):
#         queryset = AccountMturk.objects.all()
#         serializer = SerializerAccountMturk(
#             queryset,
#             many=True
#         )

#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SerializerAccountMturk(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class AccountsDetail(APIView):

#     def get(self, request, name, format=None):
#         account = AccountMturk.objects.filter(name=name)
#         if account:
#             serializer = SerializerAccountMturk(account[0])
#             return Response(serializer.data)
#         return Response(status=status.HTTP_404_NOT_FOUND)


class Accounts(ModelViewSet):
    queryset = AccountMturk.objects.all()
    serializer_class = SerializerAccountMturk
