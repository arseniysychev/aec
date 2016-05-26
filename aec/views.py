from django.shortcuts import render, redirect
from django.core.management import call_command


def index(request):
    return render(request, 'static/index.html')


def load_dicts(request):
    for l in range(6):
        less = l + 1
        call_command('load_dict', file='1-{less}.csv'.format(less=less), level=1, lesson=less)
    return redirect('index')
