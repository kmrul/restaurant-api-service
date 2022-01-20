from sqlite3 import IntegrityError
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vote, Candidate
from vote.api.serializers import VoteSerializer, CandidateSerializer




def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip




class VoteView(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer




class CandidateView(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer




class CastVoteView(APIView):

    def post(self, request):
        print("request:", request)
        serializer = VoteSerializer(data=request.data)
        print("serializer:", serializer)
        if serializer.is_valid(raise_exception=ValueError):
            created_instance = serializer.create(validated_data=request.data)
            created_instance.ip_address = get_client_ip(request)

            print("created_instance:", created_instance)
            try:
                created_instance.save()
            except IntegrityError:
                return Response(
                    {
                        "message": "Already voted"
                    },
                    STATUS=status.HTTP_400_BAD_REQUEST
                )
            return Response(
                {
                    "message": "Vote cast successfull."
                },
                status=status.HTTP_200_OK
            )