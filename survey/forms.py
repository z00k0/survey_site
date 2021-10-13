from datetime import datetime
from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets

from survey.models import Personal, RoomFilling, Visual, MATS_CHOICES


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

class VisualForm(forms.ModelForm):
    
    class Meta:
        model = Visual

        fields = [
            'user',
            'materials',
            'material_other',
            'styles',
            'style_other',
            'unsuitable',
            'furniture',
            'furniture_other',
            'planning',
            'planning_other',
            'planning_type',
            'planning_type_other',
        ]


        widgets = {
            'material_other': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'style_other': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'unsuitable': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'furniture_other': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'planning_other': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'planning_type_other': forms.Textarea(attrs={'rows': 1, 'cols': 30}),

        }

class RoomForm(forms.ModelForm):

    class Meta:
        model = RoomFilling
        fields = '__all__'
        widgets = {
            'kitchen_photo': forms.FileInput(),
            'kitchen_other': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'bedroom_photo': forms.FileInput(),
            'bedroom_other': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'livingroom_photo': forms.FileInput(),
            'livingroom_other': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'childroom_photo': forms.FileInput(),
            'childroom_other': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'bathroom_photo': forms.FileInput(),
            'bathroom_other': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'toilet_photo': forms.FileInput(),
            'toilet_other': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'additional': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'interior_photos': forms.FileInput(),
        }
