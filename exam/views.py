from django.shortcuts import render
from .models import Contact
from .models import Rejister
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'exam/index.html')

def about(request):
    return render(request,'exam/about.html')

def jeetest(request):
    return render(request,'exam/jeetest.html')

def success(request):
    return render(request,'exam/success.html')

def program(request):
    return render(request,'exam/program.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'exam/contact.html')

def rejister(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        gender = request.POST.get('gender', '')
        cources = request.POST.get('cources', '')
        rejister = Rejister(name=name, email=email, phone=phone, address=address, gender=gender, cources=cources)
        rejister.save()
    return render(request, 'exam/rejister.html')