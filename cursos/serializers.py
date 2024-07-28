from rest_framework import serializers
from django.db.models import Avg

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

    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError(
            'A avaliação precisa ser um inteiro entre 1 e 5!'
        )


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # Hyperlinked Related Field
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='avaliacao-detail'
    )

    # Primary Key Related Field
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'atualizacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes',
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get(
            'avaliacao__avg'
        )

        if media is None:
            return 0
        return round(media * 2) / 2