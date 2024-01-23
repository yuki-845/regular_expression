
from django.shortcuts import render


def confirm(request):
    
    if request.method == 'GET':
        return render(request, 'regex_app/index.html')