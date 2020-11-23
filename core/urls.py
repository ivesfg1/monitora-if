from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('aulas/', AulasView.as_view(), name='aulas'),

    path('monitores/', MonitoresListView.as_view(), name='monitores'),
    path('monitores/<int:pk>/', MonitoresDetailView.as_view(), name='monitores-detail'),
    path('monitores/create/', MonitoresCreateView.as_view(), name='monitores-create'),

    path('eventos/', EventosView.as_view(), name='eventos'),
    path('login/', LoginView.as_view(), name='login')
]
