from django.urls import path
from blog import views

urlpatterns =[
    path('blog/', views.home, name='home'),
    path('blog/post/new/', views.post_create, name="post-create"),
    path('blog/post/edit/', views.post_edit_form, name="post-edit"),
    path('blog/post/edit-success/', views.post_edit, name="post-edited"),
    path('blog/post/form/', views.post_form, name="post-form"),
    path('blog/post/<str:slug>/', views.post_detail, name='post-detail'),
    path('blog/post/<str:slug>/delete/', views.post_delete, name='post-delete'),
    path('blog/post/<str:slug>/delete/confirm/', views.post_delete_confirm, name="post-delete-confirm"),
    path('blog/post/search', views.search, name="search"),
    path('blog/my-posts', views.my_posts, name="my-posts"),
]