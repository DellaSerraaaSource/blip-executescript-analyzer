🔐 1. Reanalisar a lógica de inserção da chave da OpenAI

Permitir salvar a chave via session state após primeira inserção.

Validar a chave ao inserir e exibir erro caso esteja inválida.

    Evitar que o usuário precise reescrever a chave toda vez.

🔁 2. Corrigir a lógica de fluxo: leitura → seleção → análise

Ajustar o fluxo para que a análise ocorra após a seleção correta do script, não antes.

Garantir que o script seja realmente enviado para a LLM.

    Adicionar verificação de conteúdo vazio ou malformado no script antes de enviar.

🔄 3. Melhorar a experiência de uso: escolha entre ações de entrada ou saída

Incluir um selectbox ou radio com:

    [ ] Apenas entrada

    [ ] Apenas saída

    [x] Todas

Enviar todos os scripts de uma vez para o LLM quando selecionado (modo batch).

    Tratar o prompt para aceitar múltiplos scripts e formatar bem a resposta.

🧩 4. Modularizar o código

Criar uma pasta modules/ com:

    llm_client.py: responsável pela chamada ao GPT.

    extractor.py: responsável pela extração dos scripts.

    interface.py: funções auxiliares para o front.

    Separar o carregamento de JSON do layout principal do Streamlit.

🎨 5. Melhorar o layout da interface

Adicionar título e descrição no topo com markdown elegante.

Usar columns para separar visualização de script e resposta.

Adicionar contadores e estatísticas (ex: X scripts encontrados).

Adicionar loading progress ao fazer análise de múltiplos scripts.

    Aplicar tema customizado via .streamlit/config.toml (ex: modo escuro, cor primária, etc).

🚀 Sugestão de extra

Adicionar botão para exportar resultado da análise em .txt ou .md.

Permitir múltiplas análises com histórico visível.

Habilitar logs e debug com st.expander("Logs").
