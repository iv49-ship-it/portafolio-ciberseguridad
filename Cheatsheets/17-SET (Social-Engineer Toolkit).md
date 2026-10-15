# CHEATSHEET - SET (Social-Engineer Toolkit)

## 🛠️ INSTALACIÓN Y EJECUCIÓN

```bash
# Instalar en Kali
sudo apt update
sudo apt install set -y

# Ejecutar SET
sudo setoolkit
```

---

## 📋 MENÚ PRINCIPAL

| Opción | Nombre | Descripción |
|--------|--------|-------------|
| **1** | Social-Engineering Attacks | Ataques de ingeniería social |
| **2** | Penetration Testing (Fast-Track) | Pruebas de penetración |
| **3** | Third Party Modules | Módulos de terceros |
| **4** | Update the Social-Engineer Toolkit | Actualizar SET |
| **5** | Update SET configuration | Configuración |
| **6** | Help, Credits, and About | Ayuda |
| **99** | Exit | Salir |

---

## 📋 MENÚ DE ATAQUES (Opción 1)

| Opción | Nombre | Descripción |
|--------|--------|-------------|
| **1** | Spear-Phishing Attack Vectors | Ataques de phishing dirigido |
| **2** | Website Attack Vectors | Ataques a sitios web (clonación) |
| **3** | Infectious Media Generator | Generar USB maliciosos |
| **4** | Create a Payload and Listener | Crear payload y listener |
| **5** | Mass Mailer Attack | Enviar correos masivos |
| **6** | Arduino-Based Attack Vector | Ataques con Arduino |
| **7** | SMS Spoofing Attack Vector | Suplantación de SMS |
| **8** | Wireless Access Point Attack | Ataques a puntos de acceso |
| **9** | QRCode Generator Attack | Ataques con códigos QR |
| **10** | Powershell Attack Vectors | Ataques con PowerShell |
| **11** | Third Party Modules | Módulos externos |
| **99** | Return to Main Menu | Volver |

---

## 📋 MENÚ SPEAR-PHISHING (Opción 1 → 1)

| Opción | Nombre | Descripción |
|--------|--------|-------------|
| **1** | Perform a Mass Email Attack | Enviar correos masivos |
| **2** | Create a FileFormat Payload | Generar payload en archivo (PDF, DOC, etc.) |
| **3** | Create a Social-Engineering Template | Crear plantilla de correo |
| **99** | Return to Main Menu | Volver |

---

## 📋 MENÚ FILEFORMAT PAYLOAD (Opción 1 → 1 → 2)

| Opción | Payload | Descripción |
|--------|---------|-------------|
| **1** | Windows Reverse TCP Shell | Shell TCP reversa |
| **2** | Windows Reverse TCP Meterpreter | Meterpreter (Metasploit) |
| **3** | Windows Reverse VNC DLL | Acceso a escritorio remoto |
| **4** | Windows Reverse TCP Shell (x64) | Shell TCP reversa x64 |
| **5** | Windows Reverse TCP Meterpreter (x64) | Meterpreter x64 |
| **6** | Windows Reverse HTTPS Meterpreter | Meterpreter vía HTTPS |
| **99** | Return to Main Menu | Volver |

---

## 🔧 CONFIGURACIÓN DE PAYLOAD

```text
1. Elegir protocolo: http o https
2. Elegir puerto: (default 80 para http, 443 para https)
3. SET genera el payload en:
   /root/.set/reports/payloads/
4. Se genera un archivo .pdf o .doc con el payload integrado
```

---

## ⚠️ COMANDOS ÚTILES

```bash
# Ver configuración de SET
cat /etc/setoolkit/set.config

# Activar Sendmail (para spoofing de correo)
# Editar set.config: SENDMAIL=OFF → SENDMAIL=ON

# Ver reportes generados
ls /root/.set/reports/payloads/
```

---

## 🧠 FLUJO BÁSICO DE ATAQUE

```text
1. Iniciar SET: sudo setoolkit
2. Seleccionar: 1) Social-Engineering Attacks
3. Seleccionar: 1) Spear-Phishing Attack Vectors
4. Seleccionar: 2) Create a FileFormat Payload
5. Seleccionar: 2) Windows Reverse TCP Meterpreter (o la que elijas)
6. Elegir protocolo y puerto
7. SET genera el payload
8. Enviar el archivo a la víctima (simulado)
9. Esperar conexión (con Metasploit u otro listener)
```

---

## ✅ REGLA DE ORO

> **SET solo se usa en entornos autorizados.**  
> No se envían correos a personas reales.  
> No se clonan páginas sin permiso explícito.

---

## ⚠️ NOTAS IMPORTANTES

- **No uses SET en entornos reales** sin autorización por escrito.
- **En TryHackMe** solo explorar el menú, no enviar correos reales.
- **El valor está en entender el flujo**, no en ejecutarlo.