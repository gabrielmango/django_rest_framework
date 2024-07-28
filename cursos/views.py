from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializer, CursoSerializer

""" Version 1 of API """


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
                curso_id=self.kwargs.get('curso_pk'),
                pk=self.kwargs.get('avaliacao_pk'),
            )
        return get_object_or_404(
            self.get_queryset(), pk=self.kwargs.get('avaliacao_pk')
        )


""" Version 2 of API """


class CursoViewSet(viewsets.ModelViewSet):
    """View set for the Curso model."""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    """View set for the Avaliacao model."""

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
