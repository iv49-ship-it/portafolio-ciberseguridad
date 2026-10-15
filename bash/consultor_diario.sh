#!/bin/bash
# consultor_diario.sh - Versión Bash del script de auditoría

echo "📋 REPORTE DIARIO - "
echo "=================================================="

# IAM
echo -e "\nUSUARIOS SIN MFA:"
grep "no-mfa" usuarios_simulados.txt 2>/dev/null | while read linea; do
    usuario=\
    echo "  - \"
done

# Security Groups
echo -e "\nREGLAS CRÍTICAS:"
echo "=================================================="

grep "0.0.0.0/0" security_groups.txt 2>/dev/null | while read linea; do
    nombre=\
    if echo "\" | grep -q ":22\|:3389"; then
        echo "  [CRITICO] \ - SSH/RDP público"
    elif echo "\" | grep -q ":80\|:443"; then
        echo "  [WEB] \ - Web (aceptable)"
    else
        echo "  [?] \ - Puerto público sin clasificar"
    fi
done
