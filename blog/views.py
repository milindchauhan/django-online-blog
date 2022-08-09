from django.shortcuts import render

posts = [
    {
        'author': 'Milind Chauhan',
        'title': 'blog-post-1',
        'content': 'this is a test blog post',
        'created': 'august 9th 2022',
    },
    {
        'author': 'Jane Doe',
        'title': 'blog-post-2',
        'content': 'this is a second test blog post',
        'created': 'august 9th 2022',
    },
]


# Create your views here.
def home(request):
    return render(request, "blog/home.html")

def about(request):
    return render(request, "blog/about.html")
