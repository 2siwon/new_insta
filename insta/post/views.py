from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm, CommentForm
from .models import Post, PostComment


def post_list(request):
    """
    모든 포스트 목록 리턴
    :param request:
    :return:
    """
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'post/post_list.html', context)


def post_create(request):
    """
    포스트를 생성
    반드시 photo필드에 해당하는 파일이 와야한다.
    :param request:
    :return:
    """
    if request.method == 'POST':
        # POST 요청의 경우 PostForm 인스턴스 생성과정에서 request.POST, request.FILES 사용
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['photo']
            post = Post.objects.create(photo=photo)
            return HttpResponse(f'<img src={post.photo.url}>')

    else:
        # GET 요청일 경우 빈 Form 전달
        form = PostForm()

    # GET 요청 무조건 실행
    # POST 요청에선 form.is_valid() 통과하지 못하면 이 부분 실행
    context = {
        'form': form,
    }
    return render(request, 'post/post_create.html', context)


def post_detail(request, post_pk):
    if request.method == 'GET':
        # post = Post.objects.create(pk=post_pk)
        post = get_object_or_404(Post, pk=post_pk)
        comment_form = CommentForm()
        context = {
            'post': post,
            'comment_form': comment_form,
        }
        return render(request, 'post/post_detail.html', context)

    else:
        return render(request, 'post/post_list.html')


def comment_create(request, post_pk):
    """
    post_pk에 해당하는  Post에 PostComment를 작성
    :param request:
    :param post_pk:
    :return:
    """
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            PostComment.objects.create(
                post=post,
                content=form.cleaned_data['content'],
            )
            next = request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('post_detail', post_pk=post_pk)
