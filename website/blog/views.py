from django.shortcuts import render

from website.blog.models import Article

def blog_pages(request, num="1"):
    count = 10 # Articles per page
    num = max(1, int(num))
    articles = Article.objects.order_by('-date')[count*(num-1):count*num]
    objects = {
        'articles' : articles,
        'pages' : range(1, 1 + Article.objects.all().count()/count),
    }
    return render(request, 'blog_index.html', objects)

def blog_entry(request, year='', month='', day='', slug=''):
    articles = Article.objects.all()
    if year:
        articles = articles.filter(date__year=year)
    if month:
        articles = articles.filter(date__month=month)
    if day:
        articles = articles.filter(date__day=day)
    if title:
        # Specific article
        article = articles.filter(slug=slug)[0]
        return render(request, 'blog_article.html', {'article' : article})
    else:
        # List of articles
        objects = {
            'articles' : articles,
        }
        return render(request, 'blog_index.html', objects)
