from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'cse/home.html')
def intro(request):
    return render(request,'cse/intro.html')
def about(request):
    return render(request,'cse/about.html')
def profile(request):
    return render(request,'cse/profile.html')
def service(request):
    return render(request,'cse/service.html')
def schedule(request):
    return render(request,'cse/schedule.html')
