from django.urls import path

from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('', views.index, name='index'),

    # Monitores
    path('monitores/', views.monitores_list, name='monitores'),
    path('monitores/create/', views.monitores_create, name='monitores-create'),
    path('monitores/<uuid:pk>/', views.monitores_detail, name='monitores-detail'),
    path('monitores/<uuid:pk>/update', views.monitores_update, name='monitores-update'),
    path('monitores/<uuid:pk>/delete', views.monitores_delete, name='monitores-delete'),

    # Outros
    path('home/', views.home, name='home'),

    # Login e Logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
