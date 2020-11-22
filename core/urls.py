from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('aulas/', AulasView.as_view(), name='aulas'),
    path('monitores/', MonitoresView.as_view(), name='monitores'),
    path('eventos/', EventosView.as_view(), name='eventos'),
]
