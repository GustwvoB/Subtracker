from django.contrib import admin
from .models import Categoria, Assinatura, PessoaVinculada, DivisaoAssinatura

# Cada register() coloca o model no painel administrativo do Django
admin.site.register(Categoria)
admin.site.register(Assinatura)
admin.site.register(PessoaVinculada)
admin.site.register(DivisaoAssinatura)