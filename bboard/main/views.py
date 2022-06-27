from django.shortcuts import render

def index(requerst):
    return render(requerst, 'main/index.html')
