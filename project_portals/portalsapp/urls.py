from django.urls import path
from . import views
from django.contrib.auth import views as ad

urlpatterns = [
	path('',views.home,name="hm"),
	path('register/', views.register, name='register'),
	path('lgn/',ad.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('lgot/',ad.LogoutView.as_view(template_name="html/logout.html"),name="lgt"),
	path('pfle/',views.profile,name="pf"),
	path('add_project/', views.add_project, name='add_projects'),
	path('projects/', views.project_list, name='project_list'),
	path('request_approval/<int:project_id>/', views.request_approval, name='request_approval'),
	path('request_project/<int:project_id>/', views.request_project, name='request_project'),
    path('approve_request/<int:request_id>/', views.approve_request, name='approve_request'),
    path('start_project_work/<int:project_id>/', views.start_project_work, name='start_project_work'),
    path('agent_approval/', views.agent_approval, name='agent_approval'),
    path('project_detail/<int:project_id>/', views.project_detail, name='project_detail'),
    
]