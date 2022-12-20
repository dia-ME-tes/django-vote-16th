from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView


#투표
from account.models import User
from account.views import AuthView
from users.models import Profile, Department, Vote, Candidate, Team
from users.serializers import VoteSerializer, ProfileSerializer


class VoteView(APIView):
    def post(self, request):
        vote = request.data
        login_user = AuthView.get(self, request).data
        print(login_user)
        if AuthView.get(self,request).status_code is status.HTTP_200_OK:
            login_user_detail = Profile.objects.get(name = login_user['name'])

            if login_user_detail is not None:

                #투표정보 가져오기
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

                #팀 투표
                if team is not None:
                    vote_serializer = VoteSerializer(data={
                        'user_id' : login_user_detail.user.id,
                        'department_id' : login_user_detail.department.id,
                        'team_id' : team.id,
                        'candidate_id' : None
                    })

                #후보자 투표
                elif candidate is not None:
                    vote_serializer = VoteSerializer(data={
                        'user_id': login_user_detail.user.id,
                        'department_id': login_user_detail.department.id,
                        'team_id': None,
                        'candidate_id': candidate.id
                    })

                if vote_serializer.is_valid(raise_exception=True):
                    vote_serializer.save()
                    return Response('success', status=status.HTTP_200_OK)
                else:
                    return Response('bad request',status=status.HTTP_400_BAD_REQUEST)

        elif AuthView.get(self,request).status_code is status.HTTP_400_BAD_REQUEST:
            raise exceptions.ValidationError(detail='Please login for voting')

        elif AuthView.get(self,request).status_code is status.HTTP_401_UNAUTHORIZED:
            raise exceptions.ValidationError(detail='token is expired')

        elif AuthView.get(self,request).status_code is status.HTTP_403_FORBIDDEN:
            raise exceptions.ValidationError(detail='Please login again')