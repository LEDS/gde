from django.forms import ModelForm, Select, TextInput
from .models import *


class FormAtividade(ModelForm):
    class Meta:
        model = Atividade
        fields = ['setor', 'descricao']


class FormSetor(ModelForm):
    class Meta:
        model = Setor
        fields = ['campus', 'nome', 'sigla', 'funcao', 'historico']
        widgets = {
            'campus': Select(attrs={'id': 'id-campus', 'class': 'browser-default selectField'}),
            'nome': TextInput(attrs={'class': 'validate'})
        }


class FormCampus(ModelForm):
    class Meta:
        model = Campus
        fields = ['nome']


class FormTipologia(ModelForm):
    class Meta:
        model = Tipologia

        fields = ['setor', 'usuario', 'fases', 'especieDocumental', 'finalidade', 'nome', 'identificacao', 'atividade',
                  'elemento', 'suporte', 'formaDocumental', 'genero', 'anexo', 'relacaoInterna', 'relacaoExterna',
                  'inicioAcumulo', 'fimAcumulo', 'quantidadeAcumulada', 'embasamentoLegal',
                  'informacaoOutrosDocumentos', 'restricaoAcesso', 'riscoPerda','sugestao']
        widgets = {
            'inicioAcumulo': TextInput(attrs={'type': 'date', 'class': 'datepicker'}),
            'fimAcumulo': TextInput(attrs={'class': 'datepicker'})
        }
