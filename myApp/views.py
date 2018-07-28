from django.shortcuts import render
# from .forms.contact_us import ContacterForm
from .forms.contact_us import ContacterModelForm
# from .models import Contacter
from .controller.contact_us_view import ContactView
# Create your views here.


def index(request):
    titulo = ''
    if request.user.is_authenticated:
        titulo = 'Bienvenido %s' % request.user
    form = ContacterModelForm(request.POST or None)
    if form.is_valid():
        # instance.save()
        # print(instance)
        datos = form.cleaned_data
        name = datos.get("name")
        email = datos.get("email")
        subject = datos.get("subject")
        view = ContactView(name, email, subject)
        view.create()

    context = {'form': form, 'titulo': titulo}
    return render(request, "index.html", context)



