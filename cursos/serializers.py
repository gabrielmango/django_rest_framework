from rest_framework import serializers

from .models import Avaliacao, Curso


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        extra_kwargs = {'email': {'write_only': True}}
        fields = (
            'id',
            'nome',
            'email',
            'curso',
            'avaliacao',
            'comentario',
            'criacao',
            'atualizacao',
            'ativo',
        )


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #Hyperlinked Related Field
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True,
        view_name='avaliacao-detail'
    )

    # Primary Key Related Field
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'url', 'criacao', 'atualizacao', 'ativo', 'avaliacoes')
