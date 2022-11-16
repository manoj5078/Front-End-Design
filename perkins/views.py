from django.shortcuts import render
# from perkins.serialport import data_str

# Create your views here.
def dashboard(request):
    return render(request,'perkins/dashboard.html')

def headline(request):
    return render(request,'perkins/headline.html')

def finalinspection(request):
    return render(request,'perkins/finalinspection.html')

def headline2(request):
    return render(request,'perkins/headline2.html')

def machinediagram(request):
    return render(request,'perkins/machinediagram.html')

# def serial(request):
#     return render(request,'perkins/serial.html',{'data_str': data_str})