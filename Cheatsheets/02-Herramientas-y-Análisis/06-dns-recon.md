
---

## 📄 06-dns-recon.md

```markdown
# DNS Recon - Cheatsheet

## 🛠️ Herramientas principales

| Herramienta | Función | Cuándo usarla |
|-------------|---------|---------------|
| `nslookup` | Consulta DNS tradicional | Exploración interactiva, aprender |
| `dig` | Consulta DNS potente | Resultado detallado, scripts, profesional |
| `host` | Búsqueda simple | Consultas rápidas, minimalista |
| `whois` | Información de registro de dominio | Dueño del dominio, contactos |

## 📝 nslookup

### Uso básico
```bash
# Modo no interactivo
nslookup cisco.com

# Búsqueda inversa (IP → nombre)
nslookup 72.163.5.201

# Usar servidor DNS específico
nslookup netacad.com 8.8.8.8

#MODO INTERACTIVO
nslookup
> server 8.8.8.8
> set type=ns
> cisco.com
> set type=mx
> cisco.com
> set type=any
> netacad.com
> exit

#DIG-USO BÁSICO
# Consulta normal (solo IPv4 por defecto)
dig cisco.com

# Consultar IPv6
dig cisco.com AAAA

# Usar servidor DNS específico
dig cisco.com @8.8.8.8

# Consultar registros NS
dig cisco.com ns

# Consultar registros MX
dig cisco.com mx

# Consultar ANY (todos los registros)
dig netacad.com any

# Búsqueda inversa (IP → nombre)
dig -x 72.163.5.201

#Formato de salida de dig
Columna	        |Significado
Nombre/Dominio	|El dominio que consultaste
TTL	            |Tiempo de vida en caché (segundos)
Clase	        |Casi siempre IN (Internet)
Tipo de Registro|	A, AAAA, NS, MX, TXT, etc.
Datos/Respuesta	 |   La respuesta (IP, servidor, texto)

# Resolver nombre a IP
host netflix.com

# Búsqueda inversa
host 72.163.10.1

# Consultar tipo específico
host -t mx cisco.com
host -t ns cisco.com

Tipos de registros DNS
Tipo  |Información	           |Ejemplo
A	     IPv4 cisco.com ->       |72.163.4.185
AAAA	 IPv6 cisco.com ->      |2001:420:1101:1::185
NS	     Name Server (servidor DNS)	|ns1.cisco.com
MX	 Mail Exchange (servidor de correo)	|mail.cisco.com
TXT	Texto (verificaciones, SPF, etc.)	|"v=spf1 include:_spf.google.com ~all"
PTR	Pointer (búsqueda inversa)	|IP → nombre de host
CNAME	Canonical Name (alias)	|www -> @

# Información de dominio
whois cisco.com

# Información de IP (rango asignado)
whois 72.163.5.201

# Filtrar por nombre de organización
whois 3.230.129.93 | grep OrgName

#Identificar hosts por nombre
|Si el nombre contiene...|	Es probablemente un...
hsrp	                    Router (protocolo de alta disponibilidad)
gw                          o gateway	Puerta de enlace
fw	                       Firewall
ws o web	               Servidor web
db	                       Servidor de base de datos
dns	                       Servidor DNS
mail o smtp	               Servidor de correo
proxy	                   Proxy server

# Verificar si una IP pertenece a la nube
whois 3.230.129.93 | grep OrgName
# Salida: Amazon Technologies Inc.

#Comparativa rápida
|Herramienta|	|Formato	     |Mejor para|
dig	         |Detallado, tabular|	Profesional, scripts
host	       Minimalista         Consultas rápidas
nslookup	Interactivo	          Exploración, aprendizaje
whois	          Texto	         Info de registro/dominio
