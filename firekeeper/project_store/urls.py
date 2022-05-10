from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view_files/<dir_name>', views.view_files, name='files'),
    path('download_file/<dir_name>/<file_name>', views.download_file, name='download_file')
]
