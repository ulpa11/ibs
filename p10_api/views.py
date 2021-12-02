from django.shortcuts import render
from django.http import  HttpResponse
from json import dumps
# Create your views here.
from .serializers import  P10StatusSerializer
from .models import P10Status
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello P10</h1>")

class P10ApiViewSet(viewsets.ModelViewSet):
    queryset=P10Status.objects.all()
    serializer_class=P10StatusSerializer
    def perform_update(self, serializer):
        # Save with the new value for the target model fields
        user = self.request.user
        userid = str(user.id)
        serializer.save(stu_enrolled_classes=userid)
