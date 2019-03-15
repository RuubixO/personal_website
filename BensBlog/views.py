from django.shortcuts import render
from django.http import HttpReponse

def home(request):
    return HttpReponse('<h1>Blog Home</h1>')
