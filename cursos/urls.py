from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    AvaliacaoListCreateAPIView,
    AvaliacaoRetrieveUpdateDestroyAPIView,
    AvaliacaoViewSet,
    CursoListCreateAPIView,
    CursoRetrieveUpdateDestroyAPIView,
    CursoViewSet,
)

router = SimpleRouter()

router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path(
        'cursos/<int:pk>/',
        CursoRetrieveUpdateDestroyAPIView.as_view(),
        name='curso',
    ),
    path('cursos/', CursoListCreateAPIView.as_view(), name='cursos'),
    path(
        'cursos/<int:curso_pk>/avaliacoes/',
        AvaliacaoListCreateAPIView.as_view(),
        name='cursos_avaliacoes',
    ),
    path(
        'cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/',
        AvaliacaoRetrieveUpdateDestroyAPIView.as_view(),
        name='cursos_avaliacoes',
    ),
    path(
        'avaliacoes/<int:avaliacao_pk>/',
        AvaliacaoRetrieveUpdateDestroyAPIView.as_view(),
        name='avaliacao',
    ),
    path(
        'avaliacoes/', AvaliacaoListCreateAPIView.as_view(), name='avaliacoes'
    ),
]
