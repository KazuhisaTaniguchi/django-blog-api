from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)

from comments.api.serializers import CommentSerializer
from comments.models import Comment
from posts.models import Post


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'publish'
        )


class PostDetailSerializer(ModelSerializer):
    delete_url = HyperlinkedIdentityField(
        view_name='posts-api:delete', lookup_field='slug')
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'slug',
            'image',
            'content',
            'html',
            'publish',
            'delete_url',
            'comments'
        )

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_html(self, obj):
        return obj.get_markdown()

    def get_comments(self, obj):
        content_type = obj.get_content_type
        object_id = obj.id
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments


class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='posts-api:detail', lookup_field='slug')
    # Fieldに特定の処理をして返したい場合
    user = SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'url',
            'user',
            'title',
            'content',
            'publish',
        )

    def get_user(self, obj):
        return str(obj.user.username)
