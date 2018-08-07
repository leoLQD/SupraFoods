

from nfelib.v3_10 import leiauteNFe as leiauteNFe3


import os
from lxml import etree

import tempfile
os.chdir('C:\\\\Mettricx\\Projetos\\\\SupraAlimentos\\\\bkp_xml')




# In[3]:

sep=','
flinha='\n'
row=2
g=1
files = os.listdir()

f = open('NFe-SupraAlimentos.csv','w')
f.write('cliente,NF,data,CNPJ,cidade,bairro,UF,cod,descricao,QTY,unidade,preco\n')
k=0

for x in files:
    tree = etree.parse(files[k])
    
    root = tree.getroot()      
    if  root.tag == '{http://www.portalfiscal.inf.br/nfe}nfeProc':  
                new_file,filename = tempfile.mkstemp()
                subtree = etree.ElementTree(root[0])       
                subtree.write(filename,   encoding='utf-8')      
                nota = leiauteNFe3.parse(filename)      
                #print(root.tag)      
                #print(files[k])      
                       
                xNota = nota.get_infNFe()      
                      
                nt = xNota.get_ide()      
                xNum  = nt.get_nNF()      
                xData = nt.get_dhEmi()  
                data  = xData[:10]
          
                destino = nota.get_infNFe().get_dest()      
                       
                destNome = destino.get_xNome()     
                destCNPJ = destino.CNPJ      
                destEndereco =destino.get_enderDest()      
                destCidade=destino.enderDest.get_xMun()      
                destBairro = destino.enderDest.get_xBairro() 
                destEstado = destino.enderDest.get_UF()
                        
                produtos = nota.get_infNFe().get_det()  
                
                total = nota.get_infNFe()      
                valor = total.get_total()      
                xValor = valor.ICMSTot.get_vProd() 
        
                i=0      
                item={}      
                j=1 
             
                for l in produtos:      
                                         p = produtos[i]  
                                         
                                         xProd = p.get_prod().get_xProd()  # Nome do Produto      
                                         xCod  = p.get_prod().get_cProd()  # Codigo 
                                         if len(xCod) < 7:
                                             xCod = '0'+xCod
                                         xCod  = xCod.replace('.','')    
                                         xQty  = str(int(float(p.get_prod().get_qCom())))   # Quantidade      
                                         xUnid = p.get_prod().get_uCom()   # Unidade      
                                         xPreco= p.get_prod().get_vProd()  # Preco 
                                         xProd = xProd.replace(',',' ')
                                         destNome = destNome.replace(',',' ')
                                         
                                         f.write(destNome+sep+xNum+sep+data+sep+destCNPJ+sep+destCidade+sep+destBairro+sep+destEstado+sep+xCod+sep+xProd+sep+xQty+sep+xUnid+sep+xPreco+flinha)

                                         i += 1      
                                         j += 1
                                         g += 1
                                                       
                                         #print(i)
                    
    
     
                  
                
                             
    k += 1      
print('Total Notas : ',  k)      
print('Total Gravados : ',   g, i)  
f.close()