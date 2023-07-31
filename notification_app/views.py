from django.shortcuts import render

# Create your views here.
def home(request):
    """
    A function that renders the 'home.html' template.
    """
    return render(request, 'home.html')