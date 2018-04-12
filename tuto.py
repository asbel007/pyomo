#tutorial

from pyomo.environ import *

model= AbstractModel()

model.hour=Set()

model.P_out=Param()
model.Dt_p=Param()
#model.price=Param(model.hour)
model.price=Param()

model.E_out= Var(within= NonNegativeReals)

def obj_rule(model):
	#return sum(model.E_out[i]*model.price[i] for i in 10)
	return sum(model.E_out[1]*model.price[1])
model.Obj= Objective(rule= obj_rule, sense= maximize)

def con_rule(model,i):
	#return (model.E_out[i] <= model.P_out*model.Dt_p)
	return (model.E_out[1] <= model.P_out*model.Dt_p)
model.Con1= Constraint(model.hour, rule= con_rule)

from pyomo.opt import SolverFactory
opt = SolverFactory('glpk')
instance = model.create_instance("data_tuto.dat")                               
results = opt.solve(instance)
instance.display()
instance.solutions.load_from(results)

