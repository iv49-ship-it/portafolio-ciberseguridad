# Blue Team / Analista SOC - Notas

## El Rol
No se ataca. Se detecta, se tria y se responde. El trabajo es separar ruido (falsos positivos) de incidentes reales.

## Herramientas
| Herramienta | Uso defensivo |
|---|---|
| SIEM (Splunk, Elastic) | Centraliza logs, correlaciona eventos, dispara alertas |
| EDR (CrowdStrike, Defender) | Monitorea endpoints, detecta comportamiento anómalo |
| Wireshark | Analiza tráfico para identificar C2 o exfiltración |
| MITRE ATT&CK | Mapea TTPs del adversario y guía la creación de detecciones |

## Evidencia que se busca
- **Logs de autenticación:** fallos repetidos (fuerza bruta), inicios desde ubicaciones imposibles.
- **Tráfico de red:** conexiones a IPs/dominios maliciosos, transferencias de datos inusualmente grandes, beaconing.
- **Procesos:** ejecutables corriendo desde `/tmp`, `AppData` u otras rutas temporales.

## Flujo de triage
1. **Alerta:** el SIEM dispara una regla.
2. **Enriquecimiento:** se valida el contexto (IP en VirusTotal, línea de tiempo, usuario afectado).
3. **Decisión:** falso positivo → cerrar. Incidente → escalar o contener (aislar host).
4. **Documentación:** qué pasó, cuándo, cómo se contuvo.

## Conceptos clave
- **Playbook:** estrategia general de respuesta (ej. respuesta a ransomware).
- **Runbook:** pasos exactos y ordenados para un incidente concreto.
- **MITRE ATT&CK:** táctica (objetivo del atacante) vs técnica (cómo lo ejecuta).
- **IoCs:** indicadores de compromiso (hashes, IPs, dominios, nombres de archivo).

## Diferencia con Red Team
- Red Team busca entrar.
- Blue Team busca detectar que entraron y responder.
