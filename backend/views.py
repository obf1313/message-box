from django.shortcuts import get_object_or_404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from django.core import serializers

from .models import User, Question

# Create your views here.


@csrf_exempt
def register(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User(username=username, password=password)
    user.save()
    flag = '1'
    return HttpResponse(flag, content_type='application/json')