#ejemplo de programacion
from pyomo.environ import *

model=AbstractModel()

model.hour=Set()
model.price=Set()

model.Cap=Param()
model.PDD= Param()