from django.contrib import admin
from django.urls import path
from authApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.UserListaView.as_view()),  
    path('user/<int:pk>/', views.UserRetrieveUpdateDeleteView.as_view()),  
    path('medico/', views.MedicoListCreateView.as_view()),  
    path('medico/<int:pk>/', views.MedicoRetrieveUpdateView.as_view()), 
    path('paciente/', views.PacienteListCreateView.as_view()),  
    path('paciente/<int:pk>/', views.PacienteRetrieveUpdateView.as_view()), 
]
