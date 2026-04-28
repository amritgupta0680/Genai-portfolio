import validators
import streamlit as st

from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


st.set_page_config(page_title="YT/Web Summarizer", page_icon="🦜")
st.title("🦜 Summarize YouTube or Website")

with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", type="password")

url = st.text_input("Enter URL")


prompt = PromptTemplate(
    template="Summarize the following content in 300 words:\n{text}",
    input_variables=["text"]
)


if st.button("Summarize"):

    if not groq_api_key or not url:
        st.error("Please provide API key and URL")
        st.stop()

    if not validators.url(url):
        st.error("Invalid URL")
        st.stop()

    try:
        with st.spinner("Loading content..."):

            docs = None

            # -------- TRY YOUTUBE LOADER --------
            if "youtube.com" in url or "youtu.be" in url:
                try:
                    loader = YoutubeLoader.from_youtube_url(
                        url,
                        add_video_info=True,
                        language=["en"],
                        translation="en"
                    )
                    docs = loader.load()

                except Exception:
                    st.warning("⚠️ Transcript not available. Trying fallback...")

            # -------- FALLBACK TO WEBSITE SCRAPING --------
            if docs is None:
                loader = UnstructuredURLLoader(
                    urls=[url],
                    ssl_verify=False
                )
                docs = loader.load()

            # -------- SPLIT --------
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=2000,
                chunk_overlap=200
            )
            docs = splitter.split_documents(docs)

        with st.spinner("Generating summary..."):

            llm = ChatGroq(
                model_name="llama-3.3-70b-versatile",
                groq_api_key=groq_api_key
            )

            chain = load_summarize_chain(
                llm,
                chain_type="stuff",
                prompt=prompt
            )

            summary = chain.run(docs)

            st.success("✅ Summary Generated")
            st.write(summary)

    except Exception as e:
        st.error(f"Error: {e}")