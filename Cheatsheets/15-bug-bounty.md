# CHEATSHEET - BUG BOUNTY (Reconocimiento Pasivo)

## 📋 PROCEDIMIENTO ESTÁNDAR

| Paso | Acción | Herramienta |
|------|--------|-------------|
| 1 | Identificar dominio principal | HackerOne / Programa |
| 2 | Verificar alcance (InScope) | HackerOne / Política |
| 3 | Extraer WHOIS | `whois dominio.com` |
| 4 | Extraer IPs (A) | `dig dominio.com` / `nslookup` |
| 5 | Extraer servidores DNS (NS) | `whois` / `dig` |
| 6 | Extraer servidores de correo (MX) | `dig dominio.com MX` |
| 7 | Extraer registros TXT (SPF, etc.) | `dig dominio.com TXT` |
| 8 | Verificar si responde | `ping dominio.com` |
| 9 | Identificar tecnologías | `curl -I`, Wappalyzer (extensión) |
| 10 | Documentar todo | Bloc de notas / VS Code |

---

## 🔤 SIGLAS IMPORTANTES

| Sigla | Significado | Descripción |
|-------|-------------|-------------|
| **VDP** | Vulnerability Disclosure Program | Programa sin recompensa, solo reconocimiento |
| **BBP** | Bug Bounty Program | Programa con recompensa económica |
| **CVE** | Common Vulnerabilities and Exposures | ID único de vulnerabilidad conocida |
| **CWE** | Common Weakness Enumeration | Clasificación de tipos de debilidades |
| **NVD** | National Vulnerability Database | Base de datos del NIST con CVE detalladas |
| **CVSS** | Common Vulnerability Scoring System | Puntuación de gravedad (0-10) |
| **WAF** | Web Application Firewall | Firewall para aplicaciones web (ej: Cloudflare) |
| **CDN** | Content Delivery Network | Red de distribución de contenido |
| **DNS** | Domain Name System | Traduce nombres a IPs |
| **NS** | Name Server | Servidor DNS del dominio |
| **MX** | Mail Exchange | Servidor de correo del dominio |
| **A** | Address Record | IP del dominio |
| **TXT** | Text Record | Registro de texto (SPF, verificaciones) |
| **SPF** | Sender Policy Framework | Evita spoofing de correo |
| **DKIM** | DomainKeys Identified Mail | Firma de correo electrónico |
| **DMARC** | Domain-based Message Authentication | Política de autenticación de correo |
| **TTL** | Time To Live | Tiempo de caché de DNS (en segundos) |
| **InScope** | Dentro del alcance | ✅ Puedes probar |
| **OutOfScope** | Fuera del alcance | ❌ No puedes probar |

---

## 🛠️ COMANDOS BÁSICOS (recordatorio)

