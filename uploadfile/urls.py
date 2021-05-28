from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [

    path('', views.home),
    path('file_upload', csrf_exempt(views.file), name='excel_to_json')

]
