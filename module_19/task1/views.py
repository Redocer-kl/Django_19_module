from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import UserRegister
from .models import *

def index(request):
    return render(request, "index.html")

def platform(request):
    return render(request, "platform.html")

def games(request):
    content = {"games":Game.objects.all()}
    return render(request, "games.html", content)


def cart(request):
    return render(request, "cart.html")


def sign_up_by_django(request):

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']

            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if Buyer.objects.filter(name=username).exists():
                return HttpResponse("Покупатель с таким именем уже существует.")


            Buyer.objects.create(name=username, age=int(request.POST.get('age')), balance=0)  # age можно получить из POST данных
            return HttpResponse("Успешно зарегестрировались")

    else:
        form = UserRegister()

    return render(request, 'registration_page.html')


def news(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 3)  # 10 новостей на странице
    page_number = request.GET.get('page')
    news_page = paginator.get_page(page_number)

    context = {
        'news': news_page,
    }
    return render(request, 'news.html', context)



