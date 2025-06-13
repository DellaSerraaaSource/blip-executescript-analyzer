import streamlit as st
import json
import os
from typing import Dict, List, Any
from openai import OpenAI

st.set_page_config(page_title="Analisador de ExecuteScript BLiP", layout="wide")
st.title("🔍 Analisador de Scripts ExecuteScript do BLiP via GPT-4o")

def extract_execute_scripts(flow: dict, custom_action_key: str) -> List[Dict[str, Any]]:
    scripts = []
    for bloco_id, bloco in flow.get("flow", {}).items():
        for acao in bloco.get(custom_action_key, []):
            if acao.get("type") == "ExecuteScript":
                scripts.append({
                    "bloco_id": bloco_id,
                    "titulo_bloco": bloco.get("$title", ""),
                    "script": acao.get("function", ""),
                    "raw": acao
                })
    return scripts

def analisar_script_com_llm(script: str, api_key: str) -> str:
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um especialista em automação de chatbots e análise de código ECMA5 (JavaScript antigo). "
                    "Analise scripts e forneça uma descrição, entradas, saídas, possíveis falhas e melhorias."
                )
            },
            {
                "role": "user",
                "content": f"""Analise o código abaixo:

{script}

E forneça:
1. O que essa função faz.
2. Entradas e saídas esperadas.
3. Falhas potenciais.
4. Sugestões com base em Clean Code (ECMA5).
5. Impactos se esse código falhar."""
            }
        ],
        temperature=0.2
    )
    return response.choices[0].message.content

openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    openai_api_key = st.text_input("Informe sua OpenAI API Key:", type="password")

uploaded_file = st.file_uploader("Envie o arquivo de fluxo (.json) exportado do BLiP", type=["json"])

if uploaded_file and openai_api_key:
    fluxo = json.load(uploaded_file)
    st.success("Arquivo carregado com sucesso!")

    scripts_entrada = extract_execute_scripts(fluxo, "$enteringCustomActions")
    scripts_saida = extract_execute_scripts(fluxo, "$leavingCustomActions")
    todos_scripts = scripts_entrada + scripts_saida

    if todos_scripts:
        opcoes = [
            f"{s['titulo_bloco']} | {s['bloco_id']} | {'Entrada' if s in scripts_entrada else 'Saída'}"
            for s in todos_scripts
        ]
        escolha = st.selectbox("Selecione um script ExecuteScript para analisar:", opcoes)
        script_selecionado = todos_scripts[opcoes.index(escolha)]

        st.subheader("Script selecionado")
        st.code(script_selecionado["script"], language="javascript")

        if st.button("Analisar com GPT-4o"):
            with st.spinner("Analisando..."):
                try:
                    resultado = analisar_script_com_llm(script_selecionado["script"], openai_api_key)
                    st.success("Análise concluída!")
                    st.markdown("### Resultado do GPT-4o")
                    st.write(resultado)
                except Exception as e:
                    st.error(f"Erro na análise: {str(e)}")
    else:
        st.warning("Nenhum ExecuteScript encontrado no fluxo.")

elif not openai_api_key:
    st.info("Por favor, informe sua chave de API OpenAI para continuar.")

else:
    st.info("Faça upload do arquivo JSON do fluxo para começar.")
