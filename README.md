# Proffit Optimization
-
Variables
-
Set
Param
Var
Objective
Contraint

Details
-
Set: hour
Param: Cap, PDD, t_in, t_out, P_in, P_out, 
Var: SOC, E_in, E_out
Objective: Sum((E_out-E_in)* Price) , Maximize
Constraint:
  P_i/o * t_p >= E_i/o
  Cap * PDD <= SOC<= Cap  
