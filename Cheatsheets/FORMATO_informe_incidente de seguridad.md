# FORMATO Y EJERCICIO DE INFORME DE INCIDENTE DE SEGURIDAD - ANÁLISIS DE TRÁFICO

**Fecha del informe:** [DD/MM/AAAA]
**Número de incidente:** [INC-XXXXXX]
**Prioridad:** [Alta / Media / Baja]
**Estado:** [Abierto / En investigación / Resuelto]

---

## 📋 PARTE 1: RESUMEN DEL PROBLEMA IDENTIFICADO EN LA RED

Los análisis de tráfico DNS y ICMP indican que la organización está experimentando una falla en la resolución de nombres o en la conectividad a un servicio crítico. Durante la revisión de los registros del analizador de protocolos, se observó que:

- [Describe el problema principal encontrado, por ejemplo: "El puerto 443 no responde al intentar acceder al portal web de la empresa."]
- [Agrega detalles específicos, por ejemplo: "Las solicitudes ICMP devuelven 'Destination Port Unreachable'."]
- [Menciona el contexto, por ejemplo: "Este puerto es normalmente utilizado para tráfico HTTPS."]

**Posibles implicaciones:**
- [Fallo en el servidor web]
- [Error en la configuración del firewall]
- [Indicador temprano de un ataque malicioso]

---

## 🔍 PARTE 2: ANÁLISIS DE DATOS Y CAUSA PROBABLE DEL INCIDENTE

### 📌 Descripción del incidente
El incidente ocurrió aproximadamente a las [hora], cuando el equipo de [nombre del equipo o área afectada] reportó que no podía acceder al [servicio/portal afectado]. El equipo de seguridad respondió rápidamente y comenzó a ejecutar pruebas utilizando herramientas de monitoreo de red, como [`tcpdump` / `Wireshark`].

### 🔎 Hallazgos técnicos
- **Puerto afectado:** [443 / 53 / etc.]
- **Tipo de tráfico:** [HTTPS, DNS, ICMP]
- **Pruebas realizadas:** [ping, traceroute, captura de paquetes]
- **Observaciones clave:**
  - [Ejemplo: "El servidor web no responde a las solicitudes HTTPS."]
  - [Ejemplo: "El firewall parece estar bloqueando el puerto 443."]
  - [Ejemplo: "Se detectaron múltiples solicitudes ICMP desde una IP sospechosa."]

### 🧠 Causa probable
Según el análisis inicial, el incidente podría deberse a:

- [Una configuración incorrecta del firewall]
- [Un ataque de denegación de servicio (DoS)]
- [Una falla en el servidor DNS]
- [Un problema de enrutamiento]

**Investigación en curso:**
- [Se está revisando la configuración del firewall para verificar si el puerto fue bloqueado.]
- [Se está contactando al administrador del servidor para revisar los logs del sistema.]
- [Se está analizando el tráfico de red en busca de patrones maliciosos.]

---

## 📌 PRÓXIMOS PASOS

| Paso | Acción | Responsable |
|------|--------|-------------|
| 1 | Revisar configuración del firewall | Equipo de Redes |
| 2 | Verificar logs del servidor web | Administrador del Servidor |
| 3 | Analizar tráfico en busca de ataques | Equipo de Seguridad |
| 4 | Restaurar acceso al servicio | Equipo de Sistemas |

---

## 📎 ANEXOS

- Capturas de pantalla del análisis de tráfico
- Registros de tcpdump / Wireshark
- Configuración actual del firewall
- Historial de cambios en la red

---

## 👤 ELABORADO POR

- **Nombre del analista:** [Tu nombre completo]
- **Cargo:** [Analista de Ciberseguridad / Network Security]
- **Correo:** [tu.correo@empresa.com]
- **Fecha de emisión:** [DD/MM/AAAA]

---

> **NOTA:** Este informe es confidencial y está destinado únicamente al equipo de seguridad y a las partes autorizadas.

# CHEATSHEET - INFORME DE INCIDENTE DE CIBERSEGURIDAD

## 📋 ESTRUCTURA ESTÁNDAR

### SECCIÓN 1: IDENTIFICACIÓN DEL ATAQUE

| Elemento | Descripción |
|----------|-------------|
| **Tipo de ataque** | [DoS / DDoS / SYN Flood / Malware / Phishing] |
| **Evidencia principal** | [Qué muestran los logs / capturas] |
| **Origen** | [IP(s) atacante(s)] |
| **Objetivo** | [IP/Dominio/servicio afectado] |
| **Impacto inicial** | [Caída del servicio / Lentitud / Error específico] |

