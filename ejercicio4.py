def mensaje_pregunta():
    return print(" 1 si  2 no")

print("- Ingresos brutos iguales o superiores a $49.850.000")
mensaje_pregunta()
respuestaIngresosBrutos = input()

print("- Patrimonio bruto a diciembre 31 de 2020 superior a 160.232.000")
mensaje_pregunta()
respuestaPatrimonioBruto = input()

print("- Consumo de tarjetas crédito en 2020 superior a $49.850.000")
mensaje_pregunta()
respuestaTarjetasCredito = input()

print("-- Total, de compras y consumos en 2020 superior a $49.850.000")
mensaje_pregunta()
respuestaComprasConsumos = input()

print("- Consignaciones, depósitos e inversiones en 2020 superior a $49.850.000")
mensaje_pregunta()
respuestaDepositosInversiones = input()

if respuestaIngresosBrutos == "1" or respuestaPatrimonioBruto == "1" or respuestaTarjetasCredito == "1" or respuestaComprasConsumos == "1" or respuestaDepositosInversiones == "1":
    print(" -- Debe pagar impuestos")
else: print("No debe pagar impuestos")    