```bash
# WHOIS (información del dominio)
whois dominio.com

# DIG (consultas DNS)
dig dominio.com              # IP (A)
dig dominio.com A            # IP (A)
dig dominio.com NS           # Servidores DNS
dig dominio.com MX           # Servidores de correo
dig dominio.com TXT          # Registros TXT (SPF, etc.)
dig dominio.com CNAME        # Alias de subdominio

# NSLOOKUP (alternativa a DIG)
nslookup dominio.com         # IP
nslookup -type=MX dominio.com # Correo
nslookup -type=NS dominio.com # DNS

# PING (verificar si responde)
ping dominio.com
ping -c 5 dominio.com        # Solo 5 intentos

# CURL (ver tecnologías y cabeceras)
curl -I dominio.com          # Cabeceras HTTP
curl -I https://dominio.com  # Con HTTPS

[FECHA] - RECONOCIMIENTO PASIVO - DOMINIO

**1. Datos Generales**
- Dominio: 
- Creación: 
- Expiración: 
- Registrador: 
- Estado: 

**2. Infraestructura**
- DNS (NS): 
- IPs (A): 
- Propietario IP: 
- DNSSEC: 

**3. Propietario**
- Nombre: 
- País: 

**4. Servicios**
- MX: 
- TXT: 

**5. Notas**
- InScope/OutOfScope:
- Tecnologías detectadas:
- Observaciones:

**6. Subdominios encontrados (crt.sh)** EJEMPLO Con PAYSTACK y reonocimeinto pasivo AVANZADO
- okta.paystackmfb.com (Okta - autenticación) ✅ Activo
- it.paystackmfb.com (Panel IT) ✅ Activo
- paystackmfb.com (Principal) ✅ Activo

**7. Notas adicionales** EJEMPLO Con PAYSTACK y reonocimeinto pasivo AVANZADO
- Todos los certificados son de Let's Encrypt (excepto uno de Google Trust)
- Los subdominios están activos (certificados recientes)
- Okta es un servicio de autenticación → posible superficie de ataque


## 📋 CÓMO EXTRAER CADA DATO (fuentes)

| Dato | Fuente | Comando |
|------|--------|---------|
| **Fecha de creación** | WHOIS | `whois dominio.com \| grep "Creation Date"` |
| **Fecha de expiración** | WHOIS | `whois dominio.com \| grep "Expiry Date"` |
| **Registrador** | WHOIS | `whois dominio.com \| grep "Registrar"` |
| **Estado del dominio** | WHOIS | `whois dominio.com \| grep "Domain Status"` |
| **Servidores DNS (NS)** | WHOIS / DIG | `whois dominio.com \| grep "Name Server"` |
| **IPs (A)** | DIG / NSLOOKUP | `dig dominio.com A` |
| **Propietario IP** | WHOIS de IP | `whois 1.2.3.4` |
| **DNSSEC** | WHOIS | `whois dominio.com \| grep "DNSSEC"` |
| **Propietario** | WHOIS | `whois dominio.com \| grep "Registrant"` |
| **País** | WHOIS | `whois dominio.com \| grep "Country"` |
| **Servidor de correo (MX)** | DIG | `dig dominio.com MX` |
| **Registros TXT** | DIG | `dig dominio.com TXT` |
| **Tecnologías** | CURL | `curl -I https://dominio.com` |

---

## 🔍 QUÉ BUSCAR EN `curl -I`

| Cabecera | Qué indica | Bueno/Malo |
|----------|------------|------------|
| `server:` | Tecnología del servidor (Apache, nginx, Cloudflare) | ℹ️ Información |
| `strict-transport-security` | HSTS activado (obliga a usar HTTPS) | ✅ Bueno (seguridad) |
| `x-frame-options` | Protección contra clickjacking | ✅ Bueno |
| `x-content-type-options` | Protección contra MIME-sniffing | ✅ Bueno |
| `content-security-policy` | CSP (controla recursos cargados) | ✅ Bueno |
| `set-cookie` | Cookies (ver si tienen `Secure` y `HttpOnly`) | ⚠️ Revisar |
| `x-nf-request-id` | Netlify (hosting) | ℹ️ Información |
| `cf-ray` | Cloudflare (centro de datos) | ℹ️ Información |
| `alt-svc` | Soporte para HTTP/3 | ✅ Bueno (moderno) |
| `x-powered-by` | Tecnología adicional (ej: Express, PHP) | ℹ️ Información |

### 💡 EJEMPLO DE ANÁLISIS

