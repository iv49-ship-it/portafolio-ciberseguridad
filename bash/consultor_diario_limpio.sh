#!/bin/bash
# consultor_diario.sh - Versión Bash del script de auditoría

echo "📋 REPORTE DIARIO - $(date +'%d/%m/%Y %H:%M')"
echo "=================================================="

# IAM
echo -e "\nUSUARIOS SIN MFA:"
grep "no-mfa" usuarios_simulados.txt 2>/dev/null | while read linea; do
    usuario=$(echo "$linea" | cut -d: -f1)
    echo "  - $usuario"
done

# Security Groups
echo -e "\nREGLAS CRÍTICAS:"
echo "=================================================="

grep "0.0.0.0/0" security_groups.txt 2>/dev/null | while read linea; do
    nombre=$(echo "$linea" | cut -d: -f1)
    if echo "$linea" | grep -q ":22\|:3389"; then
        echo "  [CRITICO] $nombre - SSH/RDP público"
    elif echo "$linea" | grep -q ":80\|:443"; then
        echo "  [WEB] $nombre - Web (aceptable)"
    else
        echo "  [?] $nombre - Puerto público sin clasificar"
    fi
done
