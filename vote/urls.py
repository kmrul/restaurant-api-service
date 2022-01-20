from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework import routers
from vote.models import Candidate
from .views import VoteView, CastVoteView, CandidateView

router = routers.DefaultRouter()
router.register('candidate', CandidateView)


urlpatterns = [
    path('', include(router.urls)),
    path('vote/', CastVoteView.as_view(), name='vote')
]
