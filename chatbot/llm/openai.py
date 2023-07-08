from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI()  # type: ignore

conversation = ConversationChain(llm=chat)
