"""
========================================
CHEATSHEET - CAPTURAR CONTRASEÑAS CON WIRESHARK
HTTP vs HTTPS - Texto plano vs Cifrado
========================================
"""

# ========================================
# 1. CONCEPTOS CLAVE
# ========================================

"""
HTTP (Puerto 80)
- Las contraseñas viajan en TEXTO PLANO
- Cualquiera con Wireshark puede verlas
- EJEMPLO: username=admin&password=secreto123

HTTPS (Puerto 443)
- Las contraseñas viajan CIFRADAS
- Wireshark NO puede verlas
- Se ven como datos ilegibles
"""


# ========================================
# 2. CÓMO CREAR UN SERVIDOR LOCAL (para pruebas)
# ========================================

"""
# Crear el servidor (server.py)
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        datos = self.rfile.read(length).decode()
        print(f"DATOS RECIBIDOS: {datos}")

HTTPServer(("", 8080), Handler).serve_forever()

# Ejecutar:
python3 server.py
"""
"""
========================================
***** 2.0 CAPTURAR DATOS CON WIRESHARK ****
========================================
"""

# 1. INICIAR SERVIDOR (terminal 1)
# python3 -m http.server 8080

# 2. INICIAR WIRESHARK (terminal 2)
# sudo wireshark
# Seleccionar interfaz: lo (loopback)
# Doble clic

# 3. ENVIAR DATOS (Firefox)
# http://localhost:8080/?usuario=admin&password=123

# 4. BUSCAR EN WIRESHARK
# CTRL+F → "admin" → Find
# Expandir: HTTP → URI

# RESULTADO:
# GET /?usuario=admin&password=123

# ========================================
# DIFERENCIA GET vs POST
# ========================================

# GET: datos en la URL (visible)
# POST: datos en el cuerpo (requiere HTML)

# ========================================
# COMANDOS RÁPIDOS
# ========================================

"""
# Servidor simple (GET funciona)
python3 -m http.server 8080

# Servidor con POST (requiere HTML)
python3 -c '
from http.server import HTTPServer, BaseHTTPRequestHandler
class H(BaseHTTPRequestHandler):
    def do_POST(self):
        l=int(self.headers.get("Content-Length",0))
        print(self.rfile.read(l).decode())
HTTPServer(("",8080),H).serve_forever()
'
"""

# ========================================
# 3. CÓMO CREAR UN FORMULARIO HTML (login.html)
# ========================================

"""
<form method="POST" action="http://localhost:8080/enviar">
  Usuario: <input name="username"><br>
  Contraseña: <input name="password" type="password"><br>
  <button>Ingresar</button>
</form>
"""


# ========================================
# 4. PASOS PARA CAPTURAR CON WIRESHARK
# ========================================

"""
1. Inicia el servidor: python3 server.py
2. Abre Wireshark: sudo wireshark
3. Selecciona interfaz "lo" (loopback) - doble clic
4. En Firefox: file:///ruta/login.html
5. Envía el formulario (haz clic en Ingresar)
6. Detén Wireshark (icono cuadrado rojo)
7. Busca "POST" (CTRL+F)
8. Expande "HTML Form URL Encoded"
9. ¡Ahí están usuario y contraseña!
"""


# ========================================
# 5. COMANDOS ÚTILES EN WIRESHARK
# ========================================

"""
FILTROS PRINCIPALES (barra blanca):

http                    # Muestra solo tráfico HTTP
http.request.method == "POST"  # Solo peticiones POST
ip.addr == 10.6.6.13    # Tráfico hacia/desde una IP
tcp.port == 80          # Tráfico del puerto HTTP
dns                     # Tráfico DNS

BÚSQUEDA (CTRL+F):
- Find: String
- Search In: Packet details
- Value: POST, username, password, admin

VER DETALLES:
- Doble clic en un paquete
- Expandir: Ethernet II → IP → TCP → HTTP → HTML Form URL Encoded
"""


# ========================================
# 6. SI FUNCIONA LO QUE DEBO VER
# ========================================

