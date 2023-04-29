from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Schedule
import json
from .serializers import ScheduleSerializer
# Create your views here.

def main(request):
    return HttpResponse("안녕")


@api_view(['GET'])
def findMonth(request,month):
    if request.method == 'GET':
        lst = findByMonth(month)
        return Response(lst.data)
    
@api_view(['GET'])
def findDay(request):
    if request.method == 'GET':
            month = request.GET.get('month')
            day = request.GET.get('day')
            lst = findByDay(month,day)
            return Response(lst.data)


def findByMonth(month):
    queryset = Schedule.objects.filter(month=month)
    lst = ScheduleSerializer(queryset,many=True)
    print(lst)
    return lst    
        
def findByDay(month,day):
    queryset = Schedule.objects.filter(month=month,day=day)
    lst = ScheduleSerializer(queryset,many=True)
    print(lst)
    return lst