
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Define the template
prompt_template = PromptTemplate(
    input_variables=["query"],
    template="""
    Answer the question based on the context below. If the question cannot be answered using
    the information provided, answer with "I don't know".
    Context: Quantum computing is an emerging field that leverages quantum mechanics to solve complex problems
    faste than classical computers.
    ...
    Question: {query}
    Answer:
"""
)

# Init LLM and a chain
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5, max_tokens=300)
chain = prompt_template | llm

def ask_gpt(query):
    return chain.invoke({
        "query": query
    })


if __name__ == '__main__':
    question = 'What is the main advantage of quantum computing over classical computing?'
    response = ask_gpt(question)

    print("Question:", question)
    print("Answer:", response)
