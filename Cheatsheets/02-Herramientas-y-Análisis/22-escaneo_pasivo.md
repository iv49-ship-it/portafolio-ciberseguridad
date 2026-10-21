# 🔥 CHEATSHEET: SNMP Y SMTP - EXPLOTACIONES Y ENUMERACIÓN

## 📌 1. SNMP (SIMPLE NETWORK MANAGEMENT PROTOCOL)

### Conceptos clave:
| Término | Explicación |
|---------|-------------|
| **SNMP** | Protocolo para administrar dispositivos de red |
| **Puerto** | UDP 161 |
| **SNMPv2c** | Usa cadenas de comunidad (contraseñas) |
| **SNMPv3** | Usa usuarios y contraseñas (más seguro) |
| **MIB** | Management Information Base (base de datos del dispositivo) |
| **Comunidad** | Contraseña que permite acceso (public, private) |

### Comunidades SNMP comunes:
| Comunidad | Tipo de acceso |
|-----------|----------------|
| `public` | Solo lectura (más común) |
| `private` | Lectura/escritura |
| `public2` | Solo lectura (alternativa) |
| `read` | Solo lectura |
| `write` | Lectura/escritura |
| `community` | Genérica |
| `admin` | Acceso administrativo |
| `manager` | Acceso de gestión |

---

## 🛠️ 2. SCRIPTS DE Nmap PARA SNMP

