# urls.py
from django.urls import path
from .views import (
    BlogPostsList,
    BlogPostsLatest,
    BlogPostsFeaturedInLatest,
    BlogPostsDetails,
    BlogPostsCategory,
    BlogPostsHero,
    BlogPostsFeaturedInHero,
    BlogPostsPopular,
    CategoryPostsForHomepage,
)



urlpatterns = [
    path('api/posts', BlogPostsList.as_view(), name='blog_posts_list'),
    path('api/posts/latest', BlogPostsLatest.as_view(), name='blog_posts_latest'),
    path('api/posts/hero', BlogPostsHero.as_view(), name='blog_posts_hero'),
    path('api/posts/popular', BlogPostsPopular.as_view(), name='blog_posts_popular'),
    path('api/posts/category', BlogPostsCategory.as_view(), name='blog_posts_category'),
    path('api/posts/latest/featured', BlogPostsFeaturedInLatest.as_view(), name='blog_posts_featured_in_latest'),
    path('api/posts/hero/featured', BlogPostsFeaturedInHero.as_view(), name='blog_posts_featured_in_hero'),
    path('api/posts/<slug:slug>', BlogPostsDetails.as_view(), name='blog_post_detail'),
    path('api/posts/category/<str:category>', CategoryPostsForHomepage.as_view(), name='category_posts_for_homepage'),
]
