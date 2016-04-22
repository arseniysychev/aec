from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

from .serializers import DictionarySerializer
from .models import Word


class VocabularyViewSet(viewsets.ViewSet):
    queryset = Word.objects.all()

    def initial(self, request, *args, **kwargs):
        super(VocabularyViewSet, self).initial(request, *args, **kwargs)
        if 'lib' in request.query_params:
            libs = request.query_params.getlist('lib')
            self.queryset = self.queryset.filter(library__in=libs)

    def list(self, request):
        serializer = DictionarySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    @list_route(methods=['get'], url_path='random')
    def random_word(self, request):
        if 'id' in request.query_params:
            if 'released' in request.session:
                request.session.modified = True
                request.session['released'].append(request.query_params['id'])
            else:
                request.session['released'] = [request.query_params['id']]

        if 'released' in request.session:
            self.queryset = self.queryset.exclude(
                pk__in=request.session['released']
            )

        ids = self.queryset.values_list('id', flat=True)
        random_item = Word.objects.random_item(ids)
        if random_item:
            serializer = DictionarySerializer(random_item)
            return Response(serializer.data)
        else:
            if 'released' in request.session:
                del request.session['released']
            return Response(status=204)
