from datetime import datetime
from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets

from survey.models import Light, Personal, Project, RoomFilling, Tech, Visual, MATS_CHOICES


class PersonalForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'numbers'}))
    survey_date = forms.DateField(initial=datetime.now(), widget=forms.SelectDateWidget())
    addr = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}), required=False)
    square = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'class': 'numbers'}))
    plan = forms.FileField(required=False, widget=forms.FileInput())
    composition = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}), required=False)
    interests = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}), required=False)
    budget = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'class': 'numbers'}))
    equip_s = forms.ChoiceField(widget=forms.RadioSelect, choices=Personal.Equips.choices)
    equip = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}), required=False)
    project_style = forms.ChoiceField(widget=forms.RadioSelect, choices=Personal.ProjectStyles.choices, required=False)
    beauty = forms.ChoiceField(widget=forms.RadioSelect, choices=Personal.Beauties.choices, required=False)

class VisualForm(forms.ModelForm):
    
    class Meta:
        model = Visual

        fields = [
            # 'user',
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
            'material_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'style_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'unsuitable': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'furniture_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'planning_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'planning_type_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),

        }

class RoomForm(forms.ModelForm):

    class Meta:
        model = RoomFilling
        # fields = '__all__'
        exclude = ['user']
        widgets = {
            'kitchen_photo': forms.FileInput(),
            'kitchen_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'bedroom_photo': forms.FileInput(),
            'bedroom_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'livingroom_photo': forms.FileInput(),
            'livingroom_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'childroom_photo': forms.FileInput(),
            'childroom_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'bathroom_photo': forms.FileInput(),
            'bathroom_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'toilet_photo': forms.FileInput(),
            'toilet_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'additional': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'interior_photos': forms.FileInput(),
        }

class LightForm(forms.ModelForm):

    class Meta:
        model = Light
        # fields = '__all__'
        exclude = ['user']
        widgets = {
            'lights_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'temp_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }

class TechForm(forms.ModelForm):

    class Meta:
        model = Tech
        # fields = '__all__'
        exclude = ['user']
        widgets = {
            'walls_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'floors_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'doors_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'windows_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'ceil_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'heating_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'conditioner': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'warm_floor': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'electric_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'additional': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            
        }

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        # fields = '__all__'
        exclude = ['user']
        widgets = {
            'contents': forms.RadioSelect(
                choices=Project.Content.choices, 
                attrs={"required": False}
                ),
            'urgencies': forms.RadioSelect(choices=Project.Urgency.choices, ),
            'communications': forms.RadioSelect(choices=Project.Communication.choices, ),
            'content_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'urgencies_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'communications_other': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'additions': forms.Textarea(attrs={'rows': 3, 'cols': 40}),

        }