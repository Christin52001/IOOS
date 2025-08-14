from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import Http404
from .forms import LinkForm
from .models import Link

def index(request):
    form = LinkForm(request.POST or None)
    recent_links = Link.objects.order_by('-created_at')[:10]

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        code = data['custom_code'] or Link.generate_code()

        if Link.objects.filter(code=code).exists():
            form.add_error('custom_code', "This code is already taken.")
        else:
            expires_at = None
            if data['days_valid']:
                expires_at = timezone.now() + timezone.timedelta(days=data['days_valid'])

            link = Link.objects.create(
                code=code,
                long_url=data['long_url'],
                expires_at=expires_at,
                custom=bool(data['custom_code'])
            )
            return redirect('detail', code=link.code)

    return render(request, 'index.html', {'form': form, 'recent': recent_links})

def redirect_view(request, code):
    link = get_object_or_404(Link, code=code)
    if link.is_expired():
        raise Http404("This link has expired.")
    link.clicks += 1
    link.save()
    return redirect(link.long_url)

def detail(request, code):
    link = get_object_or_404(Link, code=code)
    return render(request, 'detail.html', {'link': link})
