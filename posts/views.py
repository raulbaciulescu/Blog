from django import forms
from django.shortcuts import render, redirect

# Create your views here.
from django.template.defaultfilters import last
from django.urls import reverse
from django.views.generic import ListView, DetailView

from posts.models import Post, Comment


def index(request):
    return render(request, 'index.html', {})

class PostList(ListView):
    model = Post
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['a'] = Post.objects.all().reverse()[0]
        return context

class CommentForm(forms.Form):
    comment = forms.CharField()

class PostDetail(DetailView):
    model = Post

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(
                author=request.user,
                post=self.get_object(),
                text=comment_form.cleaned_data['comment']
            )
            comment.save()
        else:
            raise Exception
        return redirect(reverse('posts:detail', args=[self.get_object().id]))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

def search(request):
    if request.method == 'GET': #GET!!!
        post_name =  request.GET.get('search') # do some research what it does
        status = []
        try:
            status = Post.objects.filter(title__icontains=post_name) #returns a list
        except:
            pass
        return render(request,"search.html",{"posts": status})
    else:
        return render(request,"search.html",{})