Final
version
of
articles.html

< !DOCTYPE
html >
< html
lang = "en" >
< head >
< meta
charset = "UTF-8" >
< title > Blog
articles(not fake) < / title >
< style >
input
{display: block;}
textarea
{display: block;}
< / style >
< / head >
< body >
< form
action = ""
method = "post" >
{ % csrf_token %}
{‌{form}}
< input
type = "submit"
value = "Create Article" >
< / form >

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
< a
href = "http://localhost:8080/blog/articles/{‌{ article.id }}" > Read
the
article < / a >
< / li >
{ % endfor %}
< / ul >
< / body >
< / html >