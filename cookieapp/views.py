from django.shortcuts import render
from django.http import HttpResponse

def input(request):
    return render(request,'base.html')
def add(request):
    x=int(request.GET['t1'])
    y=int(request.GET['t2'])
    z=x+y
    resp=HttpResponse('values submitted successfully')
    resp.set_cookie('sum',z,max_age=100)
    return resp
def display (request):
    if 'sum'in request.COOKIES:
        res=request.COOKIES['sum']
        return HttpResponse('addition of two no:' +res)
    else:
        return HttpResponse("pls enter values")
