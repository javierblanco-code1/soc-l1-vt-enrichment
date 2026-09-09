# soc-l1-vt-enrichment
Script de automatización en Python para el enriquecimiento de IoCs (reputación de IPs) mediante la API REST v3 de VirusTotal para SOC L1.
# SOC L1: Threat Intelligence & IoC Enrichment with VirusTotal API

## 📌 Descripción
Herramienta en Python para la fase de triaje en un SOC Level 1. Permite enriquecer alertas consultando de forma automatizada la reputación de direcciones IP sospechosas mediante la API REST v3 de VirusTotal.

## 🚀 Funcionalidades
- Consulta masiva de indicadores de compromiso (IoCs).
- Extracción de estadísticas de motores de seguridad en tiempo real.
- Clasificación automática para la toma de decisiones rápidas de bloqueo o descarte.

## 📋 Uso
1. Clonar el repositorio y configurar dependencias:
   ```bash
   pip install -r requirements.txt
2. Establecer tu clave de API:
   Bash
   export VT_API_KEY="tu_api_key"  # Linux/macOS
   set VT_API_KEY="tu_api_key"     # Windows CMD
3. Ejecutar el script:
   Bash
   python vt_ioc_checker.py
