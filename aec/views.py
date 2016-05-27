from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.management import call_command


def index(request):
    return render(request, 'static/index.html')


def load_dicts(request):
    level = request.GET.get('level')
    lesson = request.GET.get('lesson')
    if level and lesson:
        call_command(
            'load_dict',
            file='{level}-{lesson}.csv'.format(lesson=lesson, level=level),
            level=level,
            lesson=lesson
        )
        return redirect('index')
    else:
        return HttpResponse('No GET params "lesson" or "level"', status=400)
