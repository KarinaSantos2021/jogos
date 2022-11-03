from django.shortcuts import render
from .models import ApostaDoJogoDoBicho


from django.shortcuts import render
from django.forms import formset_factory
from .forms import ApostaForm


def apostar(request):

    aposta_formset = formset_factory(ApostaForm, extra=0)

    formset = aposta_formset(initial=[{'numero': x,} for x in range(1,60)])

    checks = []

    if request.method == 'POST':
        formset = aposta_formset(request.POST)
    
        if formset.is_valid():
            for form in formset.forms:
                if form.cleaned_data.get('checkbox', None):
                    checks.append(form.cleaned_data)

    context = {
        'formset': formset,
        'checks': checks,
    }

    return render(request, 'aposta_form.html', context)

def aposta_detail(request):
    template_name = 'jogo_do_bicho_detail.html'
    obj = None # ApostaDoJogoDoBicho.objects.get(usuario=request.user) or None
    context = {'object': obj}
    return render(request, template_name, context)


# def apostar(request):
#     template_name = 'aposta_form.html'
#     obj = None # ApostaDoJogoDoBicho.objects.get(usuario=request.user) or None
#     context = {'object': obj}
#     return render(request, template_name, context)
