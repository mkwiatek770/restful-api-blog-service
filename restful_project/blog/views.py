from blog.models import Blog
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from blog.serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to view blogs or edit blogs
    """
    # permission_classes = (IsAuthenticated,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Blog.objects.all().order_by("-date_created")
    serializer_class = BlogSerializer
