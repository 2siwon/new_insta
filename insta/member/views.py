from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
User = get_user_model()


def signup(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            # 이미 username 항목이 주어진 username 값으로 존재하는 User가 있는지 검사
            if User.objects.filter(username=username).exists():
                return HttpResponse(f'username "{username}" is already exists!')
            user = User.objects.create_user(
               username=username,
               password=password
            )
            return HttpResponse(f'{user.username}, {user.password}')
    return render(request, 'member/signup.html')