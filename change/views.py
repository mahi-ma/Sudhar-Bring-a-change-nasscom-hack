from django.shortcuts import render, get_object_or_404, redirect
from .models import Complaint
from .forms import ComplaintForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
import time, random


def start_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('change:home_page'))
    else:
      return HttpResponseRedirect(reverse('change:welcome'))


def welcome_page(request):
    return render(request, 'change/welcome_page.html')



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('change:complaint_list')
    else:
        form = RegisterForm()
    return render(request, 'change/register.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('change:home_page')

            else:
                return render(request, 'change/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'change/login.html', {'error_message': 'Invalid login'})
    return render(request, 'change/login.html')


def logout_user(request):
    logout(request)
    return render(request, 'change/welcome_page.html')


def home_page(request):
    return render(request, 'change/home.html')


def complaint_new(request):
    if request.method == "POST":
       form = ComplaintForm(request.POST)
       if form.is_valid():
           complaint = form.save(commit=False)
           complaint.c_id = random.randint(1, 101)
           complaint.date = time.strftime("%d/%m/%Y")
           complaint.save()
           return redirect('change:complaint_details', pk=complaint.pk)

    else:
        form = ComplaintForm()
    return render(request, 'change/complaint_new.html', {'form': form})


def complaint_list(request):
    complaints = Complaint.objects.all()
    return render(request, 'change/complaint_list.html', {'complaints': complaints})


def complaint_details(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    return render(request, 'change/complaint_details.html', {'complaint': complaint})


