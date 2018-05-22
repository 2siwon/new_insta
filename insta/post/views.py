from django.shortcuts import render

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
        # Post.objects.create(photo=request.photo)
        print(request.POST)
        print(request.FILES)
    elif request.method == 'GET':
        return render(request, 'post/post_create.html')