from django.shortcuts import render

# Create your views here.
from .models import UserTable
from django.forms.models import model_to_dict
from django.http import JsonResponse
import json


def search_result(request):
    result = []
    for user in UserTable.objects.all():
        result.append(model_to_dict(user, exclude=['parent']))
    return JsonResponse(result,safe=False)
