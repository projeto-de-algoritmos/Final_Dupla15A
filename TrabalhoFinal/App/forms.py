from django import forms


class Formulario(forms.Form):
    # (('Cuiaba - MT','Cuiaba - MT'), ('Goiania - GO','Goiania - GO'),('Campo Grande - MS','Campo Grande - MS'), 
    #         ('Belo Horizonte - MG','Belo Horizonte - MG'),('Sao Paulo - SP','Sao Paulo - SP'), 
    #         ('Rio de Janeiro - RJ','Rio de Janeiro - RJ'), ('Vitoria - ES','Vitoria - ES'),)
    CHOICES = (('Cuiaba - MT','Cuiaba - MT'), ('Goiania - GO','Goiania - GO'),('Campo Grande - MS','Campo Grande - MS'), 
            ('Belo Horizonte - MG','Belo Horizonte - MG'),('Sao Paulo - SP','Sao Paulo - SP'), 
            ('Rio de Janeiro - RJ','Rio de Janeiro - RJ'), ('Vitoria - ES','Vitoria - ES'),)
    partida = forms.ChoiceField(label='Cidade de partida',choices=CHOICES)
    destino = forms.ChoiceField(label='Cidade de destino',choices=CHOICES)
    autonomia = forms.CharField(label='Autonomia do veículo', max_length=3)
