from dataclasses import fields
from os import name
from rest_framework import serializers 
from vote.models import Candidate, Vote
from django.shortcuts import get_list_or_404
from django.db import IntegrityError




class CandidateSerializer(serializers.ModelSerializer):
    votes = serializers.ReadOnlyField()

    class Meta:
        model = Candidate
        fields = '__all__'




class VoteSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        candidate = Candidate.objects.filter(id=validated_data['candidate'])
        vote = Vote()
        vote.name = validated_data['name']
        vote.ip_address = validated_data['ip_address']
        vote.Candidate = candidate
        vote.date = validated_data['date']
        try:
            vote.save(commit=True)
        except IntegrityError:
            return vote
        return vote

    class Meta:
        model = Vote
        fields = ("id", "name", "ip_address", "candidate", "date")