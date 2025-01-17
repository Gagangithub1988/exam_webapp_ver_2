from django import forms
class EmailSendForm(forms.Form):
    name=forms.CharField(max_length=256)
    email=forms.EmailField()
    to=forms.EmailField()
    comment=forms.CharField(widget=forms.Textarea,required=False)

from blogApp.models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')
