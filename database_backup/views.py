from django.http import HttpResponse
from . import schedule

def database_backup(request):
    return HttpResponse("Hello world")