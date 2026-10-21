# Vulnerabilidades de Software - Cheatsheet

## 🧩 Categorización de vulnerabilidades

| Vulnerabilidad | Descripción |
|----------------|-------------|
| **Desbordamiento de búfer** | Datos se escriben más allá de los límites de un búfer → acceso a memoria de otros procesos |
| **Entrada no válida** | Datos maliciosos diseñados para que el programa se comporte inesperadamente |
| **Condiciones de carrera** | La salida depende del orden/timing de eventos (cuando no ocurren correctamente) |
| **Debilidad en prácticas de seguridad** | No usar bibliotecas probadas, crear algoritmos propios (introducen vulnerabilidades) |
| **Problemas de control de acceso** | Uso incorrecto de controles de acceso |
| **Acceso físico** | Si atacante tiene acceso físico, puede omitir el SO y leer datos directamente del disco |

## 🔐 OAuth (Open Authorization)
Protocolo estándar abierto que permite acceso a aplicaciones de terceros **sin exponer contraseñas** de usuarios.

## 🛡️ Dispositivos de seguridad

| Dispositivo | Función |
|-------------|---------|
| **Routers** | Filtrado básico de datos |
| **Cortafuegos (Firewalls)** | Analizan tráfico e identifican comportamiento malicioso |
| **IPS** | Bloquean tráfico y ataques maliciosos |
| **VPN** | Túnel cifrado seguro para conexión remota |
| **Antimalware/Antivirus** | Analizan comportamiento de aplicaciones, bloquean código malicioso |
| **Web/Email security** | Protección específica para web y correo |

## 🔥 Tipos de Cortafuegos (Firewalls)

| Tipo | Filtra por |
|------|------------|
| **Capa de red** | Direcciones IP origen/destino |
| **Capa de transporte** | Puertos origen/destino y estados de conexión |
| **Capa de aplicación** | Aplicación, programa o servicio |
| **Capa sensible al contexto** | Usuario, dispositivo, función, tipo de app, perfil de amenaza |
| **Servidor proxy** | URL, nombres de dominio, tipos de medio |
| **Proxy inverso** | Protege y oculta servidores web |
| **NAT** | Oculta/enmascara direcciones privadas |
| **Host-based** | Puertos y llamadas de sistema en un SO |

## 📡 Análisis de puertos

### Respuestas de escaneo (Nmap)

| Estado | Significado |
|--------|-------------|
| **Abierto / Aceptado** | Otros dispositivos pueden acceder al servicio |
| **Cerrado / Denegado / Sin escuchar** | El servicio no se ejecuta |
| **Filtrado / Eliminado / Bloqueado** | Acceso bloqueado por firewall |

## 🚨 IDS vs IPS

| Sistema | Función |
|---------|---------|
| **IDS** (Detección) | Escanea datos contra base de datos de reglas/firmas |
| **IPS** (Prevención) | Puede denegar o bloquear tráfico según reglas |
| **IDS/IPS combinado** | Snort de Cisco (hace ambas funciones) |

## 🧪 Honeypot
Herramienta basada en comportamiento que **atrae al atacante** para registrar, analizar y capturar su conducta.

## 📊 NetFlow
Tecnología que recopila información sobre datos que fluyen por una red:
- Quién y qué dispositivos están en la red
- Cuándo y cómo acceden
- Más de 90 atributos (IP origen/destino, etc.)

## 🎯 Pruebas de Penetración - Fases

| Fase | Actividades |
|------|-------------|
| **1. Planificación** | Recopilar info del objetivo, vulnerabilidades, exploits (reconocimiento pasivo/activo) |
| **2. Escaneo** | Escaneo de puertos, análisis de vulnerabilidades, enumeración |
| **3. Obtener acceso** | Exploits, ingeniería social, violación de controles, descifrar Wi-Fi |
| **4. Mantener acceso** | Puertas traseras, troyanos, rootkits, canales encubiertos |
| **5. Análisis y reportes** | Recomendaciones de actualizaciones, políticas, capacitación |

## 🛠️ Herramientas de prevención y detección

| Herramienta | Sigla | Función |
|-------------|-------|---------|
| **SIEM** | Security Information Event Management | Recopila y analiza alertas de seguridad, logs en tiempo real |
| **DLP** | Data Loss Prevention | Evita que datos se roben o escapen de la red |

## 📋 Mejores prácticas de seguridad

1. Realizar evaluación de riesgos
2. Crear política de seguridad
3. Medidas de seguridad física
4. Verificaciones de antecedentes (RRHH)
5. Copias de seguridad y pruebas de recuperación
6. Mantener actualizaciones y parches
7. Roles de acceso y autenticación fuerte
8. Probar respuesta a incidentes regularmente
9. Herramienta de administración y monitoreo de redes
10. Dispositivos de seguridad de red
11. Solución integral de seguridad para endpoints
12. Educar a los usuarios
13. Cifrar todos los datos
