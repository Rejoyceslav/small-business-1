from django.shortcuts import render
from django.views.generic.list import ListView

from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.views import View
from .forms import SendEmailForm
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Materialy, Uslugi

import re

from django.utils.html import escape

from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'test.html')


def oferta_View(request):
    return render(request, 'oferta.html')


def uslugi_View(request):
    return render(request, 'uslugi.html')


def przeglad_View(request):
    return render(request, 'przeglad.html')


def remonty_View(request):
    return render(request, 'remonty.html')


def sprzedaz_urzadzen_View(request):
    return render(request, 'sprzedaz_urzadzen.html')


def materialy_i_czesci_View(request):
    return render(request, 'materialy_i_czesci.html')


class MaterialyList(ListView):
    model = Materialy
    context_object_name = 'materialy'
    template_name = 'materialy_i_czesci.html'

    def get_context_data(self, **kwargs):
        qs = Materialy.objects.all()

        context = super(MaterialyList, self).get_context_data(**kwargs)
        context['materialy'] = qs
        return context


class UslugiList(ListView):
    model = Uslugi
    context_object_name = 'uslugi'
    template_name = 'materialy_i_czesci.html'

    def get_context_data(self, **kwargs):
        qs = Materialy.objects.all()

        context = super(UslugiList, self).get_context_data(**kwargs)
        context['materialy'] = qs
        return context


def kontakt_View(request):  # stary działający view, aby powrócić zmień w urls i w nawigacji w base.
    if request.method == 'POST':

        name = request.POST['kontakt_name']
        company = request.POST['kontakt_company']
        email_address = request.POST['kontakt_email_address']
        phone = request.POST['kontakt_phone']
        message = request.POST['kontakt_message']

        title = 'Pani/Pani: ' + name + ' Firma: ' + company
        # send_mail_to = ['kontakt@emartserwis.pl']
        send_mail_to = ['2629881@gmail.com']

        # email_content = name + '\n' + email_address + '\n' + message

        # send_mail(title,
        #           email_content,
        #           settings.EMAIL_HOST_USER,
        #           send_mail_to,
        #           fail_silently=False)

        html_content = render_to_string('email_template.html',
                                        {
                                            'title': title,
                                            'name': name,
                                            'company': company,
                                            'email_address': email_address,
                                            'phone': phone,
                                            'message': message,
                                         }
                                        )
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
                title,
                text_content,
                settings.EMAIL_HOST_USER,
                send_mail_to,
                )

        email.attach_alternative(html_content, 'text/html')
        email.send()

    return render(request, 'kontakt.html')


class KontaktView(View):  # testowany nowy View

    def get(self, request):  # get request comes here
        form = SendEmailForm()

        context = {
                    'form': form,
                   }

        return render(request, 'kontakt_email.html', context)

    def post(self, request):  # post request comes here
        form = SendEmailForm(request.POST)

        if form.is_valid():
            form.save()

            name = form.instance.name
            company = form.instance.company
            email_address = form.instance.email
            phone = form.instance.phone
            message = form.instance.message

            title = 'Pani/Pani: ' + name + ' Firma: ' + company
            # send_mail_to = ['kontakt@emartserwis.pl']
            send_mail_to = ['2629881@gmail.com']

            # email_content = name + '\n' + email_address + '\n' + message

            # send_mail(title,
            #           email_content,
            #           settings.EMAIL_HOST_USER,
            #           send_mail_to,
            #           fail_silently=False)

            html_content = render_to_string('email_template.html',
                                            {
                                                'title': title,
                                                'name': name,
                                                'company': company,
                                                'email_address': email_address,
                                                'phone': phone,
                                                'message': message,
                                            }
                                            )
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                title,
                text_content,
                settings.EMAIL_HOST_USER,
                send_mail_to,
            )

            email.attach_alternative(html_content, 'text/html')
            email.send()

            message = f'Formularz wysłany w imieniu: {form.instance.name}. \n Skontaktujemy się wkrótce.'
            messages.success(request, message)

            return redirect(request.path)  # redirects to request's path, <form action=''> in html has to be empty

        else:
            message = 'Adres e-mail podany błędnie. Proszę wypełnić formularz poprawnie.'
            messages.error(request, message)

            return redirect(request.path)

        # podany_email = str(form.instance.email)  # 1
        # # regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        # regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        #
        # if re.match(regex, podany_email):
        #     form.save()
        #     message = f'Formularz wysłany w imieniu: {form.instance.email}. Skontaktujemy się wkrótce.'
        #     messages.success(request, message)
        # else:
        #     form.save()
        #     message = f'Adres e-mail: \'{form.instance.email}\' nie został zaakceptowany. ' \
        #               f'Formularz nie został wysłany.'
        #     messages.error(request, message)
        #
        # return redirect(request.path)

        # if re.fullmatch(regex, podany_email):  # 2
        #     form.save()
        #     message = f'Formularz wysłany w imieniu: {form.instance.name}. \n Skontaktujemy się wkrótce.'
        #     messages.success(request, message)
        # else:
        #     form.save()
        #     message = f'Adres e-mail: \'{form.instance.email}\' nie został zaakceptowany. Formularz nie został wysłany.'
        #     messages.error(request, message)
