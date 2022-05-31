from rest_framework  import serializers
from .models import InterestBadge,InterestGroup,Experience,Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class InterestGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestGroup
        fields = '__all__'


class InterestBadgeSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField()
    class Meta:
        model = InterestBadge
        fields = ['id','name','description','description_link','is_active','group',]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
