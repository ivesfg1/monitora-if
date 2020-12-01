from django.urls import path

from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('aulas/', AulasView.as_view(), name='aulas'),

    path('monitores/', MonitoresListView.as_view(), name='monitores'),
    path('monitores/<uuid:pk>/', MonitoresDetailView.as_view(), name='monitores-detail'),
    path('monitores/create/', MonitoresCreateView.as_view(), name='monitores-create'),

    path('eventos/', EventosView.as_view(), name='eventos'),

    # login e logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
