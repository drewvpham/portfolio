from django.shortcuts import render, HttpResponse

def index(request):
    print ("Hello Wooooorld!")
    return render(request, 'portfolio/index.html')

def projects(request):
    print ("my projects route!")
    return render(request, 'portfolio/projects.html')


def about_me(request):
    print ("about me!testimonials")
    return render(request, 'portfolio/about_me.html')


def testimonials(request):
    return render(request, 'portfolio/testimonials.html')
