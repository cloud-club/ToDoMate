from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Schedule
from .serializers import ScheduleSerializer
# Create your views here.

def main(request):
    return HttpResponse("안녕")



def findMonth(month):
    queryset = Schedule.objects.filter(month=month, is_active=True)
    lst = ScheduleSerializer(queryset)
        
        
def findByDay(month,day):
    queryset = Schedule.objects.filter(month=month,day=day,is_active=True)
