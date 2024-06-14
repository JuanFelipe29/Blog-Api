from rest_framework import serializers


from posts.models import Post
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source="user", read_only=True)
    category_data = CategorySerializer(source="category", read_only=True)

    class Meta:
        model = Post
        fields = ['title','content','slug','miniature','created_at','published','user','user_data','category','category_data']