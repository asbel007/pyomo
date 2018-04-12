#tutorial

from pyomo.environ import *

model= AbstractModel()

model.hour=Set()
#hour=[1,2,3,4,5,6,7,8,9]
model.price=Param(model.hour, within=NonNegativeReals)
#price={1:4.5,2:2.5,3:5.9,4:0.8,5:8,6:5,7:1.8,8:2.5,9:8.7}

model.P_out=Param()
model.P_in=Param()
model.Dt_p=Param()

model.E_out= Var(model.hour, within= NonNegativeReals)
model.E_in= Var(model.hour, within= NonNegativeReals)

def obj_rule(model):
	#return sum(model.E_out[i]*model.price[i] for i in 10)
	return sum((model.E_out[i]-model.E_in[i])*model.price[i] for i in model.hour)
model.Obj= Objective(rule= obj_rule, sense= maximize)

def con_rule(model,i):
	#return (model.E_out[i] <= model.P_out*model.Dt_p for i in 10 )
	return (model.E_out[i] <= model.P_out*model.Dt_p)
model.Con1= Constraint(model.hour, rule= con_rule)

def con2_rule(model,i):
	#return (model.E_out[i] <= model.P_out*model.Dt_p for i in 10 )
	return (model.E_in[i] <= model.P_in*model.Dt_p)
model.Con2= Constraint(model.hour, rule= con2_rule)

from pyomo.opt import SolverFactory
opt = SolverFactory('glpk')
instance = model.create_instance("data_tuto.dat")                               
results = opt.solve(instance)
instance.display()
#instance.solutions.load_from(results)

