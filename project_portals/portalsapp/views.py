from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UsuserForm,ProjectForm,ProjectRequestForm
from .models import Project, ProjectRequest, User, ProjectStatus
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request,'html/home.html')


def register(request):
    if request.method == "POST":
        f = UsuserForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request,"User Created Successfully")
            return redirect('/')
    else:
        f = UsuserForm()
    return render(request,'html/register.html',{'g':f})

def profile(request):
    return render(request,'html/profile.html')

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')  # Redirect to a list view or another page after saving
    else:
        form = ProjectForm()
    return render(request, 'html/add_project.html', {'form': form})

def project_list(request):
    projects = Project.objects.all()
    project_status = {status.project_id: {'approved': status.approved, 'started': status.started} for status in ProjectStatus.objects.all()}
    print("Project Status:", project_status)
    return render(request, 'html/project_list.html', {'projects': projects, 'project_status': project_status})

def request_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    existing_requests = ProjectRequest.objects.filter(project=project, agent=request.user)
    
    if existing_requests.exists():
        messages.info(request, "You have already requested to work on this project.")
    else:
        ProjectRequest.objects.create(project=project, agent=request.user)
        messages.success(request, "Request sent to the team lead for approval.")
    
    return redirect('project_list')

def request_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    existing_requests = ProjectRequest.objects.filter(project=project, agent=request.user)
    
    if existing_requests.exists():
        messages.info(request, "You have already requested to work on this project.")
    else:
        ProjectRequest.objects.create(project=project, agent=request.user)
        messages.success(request, "Request sent to the team lead for approval.")
    
    return redirect('project_list')
@login_required
def request_approval(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    ProjectRequest.objects.create(project=project, agent=request.user)
    return redirect('project_list')

def approve_request(request, request_id):
    project_request = get_object_or_404(ProjectRequest, id=request_id, approved=False)

    if 'approve' in request.POST:
        project_request.approved = True
        project_request.save()
        messages.success(request, "Request approved.")
    elif 'reject' in request.POST:
        project_request.delete()
        messages.success(request, "Request rejected.")

    return redirect('agent_approval')

def start_project_work(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project_request = ProjectRequest.objects.filter(project=project, agent=request.user).first()

    if project_request and project_request.approved and not project_request.started:
        project_request.started = True
        project_request.save()
        messages.success(request, "Project started successfully.")
    else:
        messages.error(request, "You cannot start this project.")

    return redirect('project_list')

def agent_approval(request):
    project_requests = ProjectRequest.objects.filter(approved=False)
    return render(request, 'html/approve_request.html', {'project_requests': project_requests})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'html/project_detail.html', {'project': project})