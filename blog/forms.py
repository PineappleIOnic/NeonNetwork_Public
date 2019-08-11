from django import forms
from .models import BlogPosts
import markdownx

class post_create(forms.ModelForm):

    class Meta:
        model = BlogPosts
        fields = ('title', 'post_content')

    #post_content.widget.attrs.update({'class':'card bg-light mb-3','style':'height: 200px; width: 400px;',})
    #title.widget.attrs.update({'style':'width: 400px; height: 30px;',})