**Ejemplo:**
> **Tipo de ataque:** DoS (SYN Flood)  
> **Evidencia:** Múltiples paquetes SYN desde IP 203.0.113.0 hacia puerto 443  
> **Origen:** 203.0.113.0  
> **Objetivo:** Servidor web 192.0.2.1  
> **Impacto:** Error 504 Gateway Timeout, conexiones rechazadas con [RST, ACK]

---

### SECCIÓN 2: ANÁLISIS TÉCNICO

| Elemento | Descripción |
|----------|-------------|
| **Protocolo afectado** | [TCP / UDP / HTTP / HTTPS] |
| **Puerto afectado** | [443 / 80 / 22 / etc.] |
| **Handshake TCP (3 pasos)** | 1. SYN → 2. SYN-ACK → 3. ACK |
| **Comportamiento anómalo** | [Qué hace el atacante] |
| **Efecto en el servidor** | [Saturación de recursos / Caída] |

**Ejemplo:**
> **Protocolo:** TCP  
> **Puerto:** 443 (HTTPS)  
> **Handshake:** SYN → SYN-ACK → ACK  
> **Comportamiento anómalo:** El atacante envía SYN sin completar el ACK  
> **Efecto:** Servidor saturado, no responde a conexiones legítimas

---
###FORMATO INFORME PROFESIONAL INCIDENTE.
### SECCIÓN 3: RECOMENDACIONES Y PRÓXIMOS PASOS

| Acción | Prioridad | Responsable |
|--------|-----------|-------------|
| [Bloquear IP atacante] | [Alta] | [Equipo de Redes] |
| [Aumentar recursos del servidor] | [Media] | [Equipo de Infraestructura] |
| [Implementar SYN Cookies] | [Alta] | [Equipo de Seguridad] |
| [Revisar configuración del firewall] | [Media] | [Equipo de Redes] |

---

## 📝 PLANTILLA DE INFORME

### INFORME DE INCIDENTE DE CIBERSEGURIDAD

**Número de incidente:** INC-XXXXXX  
**Fecha:** DD/MM/AAAA  
**Estado:** [Abierto / En investigación / Resuelto]  
**Prioridad:** [Crítica / Alta / Media / Baja]

---

### Resumen Ejecutivo

[Descripción breve del incidente en 2-3 líneas]

---

### 1. Detalles del Incidente

| Campo | Valor |
|-------|-------|
| Fecha y hora del incidente | [DD/MM/AAAA HH:MM] |
| Tipo de ataque | [ ] |
| Servicio afectado | [ ] |
| Usuarios afectados | [ ] |
| Impacto | [ ] |

---

### 2. Análisis Técnico

[Descripción detallada del análisis técnico, incluyendo:]

- **Evidencia de logs:**
  - [Captura/descripción de los paquetes relevantes]
  - [Patrones identificados]

- **Vulnerabilidad explotada:**
  - [Descripción técnica de la vulnerabilidad]

- **Línea de tiempo:**
  | Hora | Evento |
  |------|--------|
  | HH:MM | [Descripción del evento] |

---

### 3. Impacto

| Área | Impacto |
|------|---------|
| Operaciones | [ ] |
| Financiero | [ ] |
| Reputacional | [ ] |
| Legal | [ ] |

---

### 4. Recomendaciones

| Prioridad | Acción | Plazo |
|-----------|--------|-------|
| Crítica | [ ] | [Inmediato] |
| Alta | [ ] | [24-48 horas] |
| Media | [ ] | [1 semana] |
| Baja | [ ] | [1 mes] |

---

### 5. Próximos Pasos

1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

---

### 6. Anexos

- [ ] Capturas de pantalla
- [ ] Logs completos
- [ ] Configuraciones afectadas
- [ ] Reportes adicionales

---

**Elaborado por:** [Nombre]  
**Cargo:** [Cargo]  
**Fecha:** [DD/MM/AAAA]  
**Correo:** [correo@empresa.com]

---

## 🔍 GLOSARIO DE TÉRMINOS

| Término | Significado |
|---------|-------------|
| **DoS** | Denegación de servicio (un atacante) |
| **DDoS** | Denegación de servicio distribuida (múltiples atacantes) |
| **SYN Flood** | Inundación de paquetes SYN para saturar el servidor |
| **SYN** | Solicitud de conexión TCP |
| **SYN-ACK** | Aceptación de conexión TCP |
| **ACK** | Confirmación de conexión TCP |
| **RST** | Reinicio de conexión (rechazo) |
| **504 Gateway Timeout** | El servidor no respondió a tiempo |
