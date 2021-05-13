from django.shortcuts import render, reverse, HttpResponseRedirect
from authentication.forms import LoginForm
from django.contrib.auth.decorators import login_required
import re
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, HttpResponseRedirect, reverse, render
from verse.models import CustomUser
from .models import Post
from notification.models import Notification



def index_view(request):
    return render(request, 'index.html')
