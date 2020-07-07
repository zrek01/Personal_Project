from django.shortcuts import render, get_object_or_404

from .models import Contact

def Home(request):
    contact = get_object_or_404(Contact)
    return render(request, 'home/Home.html', {'Contact': contact})



