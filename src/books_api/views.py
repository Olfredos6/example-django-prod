from rest_framework import viewsets
from rest_framework.response import Response
from website import models

from . import serializers


class BookViewSets(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def retrieve(self, requst, pk):
        book = models.Book.objects.get(id=pk)
        book.increment_view_count()
        return Response(serializers.BookSerializer(book).data)
