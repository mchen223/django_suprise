# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random

VALUES = ['Hello friend!', 'Hi buddy!', 'Howdy partner!', 'What up bruh?', 'Greetings traveler!', 'Hey pal!']

def index(request):
    random.shuffle(VALUES)
    return render(request, 'surprise/index.html')

def results(request):
    request.session.strings = []
    number = int(request.POST['number'])
    if number > 0:
        for i in range(0, number):
            request.session.strings.append(VALUES[i])
    else:
        alert('Number has to be a postive number.')
        return redirect("/")
    return render(request, 'surprise/results.html')

def reset(request):
    request.session.clear()
    return redirect("/")
