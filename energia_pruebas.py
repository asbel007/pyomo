# -*- coding: utf-8 -*-
"""
Recreate en 25 March 2017
@colaborator: Asbel Apaza Romero
"""

#importacion de la libreria para la optimizacion
from pyomo.environ import *
 
#Modelo escogido: abstracto
model = AbstractModel()

#Declaracion del conjunto de varibles_datos
model.plantas = Set()
model.mercados = Set()

#Se le asigna los parametros a cada conjunto de variables
model.produccion = Param(model.plantas)
model.costes = Param(model.plantas, model.mercados)

#cuales seran las variables que seran relacionadas, resultados no negativos
model.unidades = Var(model.plantas, model.mercados, within = NonNegativeReals)

#define la suma de r*costo*unidad
def CosteTotal (model):
    return sum(model.costes[n,i]*model.unidades[n,i]
      for n in model.plantas
      for i in model.mercados)
          
#cual se a de optimizar(en este caso minimizar costo)
model.costefinal = Objective(rule=CosteTotal)

#se define las restricciones del conjunto plantas
def MaxProduccion(model,pl):
    return sum(model.unidades[pl,j] for j in model.mercados) >= model.produccion[pl]
model.ProdConstraint = Constraint(model.plantas, rule=MaxProduccion)

#Se invoca al solver, direccion de los datos
from pyomo.opt import SolverFactory
opt = SolverFactory('glpk')
instance = model.create_instance("C:\Users\SISCBBA01\Desktop\Otras documentaciones\Python\Examples pyomo\produccion/Variables2.dat")
results = opt.solve(instance)
instance.display()
instance.solutions.load_from(results)

def pyomo_postprocess(options=None, instance=None, results=None):
  model.unidades.display()