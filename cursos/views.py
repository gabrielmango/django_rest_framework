from rest_framework import generics

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoListCreateAPIView(generics.ListCreateAPIView):
    """Handles listing and creating cursos."""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Handles retrieving, updating, and deleting a curso."""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacaoListCreateAPIView(generics.ListCreateAPIView):
    """Handles listing and creating avaliacoes."""
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class AvaliacaoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Handles retrieving, updating, and deleting an avaliacao."""
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
