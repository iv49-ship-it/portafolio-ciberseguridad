
# ========================================
# 1. COMANDOS BÁSICOS DE SCAPY
# ========================================

# Iniciar Scapy como root (en terminal, NO dentro de Python)
# $ sudo scapy

# Salir de Scapy
# >>> exit()

# Ver interfaces disponibles
# >>> conf.ifaces


# ========================================
# 2. CAPTURAR TRÁFICO (sniff)
# ========================================

# Captura básica (todas las interfaces, para con CTRL-C)
# >>> sniff()

# Capturar en interfaz específica
# >>> sniff(iface="eth0")

# Capturar solo ICMP (pings)
# >>> sniff(iface="eth0", filter="icmp")

# Capturar solo 5 paquetes (se detiene solo)
# >>> sniff(iface="eth0", filter="icmp", count=5)

# Guardar captura en variable
# >>> captura = _
# >>> captura.nsummary()      # Ver resumen numerado


# ========================================
# 3. VER PAQUETES CAPTURADOS
# ========================================

# Ver resumen con números
# >>> captura.nsummary()

# Ver un paquete específico (ejemplo: el primero)
# >>> captura[0]

# Ver solo la capa IP
# >>> captura[0][IP]

# Ver solo la dirección de origen
# >>> captura[0][IP].src

# Ver solo la dirección de destino
# >>> captura[0][IP].dst

# Ver todo el detalle del paquete
# >>> captura[0].show()


# ========================================
# 4. CREAR PAQUETES PERSONALIZADOS
# ========================================

# Capa IP sola
# >>> paquete = IP(dst="8.8.8.8")

# IP + ICMP (ping normal)
# >>> paquete = IP(dst="8.8.8.8")/ICMP()

# IP + ICMP + mensaje personalizado
# >>> paquete = IP(dst="8.8.8.8")/ICMP()/"Mi mensaje"

# Ver cómo queda el paquete
# >>> paquete.show()


# ========================================
# 5. ENVIAR PAQUETES
# ========================================

# Enviar paquete (sin recibir respuesta)
# >>> send(IP(dst="8.8.8.8")/ICMP()/"Hola!")
#EJERCICIO 2, ver si hay respuesta
>>> respuesta = sr1(IP(dst="8.8.8.8")/ICMP())
>>> respuesta.show()

# Enviar y recibir respuesta (como ping)
# >>> sr1(IP(dst="8.8.8.8")/ICMP())

# Para el laboratorio de Cisco (red 10.6.6.0/24)
# >>> send(IP(dst="10.6.6.23")/ICMP()/"This is a test")


# ========================================
# 6. FILTROS DE CAPTURA (formato BPF)
# ========================================

# Filtrar por protocolo
# filter="icmp"    # solo pings
# filter="tcp"     # solo TCP
# filter="udp"     # solo UDP

# Filtrar por dirección IP
# filter="host 8.8.8.8"           # tráfico hacia/desde 8.8.8.8
# filter="src host 10.6.6.23"     # tráfico DESDE 10.6.6.23
# filter="dst host 10.6.6.23"     # tráfico HACIA 10.6.6.23

# Filtrar por puerto
# filter="port 80"                # tráfico hacia/desde puerto 80

# Combinar filtros
# filter="icmp and host 8.8.8.8"


# ========================================
# 7. GUARDAR Y CARGAR CAPTURAS
# ========================================

# Guardar captura en archivo .pcap (para Wireshark)
# >>> wrpcap("captura.pcap", captura)

# Cargar una captura guardada
# >>> captura = rdpcap("captura.pcap")


# ========================================
# 8. PREGUNTAS LABORATORIO CISCO
# ========================================

# ¿Qué tráfico se muestra en nsummary()?
# Respuesta: Solicitudes de eco ICMP (echo-request) y 
# respuestas de eco (echo-reply) alternadas

# ¿Qué diferencia hay entre un paquete normal y uno personalizado?
# Respuesta: El campo "load" o "Raw" cambia al mensaje

# ¿Para qué sirve el flag SA (SYN-ACK)?
# Respuesta: Indica que el puerto está abierto en el destino


# ========================================
# 9. EJEMPLO COMPLETO PARA LABORATORIO
# ========================================

Terminal 1 (Scapy):
>>> sniff(iface="br-internal", filter="icmp", count=10)

Terminal 2 (ping):
$ ping -c 10 10.6.6.23

