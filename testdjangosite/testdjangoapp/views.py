from django.shortcuts import render
import json
import os
from django.http import HttpResponse

# Create your views here.


def show(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    path = "testdjangoapp\\templates\\points"
    with open("testdjangoapp\\templates\\points\\point_1.txt", "r") as file:
        strlist = json.dumps(file.readlines())
    return render(request, 'page1.html',
                  { 'liststr' : strlist },
                  { 'mapbox_access_token': mapbox_access_token })
