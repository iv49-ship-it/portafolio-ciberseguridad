# CHEATSHEET - ANÁLISIS DE TRÁFICO Y REPORTE DE INCIDENTES

## 📋 ESTRUCTURA DEL INFORME DE INCIDENTE (Coursera)

### SECCIÓN 1: Identificar el protocolo de red involucrado
- **Objetivo:** Identificar qué protocolos de red están presentes en el incidente.
- **Preguntas guía:** ¿Qué protocolos aparecen en los logs? (DNS, HTTP, TCP, etc.)
- **Evidencia:** Citar líneas específicas del archivo de logs que muestren el protocolo.

| Protocolo | Cómo identificarlo |
|-----------|-------------------|
| DNS | Líneas con `dns.google.domain` o consultas a servidores DNS |
| HTTP | Líneas con `.http` o puerto `80` |
| TCP | Líneas con flags `[S]`, `[S.]`, `[.]`, `[P.]`, `[R]`, `[F]` |
| ICMP | Líneas con `ICMP` o `ping` |

### SECCIÓN 2: Documentar el incidente
- **Objetivo:** Describir qué ocurrió en el incidente.
- **Preguntas guía:**
  - ¿Cuándo ocurrió? (timestamps)
  - ¿Qué sitios/web se visitaron?
  - ¿Qué IPs están involucradas?
  - ¿Hay cambios sospechosos?
  - ¿Qué indican los flags TCP?
- **Evidencia:** Cita líneas de logs que muestren timestamps, IPs, flags.

### SECCIÓN 3: Recomendar una remediación
- **Objetivo:** Proponer una medida de seguridad para prevenir ataques de fuerza bruta.
- **Preguntas guía:**
  - ¿Qué ataque ocurrió o podría ocurrir?
  - ¿Qué medida evitaría que ocurra?
  - ¿Qué herramientas o políticas se necesitan?

| Medida | Explicación |
|--------|-------------|
| Account Lockout | Bloquear cuenta tras intentos fallidos |
| MFA (Autenticación multifactor) | Añadir segunda capa de autenticación |
| Rate Limiting | Limitar intentos por IP |
| CAPTCHA | Prevenir ataques automatizados |
| HSTS | Forzar HTTPS para prevenir ataques MITM |
| DNSSEC | Verificar autenticidad de respuestas DNS |

---

## 🔍 CÓMO LEER UN LOG DE TCPDUMP

### Estructura de una línea de log:

Timestamp Protocol Source > Destination: Flags [X], seq N, win N, length N

#EJEMPLO: 
14:18:32.192571 IP your.machine.52444 > dns.google.domain: 35084+ A? yummyrecipesforme.com. (24)

Parte | Significado
14:18:32.19257 | 1Hora del evento
IP	| Protocolo usado  (IPv4)
your.machine.52444 | Origen (tu máquina, puerto 52444)
>	| Dirección: enviando a
dns.google.domain	| Destino (servidor DNS)
35084+ A? |	Consulta DNS: ¿cuál es la IP de...?
yummyrecipesforme.com. | 	Dominio consultado
(24) |	Tamaño del paquete en bytes

Flags TCP (los más comunes):
Flag |	Significado
[S]	| SYN - Solicitud de conexión
[S.] |	SYN-ACK - Aceptación de conexión
[.]	| ACK - Confirmación de recepción
[P.] |	PUSH-ACK - Envío de datos
[F]	| FIN - Cierre de conexión
[R]	| RST - Reinicio de conexión (error)

1. [S]    → "Quiero conectarme"
2. [S.]   ← "Ok, te acepto"
3. [.]    → "Recibido, ya estamos conectados"

#### Security Incident Report (FORMATO INFORME)

## Section 1: Identify the network protocol involved in the incident

Los protocolos involucrados son [DNS] y [HTTP].

- [DNS:] Se evidencia en las consultas a [dns.google.domain].
- [HTTP:] Se evidencia en las conexiones al puerto 80.

## Section 2: Document the incident

1. El incidente ocurre entre [timestamp inicio] y [timestamp fin].
2. Los sitios web visitados son:
   - [sitio1.com] → IP [IP1]
   - [sitio2.com] → IP [IP2]
3. Se observa un cambio de IP, lo que indica una redirección sospechosa.
4. Los flags [S], [S.], [.] y [P.] confirman que se estableció una conexión.

## Section 3: Recommend one remediation for brute force attacks

Para prevenir ataques de fuerza bruta, se recomienda:

- [Medida 1]
- [Medida 2]
- [Medida 3]
