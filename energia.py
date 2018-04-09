#ejemplo de programacion
from pyomo.environ import *

model=AbstractModel()

model.hour=Set()
model.price=Set()

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

model.E_in=Var(within= NonNegativeReals)
model.E_out=Var(within= NonNegativeReals)

def obj_rule(model):
	return ()
model.obj=Objective(rule=obj_rule)

def con1_rule():
	return ()
model.con1=Constraint(rule=con1_rule)

def con2_rule():
	return ()
model.con2=Constraint(rule=con2_rule)