from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .serializers import DictionarySerializer
from .models import Dictionary


class DictionaryViewSet(viewsets.ViewSet):
    queryset = Dictionary.objects.all()

    def list(self, request):
        del request.session['released']
        serializer = DictionarySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    @list_route(methods=['get'], url_path='random')
    def random_word(self, request):
        if 'released' in request.session:
            print request.session['released']
            self.queryset = self.queryset.exclude(
                pk__in=request.session['released']
            )
        ids = self.queryset.values_list('id', flat=True)
        random_item = Dictionary.objects.random_item(ids)
        if random_item:
            if 'released' in request.session:
                request.session.modified = True
                request.session['released'].append(random_item.id)
            else:
                request.session['released'] = [random_item.id]

            serializer = DictionarySerializer(random_item)
            return Response(serializer.data)
        else:
            del request.session['released']
            return Response(status=204)
