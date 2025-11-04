from django.shortcuts import render
from .models import Profile, LearningEntry

def index(request):
    entries = LearningEntry.objects.order_by('-created_at')
    return render(request, 'index.html', {'entries': entries})

def aboutMe(request):
    profile = Profile.objects.first()
    return render(request, 'aboutMe.html', {'profile': profile})
