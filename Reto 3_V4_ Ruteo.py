# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 23:38:42 2020

@author: ASTRID
"""

def ruteo(distancias: dict, ruta_inicial: list)-> dict:
    # Validar datos de entrada del diccionario
    for valor in distancias.values():
        if valor < 0:
            return ("Por favor revisar los datos de entrada.")
    # Validar de la lista que la distancia de un punto hacia si mismo sea diferente de 0    
    for k in range(0, len(ruta_inicial)):
        a = ruta_inicial[k]
        b = ruta_inicial[k]
        tupla = (a,b)
        if distancias[tupla] != 0:
            return ("Por favor revisar los datos de entrada.")
        
    # Convertir Lista de Ruta Inicial a lista de Tuplas de Ruta inicial para 
    # accdeder al Diccionario "distancias" y calcular la distancia inicial como
    # control de inicio
    pares_inicio = [('H','H')]
    d_inic = 0
    k = 1
    while k<=len(ruta_inicial)-1:
        llave = tuple(ruta_inicial[k-1:k+1])
        pares_inicio.append(llave)
        d_inic = d_inic + distancias[llave]
        k=k+1
    # Iniciar los ciclos de intercambios para encontar por iteracion la mejor 
    # pareja de intercambio y por ene la nueva ruta con menor distancia.
 
    par_ruta_intercambiada =  [('H','H')]
    mejor_d_ruta = d_inic
    d_Temporal = 0
    nIteracion  = 0 # Variable que controla los subciclos de iteraciones del total 
                    #  de intercambios
    esLaMenorRuta = 0 # Controla que si la ruta inicial desde comienzo es la menor, esta
                      # variable nunca se modifica en un ciclo completo de iteraciones
    seOptimizo = True
    a = len(ruta_inicial) - 3 #variable de control de iteraciones; modifica el avance de i y j 
    i = 0
    while i <= (len(ruta_inicial) - 2):
        j = 1
        while  j <= (len(ruta_inicial) - 1):
            ruta_Intercambios = ruta_inicial.copy()
            ruta_Intercambios[i + 1],ruta_Intercambios[j + 1] = ruta_Intercambios[j + 1],ruta_Intercambios[i + 1]
            k = 1
            while k<=len(ruta_Intercambios)-1:
                llave = tuple(ruta_Intercambios[k-1:k+1])
                par_ruta_intercambiada.append(llave)
                d_Temporal = d_Temporal + distancias[llave]
                k=k+1
            if (d_Temporal < d_inic) and (d_Temporal < mejor_d_ruta) :
                mejor_d_ruta = d_Temporal
                d_Temporal = 0
                mejor_ruta_intercambios = ruta_Intercambios.copy()
                par_ruta_intercambiada =  [('H','H')]
                nIteracion = nIteracion + 1
                
                esLaMenorRuta = esLaMenorRuta + 1
                seOptimizo = True
                if nIteracion == a:
                      i = i + 1
                      j = i 
                      nIteracion = 0
                      a = a - 1
                j = j + 1                
            else:
                d_Temporal= 0
                par_ruta_intercambiada =  [('H','H')]
                nIteracion = nIteracion + 1
             
                if nIteracion == a: 
                      i = i + 1
                      j = i 
                      nIteracion = 0
                      a = a - 1
                j = j + 1                
            if seOptimizo == False and a == 0:
                
                # actualizar y selecionar la mejor ruta para entregarla como salida
                # del codigo luego de un ciclo completo sin mejorias (sin "True")
                mejor_ruta_intercambios = mejor_ruta_intercambios.copy()
                mejor_ruta_intercambios = '-'.join(mejor_ruta_intercambios)
                return {'ruta':(mejor_ruta_intercambios),'distancia': mejor_d_ruta}
            
            if seOptimizo == True and a == 0:
                if esLaMenorRuta == 0: 
                    ruta_inicial = ruta_inicial.copy()
                    ruta_inicial = '-'.join(ruta_inicial)
                    return {'ruta':(ruta_inicial),'distancia': d_inic}
                # Actualizar la mejor ruta encotrada con el intercambio de la pareja que 
                # que aporta la mayor disminución de distancia al final de cada ciclo
                # completo de iteracion
                ruta_inicial= mejor_ruta_intercambios.copy()
                i = 0
                j = 1
                a = len(ruta_inicial) -3
                seOptimizo = False


         
distancias = {('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241, 
            ('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,
            ('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269, 
            ('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180, 
            ('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109, 
            ('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119, 
            ('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}


ruta_inicial = ['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']
 

"""
distancias = {('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27,
              ('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117,
              ('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199,
              ('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19,
              ('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31,
              ('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0}

ruta_inicial = ['H', 'B', 'E', 'A', 'C', 'D', 'H']
"""


"""
distancias ={('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241, ('A', 'H'):
            127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41, ('B', 'H'): 153, ('B', 'A'): 252, ('B',
            'B'): 555, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269, ('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0,
            ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180, ('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'):
            194, ('D', 'F'): 109, ('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119, ('F',
            'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}
            
ruta_inicial = ['H', 'B', 'D', 'A', 'F', 'C', 'E', 'H']
"""

"""
distancias = {('BOG', 'BOG'): 0, ('BOG', 'MDE'): 21, ('BOG', 'PEI'): 57, ('BOG', 'SMR'): 58, ('BOG', 'CTG'): 195, ('MDE',
'BOG'): 127, ('MDE', 'MDE'): 0, ('MDE', 'PEI'): 231, ('MDE', 'SMR'): 113, ('MDE', 'CTG'): 254, ('PEI', 'BOG'): 153, ('PEI',
'MDE'): 252, ('PEI', 'PEI'): 0, ('PEI', 'SMR'): 56, ('PEI', 'CTG'): 126, ('SMR', 'BOG'): 196, ('SMR', 'MDE'): 128, ('SMR',
'PEI'): 80, ('SMR', 'SMR'): 0, ('SMR', 'CTG'): 136, ('CTG', 'BOG'): 30, ('CTG', 'MDE'): 40, ('CTG', 'PEI'): 256, ('CTG',
'SMR'): 121, ('CTG', 'CTG'): 0}
                                                                                                                  
ruta_inicial = ['MDE', 'PEI', 'BOG', 'CTG', 'SMR', 'MDE']
"""
                                                                                                                  
"""                                                                                                                  
{'ruta': 'MDE-SMR-PEI-CTG-BOG-MDE', 'distancia': 370}
"""

"""
for i in ruta_inicial:
    pareja = (['i'], ['i + 1'])
    print(pareja)
"""


print(ruteo(distancias, ruta_inicial))
