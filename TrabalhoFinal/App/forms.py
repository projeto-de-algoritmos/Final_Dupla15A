from django import forms

CHOICES = (('Cuiaba - MT','Cuiaba - MT'), ('Goiania - GO','Goiania - GO'),('Campo Grande - MS','Campo Grande - MS'), 
            ('Belo Horizonte - MG','Belo Horizonte - MG'),('Sao Paulo - SP','Sao Paulo - SP'), 
            ('Rio de Janeiro - RJ','Rio de Janeiro - RJ'), ('Vitoria - ES','Vitoria - ES'),)
class Formulario(forms.Form):

    partida = forms.ChoiceField(label='Cidade de partida',choices=CHOICES)
    destino = forms.ChoiceField(label='Cidade de destino',choices=CHOICES)
    autonomia = forms.CharField(label='Autonomia do veículo', max_length=3)
#     letters = forms.MultipleChoiceField(
#             choices=CHOICES, 
#             widget=forms.CheckboxSelectMultiple()) 


class Formulario2(forms.Form):
    partida = forms.ChoiceField(label='Cidade de partida',choices=CHOICES)
    destino = forms.ChoiceField(label='Cidade de destino',choices=CHOICES)
#     autonomia = forms.CharField(label='Autonomia do veículo', max_length=3)
    paradas = forms.MultipleChoiceField(
            choices=CHOICES,
            label="Paradas",
            widget=forms.CheckboxSelectMultiple()) 
