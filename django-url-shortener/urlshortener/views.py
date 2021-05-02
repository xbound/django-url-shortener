import re
from django.shortcuts import render, redirect, reverse
from django.http import HttpRequest, JsonResponse, HttpResponseBadRequest, Http404
from django.views.decorators.http import require_http_methods

from .models import Url

@require_http_methods(['GET'])
def default_view(request: HttpRequest):
    return render(request, 'urlshortener/default.html')

@require_http_methods(['POST'])
def shorten_url(request: HttpRequest):
    url = request.POST.get('url')
    if not url:
        return HttpResponseBadRequest()
    if not re.findall(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)', url):
        return HttpResponseBadRequest("Incorrect URL format")
    shortened_url = Url.objects.create_or_get(url=url)
    return JsonResponse({'shortened_url': reverse('urlshortener:go_to', kwargs={'hashed_value': shortened_url.hashed_url})})


@require_http_methods(['GET'])
def go_to_url(request: HttpRequest, hashed_value):
    try:
        shorted_url = Url.objects.get(hashed_url=hashed_value)
    except Url.DoesNotExist:
        raise Http404()
    return redirect(shorted_url.url)