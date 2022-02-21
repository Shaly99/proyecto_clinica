from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

import psycopg2

def mainview(request):
    return render(request, 'mainview.html', {})