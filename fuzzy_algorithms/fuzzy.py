import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

cigarette = ctrl.Antecedent(np.arange(0, 41, 1))
weight = ctrl.Antecedent(np.arange(0, 51, 1))
blood_pressure = ctrl.Antecedent(np.arange(100, 181, 1))
risk = ctrl.Consequent(np.arange(0, 101, 1), 'Risk')

cigarette.automf(number=3, names=['low', 'medium', 'high'])
weight.automf(number=3, names=['normal', 'overweight', 'obesity'])
blood_pressure.automf(number=3, names=['normal', 'medium', 'high'])

risk['low'] = fuzz.trimf(risk.universe, [0, 0, 50])
risk['medium'] = fuzz.trimf(risk.universe, [0, 50, 100])
risk['high'] = fuzz.trimf(risk.universe, [50, 100, 100])

rule1 = ctrl.Rule(cigarette['low'] | weight['normal'] | blood_pressure['normal'], risk['low'])
rule2 = ctrl.Rule(cigarette['low'] | weight['normal'] | blood_pressure['medium'], risk['low'])
rule3 = ctrl.Rule(cigarette['low'] | weight['normal'] | blood_pressure['high'], risk['medium'])
rule4 = ctrl.Rule(cigarette['low'] | weight['overweight'] | blood_pressure['normal'], risk['low'])
rule5 = ctrl.Rule(cigarette['low'] | weight['overweight'] | blood_pressure['medium'], risk['medium'])
rule6 = ctrl.Rule(cigarette['low'] | weight['overweight'] | blood_pressure['high'], risk['medium'])
rule7 = ctrl.Rule(cigarette['low'] | weight['obesity'] | blood_pressure['normal'], risk['medium'])
rule8 = ctrl.Rule(cigarette['low'] | weight['obesity'] | blood_pressure['medium'], risk['medium'])
rule9 = ctrl.Rule(cigarette['low'] | weight['obesity'] | blood_pressure['high'], risk['high'])
rule10 = ctrl.Rule(cigarette['medium'] | weight['normal'] | blood_pressure['normal'], risk['low'])
rule11 = ctrl.Rule(cigarette['medium'] | weight['normal'] | blood_pressure['medium'], risk['medium'])
rule12 = ctrl.Rule(cigarette['medium'] | weight['normal'] | blood_pressure['high'], risk['medium'])
rule13 = ctrl.Rule(cigarette['medium'] | weight['overweight'] | blood_pressure['normal'], risk['medium'])
rule14 = ctrl.Rule(cigarette['medium'] | weight['overweight'] | blood_pressure['medium'], risk['medium'])
rule15 = ctrl.Rule(cigarette['medium'] | weight['overweight'] | blood_pressure['high'], risk['high'])
rule16 = ctrl.Rule(cigarette['medium'] | weight['obesity'] | blood_pressure['normal'], risk['medium'])
rule17 = ctrl.Rule(cigarette['medium'] | weight['obesity'] | blood_pressure['medium'], risk['high'])
rule18 = ctrl.Rule(cigarette['medium'] | weight['obesity'] | blood_pressure['high'], risk['high'])
rule19 = ctrl.Rule(cigarette['high'] | weight['normal'] | blood_pressure['normal'], risk['medium'])
rule20 = ctrl.Rule(cigarette['high'] | weight['normal'] | blood_pressure['medium'], risk['medium'])
rule21 = ctrl.Rule(cigarette['high'] | weight['normal'] | blood_pressure['high'], risk['high'])
rule22 = ctrl.Rule(cigarette['high'] | weight['overweight'] | blood_pressure['normal'], risk['medium'])
rule23 = ctrl.Rule(cigarette['high'] | weight['overweight'] | blood_pressure['medium'], risk['high'])
rule24 = ctrl.Rule(cigarette['high'] | weight['overweight'] | blood_pressure['high'], risk['high'])
rule25 = ctrl.Rule(cigarette['high'] | weight['obesity'] | blood_pressure['normal'], risk['high'])
rule26 = ctrl.Rule(cigarette['high'] | weight['obesity'] | blood_pressure['medium'], risk['high'])
rule27 = ctrl.Rule(cigarette['high'] | weight['obesity'] | blood_pressure['high'], risk['high'])

control_system = ctrl.ControlSystem([[rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27,]])

system = ctrl.ControlSystemSimulation(control_system)

system.input['cigarette'] = 10
system.input['weight'] = 30
system.input['blood_pressure'] = 120
system.compute()

print(system.output['risk'])
risk.view(sim=system)
