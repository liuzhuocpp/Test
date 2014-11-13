# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from admin.models import Data
import datetime

def addName(request):

    print request.method
    print request.get_full_path()
    print request.is_ajax()

    if request.method == "POST":
        print request.POST
        print request.POST['name']
        
        p = Data(name = request.POST['name'])
        p.save()
    
    return render(request, "admin/home.html")