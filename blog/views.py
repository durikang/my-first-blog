from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from django.views.decorators.cache import never_cache
from django.core.paginator import Paginator
from django.middleware import csrf
from django.utils import timezone
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.contrib.auth.forms import AuthenticationForm

@never_cache
def post_list(request):
    notice_list = Post.objects.filter(is_notice=True, published_date__lte=timezone.now()).order_by('-published_date')
    content_list = Post.objects.filter(is_notice=False, published_date__lte=timezone.now()).order_by('-published_date')
    
    notice_paginator = Paginator(notice_list, 5)  # 공지사항 페이지당 5개의 게시글을 보여줍니다.
    content_paginator = Paginator(content_list, 5)  # 일반 게시판 페이지당 5개의 게시글을 보여줍니다.
    
    notice_page_number = request.GET.get('notice_page')
    notice_page_obj = notice_paginator.get_page(notice_page_number)
    
    content_page_number = request.GET.get('content_page')
    content_page_obj = content_paginator.get_page(content_page_number)
    
    form = AuthenticationForm()

    return render(request, 'blog/post/post_list.html', {
        'notice_page_obj': notice_page_obj,
        'content_page_obj': content_page_obj,
        'form' : form
    })

#게시글 상세보기 로직
@never_cache
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    
    # 중복 방문 체크
    session_key = f'post_viewed_{pk}'  # 세션 키 생성
    if not request.session.get(session_key, False):
        # 세션에 방문 기록이 없는 경우 조회수 증가
        post.increase_views()
        request.session[session_key] = True  # 세션에 방문 기록 저장
    
    return render(request, 'blog/post/post_detail.html', {'post': post, 'comments': comments})

#게시글 생성 로직
@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        
    return render(request, 'blog/post/post_create.html',{'form':form})

# 게시글 수정 로직
@login_required
def post_update(request,pk):
    post =get_object_or_404(Post, pk=pk)
    if request.method =="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance = post)
    return render(request, 'blog/post/post_update.html',{'form':form})

@login_required
def post_delete(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('post_list')

 
# 댓글 기능 로직(댓글 등록)
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    csrf_token = csrf.get_token(request)  # CSRF 토큰 얻기
    return render(request, 'blog/functions/add_comment_to_post.html', {'form': form, 'csrf_token': csrf_token})

# 댓글 관리 로직(댓글 승인)
@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

# 댓글 관리 로직(댓글 삭제)
@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail',pk=comment.post.pk)
