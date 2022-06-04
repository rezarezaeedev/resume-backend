from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import InterestBadge,InterestGroup,Experience,Skill
from .serializers import ExperienceSerializer,SkillSerializer,InterestBadgeSerializer,InterestGroupSerializer


class SkillView(viewsets.ViewSet):
    lookup_field='badge'
    def list(self, request):
        queryset = Skill.objects.filter(is_active=True).order_by('order')
        serializer = SkillSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK )

    def retrieve(self, request, badge):
        if badge=='skills':
            familiarity_flag=False
        elif badge=='familiarities':
            familiarity_flag=True
        else:
            return Response({'message':f'Not found any data for {badge} type skill. please retrieve by "skills" and "familiarities".'}, status=status.HTTP_404_NOT_FOUND)
        queryset = Skill.objects.filter(is_active=True, is_familiarity=familiarity_flag).order_by('order')
        serializer = SkillSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExperienceView(viewsets.ViewSet):
    def list(self, request):
        queryset = Experience.objects.filter(is_active=True).order_by('order')
        serializer = ExperienceSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InterestBadgeView(viewsets.ViewSet):
    lookup_field = 'groupid'

    def retrieve(self, request ,groupid):
        group = InterestGroup.objects.filter(is_active=True, id=groupid)
        if group.exists():
            group= group.first()
            queryset_badge = InterestBadge.objects.filter(is_active=1, group=group).order_by('order')
            serializer = InterestBadgeSerializer(queryset_badge, many=1)
            return Response(serializer.data ,status=status.HTTP_200_OK)
        return Response({'message':'Not found data!'} ,status=status.HTTP_404_NOT_FOUND)


class InterestGroupView(viewsets.ViewSet):
    def list(self, request ):
        queryset = InterestGroup.objects.filter(is_active=True).order_by('order')
        serializer = InterestGroupSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
