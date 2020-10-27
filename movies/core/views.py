from django.http import HttpResponse
from django.shortcuts import render

# def hello(request):
#     return HttpResponse('Hello world!')
from core.models import Movie, Genre, AGE_CHOICES


def hello(request):
    return render(request,
                  template_name='hello.html',
                  context={'adjectives': ['beautiful', 'cruel', 'wonderful']},
                  )


def movies(request):
    return render(request,
                  template_name='movies.html',
                  context={'movies': Movie.objects.exclude(genre__age_limit=AGE_CHOICES.adults)}
                  )
