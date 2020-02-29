from django.core.mail import send_mail, get_connection
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import ContactForm
from .models import Page


def index(request, pagename):
    """
    A view to access pages based on the page name in the url.
    """
    pagename = '/' + pagename

    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all()  # A list of all pages
        # created is sent to the
        # template where they are displayed in the page's side bar
    }
    # assert False # This is for testing purposes and to debug
    return render(request, 'pages/page.html', context)


def contact(request):
    """ A view to allow users to contact the site admin """
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False (for testing purpose)
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'pages/contact.html',
                  {'form': form, 'page_list': Page.objects.all(),
                   'submitted': submitted})
