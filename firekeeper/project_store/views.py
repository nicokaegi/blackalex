from django.shortcuts import render
from django.http import FileResponse
from django.contrib.auth.decorators import login_required

from firekeeper.settings import black_alex_path

import os
import zipfile
import shutil


# Create your views here.

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

def get_files(dir_path):
    return [item for item in os.listdir(dir_path) if item[0] != '.']


@login_required
def home(request):
    '''
    main view of all the file dirs as rows of at most 3 boot strap cards
    '''
    list_of_dirs = get_files(black_alex_path)
    list_of_dirs = break_into_3s(list_of_dirs)
    return render(request, 'home.html', {'list_of_dirs' : list_of_dirs })

@login_required
def view_files(request, dir_name):
    '''
    send back a list of all the file names in a directory
    '''
    dir_path = '/'.join([black_alex_path, dir_name])
    list_of_files = get_files(dir_path)
    return render(request, 'files.html', {'dir' : dir_name, 'list_of_files' : list_of_files})

@login_required
def download_file(request, dir_name, file_name):
    '''
    handles a download file request by gettings a file object,
    and returning it as a django response object
    '''
    file_path = '/'.join([black_alex_path, dir_name, file_name])

    # if the number of bytes is greater than 5mb and not compressed thecompress

    if (os.path.getsize(file_path) > 500000000) and (file_path.split('.')[1] != 'zip'):
        zip_file_name = "{}.{}".format(file_path.split('.')[0], "zip")
        with zipfile.ZipFile(zip_file_name, "w") as zf:
            zf.write(file_path)

        shutil.move(file_path,"{}/{}".format(black_alex_path,".trash"))
        file_path = zip_file_name


    out_file = open(file_path,'rb')
    response = FileResponse(out_file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="{}"'.format(file_path.split('/')[-1])
    return response


def handle_uploaded_file(dir_path,file_obj):
    # fet the name somehow
    with open('{}/{}'.format(dir_path,file_obj.name), 'wb+') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)

@login_required
def upload_file(request, dir_name):
    '''
    handles placing a new file in a directory
    '''
    if request.method == 'POST':
        dir_path = '/'.join([black_alex_path, dir_name])
        file_obj = request.FILES['new_file']
        handle_uploaded_file(dir_path,file_obj)
        list_of_files = os.listdir(dir_path)
        return render(request, 'files.html', {'dir' : dir_name, 'list_of_files' : list_of_files})

@login_required
def new_dir(request):
    '''
    from the text input on the home page create a new dir if one with the same name
    doesn't already exist
    '''
    if request.method == 'POST':
        new_dir_name = request.POST['new_dir_name']
        list_of_dirs = get_files(black_alex_path)
        if not (new_dir_name in list_of_dirs):
            os.mkdir('{}/{}'.format(black_alex_path,new_dir_name))
            list_of_dirs = break_into_3s(list_of_dirs)

        else:
            list_of_dirs = break_into_3s(list_of_dirs)

        return render(request, 'home.html', {'list_of_dirs' : list_of_dirs })

@login_required
def about(request):
    return render(request, 'about.html')
