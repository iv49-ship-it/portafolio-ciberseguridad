
# GRC (Gobernanza, Riesgo y Cumplimiento) - Notas

## El Rol
No se configuran firewalls. Se decide qué riesgos son aceptables, qué controles son obligatorios y cómo se demuestra cumplimiento ante auditorías y clientes.

## Marcos y estándares
| Marco | Propósito | Uso |
|---|---|---|
| ISO 27001 | Sistema de Gestión de Seguridad de la Información (SGSI) | Certificar madurez de procesos |
| NIST CSF | Identificar, Proteger, Detectar, Responder, Recuperar | Guiar estrategia y medir madurez |
| PCI DSS | Protección de datos de tarjetas | Obligatorio si se procesan pagos |
| GDPR | Protección de datos personales (UE) | Evitar sanciones y proteger privacidad |

## Gestión de riesgos
1. **Identificación:** activos críticos (base de datos de clientes, servidores de producción).
2. **Evaluación:** probabilidad × impacto.
3. **Tratamiento:**
   - Mitigar: aplicar un control.
   - Transferir: seguro de ciberseguridad.
   - Aceptar: el costo del control supera el riesgo.
   - Evitar: eliminar la actividad riesgosa.

## Entregables
- Políticas (uso aceptable, contraseñas, acceso remoto).
- Matriz de riesgos: riesgo, dueño, probabilidad, impacto, estado de mitigación.
- Reportes de cumplimiento para auditoría.

## Comunicación
Traducir lo técnico a lenguaje de negocio. No "hay SQL injection", sino "riesgo de fuga de datos de clientes con impacto legal y reputacional".

## Ritmo de trabajo en GRC
- Ciclos planificados: auditorías, revisiones de políticas, cuestionarios de clientes.
- Horario de oficina. Sin guardias 24/7.
- La presión es de plazo y precisión documental, no de respuesta en tiempo real.
- El entregable principal es un documento claro, no una alerta cerrada.

## Diferencia con Red Team
- Red Team: "entré y robé la base de datos".
- GRC: "la base de datos no estaba cifrada, se viola la política interna y el GDPR; se propone plan de cifrado y actualización de política".
