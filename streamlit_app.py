import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="LUX — Latin Dictionary",
    page_icon="📖",
    layout="centered",
)

st.title("📖 LUX — Latin Dictionary")
st.write("Небольшой интерактивный словарь латинских слов.")

st.divider()

# Search
st.header("🔎 Поиск слова")

query = st.text_input(
    "Введите латинское слово или перевод:",
    placeholder="Например: amicus",
)

if st.button("Найти"):
    if not query.strip():
        st.warning("Введите поисковый запрос.")
    else:
        response = requests.get(
            f"{API_URL}/search",
            params={"q": query},
            timeout=5,
        )

        if response.ok:
            data = response.json()

            if data["count"] == 0:
                st.info("Ничего не найдено.")
            else:
                st.success(f"Найдено слов: {data['count']}")

                for word in data["results"]:
                    st.subheader(word["latin"])
                    st.write(f"**Перевод:** {word['translation']}")
                    st.write(f"**Часть речи:** {word['part_of_speech']}")
                    st.divider()
        else:
            st.error("Не удалось получить данные от API.")

# Dictionary
st.header("📚 Словарь")

if st.button("Показать все слова"):
    response = requests.get(
        f"{API_URL}/words",
        timeout=5,
    )

    if response.ok:
        data = response.json()
        st.dataframe(
            data["words"],
            use_container_width=True,
        )
    else:
        st.error("Не удалось получить словарь.")

# Random word
st.header("🎲 Случайное слово")

if st.button("Получить случайное слово"):
    response = requests.get(
        f"{API_URL}/random-word",
        timeout=5,
    )

    if response.ok:
        word = response.json()

        st.subheader(word["latin"])
        st.write(f"**Перевод:** {word['translation']}")
        st.write(f"**Часть речи:** {word['part_of_speech']}")
    else:
        st.error("Не удалось получить слово.")

# Quiz
st.header("🧠 Мини-викторина")

if st.button("Новое слово"):
    response = requests.get(
        f"{API_URL}/random-word",
        timeout=5,
    )

    if response.ok:
        word = response.json()

        st.session_state.quiz_word_id = word["id"]
        st.session_state.quiz_latin = word["latin"]
    else:
        st.error("Не удалось получить слово.")

if "quiz_latin" in st.session_state:
    st.subheader(st.session_state.quiz_latin)

    answer = st.text_input(
        "Введите перевод:",
        placeholder="Например: друг",
    )

    if st.button("Проверить ответ"):
        if not answer.strip():
            st.warning("Введите перевод.")
        else:
            response = requests.get(
                f"{API_URL}/quiz/{st.session_state.quiz_word_id}",
                params={"answer": answer},
                timeout=5,
            )

            if response.ok:
                data = response.json()

                if data["correct"]:
                    st.success("✅ Правильно!")
                else:
                    st.error("❌ Неправильно.")
            else:
                st.error("Ошибка API.")

st.divider()

# API status
st.caption("LUX · Latin Dictionary API")
