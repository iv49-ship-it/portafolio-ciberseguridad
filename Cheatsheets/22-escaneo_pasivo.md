COMANDOS DE ESCANEO PASIVO
markdown

# 🔍 COMANDOS DE ESCANEO PASIVO - KALI LINUX

## 📌 1. TCPDUMP - CAPTURA DE TRÁFICO

### Comandos básicos:
```bash
# Escuchar todo el tráfico en la interfaz eth0
sudo tcpdump -i eth0

# Escuchar sin resolver nombres (más rápido)
sudo tcpdump -i eth0 -n

# Escuchar y mostrar direcciones MAC
sudo tcpdump -i eth0 -e -n

# Escuchar sin mostrar timestamps (menos ruido)
sudo tcpdump -i eth0 -n -t

# Escuchar mostrando solo IPs (formato resumido)
sudo tcpdump -i eth0 -n -q

A) Filtros por IP:
bash

# Tráfico de una IP específica
sudo tcpdump -i eth0 -n host 192.168.1.1

# Tráfico de un rango de IPs (red)
sudo tcpdump -i eth0 -n net 192.168.1.0/24

# Tráfico de una IP de origen específica
sudo tcpdump -i eth0 -n src host 192.168.1.50

# Tráfico hacia una IP de destino específica
sudo tcpdump -i eth0 -n dst host 192.168.1.1

B) Filtros por puerto:
bash

# Tráfico de un puerto específico
sudo tcpdump -i eth0 -n port 80

# Tráfico de un rango de puertos
sudo tcpdump -i eth0 -n portrange 1-1024

# Tráfico de puertos específicos (HTTP o HTTPS)
sudo tcpdump -i eth0 -n port 80 or port 443

# Tráfico de puerto origen específico
sudo tcpdump -i eth0 -n src port 53

# Tráfico de puerto destino específico
sudo tcpdump -i eth0 -n dst port 22

B) Filtros por MAC:
bash

# Tráfico de una MAC específica
sudo tcpdump -i eth0 -n ether host cc:b1:71:c6:8d:10

# Tráfico de una MAC de origen específica
sudo tcpdump -i eth0 -n ether src cc:b1:71:c6:8d:10

# Tráfico hacia una MAC de destino específica
sudo tcpdump -i eth0 -n ether dst cc:b1:71:c6:8d:10

C) Filtros por protocolo:
bash

# Solo tráfico ICMP (ping)
sudo tcpdump -i eth0 -n icmp

# Solo tráfico TCP
sudo tcpdump -i eth0 -n tcp

# Solo tráfico UDP
sudo tcpdump -i eth0 -n udp

# Solo tráfico ARP
sudo tcpdump -i eth0 -n arp

# Solo tráfico DNS
sudo tcpdump -i eth0 -n port 53

# Solo tráfico DHCP
sudo tcpdump -i eth0 -n port 67 or port 68

D) Combinación de filtros (operadores lógicos):
bash

# IP Y puerto específico
sudo tcpdump -i eth0 -n host 192.168.1.1 and port 53

# Dos IPs (OR)
sudo tcpdump -i eth0 -n host 192.168.1.1 or host 192.168.1.5

# Excluir una IP (NOT)
sudo tcpdump -i eth0 -n not host 192.168.1.50

# Excluir un puerto
sudo tcpdump -i eth0 -n not port 22

# Red y puerto específico
sudo tcpdump -i eth0 -n net 192.168.1.0/24 and port 445

E) Guardar y leer capturas:
bash

# Guardar captura en archivo
sudo tcpdump -i eth0 -n -w captura.pcap

# Guardar con límite de paquetes
sudo tcpdump -i eth0 -n -c 100 -w captura.pcap

# Guardar con límite de tamaño (10 MB)
sudo tcpdump -i eth0 -n -C 10 -w captura.pcap

# Leer archivo de captura
sudo tcpdump -r captura.pcap -n

# Leer archivo y filtrar
sudo tcpdump -r captura.pcap -n host 192.168.1.1

F) Opciones avanzadas:
bash

# Mostrar en formato hexadecimal y ASCII
sudo tcpdump -i eth0 -n -X

# Mostrar en formato hexadecimal
sudo tcpdump -i eth0 -n -x

# Mostrar solo cabeceras (sin datos)
sudo tcpdump -i eth0 -n -s 64

# Capturar en modo verbose (más detalles)
sudo tcpdump -i eth0 -n -v

# Capturar en modo muy verbose
sudo tcpdump -i eth0 -n -vv

# Capturar en modo muy muy verbose
sudo tcpdump -i eth0 -n -vvv

📡 2. NETDISCOVER - MODO PASIVO
bash

# Escaneo pasivo (solo escucha)
sudo netdiscover -p -i eth0

# Escaneo pasivo con rango específico
sudo netdiscover -p -i eth0 -r 192.168.1.0/24

# Escaneo pasivo sin resolución de nombres (-N)
sudo netdiscover -p -i eth0 -r 192.168.1.0/24 -N

# Escaneo pasivo con salida detallada
sudo netdiscover -p -i eth0 -v

# Escaneo pasivo guardando en archivo
sudo netdiscover -p -i eth0 -o resultados.txt

# Escaneo pasivo sin mostrar progreso
sudo netdiscover -p -i eth0 -q

3. P0F - IDENTIFICACIÓN PASIVA DE SO
bash

# Iniciar p0f en modo pasivo
sudo p0f -i eth0

# Guardar resultados en un archivo
sudo p0f -i eth0 -o resultados.txt

# Modo silencioso (sin mucho detalle)
sudo p0f -i eth0 -q

# Ver solo nuevos hosts
sudo p0f -i eth0 -Q

# Ver información detallada de conexiones
sudo p0f -i eth0 -v

# Guardar resultados en formato JSON
sudo p0f -i eth0 -o resultados.json -f json

6. ARP WATCH - MONITOREO DE ARP
bash

# Iniciar arpwatch (monitorea cambios en la red)
sudo arpwatch -i eth0

# Ver el archivo de resultados
sudo cat /var/log/arpwatch/arpwatch.log

# Ver todas las MACs e IPs
sudo tcpdump -i eth0 -e -n -c 100 | grep -E "([0-9a-f]{2}:){5}[0-9a-f]{2}"

# Ver solo MACs e IPs únicas (dispositivos)
sudo tcpdump -i eth0 -n -e -c 100 | awk '{print $2 " → " $4}' | sort -u

# Ver dispositivos con netdiscover
sudo netdiscover -p -i eth0

# Ver TTL (Time To Live) para identificar SO
sudo tcpdump -i eth0 -n -v icmp

# TTL 64 → Linux/Unix
# TTL 128 → Windows
# TTL 255 → Cisco/router

# Escaneo pasivo de redes WiFi
sudo iwlist wlan0 scan

# Ver solo SSID y MAC
sudo iwlist wlan0 scan | grep -E "Address|ESSID" | paste -d " " - -

# Ver con calidad de señal
sudo iwlist wlan0 scan | grep -E "Address|ESSID|Quality"