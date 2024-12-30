from django.shortcuts import render

# Create your views here.
def all_home(request):
    return render(request,'pages/all_home.html')