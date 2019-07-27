from crudApp import views
from django.urls import path

urlpatterns = [
    
    path('', views.index, name="index"), # Home 페이지  
    path('create/', views.create, name="create"), # 글 작성
    path('<int:blog_id>/', views.detail, name="detail"), # 상세보기
    path('show/', views.show, name="show"), # 목록보기
    path('<int:pk>/edit/', views.edit, name='edit'), # 수정
    path('<int:pk>/delete/', views.delete, name='delete') # 삭제
    
]
