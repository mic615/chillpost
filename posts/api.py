from rest_framework import viewsets, permissions
from .serializers import PostSerializer

# Post Viewset

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
