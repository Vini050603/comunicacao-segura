import streamlit as st
import time
import funcoes_criptografadas as cu
import json

st.title("🔐 Aplicativo de Criptografia")

message = st.text_area("Digite o texto em claro:")
algorithm = st.selectbox("Escolha o algoritmo:", ["DES", "AES", "RSA"])

if st.button("Criptografar"):
    if not message.strip():
        st.warning("Digite uma mensagem para criptografar.")
    else:
        start = time.time()
        if algorithm == "DES":
            cipher_text, key, iv = cu.encrypt_des(message)
        elif algorithm == "AES":
            cipher_text, key, iv = cu.encrypt_aes(message)
        elif algorithm == "RSA":
            cipher_text, public_key, private_key = cu.encrypt_rsa(message)

        # Exibe resultado
        st.success("Texto criptografado com sucesso!")
        st.code(cipher_text, language='text')

        if algorithm == "RSA":
            st.text("🔑 Chave pública (para criptografar):")
            st.code(public_key, language='text')
            st.text("🔐 Chave privada (para descriptografar):")
            st.code(private_key, language='text')
        else:
            st.text("🔑 Chave secreta:")
            st.code(key, language='text')
            st.text("🔁 Vetor de Inicialização (IV):")
            st.code(iv, language='text')

        # Armazena no session_state e em arquivo
        temp_data = {
            "cipher_text": cipher_text,
            "algorithm": algorithm,
            "original_message": message
        }

        if algorithm == "RSA":
            temp_data["public_key"] = public_key
            temp_data["private_key"] = private_key
        else:
            temp_data["key"] = key
            temp_data["iv"] = iv

        with open("mensagem_temp.json", "w", encoding="utf-8") as temp_file:
            json.dump(temp_data, temp_file)
