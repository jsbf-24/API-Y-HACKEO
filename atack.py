import requests
import time

# Configuración
BASE_URL = "http://127.0.0.1:8000"

def get_all_users():
    # Obtiene todos los usuarios de la API
    try:
        response = requests.get(f"{BASE_URL}/users")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener usuarios: {e}")
        return []

def extract_credentials():
    # Iniciar temporizador
    inicio = time.time()
    
    #Extrae usuarios y contraseñas
    users = get_all_users()
    
    # Calcular tiempo transcurrido
    tiempo_transcurrido = time.time() - inicio
    
    if not users:
        print("No se pudieron conseguir los usuarios")
        print(f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")
        return
    
    print("\nUSUARIOS Y CONTRASEÑAS")
    for user in users:
        print(f"Username: {user['username']}")
        print(f"Password: {user['password']}")
        print(f"Email: {user['email']}")
        print(f"ID: {user['id']}")
        print(f"Activo: {user['is_active']}")
        print("-" * 30)
    
    # Mostrar resumen del tiempo
    print(f"\nTIEMPO DE EJECUCIÓN: {tiempo_transcurrido:.2f} segundos")
    print(f"TOTAL DE USUARIOS ENCONTRADOS: {len(users)}")

extract_credentials()

#jsbf-24