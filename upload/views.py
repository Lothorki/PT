from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
import json
# Create your views here.


@api_view(['POST'])
def hello(request):
	print(request.FILES.get('myfile'))
	return HttpResponse(123)