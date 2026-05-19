from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def crear_oraculo_constante():
    """Un oráculo constante que siempre devuelve 1 sin importar la entrada."""
    circuito = QuantumCircuit(2)
    circuito.x(1)  # Simplemente activamos el qubit de salida (siempre da 1)
    return circuito


def crear_oraculo_balanceado():
    """Un oráculo balanceado (la salida cambia según la entrada)."""
    circuito = QuantumCircuit(2)
    circuito.cx(0, 1)  # Usamos una puerta CNOT (Controlled-NOT)
    return circuito


def algoritmo_deutsch(oraculo):
    # Creamos un circuito con 2 qubits y 1 bit clásico para la medición
    qc = QuantumCircuit(2, 1)

    # 1. Preparación del estado inicial
    # El qubit 0 empieza en |0> y el qubit 1 lo pasamos a |1>
    qc.x(1)

    # Ponemos ambos qubits en superposición usando puertas Hadamard (H)
    qc.h(0)
    qc.h(1)

    qc.barrier()  # Línea visual para separar los bloques en el circuito

    # 2. Inyectamos el oráculo secreto (la "caja negra")
    qc.compose(oraculo, inplace=True)

    qc.barrier()

    # 3. Interferencia: Aplicamos otra puerta H al qubit 0
    qc.h(0)

    # 4. Medición del qubit 0
    qc.measure(0, 0)

    return qc


# --- Demostración en clase ---
if __name__ == "__main__":
    print("--- DEMOSTRACIÓN: ALGORITMO DE DEUTSCH ---")

    # Elegimos uno de los dos oráculos de forma secreta
    int_oraculo = int(input("Introduce 0 para constante o 1 para balanceado: "))
    oraculo_secreto = None
    if int_oraculo == 0:
        print(" Utilizamos el oraculo constante")
        oraculo_secreto = crear_oraculo_constante()
    else:
        print(" Utilizamos el oraculo balanceado")
        oraculo_secreto = crear_oraculo_balanceado()

    # Construimos el circuito de Deutsch
    circuito_completo = algoritmo_deutsch(oraculo_secreto)

    # Simulamos el circuito cuántico
    simulador = AerSimulator()
    resultado = simulador.run(circuito_completo, shots=1).result()
    cuentas = resultado.get_counts()

    # Interpretación del resultado cuántico
    # Si el resultado medido es '0' -> La función es CONSTANTE
    # Si el resultado medido es '1' -> La función es BALANCEADA
    print("\n[+] Ejecutando el algoritmo en el simulador cuántico...")
    print(f"[+] Resultado de la medición: {cuentas}")

    if '0' in cuentas:
        print("\nResultado: La función secreta es CONSTANTE.")
    else:
        print("\nResultado: La función secreta es BALANCEADA.")