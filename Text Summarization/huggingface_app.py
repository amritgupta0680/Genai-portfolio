import validators
import streamlit as st

from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain_huggingface import HuggingFaceEndpoint
from langchain.text_splitter import RecursiveCharacterTextSplitter


# ---------------- STREAMLIT ----------------
st.set_page_config(page_title="YT/Web Summarizer", page_icon="🦜")

st.title("🦜 Summarize YouTube or Website")
st.subheader("Paste a URL below")


# ---------------- INPUT ----------------
with st.sidebar:
    hf_api_key = st.text_input("HuggingFace API Token", type="password")

url = st.text_input("Enter URL")


# ---------------- PROMPT ----------------
prompt = PromptTemplate(
    template="Summarize the following content in about 300 words:\n{text}",
    input_variables=["text"]
)


# ---------------- BUTTON ----------------
if st.button("Summarize"):

    if not hf_api_key or not url:
        st.error("Please enter API key and URL")
        st.stop()

    if not validators.url(url):
        st.error("Please enter a valid URL")
        st.stop()

    try:
        with st.spinner("Loading content..."):

            docs = None

            # -------- YOUTUBE --------
            if "youtube.com" in url or "youtu.be" in url:
                try:
                    loader = YoutubeLoader.from_youtube_url(
                        url,
                        add_video_info=True,
                        language=["en"],
                        translation="en"
                    )
                    docs = loader.load()

                    if not docs:
                        raise Exception("Empty transcript")

                except Exception:
                    st.warning("⚠️ Transcript not available. Trying fallback...")

            # -------- FALLBACK --------
            if docs is None:
                loader = UnstructuredURLLoader(
                    urls=[url],
                    ssl_verify=False
                )
                docs = loader.load()

            # ❌ If still empty → stop
            if not docs or all(len(doc.page_content.strip()) == 0 for doc in docs):
                st.error("❌ No content could be extracted from this URL")
                st.stop()

            # -------- SPLIT TEXT --------
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=2000,
                chunk_overlap=200
            )
            docs = splitter.split_documents(docs)

        with st.spinner("Generating summary..."):

            # ✅ FIXED HuggingFace LLM
            llm = HuggingFaceEndpoint(
                repo_id="HuggingFaceH4/zephyr-7b-beta",
                task="text-generation",
                max_new_tokens=300,
                temperature=0.3,
                huggingfacehub_api_token=hf_api_key.strip()
            )

            chain = load_summarize_chain(
                llm,
                chain_type="stuff",
                prompt=prompt
            )

            summary = chain.run(docs)

            # ❌ Handle empty output
            if not summary.strip():
                st.warning("⚠️ Model could not generate a summary")
            else:
                st.success("✅ Summary Generated")
                st.write(summary)

    except Exception as e:
        st.error(f"Error: {e}")