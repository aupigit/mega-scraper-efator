# Django
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import os


def importcsv(request):
    return render(request,'importcsv.html', {})
