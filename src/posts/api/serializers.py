from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)
from accounts.api.serializers import UserDetailSerializer
from comments.api.serializers import CommentSerializer
from comments.models import Comment
from posts.models import Post


post_detail_url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug'
)


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'publish'
        )


class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    delete_url = HyperlinkedIdentityField(
        view_name='posts-api:delete', lookup_field='slug')
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()
    html = SerializerMethodField()
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'id',
            'url',
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
    url = post_detail_url
    # Fieldに特定の処理をして返したい場合
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'url',
            'user',
            'title',
            'content',
            'publish'
        )
