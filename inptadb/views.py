from django.shortcuts import render
from django.http import HttpResponse

from .models import Project, Proposal

def index(request):
    context = dict()
    return render(request, 'inptadb/index.html', context)
    #return HttpResponse("Welcome to InPTA!")

def projects(request):
    projects = Project.objects.all()
    context = {"projects" : projects}
    return render(request, 'inptadb/projects.html', context)
    
def project(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project Does Not Exist.")
    #response = "Showing Question #{}".format(question_id)
    return render(request, "inptadb/project.html", {'project':project})

def proposal(request, proposal_id):
    try:
        proposal = Proposal.objects.get(pk=proposal_id)
    except Project.DoesNotExist:
        raise Http404("Proposal Does Not Exist.")
    #response = "Showing Question #{}".format(question_id)
    return render(request, "inptadb/proposal.html", {'proposal':proposal})
