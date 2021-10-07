from datetime import datetime
from django import forms
from django.db.models import fields

from survey.models import Personal


# class EquipsForm(forms.Form):
#     eqs = forms.ChoiceField(widget=forms.RadioSelect, choices=Equips.choices)


# class ProjectStyleForm(forms.Form):
#     ps = forms.ChoiceField(widget=forms.RadioSelect, choices=ProjectStyles.choices)


# class BeautyForm(forms.Form):
#     bf = forms.ChoiceField(widget=forms.RadioSelect, choices=Beauties.choices)


class PersonalForm(forms.Form):
    name = forms.CharField()
    survey_date = forms.DateField(initial=datetime.now(), widget=forms.SelectDateWidget)
    addr = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 30}), required=False)
    square = forms.FloatField(required=False)
    plan = forms.FileField(required=False, widget=forms.FileInput)
    composition = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}), required=False)
    interests = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}), required=False)
    budget = forms.FloatField(required=False)
    equip_s = forms.ChoiceField(widget=forms.RadioSelect, choices=Personal.Equips.choices)
    equip = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 30}), required=False)
    project_style = forms.ChoiceField(widget=forms.RadioSelect, choices=Personal.ProjectStyles.choices, required=False)
    beauty = forms.ChoiceField(widget=forms.RadioSelect, choices=Personal.Beauties.choices, required=False)

