from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.core.mail import send_mail, get_connection
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings
from .models import *
from .forms import ContactForm


class HomeTemplateView(SuccessMessageMixin, TemplateView, FormView):
    template_name = 'home.html'
    ordering = ['-date_posted']
    form_class = ContactForm
    success_url = '/'  # After submiting the form keep staying on the same url
    success_message = 'Your Form has been successfully submitted!'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        return context

    def form_valid(self, form, **kwargs):
        form = ContactForm(self.request.POST)  # <- remove this line
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.smtp.EmailBackend')
            message = "{0} has sent you a new message:\n\n{1}".format(
                form.cleaned_data['email'], form.cleaned_data['message'])

            send_mail(
                cd['name'],
                message,
                cd.get('email', 'enquires'),
                ['@reciever-email.com'], connection=con) # enter the desired reciever email
        return super(HomeTemplateView, self).form_valid(form)
