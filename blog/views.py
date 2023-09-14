from django.shortcuts import reverse, HttpResponseRedirect, render,redirect
from .models import*
from .forms import*
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Q

def index(request):
    blogtopics=BlogTopic.objects.all()
    archives=Archive.objects.all()
    context={
        'blogtopics':blogtopics,
        'archives':archives
    }
    return render(request,'blog/index.html',context)

def blogtopic(request,blogtopic_id):
    blogtopic=BlogTopic.objects.get(id=blogtopic_id)
    blogposts=blogtopic.blogpost_set.order_by('-created')
    context={
        'blogtopic':blogtopic,
        'blogposts':blogposts,
    }
    return render(request,'blog/blogtopic.html',context)

def new_post(request,blogtopic_id):
    blogtopic=BlogTopic.objects.get(id=blogtopic_id)
    if request.method!='POST':
        form=BlogPostForm()
    else:
        form=BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.blogtopic=blogtopic
            new_post.save()
            return HttpResponseRedirect(reverse('blogtopic',args=[blogtopic_id]))
    context={
        'blogtopic':blogtopic,
        'form':form

    }
    return render(request,'blog/new_post.html',context)

def register_request(request):
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful." )
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
        form = NewUserForm()
        return render (request=request, template_name="blog/register.html", context={"register_form":form})

def archives(request):
    return render(request,'blog/archives.html')



