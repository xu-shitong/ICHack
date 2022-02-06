from pathlib import Path
import os

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect

from .forms import SongForm

def get_name(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = SongForm()

    return render(request, 'name.html', {'form': form})


def home(request):
    print("post")
    print(request.POST)
    print("file")
    print(request.FILES)
    if request.method == 'POST':
        # type = request.POST['type']
        #print(type)

        uploaded_file = request.FILES['track']
          
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        base_url = './../../..' + url
        print(uploaded_file.name)
        print(url)
        print(base_url)

        """
        for x in request.FILES.keys():
            print(x)
        uploaded_file_1 = request.FILES['track']
        uploaded_file_2 = request.FILES['speech']
        fs = FileSystemStorage()
        name_1 = fs.save(uploaded_file_1.name, uploaded_file_1)
        name_2 = fs.save(uploaded_file_2.name, uploaded_file_1)
        url_1 = fs.url(name_1)
        url_2 = fs.url(name_2)
        base_url_1 = './../../..' + url_1
        base_url_2 = './../../..' + url_2
        """

        return render(request, 'voice/home.html', {"file":base_url})
    return render(request, 'voice/home.html')