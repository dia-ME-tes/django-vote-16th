from rest_framework import serializers
from .models import Department, Team, Vote, Profile, Candidate
from django.contrib.auth import get_user_model

User = get_user_model()


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department  # 사용할 모델
        fields = ['id', 'name']  # 사용할 모델 필드


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team  # 사용할 모델
        fields = ['id', 'name', 'score']  # 사용할 모델 필드


class VoteSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    department_id = serializers.IntegerField(write_only=True, allow_null=True)
    team_id = serializers.IntegerField(write_only=True, allow_null=True)
    candidate_id = serializers.IntegerField(write_only=True, allow_null=True)

    class Meta:
        model = Vote  # 사용할 모델
        fields = ['user_id', 'department_id', 'team_id', 'candidate_id']  # 사용할 모델 필드


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile  # 사용할 모델
        fields = ['user_id', 'department', 'team', 'name']  # 사용할 모델 필드

    def save(self, validated_data):
        email = validated_data.get('email')
        name = validated_data.get('name')
        department_id = validated_data.get('department')
        team_id = validated_data.get('team')

        user_id = User.objects.get(email=email).id

        profile = Profile(
            user_id=user_id,
            name=name,
            department_id=department_id,
            team_id=team_id
        )
        profile.save()
        return profile


class CandidateSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()

    def get_department(self, obj):
        return obj.department.name

    def get_team(self, obj):
        return obj.team.name

    class Meta:
        model = Candidate  # 사용할 모델
        fields = ('id', 'department_id', 'department', 'team_id', 'team', 'name', 'score')
