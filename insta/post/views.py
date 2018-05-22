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