```bash
curl -I https://paystackmfb.com


| Componente | Significado |
|------------|-------------|
| `max-age=31536000` | Duración en segundos (1 año) |
| `includeSubDomains` | Aplica también a subdominios |
| `preload` | Incluido en lista de precarga de navegadores |

---

## 🔹 CLOUDFLARE (cf-ray)

| Cabecera | Significado |
|----------|-------------|
| `cf-ray: ...-IAD` | Centro de datos Cloudflare en **IAD** |

**¿Qué es `cf-ray`?**  
Identificador único de la solicitud que pasa por Cloudflare.  
El sufijo indica el centro de datos que procesó la solicitud.

**Códigos comunes de centros de datos:**

| Código | Ciudad | País |
|--------|--------|------|
| `IAD` | Dulles, Virginia | 🇺🇸 EE.UU. |
| `LHR` | Londres | 🇬🇧 Reino Unido |
| `FRA` | Fráncfort | 🇩🇪 Alemania |
| `SJC` | San José, California | 🇺🇸 EE.UU. |
| `DFW` | Dallas, Texas | 🇺🇸 EE.UU. |
| `ORD` | Chicago, Illinois | 🇺🇸 EE.UU. |
| `ATL` | Atlanta, Georgia | 🇺🇸 EE.UU. |
| `MIA` | Miami, Florida | 🇺🇸 EE.UU. |
| `CDG` | París | 🇫🇷 Francia |
| `MAD` | Madrid | 🇪🇸 España |

---

## 🧠 REGLA DE ORO

| Si ves... | Significa... |
|-----------|--------------|
| `strict-transport-security` | **HSTS activado** ✅ |
| `-IAD` en `cf-ray` | **Virginia** |
| `-LHR` en `cf-ray` | **Londres** |
| `-FRA` en `cf-ray` | **Fráncfort** |
| `-SJC` en `cf-ray` | **San José (California)** |

---

## 📝 EJEMPLO COMPLETO

```bash
curl -I https://paystackmfb.com

# SIGLAS IMPORTANTES PARA BUG BOUNTY (RECONOCIMIENTO)

## 🔹 SUBDOMINIOS COMUNES Y SU SIGNIFICADO

| Sigla / Nombre | Significado | ¿Qué suele indicar? |
|----------------|-------------|----------------------|
| **api** | Application Programming Interface | Puntos de conexión con bases de datos o servicios internos. |
| **admin** | Administración | Paneles de control, gestión de usuarios o configuración. |
| **dev** | Desarrollo | Entornos de prueba (menos seguros, más vulnerables). |
| **test** | Pruebas | Entornos de prueba (menos seguros, más vulnerables). |
| **staging** | Pre-producción | Entorno casi idéntico al real pero con menos seguridad. |
| **it** | Information Technology | Paneles internos de IT, herramientas de soporte. |
| **okta** | Proveedor de identidad (SSO) | Servicio de autenticación (Okta). |
| **auth** | Autenticación | Servicios de login, SSO, MFA. |
| **mail** / **smtp** | Correo electrónico | Servidores de correo, webmail. |
| **ftp** | File Transfer Protocol | Servidor de archivos (a menudo inseguro). |
| **cdn** | Content Delivery Network | Red de distribución de contenido. |
| **db** | Base de datos | Acceso o gestión de bases de datos. |
| **monitor** | Monitoreo | Paneles de monitoreo de servicios. |
| **logs** | Registros | Acceso a logs del sistema. |
| **backup** | Copias de seguridad | Acceso a copias de seguridad (peligroso si está expuesto). |
| **pay** / **payment** | Pagos | Procesamiento de pagos, pasarelas. |
| **partner** | Socios | Portales para socios o colaboradores. |
| **help** / **support** | Soporte | Portales de atención al cliente o tickets. |

---

## 🛠️ TECNOLOGÍAS Y SERVICIOS COMUNES

