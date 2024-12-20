from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from .models import User
import folium

# Create your views here.
def index(request):
    return render(request, 'apps/core/index.html')