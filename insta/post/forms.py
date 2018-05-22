from django import forms

__all__ = (
    'PostForm',
)


class PostForm(forms.Form):
    photo = forms.ImageField()
    text = forms.CharField(
        max_length=5,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
            }
        )
    )

    def clean_text(self):
        data = self.cleaned_data['text']
        if data != data.upper():
            raise forms.ValidationError('All text must uppercase!')
        return data


class CommentForm(forms.Form):
    content = forms.CharField(
        # 엔터가능
        widget=forms.Textarea(
            # 부트스트랩 클래스(form-control) 사용
            attrs={
                'class': 'form-control',
            }
        ),
    )
