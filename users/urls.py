from django.urls import path

from users.views import VoteView

urlpatterns = [
    path('vote/', VoteView.as_view()),  # 투표
]
