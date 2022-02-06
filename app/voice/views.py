from pathlib import Path
import os

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect

from .forms import UploadForm

def uploaded(request):
    base_url_1 = ""
    base_url_2 = ""
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            song_text = form.cleaned_data['song']
            url_2 = form.cleaned_data['speech']
            
            # TODO: do something with song text
            # base_url_1 = './../../../media/' + url_1
            base_url_2 = './../../../media/' + url_2
            # print(base_url_1)
            print(base_url_2)

            return render(request, 'voice/home.html', {'form': form, "file_2":base_url_2})
    else:
        form = UploadForm()
    return render(request, 'voice/home.html', {'form': form, "file_1":base_url_1, "file_2":base_url_2})

def home(request):
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = UploadForm()

    return render(request, 'voice/home.html', {'form': form})