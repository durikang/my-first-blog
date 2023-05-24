from django import forms
from .models import Post,Comment
#게시글 폼
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
#댓글 폼
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','text',)
