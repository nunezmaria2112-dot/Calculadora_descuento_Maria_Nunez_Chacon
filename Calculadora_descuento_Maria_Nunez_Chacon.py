def aplicar_descuento (precio, descuento):
  precio_final = precio- (precio * descuento / 100)
  return precio_final

def calcular_descuento ():
  precio = int(input("Introduce el precio de tu producto:"))
  descuento = int(input("Introduce el porcentaje de descuento:"))
    
  precio_final = aplicar_descuento(precio, descuento)

  def mostrar_mensaje (precio_final):
    print("El monto a pagar es:", precio_final)

  mostrar_mensaje(precio_final)

calcular_descuento()
