from django import forms
import datetime
from .models import Exchanger

class CurExForm(forms.Form):
    rate = forms.FloatField(label='Курс', widget=forms.TextInput(attrs={"class": "form-control"}))
    created_date = forms.DateField(label='Дата', initial=datetime.datetime.now().strftime("%Y-%m-%d"),
                           widget=forms.DateInput(attrs={"class": "form-control"}))

