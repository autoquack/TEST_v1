articles.html - to add in between the body tags

<form action="" method="post">
    {% csrf_token %}
    <label for="title">Title: </label>
    <input id="title" type="text" name="title">
    <label for="category">Category: </label>
    <input id="category" type="text" name="category">
    <label for="author">Author: </label>
    <input id="author" type="text" name="author">
    <label for="content">Content: </label>
    <textarea id="content" name="content" rows="4" cols="50"> </textarea>
    <input type="submit" value="Create Article">
</form>
or:

<form action="" method="post">
    {% csrf_token %}
    {‌{ form }}
    <input type="submit" value="Create Article">
</form>


articles.html - to add in between the head tags

<style>
    input {display: block;}
    textarea {display: block;}
</style>
