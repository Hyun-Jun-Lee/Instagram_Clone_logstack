from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

# Create your views here.

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all()
        return render(request, 'instagram/main.html', {'feed_list':feed_list})

