from django.shortcuts import render, get_object_or_404,redirect
from .forms import BlogForm
from .models import Blog
from django.utils import timezone

# Create your views here.

def index(request):
        return render(request, 'index.html');

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
        return render(request, 'create.html', {'form' : form})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog' : blog_detail})

def show(request):
    # 모든 글 대상
    blogs = Blog.objects.order_by('-id')    #id 반대로 / 글을 최신순으로
    return render(request, 'show.html', {'blogs':blogs})


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

def delete(request, pk):
        blog = Blog.objects.get(id=pk)
        blog.delete()
        return redirect('show')