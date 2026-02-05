# 🛠️ Laboratorio: Workflow e Strumenti di Sviluppo

Scopo: imparare a organizzare un repository
- file da inserire
- struttura a moduli
- documentazione

Tools:
- git
- github
- formatter
- debugger

## Struttura repository

```
├─ 01_teoria
├─ 02_esercizi
│       └─ ex_1
│
├─ .gitignore
└─ REDME.md

00_tools_summary           # Overview + linting/formatting/type hints
01_git
02_github                  # Potrebbe includere cenni a GitHub Actions
03_venv
04_debugger
05_gestione_errori         # Potrebbe includere sezione su logging
06_testing                 # ← NUOVO (pytest)
07_pyproject
08_docker
09_numpy
10_pandas
11_matplotlib
12_jupyter                 # ← NUOVO (se rilevante)
```

## Set-Up
Per svolgere questo modulo è vivamente consigliabile installare sul proprio pc personale i seguenti software:
- [**Visual Studio Code**](https://code.visualstudio.com/)
- [**Python**](https://www.python.org/)
- [**Git**](https://git-scm.com/)

Una volta installato Visual Studio Code è possibile verificare se *python* e *git* sono corretamente installati scrivendo nel terminale i seguenti comandi che stampano le rispettive versioni

```bash
python --version
git --version
```