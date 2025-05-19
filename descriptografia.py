import streamlit as st
import time
import funcoes_criptografadas as cu
import json
import os

st.title("🔓 Aplicativo de Descriptografia")

# Lê os dados
with open("mensagem_temp.json", "r", encoding="utf-8") as temp_file:
    temp_data = json.load(temp_file)

default_cipher = temp_data.get("cipher_text", "")
default_algorithm = temp_data.get("algorithm", "DES")
original_message = temp_data.get("original_message", "")

if default_algorithm == "RSA":
    default_key = temp_data.get("private_key", "")
else:
    default_key = temp_data.get("key", "")
    default_iv = temp_data.get("iv", "")

# Interface de entrada
cipher_text = st.text_area("Texto criptografado:", value=default_cipher)
key = st.text_area("Chave:", value=default_key)
iv = st.text_area("IV:", value=default_iv if default_algorithm != "RSA" else "", disabled=(default_algorithm == "RSA"))
algorithm = st.selectbox("Escolha o algoritmo:", ["DES", "AES", "RSA"],
                         index=["DES", "AES", "RSA"].index(default_algorithm))

if st.button("Descriptografar"):
    try:
        start = time.time()
        if algorithm == "DES":
            message = cu.decrypt_des(cipher_text, key, iv)
        elif algorithm == "AES":
            message = cu.decrypt_aes(cipher_text, key, iv)
        elif algorithm == "RSA":
            message = cu.decrypt_rsa(cipher_text, key)
        
        end = time.time()
        
        st.success("Texto decifrado com sucesso:")
        st.code(message, language='text')
        st.write(f"⏱️ Tempo de descriptografia: {end - start:.4f} segundos")

        # Registro completo
        with open("registro_comunicacao.txt", "a", encoding="utf-8") as f:
            f.write("======== DESCRIPTOGRAFIA RECEBIDA ========\n")
            f.write(f"Algoritmo: {algorithm}\n")
            f.write(f"Mensagem criptografada: {cipher_text}\n")
            f.write(f"Chave usada: {key}\n")
            f.write(f"Mensagem descriptografada: {message}\n")
            f.write(f"Mensagem original esperada: {original_message}\n")
            f.write("==========================================\n\n")

    except Exception as e:
        st.error(f"Erro ao descriptografar: {e}")
