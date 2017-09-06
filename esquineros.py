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
        if not resultado.isValid:
            print 'error'
        else:
            pass
        features = resultado.getFeatures()
        for f in features:  
            geom = f.geometry()
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPoint(geom.asPoint()))
            attrs = f.attributes()
            fet.setAttributes([1,attrs[1]])
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
        if not resultado.isValid:
            print 'error'
        else:
            pass
        features = resultado.getFeatures()
        for f in features:  
            geom = f.geometry()
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPoint(geom.asPoint()))
            attrs = f.attributes()
            fet.setAttributes([2,attrs[1]])
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
        if not resultado.isValid:
            print 'error'
        else:
            pass
        features = resultado.getFeatures()
        for f in features:  
            geom = f.geometry()
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPoint(geom.asPoint()))
            attrs = f.attributes()
            fet.setAttributes([3,attrs[1]])
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
        if not resultado.isValid:
            print 'error'
        else:
            pass
        features = resultado.getFeatures()
        for f in features:  
            geom = f.geometry()
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPoint(geom.asPoint()))
            attrs = f.attributes()
            fet.setAttributes([4,attrs[1]])
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
crs = puntos_esquinas.crs()
crs.createFromId(32613)
puntos_esquinas.setCrs(crs)

pr = puntos_esquinas.dataProvider()


puntos_esquinas.startEditing()
#Añadimos campos
pr.addAttributes([QgsField("id", QVariant.Int),QgsField("dis", QVariant.Double),QgsField("cve_manzana",QVariant.String)])

#Corremos las funciones
esquina_inferior_derecha(listado_gids)
esquina_superior_derecha(listado_gids)
esquina_inferior_izquierda(listado_gids)
esquina_superior_izquierda(listado_gids)
        
puntos_esquinas.commitChanges()
puntos_esquinas.updateExtents()


QgsMapLayerRegistry.instance().addMapLayer(puntos_esquinas)