Terminal 1 (Scapy):
>>> a = _
>>> a.nsummary()
>>> a[0].show()

Terminal 3 (Scapy - otra ventana):
>>> send(IP(dst="10.6.6.23")/ICMP()/"This is a test")

Terminal 1 (Scapy - la que captura):
>>> a = _
>>> a.nsummary()  # Debería ver 2 paquetes más
"""

# ========================================
# 10. MI COMANDO QUE YA FUNCIONÓ (mi red real)
# ========================================

"""
>>> sniff(iface="eth0", filter="icmp", count=5)

# En otra terminal:
$ ping -c 5 8.8.8.8

# Resultado en Scapy:
<Sniffed: TCP:0 UDP:0 ICMP:5 Other:0>

# Ver los paquetes:
>>> a = _
>>> a.nsummary()
"""

"""
========================================
SCAPY - PARTE 4: PAQUETES TCP SYN
Laboratorio: Escaneo de puerto 445
========================================
"""

# ========================================
# 1. CAPTURAR TRÁFICO EN LA INTERFAZ CORRECTA
# ========================================

# Primero, identificae interfaz (si estoy en red 10.6.6.0/24)
# >>> conf.ifaces

# Capturar tráfico TCP en la interfaz virtual (laboratorio Cisco)
# >>> sniff(iface="br-internal", filter="tcp", count=10)

# Si uso mi red real (como práctica)
# >>> sniff(iface="eth0", filter="tcp and host 8.8.8.8", count=10)


# ========================================
# 2. CREAR Y ENVIAR PAQUETE TCP SYN
# ========================================

# Estructura: IP(dst="destino")/TCP(dport=puerto, flags="S")
# flags="S" = SYN (solicitud de conexión)

# Para el laboratorio (red 10.6.6.0/24):
# >>> send(IP(dst="10.6.6.23")/TCP(dport=445, flags="S"))

# Para practicar con Google (tu red real):
# >>> send(IP(dst="8.8.8.8")/TCP(dport=80, flags="S"))


# ========================================
# 3. VER RESULTADOS DE LA CAPTURA
# ========================================

# Guardar captura
# >>> a = _

# Ver resumen numerado
# >>> a.nsummary()

# Ver un paquete específico (ej: el que tiene SA)
# >>> a[2].show()

# Ver solo los flags TCP de cada paquete
# >>> for pkt in a:
# ...     if pkt.haslayer(TCP):
# ...         print(f"Flags: {pkt[TCP].flags}")


# ========================================
# 4. INTERPRETAR LOS FLAGS TCP
# ========================================

"""
FLAGS MÁS IMPORTANTES:

| Flag | Valor | Significado | ¿Qué indica? |
|------|-------|-------------|---------------|
| S    | 0x02  | SYN         | Solicitud de conexión (yo envío) |
| SA   | 0x12  | SYN-ACK     | Puerto ABIERTO (destino responde) |
| R    | 0x04  | RST         | Puerto CERRADO o rechazado |
| A    | 0x10  | ACK         | Confirmación de recepción |
| PA   | 0x18  | PUSH+ACK    | Datos siendo enviados |
| RA   | 0x14  | RST-ACK     | Respuesta a SYN si puerto cerrado |
"""


# ========================================
# 5. SI EL PUERTO ESTÁ ABIERTO
# ========================================

"""
En la captura del laboratorio Cisco (10.6.6.23:445):

0000 Ether / IP / TCP 10.6.6.1:xxxxx > 10.6.6.23:445 S
0001 Ether / IP / TCP 10.6.6.23:445 > 10.6.6.1:xxxxx SA   ← objetivo de búsqueda
0002 Ether / IP / TCP 10.6.6.1:xxxxx > 10.6.6.23:445 A

El paquete con SA (SYN-ACK) indica que el puerto 445 está ABIERTO.
"""


# ========================================
# 6. SI EL PUERTO ESTÁ CERRADO
# ========================================

"""
0000 Ether / IP / TCP 10.6.6.1:xxxxx > 10.6.6.23:445 S
0001 Ether / IP / TCP 10.6.6.23:445 > 10.6.6.1:xxxxx RA   ← RST-ACK

