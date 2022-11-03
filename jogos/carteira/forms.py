from django import forms

from .models import Saldo


class CarteiraForm(forms.Form):
    required_css_class = 'required'
    valor_deposito = forms.FloatField(min_value=0.0, max_value=1000.00)

    def __init__(self, *args, **kwargs):
        super(CarteiraForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, usuario):
        saldo = Saldo.objects.get(usuario=usuario)
        deposito = self.data.get('valor_deposito')
        novo_saldo = saldo.saldo + float(deposito)
        saldo.saldo = novo_saldo
        saldo.save()
