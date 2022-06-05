from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import PersonalInfo,SiteSettings
from .serializers import PersonalInfoSerializer,SiteSettingsSerializer


class PersonalInfoViews(viewsets.ViewSet):
    def list(self, request):
        queryset = PersonalInfo.objects.filter(is_active=1)
        if queryset.exists():
            queryset=queryset.last()
            serializer = PersonalInfoSerializer(queryset, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message':'Not found data!'}, status=status.HTTP_404_NOT_FOUND)


class SiteSettingsViews(viewsets.ViewSet):
    def list(self, request):
        queryset = SiteSettings.objects.filter(is_active=1).last()
        if queryset:
            serializer = SiteSettingsSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Not found data!'}, status=status.HTTP_404_NOT_FOUND)




