#how to implimate the searching function by keyword

from . import Blog


def search(request):
    keyword = request.GET.get('keyword')

    blog = Blog.objects.filter(q(title__icontains=keyword) | Q(short_description__icontains=keyword), Q(blog_body__icontains=keyword) status='Published')


    context = {
        "blog": blog,
        'keyword':keyword,
    }
    return render(request, 'search.html', context)