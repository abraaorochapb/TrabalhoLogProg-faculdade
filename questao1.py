print("Bem-vindo a loja do Abraao Rocha de Paula")
valUnit = float(input("Digite o valor do produto: "))
quant = int(input("Digite a quantidade do produto: "))
print (f"O valor SEM desconto: {valUnit*quant}")

def desconto(valUnit, quant):
  if quant < 200:
   return valUnit*quant
  elif quant >= 200 and quant < 1000:
   return valUnit*quant*0.95
  elif quant >= 1000 and quant < 2000:
   return valUnit*quant*0.90
  else:
   return valUnit*quant*0.85
  
print (f"O valor COM desconto: {desconto(valUnit, quant)}")

