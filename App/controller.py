"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """

import config as cf
from App import model
import csv
import os
"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""


# ___________________________________________________
#  Inicializacion del catalogo
def InitCatalog():
    Analyzer = model.analyzer()
    return Analyzer
# ___________________________________________________


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
def loadTrips(analyzer):
    archivos = []
    for filename in os.listdir(cf.data_dir):
        if filename.endswith('.csv'):
            archivos.append(filename)
            loadFile(analyzer, filename)
    Arcos = model.TotalDeArcos(analyzer)
    Vertices = model.TotalDeVertices(analyzer)
    Clusters = model.TotaldeClusteres(analyzer)
    archivos.append({"Total de Vertices":Vertices})
    archivos.append({"Total de Arcos":Arcos})
    archivos.append({"Total de Clusters":Clusters})
    return archivos
def loadFile(analyzer, file):
    """
    """
    file = cf.data_dir + file
    input_file = csv.DictReader(open(file, encoding="utf-8"),
                                delimiter=",")
    for route in input_file:
        model.AñadirRuta(analyzer, route)
        model.AñadirRutaNombre(analyzer,route)
    return analyzer
# ___________________________________________________

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def totaldeclusters(analyzer):
    return model.TotaldeClusteres(analyzer)
def clusterentre2id(analyzer,id1,id2):
    return model.ClusterPresence(analyzer,id1,id2)
def ensayo(analyzer):
    return model.adyacensias(analyzer)
def vertices(analyzer):
    return model.vertices(analyzer)
def indices(analyzer,id1):
    return model.buscador_por_indice(analyzer,id1)
def indices_nombres(analyzer,id1):
    return model.buscador_por_nombre(analyzer,id1)
def Requerimiento2(analyzer,tiempo,estacionInicio):
    return model.Requerimiento_2(analyzer,tiempo,estacionInicio)
def Vertices2(analyzer):
    return model.vertices2(analyzer)
def indices_salida(analyzer,id1):
    return model.indices_salida(analyzer,id1)
def Requerimiento_4(analyzer, time, id1):
    return model.Requerimiento_4(analyzer,time,id1)
def Vertices3(analyzer):
    return model.vertices3(analyzer)
def indices_edades_salir(analyzer,id1):
    return model.indices_salida_edad(analyzer,id1)
def indices_edades_entrar(analyzer,id1):
    return model.buscador_por_indice_edad(analyzer,id1)
def vertices4(analyzer):
    return model.vertices_latitudes(analyzer)
def vertices5(analyzer):
    return model.vertices_longitudes(analyzer)
def indices_lat_entrar(analyzer,id1):
    return model.salida_latitudes(analyzer,id1)
def indices_lat_salir(analyzer,id1):
    return model.entrada_latitudes(analyzer,id1)
def indices_lon_salir(analyzer,id1):
    return model.salida_lon(analyzer,id1)
def indices_lon_entrar(analyzer,id1):
    return model.entrada_lon(analyzer,id1)
#========================
def cargarCategorias_1():
    return model.cargarCategorias()
def cargar_Listas():
    return model.cargar_listas()
def cargar_paises():
    return model.cargar_paises()
def Requerimiento_1(analyzer,analyzer2,landing_point1,landing_point2):
    return model.Requerimiento_1(analyzer,analyzer2,landing_point1,landing_point2) 
def Requerimiento_2(analyzer,analyzer_2):
    return model.Requerimiento_2(analyzer,analyzer_2)
def Requerimiento_3(analyzer,a,b,analyzer2):
    return model.Requerimiento_3(analyzer,a,b,analyzer2)
def Corto(graph, start, end):
    return model.find_shortest_path(graph, start, end,path=[])
def Distancias(corto,analyzer2):
    return model.Distancias(corto,analyzer2)
def Requerimiento_4(analyzer,analyzer2,analyzer_3):
    return model.Requerimiento_4(analyzer,analyzer2,analyzer_3)
def Requerimiento_5(analyzer_3,landing_point,analyzer_2):
    return model.Requerimiento_5(analyzer_3,landing_point,analyzer_2)
def Requerimiento_6(analyzer_3,pais,cable,analyzer_2,analyzer4):
    return model.Requerimiento_6(analyzer_3,pais,cable,analyzer_2,analyzer4)
def Requerimiento_7(ip1,ip2,analyzer_2,analyzer_3):
    return model.Requerimiento_7(ip1,ip2,analyzer_2,analyzer_3)