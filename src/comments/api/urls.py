from django.conf.urls import url

from .views import (
    CommentCreateAPIView,
    CommentListAPIView,
    CommentDetailAPIView,
)

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    url(r'^(?P<id>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
]
