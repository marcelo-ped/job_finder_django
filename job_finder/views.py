from django.shortcuts import render
from .models import Jobs

def index(request):
    search = request.GET.get('job', '')
    if search:
        jobs = Jobs.objects.filter(title__icontains=search)
    else:
        jobs = Jobs.objects.all()
    return render(request, 'index.html', {'jobs': jobs, 'search': search})

def add_job(request):
    if request.method == 'POST':
        # Process form
        pass
    return render(request, 'add.html')

def view_job(request, job_id):
    job = Jobs.objects.get(pk=job_id)
    return render(request, 'view.html', {'job': job})
