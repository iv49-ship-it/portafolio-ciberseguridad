

# CHEATSHEET - IPs, TOR Y BUG BOUNTY

## 📍 VER MIS IPs Y LAS DE MI RED

### 1. Ver mi IP pública (desde Kali o cualquier Linux)
```bash
# IP pública (IPv4)
curl ifconfig.me

# IP pública (IPv6)
curl -6 ifconfig.me

# Alternativa con HTTPS
curl https://icanhazip.com

# Ver detalles de la conexión
curl -v https://icanhazip.com

2. Ver mi IP local y la de mi red
bash

# Ver todas las interfaces de red
ip a

# Ver solo la IP local
hostname -I

# Ver la IP de mi router (puerta de enlace)
ip route | grep default

3. Ver IPs de otros dispositivos en mi red (vecinos)
bash

# Escaneo rápido de dispositivos en la red local
sudo nmap -sn 192.168.1.0/24

# Alternativa con netdiscover (si está instalado)
sudo netdiscover -r 192.168.1.0/24

# Ver los dispositivos conectados al router (desde el navegador)
# Abrir http://192.168.1.1 → Clientes DHCP

🔧 INSTALACIÓN DE TOR EN KALI
1. Instalar Tor (servicio para terminal)
bash

# Sincronizar hora primero (importante)
sudo timedatectl set-ntp true
sudo timedatectl set-timezone America/Santiago

# Instalar Tor
sudo apt update
sudo apt install tor -y

# Iniciar Tor
sudo systemctl start tor

# Verificar estado
sudo systemctl status tor

2. Instalar Proxychains (para anonimizar comandos)
bash

sudo apt install proxychains4 -y

3. Usar Proxychains con comandos
bash

# Ver IP anónima
proxychains curl https://icanhazip.com

# Usar con otros comandos
proxychains whois paystackmfb.com
proxychains dig paystackmfb.com A

4. Instalar Navegador Tor (interfaz gráfica)
bash

# Opción 1: Desde repositorios (si está disponible)
sudo apt install torbrowser-launcher -y
torbrowser-launcher

# Opción 2: Descarga manual (más fiable)
# Abrir Firefox → https://www.torproject.org/download/
# Descargar para Linux → descomprimir → ejecutar
tar -xf tor-browser-linux-x86_64-*.tar.xz
cd tor-browser
./start-tor-browser.desktop

5. Si hay error de repositorio (firma)
bash

# Agregar clave de firma de Kali
wget -q -O - https://archive.kali.org/archive-key.asc | sudo gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/kali-archive-keyring.gpg
sudo apt update





# CHEATSHEET - ANÁLISIS DE CÁMARAS IoT CON TOR

## 🔧 CONFIGURACIÓN INICIAL

```bash
# Iniciar Tor
sudo systemctl start tor

# Verificar IP anónima
proxychains curl icanhazip.com

🔍 RECONOCIMIENTO PASIVO (sin tocar la cámara)
1. Ver tráfico de red (Wireshark)
bash

# Abrir Wireshark y filtrar por IP de la cámara
ip.addr == 192.168.1.3

2. Buscar información de la MAC
bash

# Buscar los primeros 6 dígitos de la MAC en una base de datos OUI
# Ejemplo: 72:6c:1b → Z-IOT

3. Ver nombre de host en el router

    Entrar al panel del router → Clientes DHCP → Buscar el nombre de la cámara

🔍 BÚSQUEDAS EN SHODAN (a través de Tor)
bash

# Navegar en Firefox con Tor (usando el navegador Tor o socks5)
proxychains firefox https://shodan.io

Búsquedas recomendadas
text

"ZIOT" "123456"
"Z-IOT CAM"
port:554 "ZIOT"
html:"Z-IOT"

RECONOCIMIENTO ACTIVO (interacción directa)
1. Escaneo de puertos completo
bash

# Esto va directo (no necesita Tor porque es en red local)
sudo nmap -p- -T4 192.168.1.3

2. Identificar servicio en puerto específico
bash

nmap -sV -p 52707 192.168.1.3

3. Conectar al puerto para ver qué responde
bash

# Directo (red local)
nc -nv 192.168.1.3 52707

4. Probar panel web en puerto no estándar

    Abrir en navegador:

text

http://192.168.1.3:52707
https://192.168.1.3:52707

5. Probar credenciales por defecto
Usuario	Contraseña
admin	123456
admin	(en blanco)
(en blanco)	123456
6. Probar acceso por terminal
bash

telnet 192.168.1.3
ssh 192.168.1.3

Probar mismas credenciales.
7. Verificar RTSP (puerto 554)
bash

nmap -p 554 192.168.1.3
nmap -sV -p 554 192.168.1.3

8. Ver video en VLC (si RTSP está abierto)

    Abrir VLC → Medio → Abrir ubicación de red

    URL: rtsp://192.168.1.3:554/stream1
