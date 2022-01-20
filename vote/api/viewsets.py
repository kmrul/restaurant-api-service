from base.models import Restaurant
from vote.models import Candidate, Vote
from .serializers import VoteSerializer, CandidateSerializer
from rest_framework import viewsets




class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer




class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer