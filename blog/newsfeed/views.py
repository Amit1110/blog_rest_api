from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm

def post_put(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        object = form.save(commit=False)
        object.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(object.get_absolute_url())
    else:
        messages.success(request, "Not Successfully Created")
    #we can use below as well
    #if request.method == "POST":
     #   print(request.POST)
      #  print(request.POST.get("title"))
       # print(request.POST.get("text"))
        #Post.objects.create(title=title)

    context = {
        'form': form,
    }
    return render(request, 'post_put.html', context)

def edit(request, pk=None):
    obj = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        object = form.save(commit=False)
        object.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(object.get_absolute_url())#redirecting the page after submission here

    context = {
        'title': obj.title,
        'obj': obj,
        'form': form,
    }
    return render(request, 'post_put.html', context)

def list(request):
    queryset = Post.objects.all()
    context = {
        'objects': queryset,
        'title': 'All the Posts are',
    }
    return render( request, 'index.html', context)

def detail(request, pk):
    obj = get_object_or_404(Post, pk=pk)
    context = {
        'obj': obj,
    }
    return render(request, 'detail.html', context)

def delete(request, pk=None):
    obj = get_object_or_404(Post, pk=pk)
    obj.delete()
    return redirect('newsfeed:list')


