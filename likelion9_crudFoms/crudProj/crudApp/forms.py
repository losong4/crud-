from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post # Post라는 모델을 참고하여 Form을 만들었음
        fields = ['title', 'writer', 'body'] # Post라는 모델의 값 중 title, writer, body라는 항목을 입력 받음
