from django.shortcuts import render

from app.models import Produtos, CodigoBarras
import csv

def importcsv(request):
    with open('Inventario.csv', newline='') as csvfile:
        produtoreader = csv.reader(csvfile, delimiter=',',quotechar='"')
        # print(len(produtoreader))
        for row in produtoreader:
            # print(', '.join(row))
            print(row[0], row[1], row[2], float(row[3].replace(',','.')) )

            Produtos.objects.create(id_efator=row[1], 
                                    descricao=row[2], 
                                    precovenda=float(row[3].replace(',','.')),
                                    classificadcaofiscal=row[0])
            
    return render(request, 'importcsv.html')

        