"""
En la TERMINAL del servidor:
DATOS: username=admin&password=secreto123

En WIRESHARK (detalles del paquete):
> HTML Form URL Encoded
    username: admin
    password: secreto123

EN LA LISTA DE PAQUETES:
No.  Time   Source    Destination   Protocol Info
1    0.000  127.0.0.1 127.0.0.1     HTTP     POST /enviar HTTP/1.1
"""


# ========================================
# 7. SOLUCIÓN DE PROBLEMAS COMUNES
# ========================================

"""
PROBLEMA: El servidor no muestra "DATOS:"
SOLUCIÓN: VerificaR que el formulario POST apunte a "http://localhost:8080/enviar"

PROBLEMA: Wireshark no captura nada
SOLUCIÓN: AseguraR que el tiburón esté AZUL (capturando)

PROBLEMA: No encuentro POST
SOLUCIÓN: BuscaR "username" o "admin" en lugar de POST

PROBLEMA: El archivo HTML no se abre
SOLUCIÓN: Usa la ruta completa: file:///home/kali/login.html
         Para saber la ruta: pwd y ls login.html

PROBLEMA: La interfaz "lo" no aparece
SOLUCIÓN: En Wireshark, ir a Capture → Options → seleccionar "Loopback"
"""


# ========================================
# 8. CÓDIGO SERVIDOR COMPLETO (para copiar)
# ========================================

"""
cat > server.py << 'EOF'
from http.server import HTTPServer, BaseHTTPRequestHandler
class H(BaseHTTPRequestHandler):
    def do_POST(self):
        l=int(self.headers.get("Content-Length",0))
        d=self.rfile.read(l).decode()
        print("DATOS:", d)
HTTPServer(("",8080),H).serve_forever()
EOF

python3 server.py
"""


# ========================================
# 9. CÓDIGO HTML COMPLETO (para copiar)
# ========================================

"""
cat > login.html << 'EOF'
<form method="POST" action="http://localhost:8080/enviar">
Usuario: <input name="username" value="admin"><br>
Pass: <input name="password" type="password" value="secreto123"><br>
<button>Enviar</button>
</form>
EOF
"""


# ========================================
# 10. SÍNTESIS
# ========================================

"""
✅ HTTP envía datos en texto plano
✅ Wireshark puede capturar contraseñas en redes HTTP
✅ HTTPS cifra los datos (Wireshark no los ve)
✅ El método POST envía datos en el cuerpo del paquete
✅ HTML Form URL Encoded muestra usuario y contraseña

APLÍCAR A BUG BOUNTY:
- Sitios que usen HTTP (no HTTPS)
- Configurar Burp Suite o Wireshark para interceptar
- Reportar "Credenciales enviadas en texto plano" como vulnerabilidad
"""

#ESCANEO PASIVO
4. TSHARK - VERSIÓN TERMINAL DE WIRESHARK
bash

# Capturar en terminal (equivalente a tcpdump)
sudo tshark -i eth0

# Capturar sin resolver nombres
sudo tshark -i eth0 -n

# Capturar y guardar en archivo
sudo tshark -i eth0 -w captura.pcap

# Capturar con filtro (formato tcpdump)
sudo tshark -i eth0 -f "host 192.168.1.1"

# Mostrar solo direcciones IP de origen y destino
sudo tshark -i eth0 -T fields -e ip.src -e ip.dst

# Mostrar solo MACs e IPs
sudo tshark -i eth0 -T fields -e eth.src -e eth.dst -e ip.src -e ip.dst

# Capturar con límite de paquetes
sudo tshark -i eth0 -c 100

# Leer archivo de captura
sudo tshark -r captura.pcap

🖥️ 5. WIRESHARK - INTERFAZ GRÁFICA
bash

# Iniciar Wireshark
sudo wireshark

# Iniciar Wireshark capturando en interfaz específica
sudo wireshark -i eth0

# Iniciar Wireshark capturando directamente
sudo wireshark -i eth0 -k
