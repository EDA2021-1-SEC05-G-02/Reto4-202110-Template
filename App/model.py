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
from os import defpath
from DISClib.DataStructures.mapentry import getKey
from DISClib.Algorithms.Graphs.dfo import dfsVertex
from DISClib.Algorithms.Graphs.bfs import bfsVertex
import config as cf
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
import config1 as cf1
import config2 as cf2
import csv
from collections import defaultdict
from functools import reduce
from math import sin, cos, sqrt, atan2,radians
import ipapi
"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
def analyzer():
    analyzer={"indice":None,
                "grafo":None,
                "nombres":None,
                "id":None}
    analyzer["indice"] = m.newMap(numelements=3263, 
                                  prime=109345121, 
                                  maptype="CHAINING",
                                  loadfactor=1.0, 
                                  comparefunction=None)
    analyzer["grafo"] = gr.newGraph(datastructure='ADJ_LIST',
                                  directed=True,
                                  size=3263,
                                  comparefunction=comparer)
    analyzer["nombres"] = gr.newGraph(datastructure='ADJ_LIST',
                                  directed=True,
                                  size=3263,
                                  comparefunction=comparer)
    analyzer["id"] = gr.newGraph(datastructure='ADJ_LIST',
                                  directed=True,
                                  size=3263,
                                  comparefunction=comparer)
    return analyzer
def AñadirRuta(analyzer, route):
    """
    """
    origin = route["\ufefforigin"]
    destination = route['destination']
    d = route['cable_length']
    if d=="n.a.":
        duration=0
    else:
        a=d.split()
        z=a[0].replace(",","")
        duration=float(z)
    AñadirEstacion(analyzer, origin)
    AñadirEstacion(analyzer, destination)
    AñadirConeccion(analyzer, origin, destination, duration)
def AñadirRutaNombre(analyzer,route):
    origin=route["cable_name"]
    destination = route['cable_name']
    d = route['cable_length']
    if d=="n.a.":
        duration=0
    else:
        a=d.split()
        z=a[0].replace(",","")
        duration=float(z)
    AñadirEstacion1(analyzer, origin)
    AñadirEstacion1(analyzer, destination)
    AñadirConeccion1(analyzer, origin, destination, duration)
def AñadirRutaEdades(analyzer,route):
    origin=route["cable_id"]
    destination =route['cable_id']
    d = route['cable_length']
    if d=="n.a.":
        duration=0
    else:
        a=d.split()
        z=a[0].replace(",","")
        duration=float(z)
    AñadirEstacion4(analyzer, origin)
    AñadirEstacion4(analyzer, destination)
    AñadirConeccion4(analyzer, origin, destination, duration)
def  AñadirEstacion(analyzer, estacion):
    if not gr.containsVertex(analyzer["grafo"], estacion):
        gr.insertVertex(analyzer["grafo"], estacion)
    return analyzer
def AñadirConeccion(analyzer, origin, destination, duration):
    """
    Adiciona un arco entre dos estaciones
    """
    edge = gr.getEdge(analyzer["grafo"], origin, destination)
    if edge is None:
        gr.addEdge(analyzer["grafo"], origin, destination, duration)
    else:
        edge["weight"] = duration
    return analyzer
def  AñadirEstacion1(analyzer, estacion):
    if not gr.containsVertex(analyzer["nombres"], estacion):
        gr.insertVertex(analyzer["nombres"], estacion)
    return analyzer
def AñadirConeccion1(analyzer, origin, destination, duration):
    """
    Adiciona un arco entre dos estaciones
    """
    edge = gr.getEdge(analyzer["nombres"], origin, destination)
    if edge is None:
        gr.addEdge(analyzer["nombres"], origin, destination, duration)
    else:
        edge["weight"] = duration
    return analyzer
def  AñadirEstacion4(analyzer, estacion):
    if not gr.containsVertex(analyzer["eades"], estacion):
        gr.insertVertex(analyzer["edades"], estacion)
    return analyzer
def AñadirConeccion4(analyzer, origin, destination, duration):
    """
    Adiciona un arco entre dos estaciones
    """
    edge = gr.getEdge(analyzer["id"], origin, destination)
    if edge is None:
        gr.addEdge(analyzer["id"], origin, destination, duration)
    else:
        edge["weight"] = duration
    return analyzer
def TotaldeClusteres(analyzer):
    A = scc.KosarajuSCC(analyzer["grafo"])
    return scc.connectedComponents(A)
def ClusterPresence(analyzer,id1,id2):
    A = scc.KosarajuSCC(analyzer["grafo"])
    return scc.stronglyConnected(A, id1, id2)
def TotalDeVertices(analyzer):
    return gr.numVertices(analyzer["grafo"])
def TotalDeArcos(analyzer):
    return gr.numEdges(analyzer["grafo"])
