#tutorial

from pyomo.environ import *

model= AbstractModel()

model.hour=Set()
model.price=Param(model.hour, within=NonNegativeReals)

model.n_in=Param()
model.n_out=Param()
model.Cap=Param(initialize=6.4)
model.PDD=Param()
model.P_out=Param()
model.P_in=Param()
model.Dt_p=Param()

model.E_out= Var(model.hour, within= PositiveReals)
model.E_in= Var(model.hour, within= PositiveReals)

def obj_rule(model):
	return sum((model.E_out[i]-model.E_in[i])*model.price[i] for i in model.hour)
model.Obj= Objective(rule= obj_rule, sense= maximize)

def con_rule(model,i):
	return (model.E_out[i] <= model.P_out*model.Dt_p)
model.Con_E_out= Constraint(model.hour, rule= con_rule)

def con2_rule(model,i):
	return (model.E_in[i] <= model.P_in*model.Dt_p)
model.Con_E_in= Constraint(model.hour, rule= con2_rule)

def con3_rule(model,i):
	#return (model.Cap*model.PDD <= model.E_in[i]*model.n_in-model.E_out[i]/model.n_out
	return (model.Cap*model.PDD <= model.E_in[i]*model.n_in - model.E_out[i]*model.n_out <= model.Cap)
model.Con3= Constraint(model.hour, rule= con3_rule)

from pyomo.opt import SolverFactory
opt = SolverFactory('glpk')
instance = model.create_instance("data_tuto.dat")                               
results = opt.solve(instance)
instance.display()
#instance.solutions.load_from(results)

