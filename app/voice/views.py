from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['track']
        print(uploaded_file.name)
    return render(request, 'voice/home.html')