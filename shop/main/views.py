import datetime as dt

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import messages
from .cards import cards

from .forms import QuestionnaireForm
from .models import Card, Tag, QuestionnaireResponse


# Create your views here.


#http://127.0.0.1:8000
def home(request: HttpRequest) -> HttpResponse:
    #return HttpResponse("Hello World")
    return render(request, 'main/index.html', {'cards':cards})


# параметри url/id   url/title   rozetka.ua/tv
# query params       rozetka.ua?title=tv&start_price=3400&end_price=100000
#

def get_card(request: HttpRequest, id: int) -> HttpResponse:

    if request.GET.get('title'):
        title = request.GET.get('title')
    if id>0 and id<=len(cards):
        return render(request, 'main/card.html', {
            'card':cards[id-1],
            'title':f'{title if title else "Card "+id}'
        })
    else:
        return HttpResponse("Not Found")

def get_card_by_title(request: HttpRequest) -> HttpResponse:
    title = None
    if request.method=='GET' and  request.GET.get('title'):
        title = request.GET.get('title')

    elif request.method=='POST':
        title = request.POST.get('title')
    if title is not None:
        return JsonResponse({'title': title})
    else:
        return HttpResponse("Not Found")

def about(request: HttpRequest) -> HttpResponse:
    #return HttpResponse("Hello World")
    text = 'Це сторінка про Нас. Це точно ця сторінка'
    frameworks = []
    return render(request, 'main/about.html',
                  {'text': text, 'frameworks': frameworks, 'cards':cards,
                   'data':[1,2,105,102,7,10,100]}  )


def questions(request: HttpRequest) -> HttpResponse:
    form = QuestionnaireForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST' and form.is_valid():
        # Зберігаємо відповіді лише після успішної перевірки всіх полів.
        QuestionnaireResponse.objects.create(**form.cleaned_data)
        messages.success(request, 'Дякуємо! Ваші відповіді збережено.')
        form = QuestionnaireForm()
    return render(request, 'main/questions.html', {'form': form})


def create_card(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        #TODO:image.name поміняти при збережені (add datetime, uuid)
        #TODO:перевірити чи дійсно це малюнок за ext і розмір
        # print(image.name, image.size)
        # print(title,description,image)
        card = Card(
            title=title,
            description=description,
            image=image,
            created_at=dt.datetime.now(),
            )
        card.save()
    return JsonResponse({'message':'ok'})
#TODO: Створити модель User (повинна містити поле avatar)
#Додати можливість при реєстрації користувача завантажити
#його аватар
#Роботу з моделлю винести в окремий сервіс


def test_create(_request: HttpRequest) -> HttpResponse:
    card = Card(
        title='test card',
        description='test description',
        image='test_image.png',
        created_at=dt.datetime.now(),
    )
    card.save()
    tag = Tag.objects.create(
        name='test_tag',
    )
    card.tags.add(tag)

    return HttpResponse("ok")