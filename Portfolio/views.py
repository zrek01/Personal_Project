from django.shortcuts import render, get_object_or_404

from .models import Resume

def Resume(request):
    #contact = get_object_or_404(Resume)
    return render(request, 'portfolio/Resume.html')