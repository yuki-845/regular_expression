from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.shortcuts import render


def confirm(request):
    message = 'データ受け取ったよ！'
    if request.method == 'POST':
        nyuryoku1 = request.POST['nyuryoku1']
        nyuryoku2 = request.POST['nyuryoku2']
        nyuryoku3 = request.POST['nyuryoku3']

        params = {
            "nyuryoku1": nyuryoku1,
            "nyuryoku2": nyuryoku2,
            "nyuryoku3": nyuryoku3,
            "message": message,
        }
        return render(request, '', params)