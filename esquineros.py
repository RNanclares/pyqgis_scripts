#!/usr/bin/env python
# -*- coding: utf-8 -*-

import qgis.core
from PyQt4.QtCore import *

def esquina_inferior_derecha(listado_gids):
    for g in listado_gids:
        pkid = g
        qsql="(SELECT (dp).path[1] as id,(dp).geom, st_distance((dp).geom, (select st_setsrid(st_point(ST_XMax(geom), ST_YMin(geom)),32613) from manzanas_esquineros where gid ="+ pkid +")) as dis from (SELECT st_DumpPoints(geom) as dp FROM manzanas_esquineros WHERE gid = " + pkid +") as foo order by dis limit 1)"
        uri = QgsDataSourceURI()
        uri.setConnection("localhost", "5432", "gislocal", "postgres", "raul")
        uri.setDataSource("",qsql,"geom","","id")
        resultado = QgsVectorLayer(uri.uri(), "resultado_query", "postgres")
        crs = resultado.crs()
        crs.createFromId(32613)
        resultado.setCrs(crs)
        if not layer.isValid:
            print 'error'
        else:
            pass
        features = resultado.getFeatures()
        for f in features:  
            geom = f.geometry()
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPoint(geom.asPoint()))
            attrs = f.attributes()
            fet.setAttributes([attrs[0],attrs[1]])
            pr.addFeatures([fet])
    return
        
def esquina_superior_derecha(listado_gids):
    for g in listado_gids:
        pkid = g
        qsql="(SELECT (dp).path[1] as id,(dp).geom, st_distance((dp).geom, (select st_setsrid(st_point(ST_XMax(geom), ST_YMax(geom)),32613) from manzanas_esquineros where gid ="+ pkid +")) as dis from (SELECT st_DumpPoints(geom) as dp FROM manzanas_esquineros WHERE gid = " + pkid +") as foo order by dis limit 1)"
        uri = QgsDataSourceURI()
        uri.setConnection("localhost", "5432", "gislocal", "postgres", "raul")
        uri.setDataSource("",qsql,"geom","","id")
        resultado = QgsVectorLayer(uri.uri(), "resultado_query", "postgres")
        crs = resultado.crs()
        crs.createFromId(32613)
        resultado.setCrs(crs)
        if not layer.isValid:
            print 'error'
        else:
            pass
        features = resultado.getFeatures()
        for f in features:  
            geom = f.geometry()
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPoint(geom.asPoint()))
            attrs = f.attributes()
            fet.setAttributes([attrs[0],attrs[1]])
            pr.addFeatures([fet])
    return
        
def esquina_inferior_izquierda(listado_gids):
    for g in listado_gids:
        pkid = g
        qsql="(SELECT (dp).path[1] as id,(dp).geom, st_distance((dp).geom, (select st_setsrid(st_point(ST_XMin(geom), ST_YMin(geom)),32613) from manzanas_esquineros where gid ="+ pkid +")) as dis from (SELECT st_DumpPoints(geom) as dp FROM manzanas_esquineros WHERE gid = " + pkid +") as foo order by dis limit 1)"
        uri = QgsDataSourceURI()
        uri.setConnection("localhost", "5432", "gislocal", "postgres", "raul")
        uri.setDataSource("",qsql,"geom","","id")
        resultado = QgsVectorLayer(uri.uri(), "resultado_query", "postgres")
        crs = resultado.crs()
        crs.createFromId(32613)
        resultado.setCrs(crs)
        if not layer.isValid:
            print 'error'
        else:
            pass
        features = resultado.getFeatures()
        for f in features:  
            geom = f.geometry()
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPoint(geom.asPoint()))
            attrs = f.attributes()
            fet.setAttributes([attrs[0],attrs[1]])
            pr.addFeatures([fet])
    return
        
