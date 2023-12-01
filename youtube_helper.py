from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()


def create_vector_db_from_youtube_Url(video_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)
    # return docs
    return db

# print(create_vector_db_from_youtube_Url(video_url))

def get_response_from_query(db, query, k=4):
    # text-davinici can handle 4097 tokens

    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    llm = OpenAI(model="text-davinci-003")

    prompt = PromptTemplate(
        input_variables = ["question", "docs"],
        template = """
                You are a helpful YouTube assistant that can answer questions about videos based on the video's transcript.

                Answer the following question: {question}
                By searching the following video transcript: {docs}

                Only use factual information from the transcript to answer the question.
                If you feel you don't have enough inforamtion to answer the question say "I don't know".

                Your answers should be detailed.
                """,
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(question=query, docs=docs_page_content)
    response = response.replace("\n", "")
    return response




