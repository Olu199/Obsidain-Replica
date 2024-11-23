from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
from pathlib import Path
from urllib.parse import unquote
import re

# Base directory
BASE_DIR = Path(r'C:\Users\oyalu\Documents\obsidian')

def home(request):
    p = BASE_DIR
    directories = []
    files = []

    # Collect directories and files as strings
    for unknown_types in p.iterdir():
        if not re.search(pattern='^\.', string=unknown_types.name):
            if unknown_types.is_dir():
                directories.append(str(unknown_types.relative_to(BASE_DIR)))
            elif unknown_types.is_file():
                files.append(str(unknown_types.relative_to(BASE_DIR)))

    return render(request, 'index.html', {
        'directories': directories,
        'files': files,
        'current_directory': p,
        'base_dir': BASE_DIR,
    })


def click(request, new_path):
    try:
        new_path = unquote(new_path)
        p = BASE_DIR / new_path

        # Check if the path exists and is within the BASE_DIR
        if not p.exists() or not str(p).startswith(str(BASE_DIR)):
            raise Http404("Invalid path")
        # Present files for download
        if p.is_file():
            return FileResponse(p.open('rb'), content_type='application/octet-stream')
        # Collect directory and files
        directories = []
        files = []
        for unknown_types in p.iterdir():
            if not re.search(pattern='^\.', string=unknown_types.name):
                if unknown_types.is_dir():
                    directories.append(str(unknown_types.relative_to(BASE_DIR)))
                elif unknown_types.is_file():
                    files.append(str(unknown_types.relative_to(BASE_DIR)))


        return render(request, 'index.html', {
            'directories': directories,
            'files': files,
            'current_directory': p,
            'base_dir': BASE_DIR,
        })
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)
