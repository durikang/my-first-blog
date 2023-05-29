from django import forms
from .models import Post,Comment
# from ckeditor.widgets import CKEditorWidget
#게시글 폼
class PostForm(forms.ModelForm):
    # text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ('title', 'text',)
#댓글 폼
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','text',)
