from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(streaming=True)  # type: ignore

conversation = ConversationChain(llm=chat, verbose=True)
