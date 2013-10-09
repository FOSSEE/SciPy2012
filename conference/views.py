from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.conf import settings
from models import *
import csv


def home(request):
    return render_to_response('base.html', context_instance=RequestContext(request))
    

def keynote(request):
    return render_to_response('conference/keynote.html', context_instance=RequestContext(request))
    
    
def sponsors(request):
    return render_to_response('conference/sponsors.html', context_instance=RequestContext(request))
    

def tutorials(request):
    tutorials = TalkTutorial.objects.filter(type="tutorial")
    context = {"tutorials":tutorials}
    return render_to_response('conference/tutorials.html', context, context_instance=RequestContext(request))


def talks(request):
    talks = TalkTutorial.objects.filter(type="talk")
    context = {"talks":talks}
    return render_to_response('conference/talks.html', context, context_instance=RequestContext(request))


def details(request, talktutorial_id=None):
    slides = True
    video = True
    details = TalkTutorial.objects.get(id=talktutorial_id)
    if details.slides == "None":
        slides = False
    if details.video == "None":
        video = False
    context = {"detail":details, "slides":slides, "video":video}
    return render_to_response('conference/details.html', context, context_instance=RequestContext(request))         
