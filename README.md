# comunicacao-segura

# Comunicação Segura com Streamlit 🔐

Este projeto simula uma comunicação segura entre duas partes usando algoritmos de criptografia (DES, AES e RSA). O usuário insere um texto plano que é criptografado em uma aplicação e, em outra ponta, é descriptografado usando os dados apropriados.

## Arquivos
- `criptografia.py` — Interface para criptografar texto.
- `descriptografia.py` — Interface para descriptografar texto.
- `funcoes_criptografadas.py` — Funções que implementam os algoritmos.
- `mensagem_temp.json` — Arquivo intermediário de troca de dados.
- `registro_comunicacao.txt` — (opcional) arquivo de log das interações.

## Requisitos
- Python 3.8+
- Instalar dependências:
```bash

pip install pycryptodome streamlit

## Como usar

1. Acesse `criptografia.py` para digitar a mensagem e obter o texto criptografado.
2. Acesse `descriptografia.py` para colar a criptografia e descriptografar.
3. As informações são registradas em `registro_comunicacao.txt`.

## Executando localmente

```bash
streamlit run criptografia.py
# Em outro terminal:
streamlit run descriptografia.py

