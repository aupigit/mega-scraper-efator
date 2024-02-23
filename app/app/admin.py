from django.contrib import admin
from app.models import Produtos, CodigoBarras

# class CodigoBarrasInLine(admin.TabularInline):
#      model = CodigoBarras

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('id_produto', 'id_efator', 'descricao', 'grupo', 'custocompra', 'precovenda', 'classificadcaofiscal', 'fornecedor')
    # inlines = [CodigoBarrasInLine]
admin.site.register(Produtos, ProdutosAdmin) 


class CodigoBarrasAdmin(admin.ModelAdmin):
    list_display = ('id_codigobarras', 'codigobarras', 'id_produto')
admin.site.register(CodigoBarras, CodigoBarrasAdmin)