from datetime import datetime
import os

class Color:
    VERDE = '\033[92m'
    AMARILLO = '\033[93m'
    ROJO = '\033[91m'
    AZUL = '\033[94m'
    RESET = '\033[0m'

def leer_usuarios():
    """Lee usuarios sin MFA del archivo"""
    sin_mfa = []
    try:
        with open('usuarios_simulados.txt', 'r', encoding='utf-8-sig') as f:
            for linea in f:
                if 'no-mfa' in linea:
                    usuario = linea.strip().split(':')[0]
                    sin_mfa.append(usuario)
    except FileNotFoundError:
        print("Archivo usuarios_simulados.txt no encontrado")
    return sin_mfa

def leer_reglas_criticas():
    """Lee Reglas Críricas (SSH/RDP públicos)"""
    criticas = []
    try:
        with open('security_groups.txt', 'r', encoding='utf-8-sig') as f:
            for linea in f:
                if '0.0.0.0/0' in linea and (':22' in linea or ':3389' in linea):
                    nombre = linea.strip().split(':')[0]
                    criticas.append(nombre)
    except FileNotFoundError:
        print("Archivo security_groups.txt no encontrado")
    return criticas
    
def leer_contraseñas_debiles():
    """Lee Contraseñas Débiles"""
    debiles = []
    try:
        with open('usuarios_simulados.txt', 'r', encoding='utf-8-sig') as f:
            for linea in f:
                if 'no-mfa' in linea:
                    partes = linea.strip().split(':')
                    usuario = partes[0]
                    password = partes[1]
                    if '123' in password or '2024' in password or password.startswith('password'):
                        debiles.append(usuario)
    except FileNotFoundError:
        print("Archivo usuarios_simulados.txt no encontrado")
    return debiles

def calcular_puntuacion(sin_mfa, criticas, debiles):
    """Calcula puntuación de seguridad (0-100)"""
    puntuacion = 100
    puntuacion -= len(sin_mfa) * 10
    puntuacion -= len(criticas) *15
    puntuacion -= len(debiles) *5
    return max(0, puntuacion)

def detectar_usuarios_privilegiados(sin_mfa):
    """Detecta usuarios con 'admin' en el nombre"""
    admin_users = []
    for usuario in sin_mfa:
        if 'admin' in usuario.lower():
            admin_users.append(usuario)
    return admin_users

def detectar_puertos_no_estandar():
    """Detecta puertos no estándar en Security Groups"""
    puertos_no_estandar = []
    try:
        with open('security_groups.txt', 'r', encoding='utf-8-sig') as f:
            for linea in f:
                if '0.0.0.0/0' in linea:
                    puertos = linea.strip().split(':')[3]
                    # Si hay múltiples puertos separados por coma
                    for p in puertos.split(','):
                        if p not in ['22', '3389', '80', '443']:
                            puertos_no_estandar.append(p)
    except FileNotFoundError:
        print("Archivo security_groups.txt no encontrado")
    return puertos_no_estandar