def comparer(stop, keyvaluestop):
    """
    Compara dos estaciones
    """
    stopcode = keyvaluestop['key']
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1 
def Requerimiento_1(analyzer,analyzer2,landing_point1,landing_point2):
    ids=lt.newList()
    for i in analyzer2:
        if landing_point1 in i["name"]:
            lt.addLast(ids,i["landing_point_id"])
    for i in analyzer2:
        if landing_point2 in i["name"]:
            lt.addLast(ids,i["landing_point_id"])
    A=scc.KosarajuSCC(analyzer["grafo"])
    Cluster=scc.stronglyConnected(A, ids["first"]["info"], ids["last"]["info"])
    Total=scc.connectedComponents(A)
    return (Total,Cluster,ids["first"]["info"], ids["last"]["info"])
def Requerimiento_2(analyzer,analyzer_2):
    A=scc.KosarajuSCC(analyzer["grafo"])
    ids={}
    for i in A["idscc"]["table"]["elements"]:
        if i["key"]!=None:
            ids[i["key"]]=i["value"]
    landing_points=[]
    for i in ids:
        for z in analyzer_2:
            if i==z["landing_point_id"]:
                landing_points.append({"name":z["landing_point_id"],"country":z["name"],"id":z["id"],"total":ids[i]})
    return landing_points
def Requerimiento_3(analyzer3,pais_a,pais_b,analyzer2):
    ids=lt.newList()
    for i in analyzer2:
        if pais_a in i["name"]:
            lt.addLast(ids,i["landing_point_id"])
    for i in analyzer2:
        if pais_b in i["name"]:
            lt.addLast(ids,i["landing_point_id"])
    lista=[]
    lista_2=[]
    for i in analyzer3:
        for k,v in i.items():
            if k=="\ufefforigin":
                lista.append(v)
            if k=="destination":
                lista_2.append(v)
    d = defaultdict(list)
    for i,key in enumerate(lista): 
        if lista_2[i] not in d[key]:            #to add only unique values (ex: '693':'goa')
            d[key].append(lista_2[i])
    a=dict(d) 
    return (a,ids["first"]["info"], ids["last"]["info"])
def find_shortest_path(graph, start, end, path =[]):
                path = path + [start]
                if start == end:
                    return path
                for node in graph[start]:
                    if node not in path:
                        newpath = find_shortest_path(graph, node, end, path)
                        if newpath:
                            return newpath
def Distancias(path,analyzer2):
    Lats_longs={}
    for i in analyzer2:
        for z in path:
            if i["landing_point_id"]==z:
                Lats_longs[z]=(float(i["latitude"]),float(i["longitude"]))
    latitudes=[]
    long=[]
    for i in path:
        latitudes.append(Lats_longs[i][0])
        long.append(Lats_longs[i][1])
    chunks_lat = [latitudes[x:x+2] for x in range(0, len(latitudes), 2)]
    chunks_long = [long[x:x+2] for x in range(0, len(long), 2)]
    cont=0
    pasos=[]
    while cont<len(chunks_lat):
        pasos.append([reduce(lambda x, y: x - y, chunks_lat[cont]),reduce(lambda x, y: x - y,chunks_long[cont])])
        cont+=1
    R = 6373.0
    dist=[]
    rad=[]
    for i in chunks_lat:
            for z in pasos:
                if len(i)==2:
                    dist.append(radians(sin(z[0] / 2)**2 + cos(i[0]) * cos(i[1]) * sin( z[1]/ 2)**2))
    for i in dist:
        rad.append(R * (2 *(atan2(sqrt(abs(i)), sqrt(1 - abs(i))))))
    rad=rad[::len(pasos)]
    return (rad,sum(rad))
def Requerimiento_4(analyzer,analyzer_2,analyzer_3):
    A=Requerimiento_2(analyzer,analyzer_2)
    minimo=None
    valor=1000000000000
    for i in A:
        if i["total"]<=valor:
            valor=i["total"]
            minimo=i
    lista=[]
    lista_2=[]
    for i in analyzer_3:
        for k,v in i.items():
            if k=="\ufefforigin":
                lista.append(v)
            if k=="destination":
                lista_2.append(v)
    d = defaultdict(list)
    for i,key in enumerate(lista): 
        if lista_2[i] not in d[key]:            #to add only unique values (ex: '693':'goa')
            d[key].append(lista_2[i])
    a=dict(d)
    Lats_longs={}
    for i in analyzer_2:
        for z in a[minimo["name"]]:
            if i["landing_point_id"]==z:
                Lats_longs[z]=(float(i["latitude"]),float(i["longitude"]))
    latitudes=[]
    long=[]
    for i in a[minimo["name"]]:
        latitudes.append(Lats_longs[i][0])
        long.append(Lats_longs[i][1])
    R = 6373.0
    valor=radians(sin(long[0] / 2)**2 + cos(latitudes[0]))
    rad=R * (2 *(atan2(sqrt(abs(valor)), sqrt(1 - abs(valor)))))
    return (minimo,rad,a[minimo["name"]])
