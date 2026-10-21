from datetime import datetime, timedelta

print(f"REPORTE DIARIO - {datetime.now().strftime('%d/%m/%Y %H:%M')}")
print("="*50)

# Inicializar contadores
total_iam = 0
total_pass = 0
total_sg = 0

# IAM
print("\nUSUARIOS SIN MFA:")
with open('usuarios_simulados.txt', 'r', encoding='utf-8-sig') as f:
    for linea in f:
        if 'no-mfa' in linea:
            usuario = linea.strip().split(':')[0]
            print(f"  - {usuario}")
            total_iam += 1

# CONTRASEÑAS DÉBILES
print("\n🔐 CONTRASEÑAS DÉBILES:")
with open('usuarios_simulados.txt', 'r', encoding='utf-8-sig') as f:
    for linea in f:
        if 'no-mfa' in linea:
            partes = linea.strip().split(':')
            usuario = partes[0]
            password = partes[1]
            if '123' in password or '2024' in password or password.startswith('password'):
                print(f"  ⚠️  {usuario} - Contraseña débil: {password}")
                total_pass += 1

# SECURITY GROUPS
print("\nREGLAS CRÍTICAS:")
print("="*50)
with open('security_groups.txt', 'r', encoding='utf-8-sig') as f:
    for linea in f:
        if '0.0.0.0/0' in linea:
            nombre = linea.strip().split(':')[0]
            if ':22' in linea or ':3389' in linea:
                print(f"  [CRITICO] {nombre} - SSH/RDP público")
                total_sg += 1
            elif ':80' in linea or ':443' in linea:
                print(f"  [WEB] {nombre} - Web (aceptable)")
            else:
                print(f"  [?] {nombre} - Puerto público sin clasificar")

# USUARIOS INACTIVOS
print("\n📅 USUARIOS INACTIVOS (+90 DÍAS):")
fecha_limite = datetime.now() - timedelta(days=90)
try:
    with open('ultimo_login.txt', 'r', encoding='utf-8-sig') as f:
        for linea in f:
            usuario, fecha_str = linea.strip().split(':')
            fecha_login = datetime.strptime(fecha_str, '%Y-%m-%d')
            if fecha_login < fecha_limite:
                print(f"  ⚠️  {usuario} - Inactivo desde {fecha_str}")
except FileNotFoundError:
    print("  Archivo ultimo_login.txt no encontrado")

# RESUMEN FINAL
print(f"\n📊 RESUMEN DE HALLAZGOS:")
print(f"  🔴 Usuarios sin MFA: {total_iam}")
print(f"  ⚠️  Contraseñas débiles: {total_pass}")
print(f"  🚨 Reglas CRÍTICAS: {total_sg}")

