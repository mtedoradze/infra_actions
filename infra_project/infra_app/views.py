from django.http import HttpResponse


def index(request):
    return HttpResponse('Теперь за меня все делает скрипт!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
