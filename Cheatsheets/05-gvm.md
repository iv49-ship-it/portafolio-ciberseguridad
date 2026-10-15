# CHEATSHEET - OPENVAS / GVM (Greenbone Vulnerability Management)

## 🔧 INSTALACIÓN (Kali Linux)

```bash
# Instalar GVM
sudo apt update
sudo apt install gvm -y

# Configurar (tarda ~30-60 min)
sudo gvm-setup

# Verificar instalación
sudo gvm-check-setup

# Iniciar GVM
sudo gvm-start

# Detener GVM
sudo gvm-stop

# GVM / OPENVAS - CHEATSHEET RÁPIDO

## 🌐 ACCEDER A INTERFAZ WEB

| Elemento | Valor |
|----------|-------|
| URL | `https://127.0.0.1:9392` |
| Usuario | `admin` |
| Contraseña | (la que generó `gvm-setup`) |
| Nota | Aceptar riesgo (certificado autofirmado) |

---

## 🧙 CREAR ESCANEO (Task Wizard)

| Paso | Acción |
|------|--------|
| 1 | `Scans → Tasks` |
| 2 | Clic en icono **varita mágica** ✨ |
| 3 | Ingresar IP o dominio (ej: `scanme.nmap.org`) |
| 4 | `Start Scan` |

---

## ⏳ ESTADOS DEL ESCANEO

| Estado | Significado |
|--------|-------------|
| `Requested` | En cola |
| `Running` | Escaneando (minutos/horas) |
| `Done` | Terminado ✅ |

---

## 📊 VER REPORTE

| Paso | Acción |
|------|--------|
| 1 | `Reports` → clic en fecha del escaneo |
| 2 | Navegar pestañas: `CVE` / `Results` / `Hosts` |
| 3 | Descargar PDF: icono flecha abajo ↓ |

---

## 📄 INTERPRETAR RESULTADOS

| Campo | Significado |
|-------|-------------|
| `CVE` | ID único (ej: CVE-2019-6111) |
| `CVSS` | Gravedad (0 = bajo, 10 = crítico) |
| `Solution` | Cómo arreglarlo |
| `Nivel` | Crítico / Alto / Medio / Bajo |

---

## 🔄 ACTUALIZAR BASE DE DATOS

```bash
sudo gvm-feed-update