### Ver scripts SNMP disponibles:
```bash
ls -1 /usr/share/nmap/scripts/snmp*

Scripts SNMP de NSE:
Script	Función
snmp-brute.nse	Fuerza bruta de comunidades SNMP
snmp-hh3c-logins.nse	Enumeración de logins en dispositivos H3C
snmp-info.nse	Obtiene información básica del dispositivo
snmp-interfaces.nse	Lista las interfaces de red
snmp-ios-config.nse	Obtiene configuración de dispositivos Cisco IOS
snmp-netstat.nse	Obtiene estadísticas de red
snmp-processes.nse	Lista procesos en ejecución
snmp-sysdescr.nse	Obtiene descripción del sistema
snmp-win32-services.nse	Enumera servicios en Windows
snmp-win32-shares.nse	Enumera recursos compartidos en Windows
snmp-win32-software.nse	Enumera software instalado en Windows
snmp-win32-users.nse	Enumera usuarios en Windows
Uso de scripts SNMP:
bash

# Obtener información del sistema
nmap --script snmp-info 192.168.1.100

# Enumerar interfaces de red
nmap --script snmp-interfaces 192.168.1.100

# Listar procesos
nmap --script snmp-processes 192.168.1.100

# Enumerar usuarios de Windows
nmap --script snmp-win32-users 192.168.1.100

# Probar comunidades SNMP por defecto
nmap --script snmp-brute 192.168.1.100

# Ejecutar varios scripts de SNMP
nmap --script snmp-* 192.168.1.100

# Scripts específicos de Windows
nmap --script snmp-win32-* 192.168.1.100

Escaneo de puerto SNMP:
bash

# Escaneo UDP del puerto 161
nmap -sU -p 161 192.168.1.0/24

🔍 3. SNMPCHECK - SNMP WALK AUTOMATIZADO
Comandos básicos:
bash

# Comando básico
snmpcheck -t <IP>

# Con comunidad específica
snmpcheck -t <IP> -c public

# Ejemplo completo
snmpcheck -t 10.6.6.23 -c public

# Con comunidad privada
snmpcheck -t 192.168.1.1 -c private

Información que se puede obtener:

    Información del sistema (nombre, descripción, contacto)

    Interfaces de red y direcciones IP

    Tablas de enrutamiento

    Procesos en ejecución

    Software instalado

    Usuarios del sistema

    Recursos compartidos de red

    Configuración de dispositivos

🛡️ 4. MITIGACIONES SNMP
Medida	Explicación
Cambiar contraseñas predeterminadas	Nunca usar public/private
Limitar acceso SNMP	Solo hosts confiables
Bloquear puerto UDP 161	Firewall para tráfico externo
Usar SNMPv3	En lugar de v2c o v1
NETCONF	Alternativa moderna y segura
📧 5. SMTP (SIMPLE MAIL TRANSFER PROTOCOL)
Conceptos clave:
Término	Explicación
SMTP	Protocolo para enviar correos entre servidores
Open Relay	Servidor que reenvía correos de cualquiera (inseguro)
MUA	Mail User Agent (cliente de correo)
MTA	Mail Transfer Agent (servidor de correo)
Puertos SMTP:
Puerto	Protocolo	Descripción
25	SMTP	No cifrado (predeterminado)
465	SMTPS	SMTP sobre SSL (obsoleto)
587	SSMTP	SMTP con STARTTLS (recomendado)
110	POP3	No cifrado
995	POP3S	POP3 cifrado
143	IMAP	No cifrado
993	IMAPS	IMAP cifrado
Comandos SMTP útiles:
Comando	Función	Ejemplo
HELO	Inicia conversación SMTP	HELO 10.1.2.14
EHLO	Inicia conversación ESMTP (extendido)	EHLO mail.example.com
STARTTLS	Inicia conexión TLS cifrada	STARTTLS
MAIL	Indica dirección del remitente	MAIL FROM:<user@example.com>
RCPT	Indica dirección del destinatario	RCPT TO:<target@example.com>
DATA	Inicia transferencia del mensaje	DATA
RSET	Restablece/cancela transacción	RSET
QUIT	Cierra la conexión	QUIT
HELP	Muestra menú de ayuda	HELP
AUTH	Autentica cliente en servidor	AUTH LOGIN
VRFY	Verifica si existe un usuario	VRFY root
EXPN	Expande lista de correo y muestra miembros	EXPN mailing-list
🛠️ 6. SMTP-OPEN-RELAY.NSE (Nmap)
Uso:
bash

# Verificar si un servidor es open relay
nmap --script smtp-open-relay.nse 10.1.2.14

# Ejemplo de salida:
# |_smtp-open-relay: Server is an open relay (16/16 tests)

Significado:

    16/16 tests → El servidor reenvía correos de cualquier remitente

    Riesgo: Puede ser usado para spam, phishing y suplantación

🔍 7. SMTP-USER-ENUM (Kali Linux)
Comandos básicos:
bash

# Ver ayuda
smtp-user-enum -h

# Enumerar un usuario específico (modo VRFY)
smtp-user-enum -M VRFY -u omar -t 192.168.78.8

# Enumerar usuarios desde un archivo
smtp-user-enum -M VRFY -U users.txt -t 192.168.78.8

# Enumerar con modo EXPN
smtp-user-enum -M EXPN -u admin -t 192.168.78.8

# Enumerar con modo RCPT
smtp-user-enum -M RCPT -U users.txt -t 192.168.78.8

# Con dominio para buscar emails completos
smtp-user-enum -M VRFY -D example.com -U users.txt -t 192.168.78.8

# Múltiples servidores desde archivo
smtp-user-enum -M VRFY -U users.txt -T servers.txt

Opciones de smtp-user-enum:
Opción	Descripción
-m n	Máximo de procesos (default: 5)
-M mode	Método: EXPN, VRFY o RCPT (default: VRFY)
-u user	Verifica un usuario específico
-U file	Archivo con lista de usuarios
-t host	Servidor SMTP
-T file	Archivo con lista de servidores
-p port	Puerto SMTP (default: 25)
-D dom	Dominio para emails completos
-d	Modo debug
-v	Verbose
Ejemplo de salida:
bash

root@kali:~# smtp-user-enum -M VRFY -u omar -t 192.168.78.8
######## Scan started at Sat Apr 21 19:34:42 #########
192.168.78.8: omar exists
######## Scan completed at Sat Apr 21 19:34:42 #########
1 results.

🧠 8. SMTP VRFY VS EXPN
Comando	Función	Uso principal
VRFY	Verifica si existe un usuario específico	VRFY root → confirma si root es usuario
EXPN	Expande una lista de correo y muestra sus miembros	EXPN mailing-list → muestra todos los miembros
Ejemplo práctico con Telnet:
bash

# Conectar al servidor SMTP
telnet 192.168.78.8 25

# Respuesta del servidor
220 dionysus.theartofhacking.org ESMTP Postfix (Ubuntu)

# Verificar usuario
VRFY root
252 2.0.0 root    ← El usuario existe

VRFY admin
550 5.1.1 <admin>: Recipient address rejected   ← No existe

🔍 10. SEARCHSPLOIT - EXPLOITS SMTP
Comandos:
bash

# Buscar exploits SMTP
searchsploit smtp

# Buscar exploits específicos
searchsploit smtp open relay

# Ver detalles de un exploit
searchsploit -x windows/remote/473.c

# Buscar exploits de servidores de correo
searchsploit postfix
searchsploit exim
searchsploit sendmail

Ejemplo de salida:
bash

root@kali:~# searchsploit smtp
----------------------------------------------- ---------------------------------
 Exploit Title                                  |  Path
----------------------------------------------- ---------------------------------
Alt-N MDaemon 6.5.1 - IMAP/SMTP Remote Buffer   | windows/remote/473.c
Apache James Server 2.2 - SMTP Denial of Servi  | multiple/dos/27915.pl
Exim ESMTP 4.80 - glibc gethostbyname Denial o  | linux/dos/35951.py
----------------------------------------------- ---------------------------------

🛡️ 11. MITIGACIONES SMTP
Medida	Explicación
Deshabilitar VRFY y EXPN	Evita enumeración de usuarios
Deshabilitar Open Relay	Solo reenviar correos de dominios autenticados
Usar STARTTLS	Cifrar comunicaciones SMTP
Firewall	Bloquear puerto 25 para tráfico externo no autorizado
Autenticación	Requerir autenticación para enviar correos
Monitoreo	Detectar intentos de enumeración
📊 12. COMPARATIVA RÁPIDA: SNMP VS SMTP
Aspecto	SNMP	SMTP
Propósito	Administrar dispositivos de red	Enviar correos electrónicos
Puerto	UDP 161	TCP 25, 587, 465
Autenticación	Comunidades (v2c) o usuarios (v3)	Usuarios/contraseñas
Ataque común	Fuerza bruta de comunidades	Enumeración con VRFY/EXPN
Herramientas	snmpcheck, scripts Nmap	smtp-user-enum, Nmap
Script Nmap	snmp-*.nse	smtp-open-relay.nse

📝 13. COMANDOS RÁPIDOS PARA EL LABORATORIO
bash

# Buscar SNMP
nmap -sU -p 161 192.168.1.0/24

# Enumerar SNMP
snmpcheck -t 192.168.1.100 -c public

# Buscar SMTP
nmap -p 25 192.168.1.0/24

# Verificar open relay
nmap --script smtp-open-relay.nse 192.168.1.100

# Enumerar usuarios SMTP
smtp-user-enum -M VRFY -U users.txt -t 192.168.1.100

# Buscar exploits SMTP
searchsploit smtp

🔑 14. VOCABULARIO CLAVE
Término	Significado
SNMP	Simple Network Management Protocol
MIB	Management Information Base
Comunidad	Contraseña SNMP (public, private)
SMTP	Simple Mail Transfer Protocol
Open Relay	Servidor SMTP que reenvía correos de cualquiera
VRFY	Comando SMTP para verificar usuarios
EXPN	Comando SMTP para expandir listas de correo
STARTTLS	Inicia cifrado TLS en SMTP
MUA	Mail User Agent (cliente)
MTA	Mail Transfer Agent (servidor)


📊 TABLA RESUMEN
Tema	Riesgo principal	Mitigación clave
FTP	Datos en texto plano, login anónimo	Usar SFTP/FTPS, deshabilitar anónimo
Pass-the-Hash	Robo de hashes NTLM	Usar Kerberos, restringir admins
Kerberos	Golden/Silver Ticket, Kerberoasting	Rotar KRBTGT, usar AES, monitorear
MITM (ARP)	Intercepción de tráfico	DAI, DHCP Snooping, 802.1X
Degradación	Uso de SSL/TLS antiguo	Deshabilitar TLS 1.0/SSL 3.0

