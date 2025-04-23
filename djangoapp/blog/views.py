from django.shortcuts import render
from django.core.paginator import Paginator


posts = list(range(1000))


def index(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request=request,
        template_name='blog/pages/index.html',
        context={
            'page_obj': page_obj
            },
    )


def page(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request=request,
        template_name='blog/pages/page.html',
        context={
            # 'page_obj': page_obj
            },
    )


def post(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request=request,
        template_name='blog/pages/post.html',
        context={
            # 'page_obj': page_obj
            },
    )
