# Nmap Escaneo - Cheatsheet

## 📦 Instalación y verificación

```bash
# Verificar si está instalado
which nmap

# Instalar (si no está)
sudo apt update
sudo apt install nmap -y

# Ver versión
nmap --version

# Escaneo de puertos con detección de servicios
nmap -sV localhost

# Escaneo de puertos específicos
nmap -p 22,80,443,3306 localhost

# Escaneo de TODOS los puertos (tarda)
nmap -p- localhost

# Escaneo de rango de puertos
nmap -p 1-10000 --open localhost

# Escaneo SYN (semi-abierto, requiere sudo)
sudo nmap -sS localhost

# Ver interfaces de red
ip a

# Descubrir hosts en red local (ping scan)
nmap -sn 192.168.1.0/24

# Escaneo de red con detección de servicios
nmap -sV 192.168.1.0/24

Opciones de tiempo (-T)
Plantilla	Nombre	    Uso
-T0	       Paranoico	Muy lento, evasión de IDS
-T1	        Furtivo	    Bastante lento, evasión de IDS
-T2	         Educado	Más lento, consume menos ancho de banda
-T3	         Normal	    Predeterminado
-T4	         Agresivo	Asume red rápida y confiable
-T5	         Demente	Muy agresivo, puede abrumar objetivos

# Guardar con fecha
nmap -sV localhost > scan_$(date +%Y%m%d).txt

# Guardar con hora y minuto
nmap -sV localhost > scan_$(date +%Y%m%d_%H%M).txt

# Ver resultados guardados
cat scan_*.txt

# Ejecutar scripts por defecto
nmap --script default localhost

# Ver scripts disponibles
ls /usr/share/nmap/scripts/ | head -20

# Script de enumeración SMB
nmap --script smb-enum-users.nse -p445 <host>

# Script de recursos compartidos SMB
nmap --script smb-enum-shares.nse -p445 <host>

# Script de procesos SMB (con credenciales)
nmap --script smb-enum-processes.nse --script-args smbusername=<user>, smbpass=<pass> -p445 <host>

# Enumeración web
nmap -sV --script=http-enum <target>

# Escaneo UDP
nmap -sU localhost

# Escaneo FIN TCP
nmap -sF localhost

# Escaneo con detección de versión + scripts comunes
nmap -sC -sV localhost

Respuestas de escaneo SYN
Respuesta	    Significado
SYN/ACK	       Puerto abierto (en estado de escucha)
RST	            Puerto cerrado
Sin respuesta	Filtrado (no se puede determinar)

# Puertos comunes alternativos
nmap -p 8000,8080,8443,3000,5000 localhost

# Filtrar solo puertos abiertos
nmap -p 1-10000 --open localhost

# Escaneo con grep para ver solo abiertos/filtrados
nmap -sV -p 1-10000 localhost | grep -E "open|filtered"

Cheatsheet rápido de opciones
Opción	Significado
-sV	    Detectar versión de servicios
-sS	    Escaneo SYN (requiere sudo)
-sT	    Escaneo de conexión TCP completa
-sU	    Escaneo UDP
-sF	    Escaneo FIN
-sn	    Ping scan (solo descubrir hosts)
-p	    Especificar puertos
-p-	    Todos los puertos (1-65535)
--open	Mostrar solo puertos abiertos
-sC	    Scripts por defecto
--script	Ejecutar script específico
-T0 a -T5	Plantillas de tiempo

## 🚨 Escaneo de vulnerabilidades con script vulners

### Comando básico
```bash
nmap -sV --script vulners --script-args mincvss=4 <IP_OBJETIVO>

#Parámetros del script vulners
Parámetro	   |     Función
--script vulners	Usa la base de datos de vulnerabilidades Vulners.com
--script-args       mincvss=4	Muestra solo CVEs con puntuación ≥ 4
-sV	                Detecta versiones de servicios (OBLIGATORIO para vulners)

#EJEMPLO PARÁMETROS:
80/tcp open  http    uhttpd 1.0
| vulners:
|       CVE-2018-12345   9.8    https://vulners.com/cve/CVE-2018-12345

#Elemento	Significado (PARÁMETRO)
80/tcp open http	Puerto 80 abierto, servicio HTTP
uhttpd 1.0	Servidor web específico y versión
CVE-2018-12345	Identificador único de vulnerabilidad
9.8	Puntuación CVSS (gravedad)

#Escala de gravedad CVSS
Puntuación	Gravedad	Color	Implicación
9.0 - 10.0	CRÍTICO	🔴	Ejecución remota de código, control total
7.0 - 8.9	ALTO	🟠	Acceso a datos sensibles, escalada privilegios
4.0 - 6.9	MEDIO	🟡	Denegación de servicio, exposición limitada
0.1 - 3.9	BAJO	🟢	Impacto menor, condiciones específicas

