from django.shortcuts import render

posts = [
    {
        'author': 'Milind Chauhan',
        'title': 'Blog Post 1',
        'content': 'this is a test blog post',
        'created': 'August 9th, 2022',
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'this is a second test blog post',
        'created': 'August 9th, 2022',
    },
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {'title': 'About'})
