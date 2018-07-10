#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-

import pulp

### definindo aqui nossas limites 
lp = pulp.LpProblem("Otimização de estoque", pulp.LpMaximize) #### instânciando o problema
x = pulp.LpVariable('x', lowBound=0, cat = 'Continuous') ### tenho um limite inferior pra variável x, onde x>=0
y = pulp.LpVariable('y', lowBound=2, cat = 'Continuous') ### tenho um limite inferior para variável y, onde y>=2
### --------------------------------

####---------------------------
lp += 4*x + 3*y, "Z" ###minha função objetivo
####---------------------------

### definindo agora minhas resticrões
lp += 2 * y <= 25 - x
lp += 4 * y >= 2 * x - 8
lp += y <= 2 * x - 5
###----------------------------

lp.solve()
print("Status do problema: ",pulp.LpStatus[lp.status])
print("O valor das variáveis é: ")
for variable in lp.variables():
    print("{} = {}".format(variable.name, variable.varValue))
print("O valor ótimo é: ", pulp.value(lp.objective))
