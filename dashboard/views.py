from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.db.models import Max, F, Q
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

@api_view(['GET', 'POST'])
@csrf_exempt 
def button_list(request):
    if request.is_ajax():

        if request.method == 'GET':
            """ Get the latest click for the button name. Group by is done based on button name. Probably set the name as 
                <Button name>: <Location name>: <Campus name> to keep the button name unique"""
            button_latest_set = Button.objects.values('name').annotate(max_time_clicked=Max('time_clicked')).order_by()
            q_statement = Q()
            for pair in button_latest_set:
                q_statement |= (Q(name__exact=pair['name']) & Q(time_clicked=pair['max_time_clicked']))

            button_set = Button.objects.filter(q_statement).order_by('-time_clicked')

            serializer = ButtonSerializer(button_set, many=True)
            
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            serializer = ButtonSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    else:
        raise Http404

    # elif request.method == 'PUT':
    #     serializer = ButtonSerializer(button, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def button_patch(request, pk):
#     try:
#         button = Button.objects.get(pk=pk)
#     except Button.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

def home(request):
    buttons = Button.objects.all()
    serializer = ButtonSerializer(buttons, many=True)
    return render(request,'dashboard/main.html', {'buttons':serializer.data})