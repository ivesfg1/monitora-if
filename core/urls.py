from django.urls import path

from django.contrib.auth import views as auth_views
from core import views

# urlpatterns = [
#     path('', IndexView.as_view(), name='index'),
#     path('aulas/', AulasView.as_view(), name='aulas'),
#
#     path('monitores/', MonitoresListView.as_view(), name='monitores'),
#     path('monitores/<uuid:pk>/', MonitoresDetailView.as_view(), name='monitores-detail'),
#     path('monitores/create/', MonitoresCreateView.as_view(), name='monitores-create'),
#
#     path('eventos/', EventosView.as_view(), name='eventos'),
#
# ]

urlpatterns = [
    path('', views.index, name='index'),

    # Monitores
    path('monitores/', views.monitores_list, name='monitores'),
    path('monitores/create/', views.monitores_create, name='monitores-create'),

    # Login e Logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
