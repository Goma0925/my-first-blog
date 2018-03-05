from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm #Get PostForm from forms.py
# ----------
from django.http import HttpResponse
from django.template import loader, Context

def post_list(request): #Django gets up until here!!
    #Check the syntax blow
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #Reference in Querysets chapter
    template = loader.get_template("blog/post_list.html")
    context = {'posts': posts}
    return HttpResponse(template.render(context))
#take request, return blog/post_list.html(template)


def post_new(request):
    form = PostForm() #Don't forget to put brackets
    return render(request, 'blog/post_edit.html', {'form': form})