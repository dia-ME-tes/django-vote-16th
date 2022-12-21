from django.db.migrations import serializer
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User
from account.views import AuthView
from users.models import Profile, Department, Vote, Candidate, Team
from users.serializers import VoteSerializer, ProfileSerializer, CandidateSerializer, TeamSerializer


# 투표
class VoteView(APIView):
    def post(self, request):
        vote = request.data

        if AuthView.get(self, request).status_code is status.HTTP_200_OK:
            login_user = AuthView.get(self, request).data
            login_user_detail = Profile.objects.get(user_id=login_user['user_id'])

            if login_user_detail is not None:

                # 투표정보 가져오기
                try:
                    team = Team.objects.get(id=vote['team'])  # 투표한 팀 정보 가져오기
                    team.score += 1
                    team.save()
                except:
                    team = None

                try:
                    candidate = Candidate.objects.get(id=vote['name'])  # 투표한 파트장 정보 가져오기
                    candidate.score += 1
                    candidate.save()
                except:
                    candidate = None

                # 팀 투표
                if team is not None:
                    vote_serializer = VoteSerializer(data={
                        'user_id': login_user_detail.user.id,
                        'department_id': None,
                        'team_id': team.id,
                        'candidate_id': None
                    })

                # 후보자 투표
                elif candidate is not None:
                    vote_serializer = VoteSerializer(data={
                        'user_id': login_user_detail.user.id,
                        'department_id': candidate.department_id,
                        'team_id': None,
                        'candidate_id': candidate.id
                    })

                if vote_serializer.is_valid(raise_exception=True):
                    vote_serializer.save()
                    return Response('success', status=status.HTTP_200_OK)
                else:
                    return Response('bad request', status=status.HTTP_400_BAD_REQUEST)

        elif AuthView.get(self, request).status_code is status.HTTP_400_BAD_REQUEST:
            raise exceptions.ValidationError(detail='Please login for voting')

        elif AuthView.get(self, request).status_code is status.HTTP_401_UNAUTHORIZED:
            raise exceptions.ValidationError(detail='token is expired')

        elif AuthView.get(self, request).status_code is status.HTTP_403_FORBIDDEN:
            raise exceptions.ValidationError(detail='Please login again')


# 파트장 후보리스트
class CandidateListView(APIView):
    def get(self, request, method):
        try:
            if method == 0:  # 후보
                candidates = Candidate.objects.all()
                serializer = CandidateSerializer(candidates, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif method == 1:  # 결과
                candidates = Candidate.objects.all().order_by('-score')
                serializer = CandidateSerializer(candidates, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "필드에 0 또는 1을 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "method 필드를 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)


# 데모데이 후보리스트
class TeamListView(APIView):
    def get(self, request, method):
        try:
            if method == 0:  # 후보
                teams = Team.objects.all()
                serializer = TeamSerializer(teams, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif method == 1:  # 결과
                teams = Team.objects.all().order_by('-score')
                serializer = TeamSerializer(teams, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "필드에 0 또는 1을 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "method 필드를 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)
