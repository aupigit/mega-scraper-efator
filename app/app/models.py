from django.db import models
from datetime import date, datetime
from django.db.models import Sum 

class Produtos(models.Model):
    id_produto   = models.AutoField(primary_key=True)  # Field name made lowercase.
    id_efator    = models.IntegerField()
    descricao    = models.CharField(max_length=100) 
    grupo        = models.CharField(max_length=100, null=True, blank=True)
    custocompra  = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precovenda   = models.DecimalField(max_digits=10, decimal_places=2, default=12.00)
    classificadcaofiscal = models.CharField(max_length=100)
    fornecedor  = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return str(self.id_efator) + " - " + str(self.descricao)
    
class CodigoBarras(models.Model):
    id_codigobarras = models.AutoField(primary_key=True)  # Field name made lowercase.
    codigobarras   = models.CharField(max_length=100)
    id_produto     = models.ForeignKey('Produtos', models.DO_NOTHING, db_column='id_produto')  # Field name made lowercase.
    
    def __str__(self):
        return self.codigobarras
    
    