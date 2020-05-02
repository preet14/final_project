from django.forms import ModelForm
from django import forms
from instructor.models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={'placeholder': 'text goes here', 'cols': '50', 'style': 'font-size:20px;'}))

    class Meta:
        model = Comment
        fields = ['content']
