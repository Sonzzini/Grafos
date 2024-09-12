# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:01:41 2023

@author: icalc
"""
salario = float(input("Salario: "))
percAum = float(input("Percentual de Aumento: "))
valor_aumento = salario*percAum/100
novo_salario = salario + valor_aumento
print(f"Salario: {salario:10.2f}.")
print(f"Valor aumento: {valor_aumento:10.2f}.")
print(f"Novo Salário: {novo_salario:10.2f}.")