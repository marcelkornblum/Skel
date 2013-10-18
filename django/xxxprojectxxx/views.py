from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.utils import simplejson
from xxxprojectnamexxx import utils
from xxxprojectnamexxx import services
from xxxprojectnamexxx.models import *


def home(request):
    return render_to_response('index.html')