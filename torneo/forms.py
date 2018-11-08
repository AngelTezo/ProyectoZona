from django import forms
from .models import Jugador, Personaje

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ('nombre', 'anio','consola', 'personajes')

class PForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = ('nombre', 'anio','compania','imagen')

def __init__(self, *args, **kwargs):
    super(JugadorForm, self).__init__(*args, **kwargs)
    self.fields["personajes"].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields["personajes"].help_text = "Ingrese los personajes de este jugador"
    self.fields["personajes"].queryset = Personaje.objects.all()
