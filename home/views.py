from django.shortcuts import render, redirect
from .models import ShortURL
from django.http import Http404

def index(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        short_url = ShortURL(original_url=original_url)
        short_url.short_code = ShortURL.generate_short_code()
        short_url.save()
        return redirect('result', short_code=short_url.short_code)
    return render(request, "home/index.html")

def result(request, short_code):
    try:
        short_url = ShortURL.objects.get(short_code=short_code)
        context = {'short_url': short_url, 'domain': request.get_host()}
        return render(request, "home/result.html", context)
    except ShortURL.DoesNotExist:
        raise Http404("Short URL does not exist")

def redirect_url(request, short_code):
    try:
        short_url = ShortURL.objects.get(short_code=short_code)
        short_url.click_count += 1
        short_url.save()
        return redirect(short_url.original_url)
    except ShortURL.DoesNotExist:
        raise Http404("Short URL does not exist")