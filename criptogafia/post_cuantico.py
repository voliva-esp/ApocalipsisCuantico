"""
    Este script simula el protocolo post-cuántico descrito por el nivel 3 de Apple en
    https://security.apple.com/blog/imessage-pq3/

"""


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
import oqs
import os


def derivar_nueva_llave(llave_anterior, secreto_nuevo_kyber):
    """ Función que evoluciona la llave mezclando el pasado con el nuevo intercambio PQ """
    return HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"ratchet evolucion pq3",
    ).derive(llave_anterior + secreto_nuevo_kyber)


def cifrar_mensaje(llave, texto):
    iv = os.urandom(12)
    encryptor = Cipher(algorithms.AES(llave), modes.GCM(iv)).encryptor()
    cifrado = encryptor.update(texto.encode()) + encryptor.finalize()
    return iv, cifrado, encryptor.tag


# --- INICIO DE LA SIMULACIÓN ---
ALGO_PQ = "Kyber512"
print(f"--- SIMULACIÓN iMessage PQ3 (Nivel 3) ---")

# ESTADO INICIAL: Handshake Nivel 2
llave_actual = os.urandom(32)                           # Imaginemos que ya hicimos el primer intercambio
print(f"[Sistema] Conversación iniciada. Llave inicial: {llave_actual.hex()[:10]}...")

# ENVIANDO MENSAJES...
mensajes = ["Hola!", "¡Qué buena la charla de cuántica!", "Por cierto, tengo un secreto..."]

for i, m in enumerate(mensajes):
    # Simulamos que cada 2 mensajes, el protocolo PQ3 fuerza un RE-KEYING (Nivel 3)
    if i > 0 and i % 2 == 0:
        print("\n[PQ3 ALERT] Se ha alcanzado el límite de uso de la llave.")
        print("[PQ3] Iniciando 'Self-Healing' (Autorreparación cuántica)...")

        # El receptor genera nueva llave PQ
        with oqs.KeyEncapsulation(ALGO_PQ) as receptor:
            pk_n = receptor.generate_keypair()
            # El emisor encapsula un nuevo secreto
            with oqs.KeyEncapsulation(ALGO_PQ) as emisor:
                ct_n, secreto_n = emisor.encap_secret(pk_n)

            # EVOLUCIÓN: La llave vieja muere, nace una nueva basada en Kyber
            llave_actual = derivar_nueva_llave(llave_actual, secreto_n)
            print(f"[PQ3] Nueva llave de nivel 3 generada: {llave_actual.hex()[:10]}...")

    # Cifrado del mensaje con la llave del momento
    iv, ct, tag = cifrar_mensaje(llave_actual, m)
    print(f" -> Enviando Mensaje {i + 1} (Cifrado): {ct.hex()[:20]}...")

print("\n[Conclusión] Si un atacante robara la llave del Mensaje 1, no podría leer el Mensaje 3, porque el protocolo "
      "ya ha 'sanado' la conexión.")
