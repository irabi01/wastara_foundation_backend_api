from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Events
from .serializers import EventsSerializer
# Create your views here.

class EventsView(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by('-id')
    serializer_class = EventsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
