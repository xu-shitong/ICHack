from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.

from pathlib import Path
import os

def home(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['track']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        base_url = './../../..' + url
        print(uploaded_file.name)
        print(url)
        print(base_url)
        return render(request, 'voice/home.html', {"file":base_url})
    return render(request, 'voice/home.html')