# from django.urls import path
# from . import views 
# urlpatterns = [
#     path('',views.projects,name="projects"),
#     path('create-project/',views.createProject,name="create-project"),
#     path('project/<str:pk>/',views.project,name="project"),
#     path('update-project/<str:pk>/',views.updateProject,name="update-project"),
#     path('projects/',views.projects, name="Projects"),
#     path('singleproject/',views.singleproject, name="singleproject"),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('create-project/', views.createProject, name="create-project"),
    path('project/<str:pk>/', views.project, name="project"),
    path('update-project/<str:pk>/', views.updateProject, name="update-project"),
    path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),
    path('projects/', views.projects, name="Projects"),
    path('singleproject/', views.singleproject, name="singleproject"),
]
