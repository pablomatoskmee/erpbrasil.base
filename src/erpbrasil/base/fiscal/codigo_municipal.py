# coding=utf-8
# Copyright (C) 2023  Pablo Augusto - KMEE
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import re



CODIGOS_DE_ESTADO = {
    '11': 'Rondônia',
    '12': 'Acre',
    '13': 'Amazonas',
    '14': 'Roraima',
    '15': 'Pará',
    '16': 'Amapá',
    '17': 'Tocantins',
    '21': 'Maranhão',
    '22': 'Piauí',
    '23': 'Ceará',
    '24': 'Rio Grande do Norte',
    '25': 'Paraíba',
    '26': 'Pernambuco',
    '27': 'Alagoas',
    '28': 'Sergipe',
    '29': 'Bahia',
    '31': 'Minas Gerais',
    '32': 'Espírito Santo',
    '33': 'Rio de Janeiro',
    '35': 'São Paulo',
    '41': 'Paraná',
    '42': 'Santa Catarina',
    '43': 'Rio Grande do Sul',
    '50': 'Mato Grosso do Sul',
    '51': 'Mato Grosso',
    '52': 'Goiás',
    '53': 'Distrito Federal'
}

def __validar_digito_de_controle(codigo_municipal):

    pesos = [1, 2, 1, 2 ,1 , 2]
    digitos = []
    for digito in codigo_municipal:
        digitos.append(int(digito))

    ponderacao = []
    for peso, digito in zip(pesos, digitos[:-1]):
        ponderacao.append(peso*digito)

    somatorio = sum(ponderacao)
    if somatorio > 9:
        somatorio = int(str(somatorio)[0]) + int(str(somatorio)[1])


    digito_verificador = 10 - (somatorio%10)
    digito_de_controle = int(codigo_municipal[-1])
    if digito_de_controle != digito_verificador:
        return False

    return True

def validar_codigo_municipal(codigo_municipal):

    codigo_municipal = str(codigo_municipal)
    #codigo_municipal = re.sub(r"\D", "", codigo_municipal)

    if len(codigo_municipal) != 7:
        return False

    codigo_de_estado = codigo_municipal[:2]
    if codigo_de_estado not in CODIGOS_DE_ESTADO.keys():
        return False

    numero_de_ordem = int(codigo_municipal[2:6])
    if numero_de_ordem == 0:
        return False


    if not(__validar_digito_de_controle(codigo_municipal)):
        return False

    return True

    
    
        
        



    