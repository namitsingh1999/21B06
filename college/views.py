from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {

    }
    return render(request, 'index1.html',context)

@login_required
def charts(request):
    context = {

    }
    return render(request,'charts.html',context)

@login_required
def tables(request):
    context = {

    }
    return render(request,'tables.html',context)

@login_required
def dashboard(request):
    context = {

    }
    return render(request , 'colleges/dashboard.html',context)