def esquina_superior_izquierda(listado_gids):
    
    for g in listado_gids:
        pkid = g
        qsql="(SELECT (dp).path[1] as id,(dp).geom, st_distance((dp).geom, (select st_setsrid(st_point(ST_XMin(geom), ST_YMax(geom)),32613) from manzanas_esquineros where gid ="+ pkid +")) as dis from (SELECT st_DumpPoints(geom) as dp FROM manzanas_esquineros WHERE gid = " + pkid +") as foo order by dis limit 1)"
        uri = QgsDataSourceURI()
        uri.setConnection("localhost", "5432", "gislocal", "postgres", "raul")
        uri.setDataSource("",qsql,"geom","","id")
        resultado = QgsVectorLayer(uri.uri(), "resultado_query", "postgres")
        crs = resultado.crs()
        crs.createFromId(32613)
        resultado.setCrs(crs)
        if not layer.isValid:
            print 'error'
        else:
            pass
        features = resultado.getFeatures()
        for f in features:  
            geom = f.geometry()
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPoint(geom.asPoint()))
            attrs = f.attributes()
            fet.setAttributes([attrs[0],attrs[1]])
            pr.addFeatures([fet])
    return
        



uri2 = QgsDataSourceURI()
uri2.setConnection("localhost", "5432", "gislocal", "postgres", "raul")
uri2.setDataSource("public", "manzanas_esquineros", "geom", "")
tabla = QgsVectorLayer(uri2.uri(), "tabla", "postgres")
filas_tabla = tabla.getFeatures()

listado_gids = []

for t in filas_tabla:
    listado_gids.append(str(int(t.attributes()[0])))


#creamos la capa que va a almacenar los puntos de la query
puntos_esquinas = QgsVectorLayer("Point", "puntos_esquinas", "memory")
crs2 = puntos_esquinas.crs()
crs2.createFromId(32613)
puntos_esquinas.setCrs(crs2)

pr = puntos_esquinas.dataProvider()


puntos_esquinas.startEditing()
#Añadimos campos
pr.addAttributes([QgsField("id", QVariant.Int),QgsField("dis", QVariant.Double),QgsField("cve_manzana",QVariant.String)])

#Corremos las funciones
#esquina_inferior_derecha(listado_gids)
#esquina_superior_derecha(listado_gids)
esquina_inferior_izquierda(listado_gids)
#esquina_superior_izquierda(listado_gids)
        
puntos_esquinas.commitChanges()
puntos_esquinas.updateExtents()

QgsMapLayerRegistry.instance().addMapLayer(puntos_esquinas)




        
    
    







#    QgsMapLayerRegistry.instance().addMapLayer(resultado)
#    
#for field in resultado.fields():
#    print field.name(), field.typeName()
#    
#print resultado.wkbType() == QGis.WKBPoint
#
#features = resultado.getFeatures()
#for f in features:  
#    geom = f.geometry()
#    attrs = f.attributes()
#    print attrs[0],attrs[1]
#    print geom
#    print geom.asPoint()
    
#gPnt = QgsGeometry.fromPoint(geom.asPoint())

   
#fet = QgsFeature()
#fet.setGeometry(QgsGeometry.fromWkb     
##creamos la capa que va a almacenar los puntos de la query
#puntos_esquinas = QgsVectorLayer("Point", "puntos_esquinas", "memory")
#crs2 = puntos_esquinas.crs()
#crs2.createFromId(32613)
#puntos_esquinas.setCrs(crs2)
#
#pr = puntos_esquinas.dataProvider()
##Añadimos campos
#pr.addAttributes([QgsField("id", QVariant.Int),QgsField("dis", QVariant.Double),QgsField("cve_manzana",QVariant.String)])
  
#activamos la edicion
#puntos_esquinas.startEditing()

#For i in range(len(Receivers)):
#objeto = QgsFeature()
#objeto.setGeometry(QgsGeometry.FromPoint(QgsPoint.wellKnownText(geometria)))

