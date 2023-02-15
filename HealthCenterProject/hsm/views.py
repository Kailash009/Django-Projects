from django.shortcuts import render
from .forms import AppointmentForm
from django.http import HttpResponse

# Create your views here.
def view_home(request):
    resp=render(request,'hsm/home.html')
    return resp

def view_about(request):
    resp=render(request,'hsm/about.html')
    return resp

def view_doctor(request):
    resp=render(request,'hsm/doctor.html')
    return resp

def view_news(request):
    resp=render(request,'hsm/news.html')
    return resp

def view_contact(request):
    resp=render(request,'hsm/contact.html')
    return resp

def view_appointment(request):
    if request.method=='GET':
        frm_unbound=AppointmentForm()
        d1={'forms':frm_unbound}
        resp=render(request,'hsm/appointment.html',context=d1)
        return resp
    elif request.method=='POST':
        frm_bound=AppointmentForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            resp=HttpResponse("<h1>Appointment Added SuccessFully!!</h1>")
            return resp
        else:
            d1={'forms':frm_bound}
            resp=render(request,'hsm/appointment.html',context=d1)
            return resp



