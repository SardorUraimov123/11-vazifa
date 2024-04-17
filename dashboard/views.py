from django.shortcuts import render, redirect
from django.contrib import messages
from main import models
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard/index.html')

def log_in(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'Login was successful')
                return redirect('dashboard')
            else:
                return render(request,'dashboard/auth/login.html')
        except:
            messages.error(request,'Login failed')
            return redirect('login')
    return render(request,'dashboard/auth/login.html')

# def register(request):
#     if request.method == 'POST':
#         try:
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             password_confirm = request.POST.get('password_confirm')
#             if password == password_confirm:
#                 User.objects.create_user(username=username, password=password)
#                 user = authenticate(username=username, password=password)
#                 login(request, user)
#                 messages.success(request,'Registration was successful')
#                 return redirect('dashboard')
#         except:
#             messages.error(request,'Registration failed')
#             return redirect('register')
#     return render(request,'dashboard/auth/register.html')

def log_out(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def create_category(request):
    regions = models.Region.objects.all()
    categories = models.Category.objects.all()
    try:
        if request.method == 'POST':
            name = request.POST['name']
            models.Category.objects.create(name=name)
            messages.success(request,'Successfully created category')
            return redirect('list-category')
    except:
        messages.error(request, ('Error creating category'))
    context = {'regions': regions, 'categories': categories}
    return render(request,'dashboard/category/create.html',context)

@login_required(login_url='login')
def list_category(request):
    categories = models.Category.objects.all()
    context = {'categories': categories}
    return render(request,'dashboard/category/list.html', context)

@login_required(login_url='login')
def edit_category(request, id):
    category = models.Category.objects.get(id=id)
    try:
        if request.method == 'POST':
            name = request.POST['name']
            category.name = name
            category.save()
            messages.success(request,'Successfully edited category')
            return redirect('list-category')
    except:
        messages.error(request, ('Error editing category'))
    context = {'category': category}
    return render(request,'dashboard/category/edit.html',context)

@login_required(login_url='login')
def delete_category(request, id):
    models.Category.objects.get(id=id).delete()
    messages.success(request,'Successfully deleted')
    return redirect('list-category')

@login_required(login_url='login')
def create_region(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            models.Region.objects.create(name=name)
            messages.success(request,'Successfully created region')
            return redirect('list-region')
    except:
        messages.error(request, ('Error creating region'))
    return render(request,'dashboard/region/create.html')

@login_required(login_url='login')
def list_region(request):
    regions = models.Region.objects.all()
    context = {'regions': regions}
    return render(request,'dashboard/region/list.html', context)

@login_required(login_url='login')
def edit_region(request, id):
    region = models.Region.objects.get(id=id)
    try:
        if request.method == 'POST':
            name = request.POST['name']
            region.name = name
            region.save()
            messages.success(request,'Successfully edited region')
            return redirect('list-region')
    except:
        messages.error(request, ('Error editing region'))
    context = {'region': region}
    return render(request,'dashboard/region/edit.html',context)

@login_required(login_url='login')
def delete_region(request, id):
    models.Region.objects.get(id=id).delete()
    messages.success(request,'Successfully deleted')
    return redirect('list-region')

@login_required(login_url='login')
def create_post(request):
    regions = models.Region.objects.all()
    categories = models.Category.objects.all()
    try:
        if request.method == 'POST' and request.FILES:

            category_id = request.POST['category_id']
            region_id = request.POST['region_id']
            author_username = request.user

            author = models.User.objects.get(username=author_username)
            region = models.Region.objects.get(id=region_id)
            category = models.Category.objects.get(id=category_id)
            title = request.POST['title']
            body = request.POST['body']
            date = request.POST['date']
            banner_img = request.FILES['file']
            models.Post.objects.create(
                author = author, 
                title=title, 
                body=body,
                date=date,
                banner_img=banner_img,
                category=category,
                region=region
                )
            messages.success(request,'Successfully created post')
            return redirect('list-post')
    except:
        messages.error(request, ('Error creating post'))
    context = {'regions': regions, 'categories': categories}
    return render(request, 'dashboard/post/create.html',context)

@login_required(login_url='login')
def list_post(request):
    posts = models.Post.objects.all()
    context = {'posts': posts}
    return render(request, 'dashboard/post/list.html', context)

@login_required(login_url='login')
def edit_post(request,id):
    post = models.Post.objects.get(id=id)
    regions = models.Region.objects.all()
    categories = models.Category.objects.all()
    try:
        if request.method == 'POST':
            category_id = request.POST.get('category_id')
            region_id = request.POST.get('region_id')

            post.title = request.POST.get('title')
            post.category = models.Category.objects.get(id=category_id)
            # print(post.category)
            post.region = models.Region.objects.get(id=region_id)
            post.body = request.POST.get('body')
            post.date = request.POST.get('date')
            if request.FILES:
                post.banner_img = request.FILES['file']
            post.save()
            messages.success(request,'Successfully updated')
            redirect('list-post')
    except:
        messages.error(request,'Updating failed')
        redirect('list-post',post.id)
    context = {'post':post, 'regions': regions, 'categories': categories}
    return render(request, 'dashboard/post/edit.html',context)

@login_required(login_url='login')
def delete_post(request, id):
    models.Post.objects.get(id=id).delete()
    messages.success(request,'Successfully deleted')
    return redirect('list-post')
