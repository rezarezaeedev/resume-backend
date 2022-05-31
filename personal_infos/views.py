from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import PersonalInfo
from .serializers import PersonalInfoSerializer


class PersonalInfoViews(viewsets.ViewSet):
    def list(self, request, pk=0):
        if pk==0:
            queryset = PersonalInfo.objects.filter(is_active=1).last()
        else:
            queryset = PersonalInfo.objects.filter(is_active=1, pk=pk)
            if queryset.exists():
                queryset = queryset.first()
            else:
                return Response({'message':'Not found data!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PersonalInfoSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

