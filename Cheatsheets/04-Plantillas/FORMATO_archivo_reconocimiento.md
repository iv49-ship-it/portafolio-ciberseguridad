# RECONOCIMIENTO - PAYSTACKMFB.COM
**Fecha:** 05/07/2026
**Herramientas:** crt.sh, whois, dig, urlscan.io
**Objetivo:** Identificar subdominios y superficie de ataque

---

## 1. DOMINIO PRINCIPAL

| Campo | Valor |
|-------|-------|
| Dominio | paystackmfb.com |
| Creación | 2025-05-19 |
| Expiración | 2027-05-19 |
| Registrador | Amazon Registrar, Inc. |
| DNS (NS) | Cloudflare (dion.ns.cloudflare.com, hope.ns.cloudflare.com) |
| DNSSEC | No configurado |

---

## 2. SUBDOMINIOS ENCONTRADOS

### 2.1. okta.paystackmfb.com
| Campo | Valor |
|-------|-------|
| Estado | Activo |
| Tecnología | Okta (autenticación/SSO) |
| Servidor | Nginx |
| HSTS | Activado (max-age=31536000) |
| Observaciones | Panel de autenticación expuesto |

### 2.2. it.paystackmfb.com
| Campo | Valor |
|-------|-------|
| Estado | Activo |
| Tecnología | Cloudflare |
| Observaciones | Posible panel de IT/administración |

### 2.3. public.paystackmfb.com (NUEVO)
| Campo | Valor |
|-------|-------|
| Estado | [Pendiente de verificar] |
| Tecnología | [Pendiente de identificar] |
| Observaciones | Posible portal público o contenido estático |

---

## 3. TECNOLOGÍAS DETECTADAS

| Tecnología | Dominio |
|------------|---------|
| Cloudflare | paystackmfb.com, it.paystackmfb.com |
| Okta | okta.paystackmfb.com |
| Nginx | okta.paystackmfb.com |
| Google Workspace | paystackmfb.com (MX) |

---

## 4. INFRAESTRUCTURA

| Recurso | Detalle |
|---------|---------|
| IPs (Cloudflare) | 104.18.8.49, 104.18.9.49, 172.67.162.237 |
| Ubicación IP | EE. UU. (Cloudflare) |
| Correo (MX) | smtp.google.com (Google Workspace) |

---

## 5. PRÓXIMOS PASOS

- [ ] Verificar estado de `public.paystackmfb.com` (ping/curl)
- [ ] Identificar tecnologías en `public.paystackmfb.com`
- [ ] Revisar si `public.paystackmfb.com` tiene archivos expuestos (robots.txt, .well-known/)
- [ ] Actualizar este archivo con nuevos hallazgos

---

## 6. NOTAS ADICIONALES

- Todos los subdominios usan Cloudflare (WAF/CDN)
- DNSSEC no está configurado (hallazgo bajo)
- Dominio joven (creado en 2025) pero activo

#FORMATO ARCHIVO DESCARTADO
### public.paystackmfb.com (DESCARTADO)

| Campo | Valor |
|-------|-------|
| Fuente | crt.sh (certificado emitido) |
| Estado | DNS no resuelve (NXDOMAIN) |
| Verificación | No resuelve en AttackBox ni urlscan.io |
| Decisión | Falso positivo - descartado para reconocimiento |
| Lección | Los certificados pueden existir sin DNS público (uso interno) |
