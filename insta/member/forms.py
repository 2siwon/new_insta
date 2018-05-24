from django import forms
from django.contrib.auth import get_user_model, authenticate, login as django_login

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    # clean_<field_name>과 같이 하나의 필드가 아니고
    # 동시에 여러필드(form 자체)에 대한 validation
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        # authenticate 성공시 유저 객체 반환
        self.user = authenticate(
            username=username,
            password=password,
        )

        if not self.user:
            raise forms.ValidationError(
                'Invalid login credentials'
            )
        else:
            # 자기자신에게 login 이란 메서드를 추가
            setattr(self, 'login', self._login)

    # 인증에 성공하면 user 변수에 User 객체 할당
    def _login(self, request):
        # 인증이 되면 django session 에 해당 User 정보추가,
        # Response 시 set-cookie 헤더에 세션키값을 담아서 보냄
        # 이후 브라우저와의 요청 응답 시 로그인 유지
        django_login(request, self.user)


class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    # clean_<field_name>
    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError(f'Username {data} is already exists!')
        return data
