from django.urls import path

from users.views import VoteView, CandidateListView, TeamListView

urlpatterns = [
    path('vote/', VoteView.as_view()),  # 투표
    path('department/<int:method>', CandidateListView.as_view()),  # 파트장 리스트
    path('team/<int:method>', TeamListView.as_view()),  # 팀 리스트
]