def generar_reporte():
    """Generar reporte profesional"""
    print("="*60)
    print("INFORME DE AUDITORÍA DE SEGURIDAD")
    print("="*60)
    print(f"Fecha: {datetime.now().strftime('%d/%m/%Y')}")
    print(f"Hora: {datetime.now().strftime('%H:%M')}")
    print("-"*60)

    # OBTENER DATOS
    sin_mfa = leer_usuarios()
    criticas = leer_reglas_criticas()
    debiles = leer_contraseñas_debiles()

    #NUEVO.Detectar usuarios admin sin MFA
    admin_riesgo = detectar_usuarios_privilegiados(sin_mfa)

    #NUEVA: Llamar a la función 
    puertos_no_estandar = detectar_puertos_no_estandar()

    # Calcular puntuacion
    puntuacion = calcular_puntuacion(sin_mfa, criticas, debiles)

    # Nivel de riesgo
    if puntuacion >= 80:
        nivel = f"{Color.VERDE} BAJO {Color.RESET}"
    elif puntuacion >= 60:
        nivel = f"{Color.AMARILLO} MEDIO {Color.RESET}"
    else:
        nivel = f"{Color.ROJO} ALTO {Color.RESET}"
    
    print(f"\n📊 PUNTUACIÓN DE SEGURIDAD: {puntuacion}/100")
    print(f"   Nivel de riesgo: {nivel}")

    # HALLAZGOS
    print("\n⚠️ HALLAZGOS CRÍTICOS:")
    if sin_mfa:
        print(f"{Color.ROJO}   • {len(sin_mfa)} usuarios sin MFA: {', '.join(sin_mfa)}{Color.RESET}")
    if criticas:
        print(f"{Color.ROJO}   • {len(criticas)} reglas con acceso público: {', '.join(criticas)}{Color.RESET}")
    if debiles:
        print(f"{Color.ROJO}   • {len(debiles)} usuarios con contraseñas débiles: {', '.join(debiles)}{Color.RESET}")
    if puertos_no_estandar:
        print(f"  . Puertos nos estándar expuestos: {', '.join(puertos_no_estandar)}")
    
    #NUEVO. Mostrar usuarios admin sin MFA
    if admin_riesgo:
        print(f"{Color.ROJO}   • Usuarios ADMIN sin MFA {', '.join(admin_riesgo)} (CRÍTICO){Color.RESET}")

    if not sin_mfa and not criticas and not debiles:
        print("   ✅ No se encontraron hallazgos críticos")

    # RECOMENDACIONES (SIN ANIDAR)
    print("\n✅ RECOMENDACIONES:")
    if sin_mfa:
        print("   1. Activar MFA para usuarios sin autenticación de dos factores")
    if criticas:
        print("   2. Restringir acceso SSH y RDP a IPs autorizadas")
    if debiles:
        print("   3. Forzar cambio de contraseñas débiles")
    print("   4. Realizar seguimiento en 30 días")

    # GUARDAR REPORTE (SIEMPRE, NO DENTRO DE LOS IF)
    nombre_archivo = f"reporte_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write("INFORME DE AUDITORÍA DE SEGURIDAD\n")
        f.write("="*50 + "\n")
        f.write(f"Fecha: {datetime.now().strftime('%d/%m/%Y')}\n")
        f.write(f"Puntuación: {puntuacion}/100\n")
        f.write(f"Hallazgos: {len(sin_mfa)} sin MFA, {len(criticas)} reglas críticas\n")
    
    print(f"\n📄 Reporte guardado: {nombre_archivo}")

# AL FINAL DEL ARCHIVO (fuera de la función)
if __name__ == "__main__":
    generar_reporte()

def guardar_reporte_completo(sin_mfa, criticas, debiles, puntuacion):
    """Guardar reporte completo con timestamp más detallado"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    nombre = f"reporte_auditoria_{timestamp}.txt"

    with open(nombre, 'w', encoding='utf-8') as f:
        f.write("="*60 + "\n")
        f.write("INFORME DE AUDITORÍA DE SEGURIDAD\n")
        f.write("="*60 + "\n")
        f.write(f"Fecha:{datetime.now().strftime('%Y%m%d_%H%M')}\n")
        f.write(f"Puntuacion:{puntuacion}/100\n\n")
        
        f.write("HALLAZGOS:\n")
        f.write(f"-Usuarios sin MFA:{len(sin_mfa)} -> {',  '.join(sin_mfa)}\n")
        f.write(f"-Reglas críticas: {len(criticas)} -> {',  '.join(criticas)}\n ")
        f.write(f"-Contraseñas débiles:{len(debiles)} -> {',  '.join(debiles)}\n")

        f.write("RECOMENDACIONES\n")
        if sin_mfa:
            f.write("1.Activar MFA para usuarios sin autenticación\n")
        if criticas:
            f.write("2.Restringir acceso SSH y RDP a IPs autorizadas\n")
        if debiles:
            f.write("3.Forzar cambios de contraseñas débiles\n")

    print(f"Reporte detallado guardado:{nombre}")
    return nombre



