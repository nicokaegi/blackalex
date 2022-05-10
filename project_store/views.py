from django.shortcuts import render
from django.http import FileResponse

import os

# Create your views here.
black_alex_path = "/home/sindri/blackalex"

#app_name = 'project_store'

def break_into_3s(in_list):

    if(len(in_list) != 0):
        count = 1
        list_pos = 0

        out_list = [[]]
        out_list[list_pos].append(in_list.pop())

        for item in in_list:
            if (count % 3 == 0):
                out_list.append([])
                list_pos += 1
            out_list[list_pos].append(item)
            count += 1

        return out_list

    else:
        return []

def home(request):
    list_of_dirs = os.listdir(black_alex_path)
    list_of_dirs = break_into_3s(list_of_dirs)
    return render(request, 'home.html', {'list_of_dirs' : list_of_dirs })

def view_files(request, dir_name):
    dir_path = '/'.join([black_alex_path, dir_name])
    list_of_files = os.listdir(dir_path)
    return render(request, 'files.html', {'dir' : dir_name, 'list_of_files' : list_of_files})

def download_file(request, dir_name, file_name):
    file_path = '/'.join([black_alex_path, dir_name, file_name])
    out_file = open(file_path,'rb')
    response = FileResponse(out_file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="{}"'.format(file_name)
    return response
