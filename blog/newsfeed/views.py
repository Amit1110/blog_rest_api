from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
from .serializers import PostSerializer

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



class PostList(APIView):
    def get(self, request, format=None):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def PostDetail(request, pk, format = None):
    obj = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        serializer = PostSerializer(obj)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PostSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

