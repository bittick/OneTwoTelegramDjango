from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.decorators import api_view
from django.http import HttpResponse



def api_response(request):
    return HttpResponse( '123')