| Sigla / Nombre | Significado | ¿Qué suele indicar? |
|----------------|-------------|----------------------|
| **Okta** | Proveedor de identidad | Autenticación y SSO (Single Sign-On). |
| **AWS** | Amazon Web Services | Infraestructura en la nube de Amazon (EC2, S3, etc.). |
| **Azure** | Microsoft Azure | Infraestructura en la nube de Microsoft. |
| **GCP** | Google Cloud Platform | Infraestructura en la nube de Google. |
| **Cloudflare** | CDN / WAF | Servicio de CDN, protección DDoS y WAF. |
| **Nginx** | Servidor web | Servidor web y proxy inverso. |
| **Apache** | Servidor web | Servidor web. |
| **Tomcat** | Servidor de aplicaciones | Servidor Java, a menudo para aplicaciones web. |
| **Node.js** | Entorno de ejecución | Aplicaciones JavaScript en el servidor. |
| **PHP** | Lenguaje de programación | Aplicaciones web en PHP. |
| **Python** | Lenguaje de programación | Aplicaciones web en Python (Django, Flask). |
| **WordPress** | CMS | Sitios web basados en WordPress. |
| **Joomla** | CMS | Sitios web basados en Joomla. |
| **Drupal** | CMS | Sitios web basados en Drupal. |
| **Magento** | CMS (e-commerce) | Tiendas online. |

---

## 🔐 SEGURIDAD Y AUTENTICACIÓN

| Sigla / Nombre | Significado | ¿Qué suele indicar? |
|----------------|-------------|----------------------|
| **SSO** | Single Sign-On | Autenticación única para múltiples servicios. |
| **MFA** | Multi-Factor Authentication | Autenticación de múltiples factores (2FA). |
| **OAuth** | Protocolo de autorización | Delegación de acceso (ej: "Login with Google"). |
| **SAML** | Security Assertion Markup Language | Intercambio de datos de autenticación y autorización. |
| **LDAP** | Lightweight Directory Access Protocol | Directorio de usuarios (ej: Active Directory). |
| **JWT** | JSON Web Token | Token de autenticación y autorización. |
| **HSTS** | HTTP Strict Transport Security | Obliga a usar HTTPS (cabecera de seguridad). |
| **CSP** | Content Security Policy | Controla recursos que puede cargar la página. |
| **CORS** | Cross-Origin Resource Sharing | Controla qué dominios pueden acceder a recursos. |
| **CNAME** | Canonical Name | Alias de un subdominio a otro dominio. |

---

## 📋 PROTOCOLOS Y SERVICIOS DE RED

| Sigla / Nombre | Significado | ¿Qué suele indicar? |
|----------------|-------------|----------------------|
| **HTTP** | Hypertext Transfer Protocol | Tráfico web no cifrado. |
| **HTTPS** | HTTP Secure | Tráfico web cifrado (más seguro). |
| **DNS** | Domain Name System | Traduce nombres de dominio a IPs. |
| **NS** | Name Server | Servidor DNS del dominio. |
| **MX** | Mail Exchange | Servidor de correo del dominio. |
| **A** | Address Record | IP del dominio (IPv4). |
| **AAAA** | Address Record IPv6 | IP del dominio (IPv6). |
| **TXT** | Text Record | Registro de texto (SPF, verificaciones). |
| **SPF** | Sender Policy Framework | Evita spoofing de correo. |
| **DKIM** | DomainKeys Identified Mail | Firma de correo electrónico. |
| **DMARC** | Domain-based Message Authentication | Política de autenticación de correo. |
| **TTL** | Time To Live | Tiempo de caché de DNS (en segundos). |
| **TLS** | Transport Layer Security | Cifrado de comunicaciones. |

---

## 🧠 TIPOS DE VULNERABILIDADES

| Sigla / Nombre | Significado | ¿Qué suele indicar? |
|----------------|-------------|----------------------|
| **XSS** | Cross-Site Scripting | Inyección de scripts en páginas web. |
| **SQLi** | SQL Injection | Inyección de código SQL en bases de datos. |
| **CSRF** | Cross-Site Request Forgery | Falsificación de peticiones en sitios web. |
| **SSRF** | Server-Side Request Forgery | Falsificación de peticiones desde el servidor. |
| **XXE** | XML External Entity | Ataque a procesadores XML. |
| **RCE** | Remote Code Execution | Ejecución de código remoto (crítico). |
| **LFI** | Local File Inclusion | Inclusión de archivos locales. |
| **RFI** | Remote File Inclusion | Inclusión de archivos remotos. |
| **IDOR** | Insecure Direct Object Reference | Acceso a objetos sin autorización. |
| **CVE** | Common Vulnerabilities and Exposures | ID único de vulnerabilidad conocida. |
| **CWE** | Common Weakness Enumeration | Clasificación de tipos de debilidades. |
| **NVD** | National Vulnerability Database | Base de datos del NIST con CVE detalladas. |
| **CVSS** | Common Vulnerability Scoring System | Puntuación de gravedad (0-10). |