def Requerimiento_5(analyzer_3,landing_point,analyzer_2):
    ids=lt.newList()
    for i in analyzer_2:
        if landing_point in i["name"]:
            lt.addLast(ids,i["landing_point_id"])
    valor=ids["first"]["info"]
    lista=[]
    lista_2=[]
    for i in analyzer_3:
        for k,v in i.items():
            if k=="\ufefforigin":
                lista.append(v)
            if k=="destination":
                lista_2.append(v)
    d = defaultdict(list)
    for i,key in enumerate(lista): 
        if lista_2[i] not in d[key]:            #to add only unique values (ex: '693':'goa')
            d[key].append(lista_2[i])
    a=dict(d)
    pais=[]
    for i in a:
        if i==valor:
            for z in a[i]:
                pais.append([valor,z])
    paises={}
    for i in pais:
        paises[i[1]]=Distancias(i,analyzer_2)[1]
    nombres={}
    for z in analyzer_2:
        for i in paises:
            if z["landing_point_id"]==i:
                nombres[z["name"]]=paises[i]
    n=dict(sorted(nombres.items(), key=lambda item: item[1],reverse=True))
    return n
def Requerimiento_6(analyzer_3,pais,nombre_cable,analyzer_2,analyzer4):
    paises=[]
    for i in analyzer_2:
        if pais in i["name"]:
            paises.append(i["landing_point_id"])
    cable={}
    for i in analyzer_3:
        for z in paises:
            for k,v in i.items():
                if k=="\ufefforigin" and v==z:
                    cable[i["cable_name"]]=(z,float(i["capacityTBPS"]))
    util=()
    for i in cable:
        if nombre_cable in i:
            util=(cable[i],i)
    if len(util)==0:
        return None
    else:
        lista=[]
        lista_2=[]
        for i in analyzer_3:
            for k,v in i.items():
                if k=="\ufefforigin":
                    lista.append(v)
                if k=="destination":
                    lista_2.append(v)
        d = defaultdict(list)
        for i,key in enumerate(lista): 
            if lista_2[i] not in d[key]:            #to add only unique values (ex: '693':'goa')
                d[key].append(lista_2[i])
        a=dict(d)
        resp=None
        for i in a:
            if i in util[0][0]:
                resp=a[i]
        paises_nombres={}
        for i in resp:
            paises_nombres[i]=convertir(analyzer_2,i)
        poblacion=[]
        for z in paises_nombres:
            poblacion.append(population(analyzer4,paises_nombres[z]))
        respuesta=[]
        nombres=list(paises_nombres.values())
        for z in poblacion:
                respuesta.append((util[0][1]/z))
        tbsp=list(zip(nombres,respuesta))
        return tbsp
def Requerimiento_7(ip1,ip2,analyzer_2,analyzer_3):
    dir1=ipapi.location(ip=ip1,output="country_name")
    dir2=ipapi.location(ip=ip2,output="country_name")
    if dir1=="Undefined" or dir2=="Undefined":
        return None
    else:
        paises=Requerimiento_3(analyzer_3,dir1,dir2,analyzer_2)
        camino=find_shortest_path(paises[0],paises[1],paises[2])
        return camino
    #165.132.67.89
    #186.86.125.19
#3316
def convertir(analyzer_2,id):
    pais=None
    for i in analyzer_2:
        if i["landing_point_id"] in id:
            if "St. Croix" in i["name"]:
                pais=" United States"
            else:
                pais=i["name"].split(",")[1]
    return pais
def population(analyzer4,pais):
    poblacion=None
    for i in analyzer4:
        if pais[1::] in i["CountryName"]:
            poblacion=int(i["Population"])
    return poblacion
def cargarCategorias():
    vfile = cf1.data_dir + "landing_points.csv"
    reader = csv.DictReader(open(vfile,encoding="utf-8"))
    analyzer2 = []
    for line in reader:
        analyzer2.append(dict(line))
    return analyzer2  
def cargar_listas():
    vfile=cf.data_dir+"connections.csv"
    reader = csv.DictReader(open(vfile,encoding="utf-8"))
    analyzer3= []
    for line in reader:
        analyzer3.append(dict(line))
    return analyzer3
def cargar_paises():
    vfile=cf2.data_dir+"countries.csv"
    reader = csv.DictReader(open(vfile,encoding="utf-8"))
    analyzer4= []
    for line in reader:
        analyzer4.append(dict(line))
    return analyzer4
