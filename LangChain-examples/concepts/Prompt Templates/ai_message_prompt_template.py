from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate)
from langchain_openai import ChatOpenAI

chat_prompt_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are helpful assistant that translates english to pirate language."),
    HumanMessagePromptTemplate.from_template("Hi"),
    AIMessagePromptTemplate.from_template("Argh me mateys"),
    HumanMessagePromptTemplate.from_template("{prompt}")])

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, max_tokens=300)
chain = chat_prompt_template | llm

def ask_pirate_english(prompt):
    return chain.invoke({
        "prompt": prompt
    }).content

if __name__ == '__main__':
    response = ask_pirate_english("How are you?")
    print(response)