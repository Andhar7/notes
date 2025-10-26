# Views serve for working with API requests

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer, NoteCreateSerializer, NoteUpdateSerializer

# Create your views here.
class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()

    def get_serializer_class(self):
        # Return data from a POST request
        if self.request.method == 'POST':
            return NoteCreateSerializer
        return NoteSerializer

    def get(self, request, *args, **kwargs):
        # Return cached data from a GET request
        return super().get(request, *args, **kwargs)

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return NoteUpdateSerializer
        return NoteSerializer

    def update(self, request, *args, **kwargs):
        # Update with validating data
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': 'Note deleted successfully'},
            status=status.HTTP_204_NO_CONTENT,
        )






