--
## 🏢 PROGRAMAS Y PLATAFORMAS

| Sigla / Nombre | Significado | ¿Qué suele indicar? |
|----------------|-------------|----------------------|
| **VDP** | Vulnerability Disclosure Program | Programa sin recompensa, solo reconocimiento. |
| **BBP** | Bug Bounty Program | Programa con recompensa económica. |
| **InScope** | Dentro del alcance | ✅ Puedes probar. |
| **OutOfScope** | Fuera del alcance | ❌ No puedes probar. |

---

## 🧠 REGLA DE ORO

> **En reconocimiento pasivo NO se toca el servidor.**  
> Solo se consultan bases de datos públicas y DNS.  
> **No se escanea, no se prueba, no se explota.**

### ¿Qué significa esto en la práctica?

| ✅ SÍ puedes hacer | ❌ NO puedes hacer |
|-------------------|-------------------|
| `whois`, `dig`, `nslookup` | `nmap -p-` (escaneo de puertos) |
| `ping` (ICMP) | `gobuster`, `dirb` (fuerza bruta) |
| `curl -I` (solo cabeceras) | `curl` con payloads o exploits |
| Ver código fuente (F12) | Modificar peticiones con Burp Suite |
| Buscar en `crt.sh` | Probar credenciales o inyecciones |
| Navegar por el sitio | Enviar correos de phishing |
| Leer archivos públicos (`robots.txt`, `.well-known/`) | Intentar subir archivos |



Término	¿Qué es? | 	Ejemplo en tu caso
Common Name (CN)  |	El dominio principal del certificado	public.paystackmfb.com
Matching Identities	| Todos los dominios/subdominios que comparten el mismo certificado	paystackmfb.com, *.paystackmfb.com

**Si no estás seguro de si una acción es pasiva o activa, pregúntate:**
> "¿Estoy enviando algo al servidor que el servidor no espera de un usuario normal?"

- **Usuario normal:** hace clic en enlaces, ve páginas, lee contenido.
- **Atacante:** envía peticiones malformadas, escanea puertos, prueba exploits.

---
BUG BOUNTY - RECONOCIMIENTO PASIVO
1. Buscar subdominios con crt.sh
bash

# Desde terminal (con User-Agent para evitar bloqueos)
curl -s -A "Mozilla/5.0" "https://crt.sh/?q=%.paystackmfb.com&output=json" | jq '.[].name_value' | sort -u

# Sin jq (si no está instalado)
curl -s -A "Mozilla/5.0" "https://crt.sh/?q=%.paystackmfb.com&output=json" > subdominios.txt
cat subdominios.txt

2. Verificar si un subdominio existe
bash

# Ping (si responde, existe)
ping -c 2 subdominio.paystackmfb.com

# Consulta DNS
nslookup subdominio.paystackmfb.com

# Ver cabeceras HTTP
curl -I https://subdominio.paystackmfb.com

3. Documentar hallazgos en el portafolio
text

[FECHA] - Reconocimiento pasivo - [DOMINIO]

**Subdominios encontrados:**
- okta.paystackmfb.com → Activo
- it.paystackmfb.com → Activo
- private.paystackmfb.com → No resuelve
- public.paystackmfb.com → No resuelve

**Observaciones:**
- Todos los subdominios usan Cloudflare.
- DNSSEC no configurado.
- Certificados emitidos por Let's Encrypt.

**Próximo paso:** Analizar cabeceras HTTP y tecnologías.