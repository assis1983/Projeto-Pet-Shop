from datetime import date
from django import forms
from reserva.models import Reserva

class ReservaForm(forms.ModelForm):
    
    '''def clean_data(self):
        data = self.cleaned_data['data']
        hoje = date.today()
        if data < hoje:
            raise forms.ValidationError('Não é possível realizar a reserva para datas passadas!')
        return data'''

    class Meta:
        model = Reserva
        fields = [
            'nome', 'email', 'nome_pet', 'data', 'turno', 'tamanho', 'observacoes'
        ]