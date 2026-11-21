from django import forms
from .models import Assinatura


class AssinaturaForm(forms.ModelForm):
    class Meta:
        model = Assinatura
        # O dono (usuario) não aparece no formulário: a view preenche com o usuário logado
        fields = ['nome_servico', 'categoria', 'valor', 'moeda', 'ciclo_cobranca',
                  'data_vencimento', 'eh_free_trial', 'data_limite_trial']
        widgets = {
            'nome_servico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Netflix', 'maxlength': 100}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.01'}),
            'moeda': forms.Select(attrs={'class': 'form-select'}),
            'ciclo_cobranca': forms.Select(attrs={'class': 'form-select'}),
            # format='%Y-%m-%d' é necessário para o campo de data vir preenchido na edição
            'data_vencimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'eh_free_trial': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'data_limite_trial': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
        }
        labels = {
            'nome_servico': 'Nome do serviço',
            'categoria': 'Categoria',
            'valor': 'Valor',
            'moeda': 'Moeda',
            'ciclo_cobranca': 'Ciclo de cobrança',
            'data_vencimento': 'Próximo vencimento',
            'eh_free_trial': 'Está em período de teste (free trial)',
            'data_limite_trial': 'Data limite do teste',
        }

    # Validação de um campo: clean_<campo>
    def clean_nome_servico(self):
        nome_servico = self.cleaned_data['nome_servico'].strip()
        if len(nome_servico) < 2:
            raise forms.ValidationError('O nome do serviço deve ter pelo menos 2 caracteres.')
        return nome_servico

    # Regra do modelo de dados: valor > 0 (o CHECK do modelo lógico)
    def clean_valor(self):
        valor = self.cleaned_data['valor']
        if valor <= 0:
            raise forms.ValidationError('O valor deve ser maior que zero.')
        return valor

    # Validação de vários campos juntos: clean()
    # Regra do modelo conceitual: se é free trial, a data limite é obrigatória.
    def clean(self):
        dados = super().clean()
        eh_free_trial = dados.get('eh_free_trial')
        data_limite_trial = dados.get('data_limite_trial')

        if eh_free_trial and not data_limite_trial:
            raise forms.ValidationError('Informe a data limite do período de teste.')

        if not eh_free_trial:
            dados['data_limite_trial'] = None   # sem teste, não guarda data limite

        return dados