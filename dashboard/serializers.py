from django.contrib.auth.models import User, Group
from rest_framework import serializers


import datetime
import pytz

from .models import *

class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Button
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ButtonSerializer, self).to_representation(instance)

        instance.time_clicked = instance.time_clicked.astimezone(pytz.timezone('America/Chicago'))
        representation['time_clicked'] = instance.time_clicked.strftime("%m/%d/%Y %H:%M:%S")    
        # print(tz_time_clicked)
        representation['location'] = instance.location.name
        representation['campus'] = instance.location.campus.name


        return representation

