 🔥 CHEATSHEET: FTP, PASS-THE-HASH, KERBEROS Y ATAQUES EN RUTA

## 📌 1. FTP (FILE TRANSFER PROTOCOL)

### Conceptos clave:
| Término | Explicación |
|---------|-------------|
| **FTP** | Protocolo heredado SIN cifrado (puerto 21) |
| **FTPS** | FTP sobre SSL/TLS (puerto 990) |
| **SFTP** | FTP sobre SSH (puerto 22) - Más seguro |
| **Anonymous Login** | Inicio de sesión sin credenciales (¡inseguro!) |

### Escaneo de servidor FTP:
```bash
# Escanear versión del servidor FTP
nmap -sV -p 21 172.16.20.136

# Resultado ejemplo: vsftpd 3.0.3

Verificar login anónimo con Metasploit:
bash

msf6 > use auxiliary/scanner/ftp/anonymous
msf6 > set RHOSTS 172.16.20.136
msf6 > exploit
# [+] 172.16.20.136:21 - Anonymous READ

Conexión manual a FTP:
bash

# Conectar a servidor FTP
ftp 172.16.20.136

# Comandos dentro de FTP:
ftp> ls          # Listar archivos
ftp> get archivo # Descargar archivo
ftp> put archivo # Subir archivo
ftp> bye         # Salir

Mitigaciones FTP:
Medida	Explicación
Deshabilitar login anónimo	Editar /etc/vsftpd.conf → anonymous_enable=NO
Usar FTPS o SFTP	Cifrar comunicaciones
Contraseñas seguras	Políticas de complejidad
Cifrado en reposo	Cifrar archivos almacenados
Bloquear cuentas admin	No usar root/admin como usuarios
🔑 2. PASS-THE-HASH (PTH)
¿Qué es?
Concepto	Explicación
Pass-the-Hash	Usar el hash de contraseña (no la contraseña en texto plano) para autenticarse
NTLM	Protocolo de autenticación de Windows (v1 y v2)
SAM	Security Account Manager - archivo donde Windows almacena hashes
Mimikatz	Herramienta para extraer hashes de la memoria
¿Cómo funciona?
text

1. Atacante compromete un sistema y obtiene hashes NTLM (con Mimikatz)
2. Atacante usa esos hashes para autenticarse en OTRO sistema
3. El sistema acepta el hash como prueba de identidad

Comandos Mimikatz (dentro de Meterpreter):
bash

# Cargar Mimikatz en Metasploit
meterpreter > load kiwi

# Extraer hashes de la memoria
meterpreter > creds_all

# Extraer hashes de todos los usuarios
meterpreter > lsa_dump_sam

Mitigaciones Pass-the-Hash:
Medida	Explicación
Usar Kerberos	En lugar de NTLM
Restringir administradores	Menos cuentas con privilegios
Proteger cuentas	Cuentas administrativas solo para tareas específicas
Actualizar sistemas	Parches de seguridad
🎫 3. KERBEROS
Componentes de Kerberos:
Componente	Función
Cliente	Usuario que solicita acceso
Servidor	Recurso al que se quiere acceder
KDC	Centro de Distribución de Claves (contiene AS y TGS)
AS	Authentication Server - autentica al cliente
TGS	Ticket-Granting Server - emite tickets
TGT	Ticket-Granting Ticket - prueba de identidad
Flujo de autenticación Kerberos:
text

1. Cliente → AS: Solicita autenticación
2. AS → Cliente: Envía TGT y clave de sesión
3. Cliente → TGS: Envía TGT
4. TGS → Cliente: Envía ticket de servicio
5. Cliente → Servidor: Presenta ticket
6. Servidor → Cliente: Concede acceso

Ataques Kerberos:
Ataque	Explicación	Herramienta
Golden Ticket	Forjar TGT usando hash KRBTGT	Mimikatz, Empire
Silver Ticket	Forjar ticket de servicio específico	Mimikatz, Empire
Kerberoasting	Extraer hashes de cuentas de servicio	Impacket, Rubeus
Golden Ticket con Empire:
bash

(Empire) > use module powershell/credentials/mimikatz/golden_ticket
(Empire) > set user Administrator
(Empire) > set domain example.com
(Empire) > set krbtgt <hash>
(Empire) > execute

Mitigaciones Kerberos:
Medida	Explicación
Cambiar KRBTGT	Cambiar contraseña KRBTGT periódicamente (2 veces)
Monitorear eventos	Detectar tickets anómalos
Deshabilitar delegación	Solo habilitar cuando sea necesario
Usar AES	En lugar de RC4 para cifrado
🌐 4. ATAQUES EN RUTA (MAN-IN-THE-MIDDLE)
¿Qué es?
Término	Explicación
MITM	Atacante se coloca entre dos dispositivos que se comunican
Capa 2 (Enlace)	ARP Spoofing, STP manipulation
Capa 3 (Red)	Ruteo malicioso, BGP hijacking
Tipos de ataques en ruta:
Ataque	Capa	Explicación
ARP Spoofing	Capa 2	Falsificar MAC para interceptar tráfico
STP Manipulation	Capa 2	Convertirse en switch raíz
Ruteo malicioso	Capa 3	Inyectar rutas falsas
SSLStrip	Capa 7	Degradar HTTPS a HTTP
Herramientas de MITM:
bash

# ARP Spoofing con arpspoof
sudo arpspoof -i eth0 -t 192.168.1.1 192.168.1.50

# SSLStrip
sudo sslstrip -l 8080

# BetterCAP (todo en uno)
sudo bettercap -eval "set arp.spoof.targets 192.168.1.1; arp.spoof on; net.sniff on"

Mitigaciones Capa 2:
Medida	Explicación
DAI	Dynamic ARP Inspection - evita ARP Spoofing
IP Source Guard	Evita suplantación de IP
802.1X -	Autenticación de puertos
Root Guard	 - Evita STP manipulation
BPDU Guard	- Bloquea BPDU en puertos de acceso
VLAN nativa	Usar - VLAN no utilizada (no VLAN 1)
DHCP Snooping	- Evita servidores DHCP maliciosos
Storm Control	- Limita tráfico de difusión
ACLs	- Listas de control de acceso

Ataque de Degradación (POODLE):
Concepto	Explicación
POODLE	Forzar uso de SSL 3.0 (vulnerable) para descifrar tráfico
Mitigación	Deshabilitar SSL 3.0 y TLS 1.0 en servidores

🛠️ 5. COMANDOS ÚTILES
bash

# Escanear puerto FTP
nmap -p 21 -sV 172.16.20.136

# Buscar exploits FTP
searchsploit vsftpd

# Conectar a FTP (modo anónimo)
ftp 172.16.20.136
Username: anonymous
Password: (enter)

# Extraer hashes con Mimikatz (Windows)
mimikatz # privilege::debug
mimikatz # sekurlsa::logonpasswords

# En Metasploit con Mimikatz
meterpreter > load kiwi
meterpreter > creds_all

🔑 6. VOCABULARIO CLAVE
Término	Significado
FTP	File Transfer Protocol (puerto 21)
FTPS	FTP sobre SSL/TLS (puerto 990)
SFTP	FTP sobre SSH (puerto 22)
SAM	Security Account Manager (hashes de Windows)
NTLM	New Technology LAN Manager (autenticación Windows)
Pass-the-Hash	Usar hash para autenticarse sin contraseña
Mimikatz	Herramienta para extraer hashes de memoria
Kerberos	Protocolo de autenticación (RFC 4120)
KDC	Key Distribution Center
TGT	Ticket-Granting Ticket
Golden Ticket	TGT falsificado con hash KRBTGT
Silver Ticket	Ticket de servicio falsificado
Kerberoasting	Extraer hashes de cuentas de servicio
MITM	Man-In-The-Middle (ataque en ruta)
ARP Spoofing	Falsificar MAC para interceptar tráfico
DAI	Dynamic ARP Inspection (mitigación)
POODLE	Ataque de degradación SSL/TLS
🎯 7. REFLEXIÓN FINAL

    FTP sin cifrar es como enviar una carta sin sobre. Usa SFTP o FTPS siempre que sea posible.

    Pass-the-Hash explota la forma en que Windows almacena contraseñas. La mejor defensa es usar Kerberos y restringir cuentas privilegiadas.

    Kerberos es seguro por diseño, pero configuraciones incorrectas (como no rotar KRBTGT) pueden ser explotadas con Golden Tickets.

    Los ataques en ruta ocurren cuando el atacante se interpone entre tú y tu destino. Usa cifrado (HTTPS, SSH) y protege tu red con DAI, DHCP Snooping y Root Guard.

FIN DEL CHEATSHEET
text


---

## ✅ RECOMENDACIÓN FINAL

| Archivo | Acción |
|---------|--------|
| `20-resolucion_nombres_ataquesSMB.md` | **Eliminar** (fusionar con el otro) |
| `20-windows-naming-smb-attacks.md` | **Mantener** (renombrar a `20-smb-nombres-windows.md`) |
| `21-SMNP_SMTP.md` | **Renombrar** a `21-protocolos-red-snmp-smtp-ftp.md` |
| `22-escaneo_nucleo.md` | **Mantener** |
| **NUEVO** | Crear `22-ataques-autenticacion-kerberos.md` con el contenido de arriba |

**Total final:** ~22 archivos bien organizados y sin redundancias. 🚀

. REFLEXIÓN FINAL

    FTP sin cifrar es como enviar una carta sin sobre. Usa SFTP o FTPS siempre que sea posible.

    Pass-the-Hash explota la forma en que Windows almacena contraseñas. La mejor defensa es usar Kerberos y restringir cuentas privilegiadas.

    Kerberos es seguro por diseño, pero configuraciones incorrectas (como no rotar KRBTGT) pueden ser explotadas con Golden Tickets.

    Los ataques en ruta ocurren cuando el atacante se interpone entre tú y tu destino. Usa cifrado (HTTPS, SSH) y protege tu red con DAI, DHCP Snooping y Root Guard.