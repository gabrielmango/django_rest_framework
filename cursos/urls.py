from django.urls import path

from .views import (
    CursoListCreateAPIView,
    CursoRetrieveUpdateDestroyAPIView,
    AvaliacaoListCreateAPIView,
    AvaliacaoRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('cursos/<int:pk>/', CursoRetrieveUpdateDestroyAPIView.as_view(), name='curso'),
    path('cursos/', CursoListCreateAPIView.as_view(), name='cursos'),
    path('avaliacoes/<int:pk>/', AvaliacaoRetrieveUpdateDestroyAPIView.as_view(), name='avaliacao'),
    path('avaliacoes/', AvaliacaoListCreateAPIView.as_view(), name='avaliacoes'),
]

