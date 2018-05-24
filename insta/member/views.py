from django.contrib.auth import get_user_model, authenticate, login as django_login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import SignupForm, LoginForm

User = get_user_model()


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('post_list')
        else:
            return HttpResponse('login credentials invalid!')
    else:
        # GET 요청에서는 Form 을 보여줌
        return render(request, 'member/login.html')


def signup(request):
    if request.method == "POST":
        # 데이터가 바인딩된 SignForm인스턴스를 생성
        form = SignupForm(request.POST)
        # 해당 form이 자신의 필드에 유효한 데이터를 가지고 있는지 검사
        if form.is_valid():
            # is_valid를 통해서 정제된 데이터(cleaned_data)에서 username과 password를 가져옴
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # 이미 username 항목이 주어진 username 값으로 존재하는 User가 있는지 검사
            user = User.objects.create_user(
                username=username,
                password=password,
            )
            return HttpResponse(f'{user.username}, {user.password}')
        print(form.cleaned_data)
        print(form.errors)
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'member/signup.html', context)
