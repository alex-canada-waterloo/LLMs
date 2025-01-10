from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

prompt_template = PromptTemplate.from_template("What is a word to replace the following: {word}?")

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

llm_chain = prompt_template | llm

def run_chain(world):
    return llm_chain.invoke({"word": world}).content

if __name__ == "__main__":
    print(run_chain("artificial"))

