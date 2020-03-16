from django.views.generic import View
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from .models import Room

class  RoomForm(forms.ModelForm):
    class  Meta:
        model = Room
        fields =  '__all__'

class  RoomList(View):
    def  get(self, request):
        rooms =  list(Room.objects.all().values())[-1:]
        data =  dict()
        print(rooms[0])
        if rooms[0]['room_type'] == 3:
            data['bg_css'] = 'red'
        elif rooms[0]['room_type'] == 2:
            data['bg_css'] = 'blue'
        else:
            data['bg_css'] = 'green'

        data['rooms'] = rooms
        return JsonResponse(data)

