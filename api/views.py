from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.encrpyt.cipher import *
from core.sql import *

@api_view(['GET'])
def getData(request):
    person = {'name':'pavan'}
    return Response(person)

