print('esto es un ejercicio sobre bucles')
# Lista de usuarios y contraseñas (como si fuera una base de datos simple)
usuarios = {
    'ana': 'clave123',
    'juan': 'python456',
    'maria': 'secreta789'
}

# Registro de intentos
intentos = []

# Bucle de verificación (máximo 5 intentos)
for intento in range(5):
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    # Guardamos el intento en el registro
    intentos.append((usuario, contraseña))

    # Validamos
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print(f"✅ Acceso concedido, bienvenido/a {usuario}!")
        break
    else:
        print("❌ Usuario o contraseña incorrectos.")
        continue
else:
    print("🔒 Demasiados intentos fallidos. Acceso denegado.")

# Mostrar resumen de intentos usando enumerate y comprensión de listas
print("\n📋 Registro de intentos:")
[print(f"{i+1}. Usuario: {u}, Contraseña: {p}") for i, (u, p) in enumerate(intentos)]
