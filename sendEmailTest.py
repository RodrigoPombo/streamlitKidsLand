import streamlit as st
import datetime
import smtplib
from streamlit_image_select import image_select
import time
import ssl
from email.message import EmailMessage

choice=st.sidebar.selectbox('Menu',('BookNow',"BookNow"))

st.sidebar.image("448213819_797363309157234_5793914166563067226_n.jpg")

if(choice=='BookNow'):
    placeholder = st.empty()

    if 'button1_pressed' not in st.session_state:
        st.session_state['button1_pressed'] = 1

    def next_page():
        placeholder.empty()
        st.session_state['button1_pressed'] += 1
        time.sleep(3)
        email_sender = 'kidslandinsuflaveis@gmail.com'
        email_password = str(st.secrets["keygmail"])
        email_receiver = 'kidslandinsuflaveis@gmail.com'
        subject = 'Check out my new video!'
        body = """Aluguer chegou!
                  Morada: """ + str(Morada_) + """ \n Data: """ + str(data)  + """ \n Nome: """ + str(nome) + """ \n Contacto: """ + str(contacto)

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

    with st.empty():
        if (st.session_state['button1_pressed']) == 1:
            with st.container():
                placeholder.empty()
                st.title('Bem-vindo à KidsLand, onde pode alugar os melhores insufláveis!')
                img = image_select(
                    label="Selecione o seu insuflável favorito!",
                    images=[
                        "elephant.jpg",
                        "colorido75.jpg",
                        "trampolim.jpeg"
                    ],
                    captions=["Elefante", "Colorido", "Trampolim"],
                    return_value="index"
                )
                print("IMAGE: " + str(img))
                global data
                global Morada_
                global nome
                global contacto
                data = st.date_input("Data da reserva: ", datetime.date(2024, 1, 1))
                Morada_ = st.text_input("Morada: ", "")
                nome = st.text_input("Nome: ", "")
                contacto = st.text_input("Contacto: ", "")
                st.button("Click me for booking", on_click=next_page)
        if (st.session_state['button1_pressed']) == 2:
            with st.container():
                placeholder.empty()
                st.title("Obrigado pela Reserva! Enviaremos a confirmacão nas próximas 24 horas!")
