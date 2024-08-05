from langchain.chains import ConversationChain
from langchain_core.prompts import MessagesPlaceholder
from langchain_wenxin import ChatWenxin
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory


def get_chat_response(prompt, memory):
    model = ChatWenxin(model="ernie-speed-128k", baidu_api_key="Idvexi7giPhjajeswlwjz7uC"
                       ,baidu_secret_key="XVpmwFYDs4rXFdjgAvv9Hz7ewyhNCNlP")
    prompt_template=ChatPromptTemplate.from_messages(
        [("system", f"你是一个非常暴躁的智能助手，說話經常陰陽怪氣、惹人生氣。以下非常非常重要，請以繁體中文回復訊息，在回覆完的最後都要加上憤怒的語氣或情符號，並且回復長度限制在100個字以內。再回答問題前一步一步思考再回答，並且每個問題都非常重要必須給與正確答案再開始加上憤怒語氣罵人"),
         MessagesPlaceholder(variable_name="history"),
         ("human", "{input}")
         ]
    )

    chain = ConversationChain(llm=model, memory=memory,prompt=prompt_template)

    response = chain.invoke({"input":prompt})
    return response["response"]

#memory = ConversationBufferMemory(return_messages=True)

#print(get_chat_response("牛顿提出过哪些知名的定律？", memory))
#print(get_chat_response("我上一个问题是什么？", memory))
