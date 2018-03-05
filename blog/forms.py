from django import forms
from .models import Post

class PostForm(forms.ModelForm): #Declare a class for a form of Post

    class Meta: # Set what
        model = Post
        fields = ('title', 'text',) #Note the fields are specified in strings!