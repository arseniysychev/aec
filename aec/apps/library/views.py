from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .serializers import LibrarySerializer
from .models import Library


class LibraryViewSet(viewsets.ViewSet):
    queryset = Library.objects.all()

    def list(self, request):
        serializer = LibrarySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        lib = LibrarySerializer(data=request.data)
        if lib.is_valid():
            lib.save()
            return Response(lib.data, status=201)
        return Response(lib.errors, status=400)
