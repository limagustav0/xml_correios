import xmltodict
from dataclasses import dataclass
    

with open('xml.xml','r', encoding='utf-8') as xml:
    content = xml.read()
    doc = xmltodict.parse(content)

    remetente_dict = {
        'nome' : doc['nfeProc']['NFe']['infNFe']['emit']['xFant'],
        'endereco' : doc['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['xLgr'] + ' ' + doc['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['nro']  + ' ' + doc['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['xBairro'],
        'cidade' : doc['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['xBairro'],
        'uf' : doc['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['UF'],
        'cep' : doc['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['CEP'],
        'cnpj_cpf' : doc['nfeProc']['NFe']['infNFe']['emit']['CNPJ']
    }

    remetente = Contato(**remetente_dict)

    destinatario = {
        'nome' : doc['nfeProc']['NFe']['infNFe']['dest']['xNome'],
        'endereco' : doc['nfeProc']['NFe']['infNFe']['dest']['enderDest']['xLgr'] + ' ' + doc['nfeProc']['NFe']['infNFe']['dest']['enderDest']['nro'],
        'cidade' : doc['nfeProc']['NFe']['infNFe']['dest']['enderDest']['xMun'],
        'uf' : doc['nfeProc']['NFe']['infNFe']['dest']['enderDest']['UF'],
        'cep' : doc['nfeProc']['NFe']['infNFe']['dest']['enderDest']['CEP'],
        'cnpj_cpf' : doc['nfeProc']['NFe']['infNFe']['dest']['CPF'],
    }

    
  
    lista_bens = []
    for prod in range(0,len(doc['nfeProc']['NFe']['infNFe']['det'])):
        identificacao_bem = {}

        identificacao_bem['conteudo'] = doc['nfeProc']['NFe']['infNFe']['det'][prod]['prod']['xProd'],
        identificacao_bem['quant'] = doc['nfeProc']['NFe']['infNFe']['det'][prod]['prod']['qCom'],
        identificacao_bem['valor'] = doc['nfeProc']['NFe']['infNFe']['det'][prod]['prod']['vUnCom'],
        
        lista_bens.append(identificacao_bem)
    

print()