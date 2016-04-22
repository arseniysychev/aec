from rest_framework import serializers

from aec.apps.vocabulary.models import Word


class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'