#Servicios comunes y sus vulnerabilidades típicas
Servicio	|Puerto(s)|	Tipo de vulnerabilidades comunes
OpenSSH	    |    22	 |  Escalada de privilegios, bypass de autenticación
HTTP (uhttpd, nginx, Apache) |80, 443, 8080|	RCE, XSS, inyección SQL, path traversal
DNS (dnsmasq, BIND)	|53|	Cache poisoning, DoS, información expuesta
SMB (microsoft.ds, Samba)	|139, 445|	EternalBlue, ransomware, acceso no autorizado
MySQL/MariaDB	|3306| Inyección, acceso no autorizado, escalada
FTP	            |21| 	Ataques de fuerza bruta, acceso anónimo
RDP	          |3389|	BlueKeep, fuerza bruta, escalada

¿Qué puede hacer un atacante con CVSS 9.8?

-RCE (Remote Code Execution): Ejecutar comandos en el dispositivo

-Control total: Tomar control completo del sistema

-Sin autenticación: No necesita usuario/contraseña

-Explotable remotamente: Desde cualquier lugar de Internet

¿Qué es un falso positivo? Cuando una herramienta reporta una vulnerabilidad que NO existe realmente.

#Cómo verificar un posible falso positivo:
# 1. Confirmar qué dispositivo es
nmap -sV <IP> | grep "Service Info"

# 2. Intentar exploit específico (con permiso)
nmap --script http-vuln* -p 80 <IP>

# 3. Acceder manualmente (si es web)
curl -I http://<IP>

*Regla de oro: Si la IP es del gateway de VirtualBox (10.0.2.2) o una VM interna, probablemente es falso positivo.

# Escaneo completo con vulners
nmap -sV --script vulners --script-args mincvss=4 -p- <IP_OBJETIVO>

# Guardar resultados
nmap -sV --script vulners --script-args mincvss=4 <IP> > vulners_scan_$(date +%Y%m%d).txt

## 🖥️ Detección de Sistema Operativo (OS Detection)

### Comando básico
```bash
sudo nmap -O <IP_OBJETIVO>

*¿Por qué usar sudo?
La detección de OS requiere enviar paquetes especiales que necesitan privilegios de root.

# Detección estándar
sudo nmap -O <IP>

# Detección más agresiva (adivina versiones)
sudo nmap -O --osscan-guess <IP>

# Detección con scripts adicionales
sudo nmap -O -sC <IP>

# Detección en puertos específicos (más rápido)
sudo nmap -O -p 22,80,445 <IP>

*Ejemplo de salida para Linux:
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
445/tcp open  microsoft.ds?

MAC Address: 08:00:27:AB:CD:EF (Oracle VirtualBox)
Device type: general purpose
Running: Linux 4.X|5.X
OS CPE: cpe:/o:linux:linux_kernel:4.15
         cpe:/o:linux:linux_kernel:5.8
OS details: Linux 4.15 - 5.8

*Ejemplo de salida para Windows:
PORT    STATE SERVICE
135/tcp open  msrpc
139/tcp open  netbios-ssn
445/tcp open  microsoft.ds

MAC Address: 08:00:27:AB:CD:EF (Oracle VirtualBox)
Device type: general purpose
Running: Microsoft Windows 2008|2012|10
OS CPE: cpe:/o:microsoft:windows_server_2008:r2
         cpe:/o:microsoft:windows_server_2012
         cpe:/o:microsoft:windows_10
OS details: Microsoft Windows 2008 R2 or 2012 or Windows 10

*Indicadores para identificar el OS 
Si ves...	          Es...
Puerto 22 (SSH) + Linux en OS CPE	Linux
Puerto  135, 139, 445 abiertos	Windows
microsoft.ds en puerto 445 Windows
Samba en puerto 445 Linux con Samba
VirtualBox o VMware en MAC	Máquina virtual

*Limitaciones de OS detection
Situación	Por qué falla
Firewall   activo	Bloquea los paquetes especiales
Máquina   virtual	Respuestas diferentes a hardware real
Pocos    puertos abiertos	No hay suficiente información
TCP/IP    stack modificado	Comportamiento no estándar

# 1. Usar scripts específicos para Windows
nmap --script smb-os-discovery -p 445 <IP>

# 2. Usar scripts específicos para SSH (Linux)
nmap --script ssh-hostkey -p 22 <IP>

# 3. Ver el TTL del ping
ping -c 1 <IP> | grep ttl
# TTL 128 = Windows
# TTL 64 = Linux
# TTL 255 = Unix/Solaris

# 4. Usar enum4linux para Windows
enum4linux -O <IP>

*Tabla de TTL por sistema operativo
TTL	Sistema Operativo
128	Windows 10/8/7/Vista/XP
64	Linux, macOS, Unix
255	Solaris, AIX, Cisco IOS
60	Windows 98/ME (antiguos)

# Escaneo completo con OS detection
sudo nmap -O -sV -p- <IP_OBJETIVO>

# Guardar resultados
sudo nmap -O <IP> > os_detection_$(date +%Y%m%d).txt

#Escaneo PASIVO TCP
# Escuchar tráfico en la red sin enviar nada
sudo tcpdump -i eth0

# Ver equipos que ya están comunicándose
sudo arp-scan -l   # (también es activo porque envía ARP)


