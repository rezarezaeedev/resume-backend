from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import InterestBadge,InterestGroup,Experience,Skill
from .serializers import ExperienceSerializer,SkillSerializer,InterestBadgeSerializer,InterestGroupSerializer


class SkillView(viewsets.ViewSet):
    def list(self, request):
        queryset = Skill.objects.filter(is_active=True)
        serializer = SkillSerializer(queryset, many=True)
        return Response(serializer.data)


class ExperienceView(viewsets.ViewSet):
    lookup_field = 'badge'

    def retrieve(self, request ,badge):
        queryset = Experience.objects.filter(is_active=True)
        serializer = ExperienceSerializer(queryset, many=True)
        return Response(serializer.data)


class InterestBadgeView(viewsets.ViewSet):
    lookup_field = 'groupid'

    def retrieve(self, request ,groupid):
        group = InterestGroup.objects.filter(is_active=True, id=groupid)
        if group.exists():
            group= group.first()
            queryset_badge = InterestBadge.objects.filter(is_active=1, group=group)
            serializer = InterestBadgeSerializer(queryset_badge, many=1)
            return Response(serializer.data ,status=status.HTTP_200_OK)
        return Response({'message':'Not found data!'} ,status=status.HTTP_404_NOT_FOUND)


class InterestGroupView(viewsets.ViewSet):
    def list(self, request ):
        queryset = InterestGroup.objects.filter(is_active=True)
        serializer = InterestGroupSerializer(queryset, many=True)

        return Response(serializer.data)
