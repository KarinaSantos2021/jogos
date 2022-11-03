from django.shortcuts import render, redirect
from .forms import CarteiraForm
from .models import Saldo


def saldo_detail(request):
    template_name = 'saldo_carteira.html'
    obj = Saldo.objects.get(usuario=request.user)
    context = {'object': obj}
    return render(request, template_name, context)

def depositar(request):
    template_name = 'carteira_form.html'
    form = CarteiraForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save(usuario=request.user)
            return redirect('carteira:saldo_detail')

    context = {'form': form}
    return render(request, template_name, context)
