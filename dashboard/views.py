from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.db.models import Max, F, Q
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework_api_key.permissions import HasAPIKey

from .serializers import *

class CampusAPIView(generics.ListCreateAPIView):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer


class LocationAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ButtonAPIView(generics.ListCreateAPIView):
    queryset = Button.objects.all()
    serializer_class = ButtonSerializer

@api_view(['GET'])
def button_list(request):
    if request.is_ajax():

        if request.method == 'GET':
            """ Get the latest click for the button name. Group by is done based on button ID. Using UUID for testing but will 
                use the button DSN in production"""
            button_latest_set = Button.objects.values('button_id').annotate(max_time_clicked=Max('time_clicked')).order_by()
            q_statement = Q()
            for pair in button_latest_set:
                q_statement |= (Q(button_id__exact=pair['button_id']) & Q(time_clicked=pair['max_time_clicked']))

            button_set = Button.objects.filter(q_statement).order_by('-time_clicked')

            if not request.user.is_superuser:
                button_set = button_set.filter(location__campus__user=request.user)

            serializer = ButtonSerializer(button_set, many=True)
            
            return JsonResponse(serializer.data, safe=False)

    else:
        raise Http404


@api_view(['POST'])
@csrf_exempt
@permission_classes([HasAPIKey])
def button_post(request):
    if request.method == 'POST':
        serializer = ButtonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

@login_required(login_url='/login/')
def home(request):
    buttons = Button.objects.all()
    serializer = ButtonSerializer(buttons, many=True)
    return render(request,'dashboard/main.html', {'buttons':serializer.data})