from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import utils

def index(request):
    mhandle, mclient = utils.get_db_handle()
    warframes_list = list(mhandle['warframes'].find({}, {"name": 1, "_id": 0}))
    template = loader.get_template("warframes_index.html")
    context = { "warframes_list": warframes_list }
    return HttpResponse(template.render(context, request))

def by_name(request, warframe_name):
    mhandle, mclient = utils.get_db_handle()
    warframe_data = list(mhandle['warframes'].find({"name": warframe_name}, {"patchlogs": 0, "components": 0}))
    template = loader.get_template("warframes_by_name.html")
    context = { "warframe_data": warframe_data }
    return HttpResponse(template.render(context, request))
