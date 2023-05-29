from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.urls import include, path

urlpatterns = [
    path('', views.post_list, name ='post_list'),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    path('footer/', views.index_footer, name ='index_footer'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_update, name='post_update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/comment/', views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove,name='comment_remove'),

]  
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
