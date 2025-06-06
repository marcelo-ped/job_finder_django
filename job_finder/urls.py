from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/add', views.add_job, name='add_job'),
    path('jobs/view/<int:job_id>/', views.view_job, name='view_job'),
]
