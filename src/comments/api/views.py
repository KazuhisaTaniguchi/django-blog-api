from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from rest_framework.mixins import (
    DestroyModelMixin,
    UpdateModelMixin
)
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from posts.api.permissions import IsOwnerOrReadOnly
from posts.api.pagination import (
    PostPageNumberPagination
)
from comments.models import Comment
from .serializers import (
    CommentListSerializer,
    CommentDetailSerializer,
    create_comment_serializer,
)


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        model_type = self.request.GET.get("type")
        slug = self.request.GET.get("slug")
        parent_id = self.request.GET.get("parent_id", None)
        return create_comment_serializer(
            model_type=model_type, slug=slug,
            parent_id=parent_id, user=self.request.user)


class CommentDetailAPIView(
        DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    queryset = Comment.objects.filter(id__gte=0)
    serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *arsg, **kwargs):
        return self.destroy(request, *arsg, **kwargs)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__first_name']
    pagination_class = PostPageNumberPagination

    def get_queryset(self):
        queryset_list = Comment.objects.filter(id__gte=0)
        query = self.request.GET.get("p")
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list
