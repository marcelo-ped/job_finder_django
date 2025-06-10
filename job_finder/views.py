from django.shortcuts import render, redirect
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
        title = request.POST['title']
        description = request.POST['description']
        company = request.POST['company']
        email = request.POST['email']
        salary = request.POST['salary']
        new_job = request.POST.get('new_job', 0)

        Jobs.objects.create(
            title=title,
            description=description,
            company=company,
            email=email,
            salary=salary,
            new_job=new_job
        )

        return redirect('/')
    return render(request, 'add.html')

def view_job(request, job_id):
    job = Jobs.objects.get(pk=job_id)
    return render(request, 'view.html', {'job': job})
