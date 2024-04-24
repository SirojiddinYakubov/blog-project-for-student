from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, TagViewSet, CommentViewSet, FollowViewSet, ReactionViewSet, NotificationViewSet

router = DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'follows', FollowViewSet)
router.register(r'reactions', ReactionViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
