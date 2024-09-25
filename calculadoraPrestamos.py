class Prestamo:
    def __init__(self, monto, tasa_interes, años):
        self.monto = monto
        self.tasa_interes = tasa_interes
        self.años = años

    def calcular_cuota_mensual(self):
        tasa_mensual = self.tasa_interes / 100 / 12
        pagos_totales = self.años * 12
        
        cuota = self.monto * (tasa_mensual * (1 + tasa_mensual) ** pagos_totales) / ((1 + tasa_mensual) ** pagos_totales - 1)
        return cuota

    def calcular_interes_total(self, cuota):
        pagos_totales = self.años * 12
        return (cuota * pagos_totales) - self.monto

    def simulacion(self, nuevas_tasas):
        resultados = {}
        for tasa in nuevas_tasas:
            self.tasa_interes = tasa
            cuota = self.calcular_cuota_mensual()
            interes_total = self.calcular_interes_total(cuota)
            resultados[tasa] = {
                'cuota_mensual': cuota,
                'interes_total': interes_total
            }
        return resultados

def mostrar_menu():
    print("Bienvenido a la Calculadora de Préstamos Avanzada")
    print("Por favor, ingresa los datos del préstamo.")

def main():
    mostrar_menu()

    try:
        monto = float(input("Monto del préstamo: $"))
        tasa_interes = float(input("Tasa de interés anual (%): "))
        años = int(input("Años para pagar el préstamo: "))
        
        # Validar que los valores sean positivos
        if monto <= 0 or tasa_interes <= 0 or años <= 0:
            raise ValueError("Los valores deben ser números positivos.")

        # Crear una instancia de la clase Prestamo
        prestamo = Prestamo(monto, tasa_interes, años)

        # Calcular la cuota mensual
        cuota = prestamo.calcular_cuota_mensual()
        # Calcular el interés total
        interes_total = prestamo.calcular_interes_total(cuota)
        
        print(f"\nLa cuota mensual será: ${cuota:.2f}")
        print(f"El interés total pagado será: ${interes_total:.2f}")

        # Simulación de diferentes tasas de interés
        nuevas_tasas = [tasa_interes - 1, tasa_interes, tasa_interes + 1]
        print("\nSimulaciones con diferentes tasas de interés:")
        resultados_simulacion = prestamo.simulacion(nuevas_tasas)
        
        for tasa, resultados in resultados_simulacion.items():
            print(f"Tasa de interés: {tasa}% - Cuota mensual: ${resultados['cuota_mensual']:.2f}, Interés total: ${resultados['interes_total']:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}. Asegúrate de introducir valores válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Llamar a la función principal para ejecutar la calculadora
main()
