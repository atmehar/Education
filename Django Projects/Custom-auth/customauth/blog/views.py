from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog


def blog_list(request):
    blogs = Blog.objects.filter(status=Blog.STATUS_PUBLISHED)
    return render(request, "blog_list.html", {"blogs": blogs})


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status=Blog.STATUS_PUBLISHED)
    return render(request, "blog_detail.html", {"blog": blog})


@login_required(login_url="login")
def my_blogs(request):
    blogs = Blog.objects.filter(author=request.user)
    return render(request, "my_blogs.html", {"blogs": blogs})


@login_required(login_url="login")
def blog_create(request):
    errors = []
    title = ""
    content = ""
    status = Blog.STATUS_PUBLISHED

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        status = request.POST.get("status", Blog.STATUS_PUBLISHED)

        if not title or not content:
            errors.append("Title and content are required.")

        if status not in dict(Blog.STATUS_CHOICES):
            status = Blog.STATUS_PUBLISHED

        if not errors:
            blog = Blog.objects.create(
                title=title,
                content=content,
                status=status,
                author=request.user,
            )
            return redirect("blog_detail", slug=blog.slug)

    context = {
        "is_edit": False,
        "errors": errors,
        "title": title,
        "content": content,
        "status": status,
        "blog": None,
    }
    return render(request, "blog_form.html", context)


@login_required(login_url="login")
def blog_edit(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    if blog.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this blog post.")

    errors = []
    title = blog.title
    content = blog.content
    status = blog.status

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        status = request.POST.get("status", Blog.STATUS_PUBLISHED)

        if not title or not content:
            errors.append("Title and content are required.")

        if status not in dict(Blog.STATUS_CHOICES):
            status = Blog.STATUS_PUBLISHED

        if not errors:
            blog.title = title
            blog.content = content
            blog.status = status
            blog.save()
            return redirect("blog_detail", slug=blog.slug)

    context = {
        "is_edit": True,
        "errors": errors,
        "title": title,
        "content": content,
        "status": status,
        "blog": blog,
    }
    return render(request, "blog_form.html", context)


@login_required(login_url="login")
def blog_delete(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    if blog.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this blog post.")

    if request.method == "POST":
        blog.delete()
        return redirect("blog_list")

    return render(request, "blog_confirm_delete.html", {"blog": blog})

