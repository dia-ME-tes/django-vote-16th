from django.urls import path

from .views import CandidateListView, TeamListView

urlpatterns = [
    path('department/', CandidateListView.as_view()),  # 파트장 리스트
    path('team/', TeamListView.as_view()),  # 팀 리스트
]
