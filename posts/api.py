from rest_framework import viewsets, permissions
from .serializers import PostSerializer
from rest_framework.response import Response
from .models import Post


# Post Viewset

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PostSerializer

    def list(self,request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
