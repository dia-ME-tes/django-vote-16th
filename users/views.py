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
        vote_list = request.data['vote']
        login_user = AuthView.get(self, request).data
        print(login_user)
        if login_user['message'] == '토큰 없음':
            raise exceptions.ValidationError(detail='Please login for voting')
        else:
            login_user_detail = Profile.objects.get(name = login_user['name'])
            print(login_user_detail.name)

            # 투표 정보 가져오기
            part_vote, demoday_vote = vote_list[0], vote_list[1]
            candidate = Candidate.objects.get(id=part_vote['name']) #투표한 파트장 정보 가져오기
            team = Team.objects.get(id=demoday_vote['team']) #투표한 팀 정보 가져오기

            candidate.score += 1
            team.score += 1

            candidate.save()
            team.save()

            vote_serializer = VoteSerializer(data={
                'user_id' : login_user_detail.user.id,
                'department_id' : login_user_detail.department.id,
                'team_id' : team.id,
                'candidate_id' : candidate.id
            })

            print(vote_serializer)
            if vote_serializer.is_valid(raise_exception=True):
                vote_serializer.save()
                return Response('success', status=status.HTTP_200_OK)
            else:
                return Response('bad request',status=status.HTTP_400_BAD_REQUEST)
