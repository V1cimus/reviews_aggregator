from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.v1.views import (
    CategoryViewSet,
    GenreViewSet,
    TitleViewSet,
    ReviewViewSet,
    CommentViewSet,
    UsersViewSet,
    auth_signup_post,
    get_token_post,
)


v1_router = DefaultRouter()
v1_router.register("categories", CategoryViewSet)
v1_router.register("genres", GenreViewSet)
v1_router.register("titles", TitleViewSet)
v1_router.register(
    r"titles/(?P<title_id>\d+)/reviews", ReviewViewSet, basename="reviews"
)
v1_router.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentViewSet,
    basename="comments",
)
v1_router.register("users", UsersViewSet)

auth_url = [
    path("token/", get_token_post, name="token"),
    path("signup/", auth_signup_post, name="signup"),
]

urlpatterns = [
    path("auth/", include(auth_url)),
    path("", include(v1_router.urls)),
]
