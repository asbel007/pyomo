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

fun obj_rule(model):
	return ()
model.obj=Objective()

fun con1_rule()
	return ()
model.con1=Constraint()

fun con2_rule()
	return ()
model.con2=Constraint()