from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Candidate, Team
from .serializers import CandidateSerializer, TeamSerializer


class CandidateListView(APIView):
    def get(self, request):
        try:
            if request.data['method'] == 0:  # 후보
                candidates = Candidate.objects.all()
                serializer = CandidateSerializer(candidates, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif request.data['method'] == 1:  # 결과
                candidates = Candidate.objects.all().order_by('-score')
                serializer = CandidateSerializer(candidates, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "필드에 0 또는 1을 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "method 필드를 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)


class TeamListView(APIView):
    def get(self, request):
        try:
            if request.data['method'] == 0:  # 후보
                teams = Team.objects.all()
                serializer = TeamSerializer(teams, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif request.data['method'] == 1:  # 결과
                teams = Team.objects.all().order_by('-score')
                serializer = TeamSerializer(teams, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "필드에 0 또는 1을 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "method 필드를 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)