from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

dynamic_prompt = FewShotPromptTemplate(
    prefix="Identify the habitat of given animal",
    example_prompt=PromptTemplate(
        template="""
            Animal: {animal}
            Habitat: {habitat}""",
        input_variables=["animal", "habitat"]),
    suffix="Animal: {animal}/nHabitat:",
    input_variables=["animal"],
    examples=[
        {"animal": "lion", "habitat": "savannah"},
        {"animal": "polar bear", "habitat": "Arctic"},
        {"animal": "elephant", "habitat": "African grasslands"}
    ],
    example_separator="\n\n"
)

# Init LLM and a chain
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, max_tokens=300)
chain = dynamic_prompt | llm

def ask_gpt_animal_habitat(animal):
    return chain.invoke({
        "animal": animal
    }).content

if __name__ == '__main__':
    question = "tiger"
    response = ask_gpt_animal_habitat(question)
    print(response)

