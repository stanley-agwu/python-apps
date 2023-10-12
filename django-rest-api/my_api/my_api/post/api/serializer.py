from rest_framework import serializers

from post.models import Post, PostsRate

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'rates']
        extra_kwargs = {
            'rates': { 'read_only': True}
        }
        depth = 1

class PostsRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostsRate
        fields = ['id', 'likes', 'dislikes']