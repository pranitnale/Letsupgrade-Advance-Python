from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        date=request.POST.get('date')
        index=Contact(name=name,email=email,phone=phone,date=datetime.today())
        index.save()
    
    return render(request,'index.html')
