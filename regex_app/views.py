from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django import forms
from .forms import MemberForm


class IndexView(FormView):
    template_name = 'regex_app/index.html'
    success_url = reverse_lazy('index')
    MemberFormSet = forms.formset_factory(
        form=MemberForm,
        extra=1,
        max_num=10,
    )
    form_class = MemberFormSet