El paquete con RA indica que el puerto está CERRADO.
"""


# ========================================
# 7. COMANDOS ÚTILES PARA FILTRAR
# ========================================

# Ver solo paquetes con flag SYN-ACK (SA)
# >>> a.nsummary(filter="tcp[13] == 0x12")

# Ver solo paquetes con flag SYN (S)
# >>> a.nsummary(filter="tcp[13] == 0x02")

# Ver solo paquetes hacia un puerto específico
# >>> a.nsummary(filter="tcp and dst port 445")


# ========================================
# 8. PREGUNTAS Y RESPUESTAS DEL LABORATORIO CISCO
# ========================================

"""
¿Qué indica el indicador SA en el paquete devuelto desde 10.6.6.23?

RESPUESTA:
El indicador SA (SYN-ACK) indica que el puerto 445 está ABIERTO en la 
computadora de destino (10.6.6.23). Esto significa que el destino recibió 
el paquete SYN que enviamos y respondió con un SYN-ACK, completando el 
primer paso del handshake TCP de tres vías. Si el puerto estuviera 
cerrado, el destino habría respondido con un paquete RA (RST-ACK).
"""


# ========================================
# 9. EJEMPLO COMPLETO CON MI RED LOCAL
# ========================================

"""
TERMINAL 1 (Scapy - captura):
>>> sniff(iface="eth0", filter="tcp and host 8.8.8.8", count=10)

TERMINAL 2 (Scapy - envía SYN):
>>> send(IP(dst="8.8.8.8")/TCP(dport=80, flags="S"))

TERMINAL 1 (ver resultados):
>>> a = _
>>> a.nsummary()
0000 Ether / IP / TCP 10.65.119.58:xxxxx > 8.8.8.8:http S
0001 Ether / IP / TCP 8.8.8.8:http > 10.65.119.58:xxxxx SA  ← PUERTO 80 ABIERTO
0002 Ether / IP / TCP 10.65.119.58:xxxxx > 8.8.8.8:http A
"""


# ========================================
# 10. POSIBLES ERRORES Y SOLUCIONES
# ========================================

"""
| Error | Causa | Solución |
|-------|-------|----------|
| No se ve el paquete SA | Puerto cerrado o firewall | Probar con otro puerto (80, 443) |
| No se capturan paquetes | Interfaz incorrecta | Verificar con conf.ifaces |
| SyntaxError | Usar : en lugar de = | filter="icmp" (con =) |
| No hay respuesta | Destino no alcanzable | Verificar conectividad con ping |
"""

# GLOSARIO SCAPY PARA CHEATSHEET

## 🧠 CAPAS DE RED

| Término | Significa |
|---------|-----------|
| **IP()** | Capa de red (direcciones origen/destino) |
| **ICMP()** | Protocolo de ping (echo-request / echo-reply) |
| **TCP()** | Protocolo de conexión (puertos, flags SYN/ACK) |
| **Raw** | Datos enviados (carga útil, mensaje personalizado) |
| **Padding** | Relleno para completar tamaño mínimo del paquete |

---

## 🚩 FLAGS TCP (importantes)

| Flag | Nombre | Qué significa |
|------|--------|---------------|
| **S** | SYN | Solicito conexión |
| **A** | ACK | Confirmo recepción |
| **SA** | SYN-ACK | Puerto abierto (responde a SYN) |
| **R** | RST | Puerto cerrado o rechazo |
| **P** | PUSH | Envío datos inmediatamente |
| **F** | FIN | Cierro conexión |

---

## 🛠️ COMANDOS SCAPY

| Comando | Qué hace |
|---------|----------|
| `send(pkt)` | Envía paquete sin esperar respuesta |
| `sr1(pkt)` | Envía y espera 1 respuesta |
| `pkt.show()` | Muestra detalles del paquete |
| `pkt.summary()` | Resumen de una línea |
| `ls(IP)` | Lista campos de la capa IP |
| `conf.iface` | Ver/mostrar interfaz actual |
| `exit()` | Salir de Scapy |

---

## 📦 CREACIÓN DE PAQUETES (ejemplos para practicar)
# Ping normal
IP(dst="8.8.8.8")/ICMP()

# Ping con mensaje personalizado
IP(dst="8.8.8.8")/ICMP()/"Hola"

# TCP SYN a puerto 80
IP(dst="8.8.8.8")/TCP(dport=80, flags="S")


#Siempre buscar echo-reply o SA. (señal de que funciona)

#El Padding son datos de relleno.
#El Raw es tu mensaje personalizado.
