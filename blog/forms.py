from django import forms
from .models import Post,Comment,Footer
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

class FooterForm(forms.ModelForm):
    class Meta:
        model = Footer
        fields = ('content',)