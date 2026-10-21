

### 📄 Cheatsheet 2: Análisis GRC (Governance, Risk & Compliance)

Este es un resumen conceptual de los pilares de GRC, sus marcos y cómo se aplican en la práctica, complementando el enfoque técnico de tus otros cheatsheets [citation:2][citation:4].

```markdown
# Cheatsheet: Análisis GRC (Gobernanza, Riesgo y Cumplimiento)

## 🏛️ ¿Qué es GRC?
Es un enfoque integrado para gestionar la **Gobernanza**, el **Riesgo** y el **Cumplimiento** de una organización. No es un departamento, sino una cultura y un conjunto de procesos que alinean la seguridad con los objetivos del negocio [citation:2][citation:4].

## 🧱 Los 3 Pilares

### 1. Gobernanza (Governance)
**Define QUIÉN decide y CÓMO.**
- **Políticas:** Reglas de alto nivel (ej: "Todos los empleados deben usar MFA").
- **Roles y Responsabilidades:** Quién es el dueño del riesgo, quién aprueba los cambios.
- **Estrategia:** Cómo la seguridad apoya al negocio.
- **Cultura:** Concientización y comportamiento ético.
- **Métrica clave:** ¿El consejo directivo entiende y apoya la seguridad?

### 2. Gestión de Riesgos (Risk Management)
**Define QUÉ proteger y CUÁNTO invertir.**
- **Identificación:** ¿Qué activos son críticos? (datos de clientes, servidores).
- **Evaluación:** ¿Cuál es la probabilidad y el impacto de una amenaza? (ej: un ransomware en el servidor principal es Alta Probabilidad / Alto Impacto).
- **Priorización:** No todos los riesgos son iguales. Se priorizan los que afectan al negocio.
- **Tratamiento:** Mitigar (aplicar control), Transferir (seguro), Aceptar (riesgo residual) o Evitar (eliminar la actividad).
- **Herramientas:** ISO 27001, NIST SP 800-30.

### 3. Cumplimiento (Compliance)
**Define QUÉ LEYES Y NORMAS seguir.**
- **Regulaciones legales:** GDPR (Europa), HIPAA (Salud en EE. UU.), PCI DSS (Tarjetas de crédito).
- **Estándares y Certificaciones:** ISO 27001, SOC 2.
- **Obligaciones contractuales:** Requisitos de clientes o proveedores.
- **Peligro:** "Cumplimiento de checkbox" (cumplir por cumplir sin entender el riesgo real).

## 📊 Marcos y Estándares Clave

| Marco | Propósito | ¿Obligatorio? |
| :--- | :--- | :--- |
| **ISO 27001** | Sistema de Gestión de Seguridad de la Información (SGSI). Certificable. | No (pero muy solicitado) |
| **NIST CSF** | Marco voluntario de 5 funciones: Identificar, Proteger, Detectar, Responder, Recuperar. | No (referencia global) |
| **PCI DSS** | Proteger datos de tarjetas de pago. | **Sí** (si manejas tarjetas) |
| **GDPR** | Protección de datos personales en la UE. | **Sí** (si tratas datos de residentes UE) |
| **SOC 2** | Informe de auditoría sobre controles de seguridad (para proveedores de servicios). | No (contractual) |

## 🔗 GRC vs. Cumplimiento Ad-Hoc

| Sin GRC (Reactivo) | Con GRC (Proactivo) |
| :--- | :--- |
| Se hace lo mínimo para pasar la auditoría. | Se entiende el riesgo y se invierte donde importa. |
| Controles duplicados para cada norma. | Un solo conjunto de controles mapea múltiples normas. |
| La seguridad es un "problema de IT". | La seguridad es un riesgo de negocio gestionado por la dirección. |

## 🎯 Habilidades Clave para un Analista GRC
- **Comunicación:** Traducir conceptos técnicos a lenguaje de negocio.
- **Pensamiento Crítico:** Evaluar riesgos más allá de la lista de verificación.
- **Conocimiento de Marcos:** Saber qué control de ISO 27001 satisface un requisito de NIST.
- **Documentación:** Redactar políticas, procedimientos y reportes de riesgo claros.
