from django.forms import ModelForm
from django import forms
from instructor.models import FileUpload


class FileForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['courseName', 'topic', 'content', 'filename', 'filepath']


class ChangeFileForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['topic', 'content', 'filename', 'filepath']


from instructor.models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={'placeholder': 'text goes here', 'cols': '50', 'style': 'font-size:20px;'}))

    class Meta:
        model = Comment
        fields = ['content']
