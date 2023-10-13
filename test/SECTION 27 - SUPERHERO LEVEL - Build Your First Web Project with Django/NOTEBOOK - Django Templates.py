class Article(View)


class Article(View):
    def get(self, request):

        articles = [
            {
                "title": "Python 5 is officially announced",
                "category": "tech",
                "author": "Guido van Rossum",
                "content": "Just joking, we will have Python 3 for some years",
                "creation_date": datetime.now()
            },
            {
                "title": "Tesla goes bankrupt",
                "category": "auto",
                "author": "Elon Musk",
                "content": "Just trying to increase tesla share price here!",
                "created_at": datetime.now()
            }
        ]


return HttpResponse(articles)

The
articles.html
file

< !DOCTYPE
html >
< html
lang = "en" >
< head >
< meta
charset = "UTF-8" >
< title > Blog
articles(not fake) < / title >
< / head >
< body >
< ul >
{ %
for article in articles %}
< li >
< p > Title: {‌{article.title}} < / p >
< p > Category: {‌{article.category}} < / p >
< p > Created
by: {‌{article.author}} < / p >
< p > Posted
at: {‌{article.created_at}} < / p >
< / li >
{ % endfor %}
< / ul

< / body >
< / html >
