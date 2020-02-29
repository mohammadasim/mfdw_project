"""
View for Quote app
"""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from pages.models import Page

from .forms import QuoteForm
from .models import Quote


@login_required(login_url=reverse_lazy('login'))
def quote_req(request):
    """
    A View to request a Quote and save it to the database
    once a valid quote form is submitted.
    """
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            quote = form.save(commit=False)
            try:
                quote.username = request.user
            except ObjectDoesNotExist:
                pass
            quote.save()
            return HttpResponseRedirect('/quote/?submitted=True')
        else:
            return render(request, "quotes/quote.html", {'form': form})
    else:
        form = QuoteForm()
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'quotes/quote.html',
                      {'form': form, 'page_list': Page.objects.all(),
                       'submitted': submitted})


class QuoteList(LoginRequiredMixin, ListView):
    """ A view to list quotes submitted by a user """
    model = Quote
    context_object_name = 'all_Quotes'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QuoteList, self).get_context_data()
        context['page_list'] = Page.objects.all()
        return context

    def get_queryset(self):
        return Quote.objects.filter(username=self.request.user)


class QuoteView(LoginRequiredMixin, DetailView):
    """ A view to check the details of a quote submitted by a user """
    model = Quote
    context_object_name = 'quote'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(QuoteView, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context

    def get_queryset(self):
        return Quote.objects.filter(username=self.request.user)


class Register(CreateView):
    """ A view to register a new user """
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        """
        A method to save new user details to the database
        once a valid registration form is submitted
        """
        form.save()
        return HttpResponseRedirect(self.success_url)
