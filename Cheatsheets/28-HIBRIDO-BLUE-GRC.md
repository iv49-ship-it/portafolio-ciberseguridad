# Rol Híbrido: Blue Team + GRC - Notas

## El Puente
Un incidente técnico no termina cuando se cierra la alerta. Termina cuando se documenta como riesgo, se actualiza la política y se reporta a la dirección.

## Flujo completo (de alerta a reporte)
1. **Detección (Blue):** el SIEM dispara una alerta.
2. **Triage (Blue):** se valida si es incidente real.
3. **Contención (Blue):** se aísla el host afectado.
4. **Documentación (GRC):** se registra en la matriz de riesgos.
5. **Análisis de causa (GRC):** qué control falló, qué política no se cumplió.
6. **Acción correctiva (GRC):** actualizar política, agregar control, capacitar.
7. **Reporte (GRC):** resumen ejecutivo para dirección.

## Traducción técnica → negocio
| Hallazgo técnico (Blue) | Riesgo de negocio (GRC) |
|---|---|
| Puerto 445 expuesto | Riesgo de ransomware con impacto operacional |
| Sin MFA en admin | Riesgo de acceso no autorizado, posible sanción GDPR |
| Logs incompletos | Imposibilidad de investigar incidentes, incumplimiento PCI DSS |
| Backup sin probar | Riesgo de pérdida de datos, incumplimiento ISO 27001 |

## Métricas que conectan ambos mundos
- **MTTD:** tiempo medio de detección (Blue).
- **MTTR:** tiempo medio de respuesta (Blue).
- **Riesgo residual:** lo que queda después de mitigar (GRC).
- **Cobertura de controles:** % de controles ISO/NIST implementados (GRC).

## Comunicación a dirección
No se reporta "alerta 4521 del SIEM". Se reporta:
- Qué pasó (en una frase).
- Qué riesgo representó (impacto y probabilidad).
- Qué se hizo (contención y acción correctiva).
- Qué se necesita (presupuesto, personal, herramienta).

## Por qué el híbrido elige GRC
- La base técnica sirve para evaluar riesgos con criterio, no para operar un SOC.
- El valor está en conectar el hallazgo técnico con la decisión de negocio.
- El trabajo se mide en riesgos gestionados y auditorías pasadas, no en alertas cerradas.

## Diferencia clave
- Blue Team pregunta: "¿qué está pasando ahora?"
- GRC pregunta: "¿qué riesgo representa y qué hacemos al respecto?"
- El híbrido responde ambas y documenta la respuesta.
