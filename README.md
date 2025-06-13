# BLiP ExecuteScript Analyzer

Analisador visual de scripts ExecuteScript de fluxos BLiP usando GPT-4o (OpenAI) via Streamlit Cloud.

## Funcionalidades

- Upload de arquivo JSON de fluxo BLiP.
- Lista todos os scripts `ExecuteScript` de entrada/saída.
- Analisa qualquer script selecionado usando o modelo GPT-4o.
- Interface simples, acessível pelo navegador.

## Deploy e uso local

```bash
git clone https://github.com/seu-usuario/blip-executescript-analyzer.git
cd blip-executescript-analyzer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy no Streamlit Cloud

1. Suba o repositório no GitHub.
2. Conecte no Streamlit Cloud.
3. Defina a variável OPENAI_API_KEY.
