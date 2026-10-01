# SOC L1 VT Enrichment — Threat Intelligence

Herramienta Python para **enriquecimiento de indicadores de compromiso (IoCs)** mediante la API REST v3 de VirusTotal.

> **Contexto:** proyecto de laboratorio / portfolio. El resultado de reputación es contexto para el analista, no una confirmación automática de compromiso.

## Objetivo

Aportar contexto durante el triaje para que un analista pueda pasar de un indicador aislado a una investigación mejor informada:

`IOC → API Query → Reputation → Detection Count → Analyst Context → Decision`

## Indicadores soportados

- IP addresses
- Domains
- File hashes

## SOC L1 Use Case

El proyecto está pensado para tareas como:

- enriquecer una IP observada en una alerta;
- revisar reputación y detecciones reportadas;
- acelerar la priorización de una investigación;
- alimentar una decisión **investigate / escalate / close** junto con la evidencia del endpoint y la red.

La reputación de terceros no sustituye la correlación con telemetría interna.

## Stack

- Python
- REST API v3
- `requests`
- JSON
- VirusTotal
- Git / GitHub

## Ejecución

```bash
git clone https://github.com/javierblanco-code1/soc-l1-vt-enrichment.git
cd soc-l1-vt-enrichment
pip install -r requirements.txt
```

Configurar la API key mediante variable de entorno:

```bash
export VT_API_KEY="TU_API_KEY"
```

En Windows CMD:

```cmd
set VT_API_KEY=TU_API_KEY
```

Luego:

```bash
python vt_ioc_checker.py
```

## Triage Workflow

1. Recibir IOC desde alerta o investigación.
2. Normalizar el indicador.
3. Consultar VirusTotal.
4. Revisar reputation / detection count.
5. Correlacionar con hostname, timestamp, usuario y actividad observada.
6. Documentar evidencia.
7. Escalar o cerrar según contexto y procedimiento.

## Seguridad

**Nunca** almacenar API keys en el repositorio.

Buenas prácticas:

- variables de entorno;
- `.gitignore` para archivos locales;
- rotación de claves si fueron expuestas;
- no incluir credenciales en screenshots, tickets o README.

## Roadmap

- [ ] Retry/backoff robusto.
- [ ] Cache local de resultados.
- [ ] Exportación JSON/CSV.
- [ ] Normalización y validación de IoCs.
- [ ] Integración con `soc-l1-log-analyzer`.
- [ ] Tests automatizados.
- [ ] Manejo explícito de rate limits.

## Evidencia esperada

Para convertir cada ejecución en evidencia de portfolio:

```text
IOC observado
   ↓
Consulta VT
   ↓
Reputation / detections
   ↓
Correlación interna
   ↓
Triage decision
   ↓
Ticket / escalation
```

No se publican API keys ni datos sensibles.

## Portfolio

Este repositorio demuestra **Threat Intelligence, IOC enrichment, REST API usage y automatización Python** dentro de un workflow SOC L1.
