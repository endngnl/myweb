# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    nama = "Endang"
    buah = ['Apel','melon','mantan']
    return render(request, 'index.html',{'nama':nama, 'buah':buah})

def about(request):
    return render(request, 'about.html')

def kontak_abi(request):
    kontak = "087654788654"
    return render(request, 'kontak-abi.html', {'kontak':kontak})

def blog(request):
    catatan = "hari ini"
    return render(request, 'blog.html', {'catatan':catatan})   

def date(request):
    date = "13-02-19"
    return render(request, 'date.html', {'date':date})   