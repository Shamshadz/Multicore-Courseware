from nbconvert import HTMLExporter
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    notebook_path = 'notebooks/your_notebook.ipynb'
    
    with open(notebook_path, 'r', encoding='utf-8') as notebook_file:
            notebook_content = notebook_file.read()

    html_exporter = HTMLExporter()
    html_content, resources = html_exporter.from_file(notebook_path)

    return render(request, 'notebook_config/notebook_template.html', {'html_content': html_content})

# def convert_notebook_to_html(notebook_path):
#     html_exporter = HTMLExporter()
#     (body, resources) = html_exporter.from_filename(notebook_path)
#     return body

# html_content = convert_notebook_to_html('notebook_config/notebooks/your_notebook.ipynb')
