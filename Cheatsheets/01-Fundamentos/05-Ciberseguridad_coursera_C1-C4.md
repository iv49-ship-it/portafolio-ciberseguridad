# Cheatsheet: Fundamentos de Ciberseguridad y SQL (Google C1-C4)

## 🛡️ Curso 1: Fundamentos de Ciberseguridad
### Tríada CIA (CID)
| Concepto | Significado |
| :--- | :--- |
| **Confidencialidad** | Solo usuarios autorizados acceden a la información. |
| **Integridad** | La información es precisa y no ha sido alterada sin autorización. |
| **Disponibilidad** | La información es accesible cuando los usuarios autorizados la necesitan. |

### Los 8 Dominios de CISSP
1.  Seguridad y Gestión de Riesgos
2.  Seguridad de los Activos
3.  Arquitectura e Ingeniería de Seguridad
4.  Seguridad de Redes y Comunicaciones
5.  Gestión de Identidad y Acceso (IAM)
6.  Evaluación y Pruebas de Seguridad
7.  Operaciones de Seguridad
8.  Seguridad del Desarrollo de Software

### Marcos y Controles
- **Marcos (Frameworks):** Guías para construir planes de seguridad (ej. NIST CSF).
- **Controles:** Salvaguardas específicas para reducir el riesgo.
    - **Administrativos:** Políticas, procedimientos.
    - **Técnicos:** Firewalls, cifrado.
    - **Físicos:** Puertas, cámaras.

### Herramientas del Analista
- **SIEM:** Recopila y analiza logs (ej. Splunk, Chronicle).
- **Analizadores de Protocolos:** Capturan tráfico (ej. Wireshark, tcpdump).
- **Lenguajes:** Python (automatización), SQL (consultas a bases de datos).

## 🌐 Curso 2: Seguridad de Redes
### Protocolos y Modelo OSI/TCP-IP
- **Capas clave:** Aplicación (HTTP/DNS), Transporte (TCP/UDP), Red (IP), Enlace (Ethernet).
- **TCP (3-way handshake):** SYN → SYN/ACK → ACK. (Fiable)
- **UDP:** Sin conexión, rápido (DNS, streaming).
- **Puertos Comunes:**
    - 22 (SSH), 80 (HTTP), 443 (HTTPS), 53 (DNS), 445 (SMB).

### Ataques Comunes
- **Do**: Inundación de tráfico (ICMP/UDP) para tumbar un servicio.
- **DDoS:** DoS distribuido desde múltiples fuentes (botnet).
- **MitM (Man in the Middle):** Interceptación de comunicaciones.
- **Suplantación (Spoofing):** Falsificar IP/MAC.

### Hardening (Endurecimiento)
- **Principio de mínimo privilegio.**
- **Parcheo regular** de sistemas.
- **Configuración de firewalls** (cortafuegos) y IDS/IPS.

## 🐧 Curso 3: Linux y el Shell (Bash)
### Comandos Esenciales
| Comando | Función |
| :--- | :--- |
| `ls`, `cd`, `pwd` | Navegación de archivos |
| `grep "patrón" archivo` | Buscar texto dentro de archivos |
| `chmod` | Cambiar permisos (ej: `chmod 755`) |
| `sudo` | Ejecutar como superusuario (root) |
| `ps`, `top` | Ver procesos en ejecución |
| `netstat -tulpn` | Ver puertos y servicios escuchando |
| `man <comando>` | Ver el manual de ayuda |

### Gestión de Usuarios y Permisos
- **UID 0 = root.**
- **Permisos:** Lectura (4), Escritura (2), Ejecución (1).
- **Archivos de log:** `/var/log/auth.log` (autenticación).

## 🗄️ Curso 4: SQL para Análisis de Seguridad
### Consultas Básicas
```sql
-- Seleccionar columnas específicas
SELECT nombre, email FROM empleados;

-- Filtrar resultados
SELECT * FROM logs WHERE evento = 'login_fallido';

-- Ordenar resultados
SELECT * FROM logs ORDER BY fecha DESC;

-- Límite de resultados
SELECT * FROM logs LIMIT 10;


Operadores Lógicos
Operador	Uso
AND	Ambas condiciones deben cumplirse.
OR	Al menos una condición debe cumplirse.
NOT	Niega la condición.
LIKE	Búsqueda por patrón (ej: WHERE usuario LIKE 'admin%').
BETWEEN	Rango de valores (ej: WHERE fecha BETWEEN '2024-01-01' AND '2024-01-31').
