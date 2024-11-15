# from django.shortcuts import render

# Create your views here.

from carsworld.forms import *


# def registration(request):
#     ufo=UserForm()
#     pfo=ProfileForm()
#     d={'ufo':ufo,'pfo':pfo}
#     return render(request,'registration.html',d)



from rest_framework import generics, permissions
from .models import Car
from .serializers import CarSerializer
from django.contrib.auth.models import User

class CarListCreateView(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)


from django.db.models import Q

class CarSearchView(generics.ListAPIView):
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Car.objects.filter(
            Q(owner=self.request.user) & 
            (Q(title__icontains=query) | Q(description__icontains=query) | Q(tags__icontains=query))
        )
