from django.http import HttpResponse
from django.shortcuts import render
from .cards import cards
# Create your views here.


#http://127.0.0.1:8000
def home(request):
    #return HttpResponse("Hello World")
    return render(request, 'main/index.html', {'cards':cards})


# параметри url/id   url/title   rozetka.ua/tv
# query params       rozetka.ua?title=tv&start_price=3400&end_price=100000
#

def get_card(request, id):
    if id>0 and id<=len(cards):
        return render(request, 'main/card.html', {
            'card':cards[id-1],
            'title':f'Card {id}'
        })
    else:
        return HttpResponse("Not Found")


def about(request):
    #return HttpResponse("Hello World")
    text = 'Це сторінка про Нас. Це точно ця сторінка'
    frameworks = []
    return render(request, 'main/about.html',
                  {'text': text, 'frameworks': frameworks, 'cards':cards}  )

