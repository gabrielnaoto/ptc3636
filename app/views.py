from django.shortcuts import render

from django.core.mail import send_mail


# Create your views here.

def index(request):
    context = {}
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        send_mail(
            'Mensagem enviada pelo formulário do site',
            '{mensagem} - enviada por {autor} ({email})'.format(mensagem=mensagem, autor=nome, email=email),
            'erick.joordy@gmail.com',
            ['erick.joordy@gmail.com'],
            fail_silently=False,
        )
        context['success'] = True
    return render(request, template_name='index.html', context=context)
