from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db import IntegrityError
from django import forms

from survey.forms import PersonalForm, VisualForm

from .models import User, Personal


# class PersonalForm(forms.Form):
#     name = forms.CharField()
#     survey_date = forms.DateField()
#     addr = forms.CharField()
#     square = forms.FloatField()
#     plan = forms.ImageField()
#     composition = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
#     interests = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
#     budget = forms.FloatField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
#     equip = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
#     project_style = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
#     beauty = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


def index(request):
    return render(request, 'survey/index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'survey/login.html', {
                'message': 'Invalid username or/and password'
            })
    else:
        return render(request, 'survey/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, 'survey/register.html', {
                'message': 'Пароли не совпадают.'
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'survey/register.html', {
                'message': 'Такое имя уже занято. Придумайте другое.'
            })
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'survey/register.html')


def personal(request):
    if request.method == 'POST':
        user = request.user
        form = PersonalForm(request.POST, request.FILES)
        if form.is_valid():
            user = user
            name = form.cleaned_data['name']
            survey_date = form.cleaned_data['survey_date']
            print(f'date: {survey_date}')
            addr = form.cleaned_data['addr']
            square = form.cleaned_data['square']
            plan = form.cleaned_data['plan']
            composition = form.cleaned_data['composition']
            interests = form.cleaned_data['interests']
            budget = form.cleaned_data['budget']
            equip_s = form.cleaned_data['equip_s']
            equip = form.cleaned_data['equip']
            project_style = form.cleaned_data['project_style']
            beauty = form.cleaned_data['beauty']
            mod = Personal(
                user=user,
                name=name,
                survey_date=survey_date,
                addr=addr,
                square=square,
                plan=plan,
                composition=composition,
                interests=interests,
                budget=budget,
                equip_s=equip_s,
                equip=equip,
                project_style=project_style,
                beauty=beauty,
            )
            mod.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'survey/personal.html', {
                'form': form,
            })

    form = PersonalForm()
    return render(request, 'survey/personal.html', {
        'form': form,
    })

def visual(request):
    if request.method == 'POST':
        user = request.user
        form = VisualForm(request.POST)
        list_checkbox = request.POST.getlist('material')
        print('Dir:', form.fields['material'])
        print(f'{list_checkbox=}')
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors.as_data())
            return render(request, 'survey/visual.html', {
                'form': form,
            })
    form = VisualForm()
    return render(request, 'survey/visual.html', {
        'form': form,
    })