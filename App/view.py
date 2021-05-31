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


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config
import ipapi
import folium
import random
"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


# ___________________________________________________
#  Menu principal
def Menu():
    print("\n")
    print("Bienvenido")
    print("1- Iniciar el catalogo")
    print("2- Cargar archivos al catalogo")
    print("3- Requerimiento 1 ")
    print("4- Requerimiento 2")
    print("5- Requerimiento 3")
    print("6- Requerimiento 4")
    print("7- Requerimiento 5")
    print("8- Requerimiento 6")
    print("9- Requerimiento 7")
    print("10- Salir")

# ___________________________________________________

"""
Menu principal
"""
def OpcionesMenu():
    analyzer = None
    A = True
    while A is True:
        Menu()
        opciones = str(input("Seleccione una opción:"))
        if opciones == "1":
            analyzer = controller.InitCatalog()
            if analyzer != None:  
                print("Catalogo creado") 
            else:
                print("Error al cargar el catalogo")
        elif opciones == "2":
            Data = controller.loadTrips(analyzer)
            analyzer_2=controller.cargarCategorias_1()
            analyzer3=controller.cargar_Listas()
            analyzer4=controller.cargar_paises()
            print("Se cargaron los archivos:")
            print("\n")
            for n in Data:
                print(n)  
        elif opciones == "3":
            landing_point1=input("Landing Point 1: ")
            landing_point2=input("Landing Point 2: ")
            Requerimiento_1=controller.Requerimiento_1(analyzer,analyzer_2,landing_point1,landing_point2)
            print("El número total de clústeres presentes en la red es "+str(Requerimiento_1[0]))
            if Requerimiento_1[1]==True:
                print("Si están fuertemente conectados")
            else:
                print("No están fuertemente conectados")
            lat=[]
            lat2=[]
            for i in analyzer_2:
                if i["landing_point_id"] in Requerimiento_1[2]:
                    lat.append(float(i["latitude"]))
                    lat.append(float(i["longitude"]))
            for i in analyzer_2:
                if i["landing_point_id"] in Requerimiento_1[3]:
                    lat2.append(float(i["latitude"]))
                    lat2.append(float(i["longitude"]))
            m = folium.Map(location=lat, tiles="Stamen Toner", zoom_start=3)
            folium.Circle(radius=100,
                            location=lat,
                            popup=landing_point1,
                            color="crimson",
                            fill=False,).add_to(m)
            folium.CircleMarker(
                            location=lat,
                            radius=50,
                            popup=landing_point1,
                            color="#3186cc",
                            fill=True,
                            fill_color="#3186cc",).add_to(m)
            folium.Circle(radius=100,
                            location=lat2,
                            popup=landing_point2,
                            color="crimson",
                            fill=False,).add_to(m)
            folium.CircleMarker(
                            location=lat2,
                            radius=50,
                            popup=landing_point2,
                            color="#006600",
                            fill=True,
                            fill_color="#006600",).add_to(m)
            folium.PolyLine(locations=[lat,lat2], color='#FF0000').add_to(m)
            m.save("Requerimiento_1.html")
        elif opciones=="4":
             colores=["#0000CC","#009900","#FF0000","#0BE4FC","#771290","#FFFF00","#FFFFFF","#CCFFFF","#FFFFCC","#CCCCFF","#FFCCCC","#99FFFF","#CCCCCC","#FFFF99","#66FFCC","#99CCFF","#99FF99","#99CCCC","#00FFFF","#FF99FF","#33CCCC","#66CC99","#999999","#FFCC00","#00FF99","#CCCC66","#6699FF","#FF66CC","#FF9966","#66FF00","#FF6666","#33CC66","#33CC33","#00FF00","#009999","#FF3300","#339933","#006600","#990000"]
             Requerimiento_2=controller.Requerimiento_2(analyzer,analyzer_2)
             for i in Requerimiento_2:
                 print("===============================================================")
                 print("Nombre del landing point: "+str(i["name"]))
                 print("Pais del landing point: "+str(i["country"]))
                 print("Identificador del landing point: "+str(i["id"]))
                 print("Total de cables conectados al landing point: "+str(i["total"]))
             valor=[]
             for i in Requerimiento_2:
                 valor.append(i["country"])
             lat=[]
             for z in valor:
                for i in analyzer_2:
                    if i["name"] in z:
                        lat.append([float(i["latitude"]),float(i["longitude"])])
             m = folium.Map(location=lat[0], tiles="Stamen Toner", zoom_start=2)
             cont=0
             while cont<len(lat):
                 folium.Circle(radius=1,
                            location=lat[cont],
                            popup=valor[0],
                            color="crimson",
                            fill=False,).add_to(m)
                 folium.CircleMarker(
                            location=lat[cont],
                            radius=5,
                            popup=lat[0],
                            color=random.choice(colores),
                            fill=True,
                            fill_color=random.choice(colores),).add_to(m)
                 cont+=1
             m.save("Requerimiento_2.html")
        elif opciones=="5":
            pais_a=input("Pais A: ")
            pais_b=input("Pais B: ")
            Requerimiento_3=controller.Requerimiento_3(analyzer3,pais_a,pais_b,analyzer_2)
            Corto=controller.Corto(Requerimiento_3[0],Requerimiento_3[1], Requerimiento_3[2])
            Distancias=controller.Distancias(Corto,analyzer_2)
            cont=1
            if len(Distancias[0])!=0:
                for i in Distancias[0]:
                    print("En la parte "+str(cont)+" del trayecto hay: "+str(i)+" kilómetros")
                    cont+=1
                print("Y la distancia total del trayecto es de "+str(Distancias[1])+" kilómetros")
                lat=[]
                lat2=[]
                for i in analyzer_2:
                    if i["landing_point_id"] in Requerimiento_3[1]:
                        lat.append(float(i["latitude"]))
                        lat.append(float(i["longitude"]))
                for i in analyzer_2:
                    if i["landing_point_id"] in Requerimiento_3[2]:
                        lat2.append(float(i["latitude"]))
                        lat2.append(float(i["longitude"]))
                m = folium.Map(location=lat, tiles="Stamen Toner", zoom_start=3)
                folium.Circle(radius=100,
                            location=lat,
                            popup=Requerimiento_3[1],
                            color="crimson",
                            fill=False,).add_to(m)
                folium.CircleMarker(
                            location=lat,
                            radius=50,
                            popup=Requerimiento_3[1],
                            color="#FF0011",
                            fill=True,
                            fill_color="#FF0011",).add_to(m)
                folium.Circle(radius=100,
                            location=lat2,
                            popup=Requerimiento_3[2],
                            color="crimson",
                            fill=False,).add_to(m)
                folium.CircleMarker(
                            location=lat2,
                            radius=50,
                            popup=Requerimiento_3[2],
                            color="#FF9900",
                            fill=True,
                            fill_color="#FF9900",).add_to(m)
                folium.PolyLine(locations=[lat,lat2], color='#10D824').add_to(m)
                m.save("Requerimiento_3.html")
            else:
                print("Entradas erróneas")
        elif opciones=="6":
            Requerimiento_4=controller.Requerimiento_4(analyzer,analyzer_2,analyzer3)
            print("El número de nodos conectados a la red de expansión mínima es de "+str(Requerimiento_4[0]["total"]))
            print("El costo total (distancia en [km]) de la red de expansión mínima es de "+str(Requerimiento_4[1]))
            print("La rama más larga va del nodo "+str(Requerimiento_4[0]["name"])+" al nodo "+str(Requerimiento_4[2][0]))
            lat=[]
            lat2=[]
            for i in analyzer_2:
                    if i["landing_point_id"] in Requerimiento_4[0]["name"]:
                        lat.append(float(i["latitude"]))
                        lat.append(float(i["longitude"]))
            for i in analyzer_2:
                    if i["landing_point_id"] in Requerimiento_4[2][0]:
                        lat2.append(float(i["latitude"]))
                        lat2.append(float(i["longitude"]))
            m = folium.Map(location=lat, tiles="Stamen Toner", zoom_start=7)
            folium.Circle(radius=100,
                            location=lat,
                            popup=Requerimiento_4[0],
                            color="crimson",
                            fill=False,).add_to(m)
            folium.CircleMarker(
                            location=lat,
                            radius=50,
                            popup=Requerimiento_4[0],
                            color="#FF0000",
                            fill=True,
                            fill_color="#FF0000",).add_to(m)
            folium.Circle(radius=100,
                            location=lat2,
                            popup=Requerimiento_4[2][0],
                            color="crimson",
                            fill=False,).add_to(m)
            folium.CircleMarker(
                            location=lat2,
                            radius=50,
                            popup=Requerimiento_4[2][0],
                            color="#FFFF00",
                            fill=True,
                            fill_color="#FFFF00",).add_to(m)
            folium.PolyLine(locations=[lat,lat2], color='#3333FF').add_to(m)
            m.save("Requerimiento_4.html")
        elif opciones=="7":
            rango=input("Nombre del landing point: ")
            Requerimiento_5=controller.Requerimiento_5(analyzer3,rango,analyzer_2)
            print("Número de paises afectados es de "+str(len(Requerimiento_5)))
            colores=["#0000CC","#009900","#FF0000","#0BE4FC","#771290","#FFFF00","#FFFFFF","#CCFFFF","#FFFFCC","#CCCCFF","#FFCCCC","#99FFFF","#CCCCCC","#FFFF99","#66FFCC","#99CCFF","#99FF99","#99CCCC","#00FFFF","#FF99FF","#33CCCC","#66CC99","#999999","#FFCC00","#00FF99","#CCCC66","#6699FF","#FF66CC","#FF9966","#66FF00","#FF6666","#33CC66","#33CC33","#00FF00","#009999","#FF3300","#339933","#006600","#990000"]
            for i in Requerimiento_5:
                print(i+" que se encuentra "+str(Requerimiento_5[i])+" kilómetros del landing point "+rango)
            for i in analyzer_2:
                if rango in i["name"]:
                    pais=i["name"]
            a=list(Requerimiento_5.keys())
            a.insert(0,pais)
            lat=[]
            for z in a:
                for i in analyzer_2:
                    if i["name"] in z:
                        lat.append([float(i["latitude"]),float(i["longitude"])])
            m = folium.Map(location=lat[0], tiles="Stamen Toner", zoom_start=3)
            folium.Circle(radius=100,
                            location=lat[0],
                            popup=a[0],
                            color="crimson",
                            fill=False,).add_to(m)
            folium.CircleMarker(
                            location=lat[0],
                            radius=50,
                            popup=a[0],
                            color=random.choice(colores),
                            fill=True,
                            fill_color=random.choice(colores),).add_to(m)
            for i in lat:
                folium.PolyLine(locations=[lat[0],i], color=random.choice(colores)).add_to(m)
            m.save("Requerimiento_5.html")
        elif opciones=="8":
            pais=input("Nombre del país: ")
            cable=input("Nombre del cable: ")
            Requerimiento_6=controller.Requerimiento_6(analyzer3,pais,cable,analyzer_2,analyzer4)
            if Requerimiento_6==None:
                print("Nombre de cable o país equivocado, intente de nuevo")
            else:
                a=[]
                cont=0
                for i in Requerimiento_6:
                    print(i[0]+" - "+" se puede asegurar un ancho de banda de "+str(i[1])+" Mbp")
                    a.append(i[0])
                a.insert(0,pais)
                lat=[]
                nombres=[]
                for z in a:
                    for i in analyzer_2:
                        if z in i["name"]:
                            lat.append([float(i["latitude"]),float(i["longitude"])])
                            nombres.append(z)
                indices=[]
                for i in a:
                    indices.append(nombres.index(i))
                latitudes=[]
                for i in indices:
                    latitudes.append(lat[i])
                m = folium.Map(location=latitudes[0], tiles="Stamen Toner", zoom_start=3)
            folium.Circle(radius=100,
                            location=latitudes[0],
                            popup=a[0],
                            color="crimson",
                            fill=False,).add_to(m)
            folium.CircleMarker(
                            location=latitudes[0],
                            radius=50,
                            popup="Laurelhurst Park",
                            color="#FF0000",
                            fill=True,
                            fill_color="#FF0000",).add_to(m)
            for i in latitudes:
                folium.PolyLine(locations=[latitudes[0],i], color='#009900').add_to(m)
            m.save("Requerimiento_6.html")
        elif opciones=="9":
            ip1=input("Dirección ip1: ")
            ip2=input("Dirección ip2: ")
            Requerimiento_7=controller.Requerimiento_7(ip1,ip2,analyzer_2,analyzer3)
            cont=0
            a=[]
            if Requerimiento_7==None:
                print("Dirección IP errónea")
            else:
                for i in Requerimiento_7:
                    if cont==0:
                        print("INICIO: "+str(i)+"=> ")
                        a.append(i)
                        cont+=1
                    elif cont==len(Requerimiento_7)-1:
                        print("FIN "+str(i))
                        a.append(i)
                    else:
                        print("=> "+str(i)+" =>")
                        cont+=1   
                print("El número de saltos en la ruta es de "+str(len(Requerimiento_7))) 
                lat=[]
                lat2=[]
                for i in analyzer_2:
                    if i["landing_point_id"] in a[0]:
                        lat.append(float(i["latitude"]))
                        lat.append(float(i["longitude"]))
                for i in analyzer_2:
                    if i["landing_point_id"] in a[1]:
                        lat2.append(float(i["latitude"]))
                        lat2.append(float(i["longitude"]))
                m = folium.Map(location=lat, tiles="Stamen Toner", zoom_start=3)
                folium.Circle(radius=100,
                            location=lat,
                            popup=a[0],
                            color="crimson",
                            fill=False,).add_to(m)
                folium.CircleMarker(
                            location=lat,
                            radius=50,
                            popup="Laurelhurst Park",
                            color="#3186cc",
                            fill=True,
                            fill_color="#3186cc",).add_to(m)
                folium.Circle(radius=100,
                            location=lat2,
                            popup=a[0],
                            color="crimson",
                            fill=False,).add_to(m)
                folium.CircleMarker(
                            location=lat2,
                            radius=50,
                            popup="Laurelhurst Park",
                            color="#FFFF00",
                            fill=True,
                            fill_color="#FFFF00",).add_to(m)
                folium.PolyLine(locations=[lat,lat2], color='#FF0000').add_to(m)
                m.save("Requerimiento_7.html")
        elif opciones == "10":
            A = False
OpcionesMenu()