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

'''Se le asigna los parametros a cada conjunto de variables
Cap=Capacidad Nominal [Ah]
PDD= Minima profundidad de descarga
SOC= Estado de carga
n_in=eficiencia de carga
n_out=eficiencia de descarga
Dt_in=tiempo de entrada
Dt_out=tiempo de salida
P_in=Potencia maxima de entrada
P_out=Potencia maxima de salida
Dt_p= Duracion de cada periodo
'''
model.Cap=Param()
model.PDD= Param()
model.SOC=Param()
model.n_in=Param()
model.n_out=Param()
model.Dt_in=Param()
model.Dt_out=Param()
model.P_in=Param()
model.P_out=Param()
model.Dt_p=Param()

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
instance = model.create_instance("D:\pyomo/data.dat")
results = opt.solve(instance)
instance.display()
instance.solutions.load_from(results)

def pyomo_postprocess(options=None, instance=None, results=None):
  model.unidades.display()