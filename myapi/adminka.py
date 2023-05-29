from django.http import HttpResponse
import psycopg2
import json
import hashlib
from django.shortcuts import render,redirect
from django.template import loader
from .forms import ResumeForm
from .forms import DrinkForm
import os

# Create your views here.
# visitor menu
def testadmin(request):
    return HttpResponse("Adminka works")