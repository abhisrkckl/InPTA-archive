from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('project/<int:project_id>', views.project, name='project'),
    path('proposal/<int:proposal_id>', views.proposal, name='proposal')
]
