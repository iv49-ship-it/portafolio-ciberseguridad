# Linux Essentials - Cheatsheet

## 🐧 Comandos básicos

| Símbolo | Significado |
|---------|-------------|
| `#`     | Root (usuario administrador) |
| `$`     | Usuario normal |
| `UID 0` | Root |

## 📁 Directorios importantes

| Directorio | Permisos | Significado |
|------------|----------|-------------|
| `/tmp`     | `rwxrwxrwt` | Sticky bit (solo dueño puede borrar) |

## 👤 Gestión de usuarios
# Crear usuario con home directory
useradd -m nombre_usuario


# Cambiar grupo primario
usermod -g grupo usuario


# Crear archivo tar
tar -cf archivo.tar /ruta/a/comprimir


# Extraer archivo tar
tar -xf archivo.tar


# Compresión gzip
gzip -9 archivo        # Máxima compresión (más lento)
gzip -1 archivo        # Mínima compresión (más rápido)


🔐 Permisos (chmod)
Permiso	Número	Significado
r (read)	4	Leer archivo
w (write)	2	Modificar archivo
x (execute)	1	Ejecutar (scripts)
EJEMPLOS:
chmod 755 archivo.sh   # rwxr-xr-x
chmod 744 archivo.sh   # rwxr--r--
chmod +x archivo.sh    # Dar ejecución a todos


#Copiar preservando atributos:
cp -a archivo destino   # Preserva TODO (permisos, timestamps)
cp -p archivo destino   # Preserva permisos y timestamps


📊 Monitoreo del sistema
free        # Memoria RAM y swap
df          # Espacio en disco
df /home    # Espacio del filesystem completo
du -sh /home/*  # Espacio por usuario


📂 Sistema de archivos /proc
Archivo	Información
/proc/cpuinfo	Detalles del CPU
/proc/meminfo	Estado RAM y swap
/proc/version	Versión del kernel
/proc/uptime	Tiempo activo del sistema
/proc/loadavg	Promedio de carga
/proc/filesystems	FS soportados
/proc/mounts	FS montados
/proc/devices	Dispositivos disponibles
/proc/net/	Estadísticas de red
/proc/[PID]/	Info de proceso específico


📝 Logs y configuración
/var/log/auth.log    # Logs de autenticación
~/.bashrc            # Configuración de bash (se carga al iniciar)

🔌 Red y DNS
# Modificar PATH
PATH=/nuevo:$PATH
# DNS record types
A     # IPv4
AAAA  # IPv6

⚡ Apagar sistema
shutdown -h now       # Apaga inmediatamente


🔍 Filtros y comandos útiles
sort              # Ordena (alfabético/numérico)
wc -l             # Cuenta líneas
wc -w             # Cuenta palabras
wc -c             # Cuenta caracteres
wc                # Muestra las 3 cuentas juntas

*.txt             # Todos los archivos .txt
?.txt             # Un solo caracter + .txt (ej: a.txt, 1.txt)


