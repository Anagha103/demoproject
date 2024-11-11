from  rest_framework import serializers
from .models import *


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_name']

class PersonSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = person
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        # Extract nested team data
        team_data = validated_data.pop('team', None)

        #If team data exists get or create a Team instance
        if team_data:
            team, created = Team.objects.get_or_create(**team_data)
            validated_data['team'] = team  #Assign the team instance to validated_data

        #Create the person instance with the validated data
        person_instance = person.objects.create(**validated_data)

        return person_instance
    

    def update(self, instance, validated_data):
        team_data = validated_data.pop('team')
        team, created = Team.objects.get_or_create(**team_data)
        instance.team = team
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance