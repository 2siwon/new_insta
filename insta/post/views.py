from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import PostForm
from .models import Post


def post_list(request):
    """
    모든 포스트 목록 리턴
    :param request:
    :return:
    """
    posts = Post.objects.all()
    context = {
        'posts': posts,
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
        post = Post.objects.get(pk=post_pk)
        context = {
            'post': post,
        }
        return render(request, 'post/post_detail.html', context)
    else:
        return render(request, 'post/post_list.html')
