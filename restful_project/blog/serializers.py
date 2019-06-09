from blog.models import Blog
from users.serializers import UserSerializer
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    """
    Serializer for Blog model
    """
    author = UserSerializer()

    class Meta:
        model = Blog
        fields = (
            "title",
            "content",
            "author",
            "date_created",
            "date_modified"
        )
