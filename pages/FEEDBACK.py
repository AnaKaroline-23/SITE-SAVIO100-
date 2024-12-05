import streamlit as st

# Inicializando os feedbacks no session_state
if "feedbacks" not in st.session_state:
    st.session_state.feedbacks = []

# Função para mostrar o feedback existente
def show_feedbacks():
    if st.session_state.feedbacks:
        st.subheader("Feedbacks Anteriores:")
        for feedback in st.session_state.feedbacks:
            st.write(f"Classificação: {feedback['rating']} estrelas")
            st.write(f"Comentários: {feedback['comments']}")
            st.write(f"Data: {feedback['date']}")
            st.write("---")
    else:
        st.write("Nenhum feedback registrado ainda.")

# Título da página
st.title("Deixe seu Feedback")

# Exibição dos feedbacks existentes
show_feedbacks()

# Formulário para o feedback
st.subheader("Novo Feedback")

# Campo de classificação em estrelas (1 a 5)
rating = st.slider("Qual sua classificação para o sistema?", 1, 5, 3)

# Campo de comentários
comments = st.text_area("Deixe seu comentário sobre o sistema")

# Campo de data
from datetime import date
today = date.today()
feedback_date = today.strftime("%d/%m/%Y")

# Botão para enviar o feedback
if st.button("Enviar Feedback"):
    if comments:
        # Adicionando o feedback ao session_state
        st.session_state.feedbacks.append({"rating": rating, "comments": comments, "date": feedback_date})
        st.success("Obrigado pelo seu feedback!")
        # Limpa os campos após enviar
        st.experimental_rerun()
    else:
        st.warning("Por favor, insira um comentário.")

# Definindo o CSS para mudar a fonte
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Georgia', serif;
        }
    </style>
""", unsafe_allow_html=True)

# Função para converter imagem para Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    return encoded_string

#imagem
import streamlit as st
import base64

# Função para converter imagem para Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    return encoded_string

# Caminho da imagem local
image_path = "imgs/Design sem nome (1).jpg" 

 # Substitua com o caminho da sua imagem
image_base64 = image_to_base64(image_path)

# Adicionar a imagem Base64 como fundo com CSS
st.markdown(f"""
    <style>
        .stApp{{
            background-image: url('data:image/jpeg;base64,{image_base64}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            height: 100vh;  /* Garante que o fundo ocupe toda a tela */
            margin: 0;
        }}
    </style>
""", unsafe_allow_html=True)

# imagem barra 
st.sidebar.image("imgs/ESTUDIO-removebg-preview.png")
import streamlit as st