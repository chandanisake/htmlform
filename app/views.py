from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def htmlform(request):
    if request.method=='POST':
        return HttpResponse('data is submitted')

    return render(request,'htmlform.html')
