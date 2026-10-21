REPORTE DE RECONOCIMIENTO BÁSICO
Objetivo: paystackmfb.com
Herramientas usadas: whois y curl.

1. Lo que encontré en el dominio (whois):
Revisé el dominio y vi que fue creado en mayo de 2025. Está registrado en Amazon y sus servidores DNS son de Cloudflare. 
Punto de riesgo: Noté que no tiene DNSSEC activado (dice "unsigned"). Eso significa que el dominio no tiene una capa extra de seguridad criptográfica.

2. Lo que encontré en las cabeceras (curl):
Al hacer la consulta HTTP, el servidor respondió "cloudflare". Vi que usan Netlify para el hosting. 
Punto de riesgo: Tienen activada la seguridad HSTS (que fuerza el uso de HTTPS), lo cual está bien. Sin embargo, no vi cabeceras como X-Frame-Options, lo que podría dejar la página expuesta a ataques de Clickjacking.

3. Conclusión y recomendación:
Como el dominio es relativamente nuevo y usa tecnologías modernas (Cloudflare/Netlify), la base está bien. Mi recomendación es que habiliten DNSSEC para evitar falsificaciones de DNS, y que agreguen las cabeceras de seguridad faltantes en su servidor.
