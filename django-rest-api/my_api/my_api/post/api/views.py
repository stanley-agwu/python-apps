from rest_framework import viewsets
from rest_framework.response import Response

from post.models import Post, PostsRate
from .serializer import PostSerializer, PostsRateSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_rates = PostsRate.objects.create(likes=post_data['rates']['likes'], dislikes=post_data['rates']['dislikes'])
        new_rates.save()

        new_post = Post.objects.create(title=post_data['title'], body=post_data['body'], rates=new_rates)
        new_post.save()
        serializer = PostSerializer(new_post)

        return Response(serializer.data)

class PostsRateViewSet(viewsets.ModelViewSet):
    serializer_class = PostsRateSerializer
    queryset = PostsRate.objects.all()