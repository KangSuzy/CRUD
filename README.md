# Django / CRUD
---

> ###### *django 기본 환경 설정*

- 가상환경 및 장고 설치

```
python -m venv myvenv (생성)
source myvenv/Scripts/activate (실행)
pip install django (설치)
```

- Project & App 생성
```
django-admin startproject project명
python manage.py startapp app명
```

> ###### *Collectstatic*
- Django project와 app의 static 파일들을 settings.py STATIC_ROOT 로 옮김
```
python manage.py collectstatic
```
---
## CRUD
#### ==Create==
- urls.py path 설정
```
from django.contrib import admin
from django.urls import path,include
import crudApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crudApp.views.show, name="show"),
    path('crudApp/', include('crudApp.urls')),
]
```
- models.py class 작성
```
from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    update_Date = models.DateTimeField(auto_now=True)

def __str(self):
    return self.title

def summary(self):
    return self.body[:50]

```
###### *models.py 등록 후 ==migration== 필수 !!*
```
python manage.py makemigrations
python manage.py migrate
```
- forms.py (create / update)
###### *models.py 에서 정의한  class 중 입력받을 속성만 'field'에 작성*
```
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
```
- app/urls.py 작성
###### *각 url 의 어떤 templates/html 파일을 연결시킬지 작성*
```
from crudApp import views
from django.urls import path

urlpatterns = [  
    path('create/', views.create, name="create"), # 글 작성
    path('<int:blog_id>/', views.detail, name="detail"), # 상세보기
    path('show/', views.show, name="show"), # 목록보기
]
```
- views.py
###### *create() 함수 작성*
```
from django.shortcuts import render, get_object_or_404,redirect
from .forms import BlogForm
from .models import Blog
from django.utils import timezone

# Create your views here.

def create(request):
    if request.method == "POST":
        form = BlogForm(request.POST) # BlogForm 받은 데이터를 처리하기 위한 인스턴스 생성
        if form.is_valid(): # form 검증 메소드
            blog = form.save(commit = False) # blog 오브젝트를 form 으로부터 가져오지만, 실제 DB반영은 하지 않음
            blog.update_date = timezone.now()
            blog.save()
            return redirect('show') # url name 경로 대신
    else:
        form = BlogForm() # forms.py 의 BlogForm 클래스의 인스턴스
```
#### ==Read==
- views.py
###### *show() / detail() 함수 작성*
```
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog' : blog_detail})

def show(request):
    # 모든 글 대상
    blogs = Blog.objects.order_by('-id')    #id 반대로 / 글을 최신순으로
    return render(request, 'show.html', {'blogs':blogs})
```
#### ==Update==
- urls.py path 추가
```
urlpatterns = [  ...,
    path('<int:pk>/edit/', views.edit, name='edit'), # 수정
]
```
- views.py
###### *edit() 함수 추가*
```
def edit(request, pk):
    # url-> pk 받아 처리
    # 수정하고자 하는 글의 Post 모델 인스턴스를 가져온다
    # 원하는 글은 pk를 이용해찾음
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid(): # form 검증 메소드
            blog = form.save(commit = False)
            blog.update_date = timezone.now()
            blog.save()
            return redirect('show')
    else:
        form = BlogForm(instance = blog)
        return render(request, 'edit.html' , {'form':form})

```
- templates
###### *edit.html 추가 / detail.html와 연결*
```
{% extends 'base.html' %}
{% block content %}

<h1>create test</h1>

<div class = 'container'>
    <form method = 'POST'>
        {% csrf_token %}
        <table>
            {{form.as_table}}
        </table>
        <br>
        <input class="btn bin-dark" type="submit" value="수정">
    </form>
</div>

{% endblock %}
```
#### ==Delete==
###### *detail.html과 연결*
```
<a href="{% url 'delete' pk=blog.pk %}"> 삭제 </a>
```
- urls.py path 추가
```
urlpatterns = [  ...,
   path('<int:pk>/delete/', views.delete, name='delete') # 삭제
]
```
- views.py
###### *delele() 함수 작성*
```
def delete(request, pk):
        blog = Blog.objects.get(id=pk)
        blog.delete()
        return redirect('show')
```
