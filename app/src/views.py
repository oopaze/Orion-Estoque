from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "default/index.html")