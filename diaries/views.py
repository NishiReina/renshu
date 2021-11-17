from django.shortcuts import render

# Create your views here.

def top(request):
    return render(request, 'diaries/top.html')
    
def index(request):
    items = ["日記1", "日記2", "日記3"]
    return render(request, "diaries/index.html", {'items': items})