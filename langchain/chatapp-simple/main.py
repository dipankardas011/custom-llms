from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOllama
from langchain.schema import HumanMessage, AIMessage, SystemMessage, BaseMessage

class Chat:
    def __init__(self, specialisation: str):
        self.Chat_model = ChatOllama(callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
        self.Messages: list[BaseMessage] = [SystemMessage(content=specialisation)]

    def Send(self, text: str):
        self.Messages.append(HumanMessage(content=text))
        print(">>>> USER")
        print(text)

        print(">>>> AI")
        aiOutput = self.Chat_model(self.Messages)
        self.Messages.append(AIMessage(content=str(aiOutput)))

        print("\n========")


    def ChatPromptHuman(self)-> str:
        return input("Enter your prompt / [STOP] to terminate> ")

# Example usage:
chat_instance = Chat(specialisation="You are brillant in remembering numbers")

while True:
    inp = chat_instance.ChatPromptHuman()
    if inp == "STOP":
        break

    chat_instance.Send(inp)

