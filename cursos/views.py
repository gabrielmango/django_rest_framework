from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializer, CursoSerializer


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

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return Avaliacao.objects.filter(curso=self.kwargs.get('curso_pk'))
        return Avaliacao.objects.all()


class AvaliacaoRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    """Handles retrieving, updating, and deleting an avaliacao."""

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(
                self.get_queryset(),
                curso_id = self.kwargs.get('curso_pk'),
                pk=self.kwargs.get('avaliacao_pk')
            )
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
