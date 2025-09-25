# Mean-Variance-Standard Deviation Calculator
# Proyecto por Mauro
# FreeCodeCamp - Data Analysis with Python

import numpy as np

def calculate(list_numbers):
    """
    Calcula la media, varianza, desviación estándar, máximo, mínimo y suma
    de una lista de 9 números organizados en una matriz 3x3.
    
    Args:
        list_numbers: Lista de exactamente 9 números
        
    Returns:
        dict: Diccionario con las estadísticas calculadas
        
    Raises:
        ValueError: Si la lista no contiene exactamente 9 elementos
    """
    
    # Validar que la lista tenga exactamente 9 elementos
    if len(list_numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convertir la lista en una matriz 3x3 usando NumPy
    matrix = np.array(list_numbers).reshape(3, 3)
    
    # Calcular estadísticas para cada eje y para toda la matriz
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Media por columnas
            matrix.mean(axis=1).tolist(),  # Media por filas
            matrix.mean().tolist()         # Media de toda la matriz
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # Varianza por columnas
            matrix.var(axis=1).tolist(),   # Varianza por filas
            matrix.var().tolist()          # Varianza de toda la matriz
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # Desv. estándar por columnas
            matrix.std(axis=1).tolist(),   # Desv. estándar por filas
            matrix.std().tolist()          # Desv. estándar de toda la matriz
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # Máximo por columnas
            matrix.max(axis=1).tolist(),   # Máximo por filas
            matrix.max().tolist()          # Máximo de toda la matriz
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # Mínimo por columnas
            matrix.min(axis=1).tolist(),   # Mínimo por filas
            matrix.min().tolist()          # Mínimo de toda la matriz
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # Suma por columnas
            matrix.sum(axis=1).tolist(),   # Suma por filas
            matrix.sum().tolist()          # Suma de toda la matriz
        ]
    }
    
    return calculations


# Función de prueba para verificar que funciona correctamente
def test_calculator():
    """Prueba la función calculate con datos de ejemplo"""
    
    print("🧮 Calculadora de Estadísticas - Proyecto de Mauro")
    print("=" * 50)
    
    # Ejemplo 1: Lista de números del 0 al 8
    test_list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(f"\n📊 Probando con: {test_list1}")
    print("Matriz 3x3 resultante:")
    matrix = np.array(test_list1).reshape(3, 3)
    print(matrix)
    print("\n🔢 Resultados:")
    
    result = calculate(test_list1)
    for key, value in result.items():
        print(f"{key.capitalize():20}: {value}")
    
    # Ejemplo 2: Números aleatorios
    test_list2 = [2, 6, 2, 8, 4, 0, 1, 5, 7]
    print(f"\n\n📊 Probando con: {test_list2}")
    print("Matriz 3x3 resultante:")
    matrix2 = np.array(test_list2).reshape(3, 3)
    print(matrix2)
    print("\n🔢 Resultados:")
    
    result2 = calculate(test_list2)
    for key, value in result2.items():
        print(f"{key.capitalize():20}: {value}")
    
    # Ejemplo 3: Probando el error con lista incorrecta
    print(f"\n\n❌ Probando con lista de 8 elementos (debe dar error):")
    try:
        calculate([1, 2, 3, 4, 5, 6, 7, 8])
    except ValueError as e:
        print(f"Error capturado correctamente: {e}")
    
    print(f"\n✅ ¡Todas las pruebas completadas exitosamente!")
    print("🚀 La función está lista para enviar a FreeCodeCamp")


# Ejecutar las pruebas si este archivo se ejecuta directamente
if __name__ == "__main__":
    test_calculator()