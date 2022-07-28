#from django.shortcuts import render

# Create your views here.

#def main(request):
#   return render(request, "main.html")

from django.shortcuts import redirect, render, get_object_or_404
from .forms import FreePostform
from .models import FreePost

def main(request):
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request, 'main.html', {'freeposts':freeposts})

def freepostcreate(request):
    if request.method == "POST":
        form = FreePostform(request.POST)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
            return redirect('main')
        
    else:
        form = FreePostform()
    return render(request, 'free_post_form.html', {'form':form})

def freedetail(request, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    return render(request, 'free_detail.html', {post_detail:post_detail})
