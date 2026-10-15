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

```bash
# Crear usuario con home directory
useradd -m nombre_usuario

# Cambiar grupo primario
usermod -g grupo usuario