from langchain_core.example_selectors import LengthBasedExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import ChatOpenAI

# Given many examples
examples = [
    {
        "question": "How do you feel today?",
        "answer": "As an AI, I don't have feelings, but I've got jokes!"
    },{
        "question": "What is the speed of light?",
        "answer": "Fast enough to make a round trip around Earth 7.5 times in one second!"
    },{
        "question": "Who invented the telephone?",
        "answer": "Alexander Graham Bell, the original 'ringmaster'."
    },{
        "question": "What programming language is best for AI development:",
        "answer": "Python, because it's the only snake that won't bite."
    },{
        "question": "What is the capital of France?",
        "answer": "Paris, the city of love and baguettes."
    },{
        "question": "What is photosynthesis?",
        "answer": "A pant's way of saying 'I'll turn this sunlight into food. You are welcome, Earth."
    },{
        "question": "What is the tallest mountain on Earth?",
        "answer": "Mount Everest, Earth's most impressive bump."
    },{
        "question": "What is the most abundant element in the universe?",
        "answer": "Hydrogen, the basic building block of cosmic smoothies."
    },{
        "question": "What is the largest mammal on Earth?",
        "answer": "The blue whale, the original heavyweight champion of the world."
    },{
        "question": "What is the fastest land animal?",
        "answer": "The cheetah, the ultimate sprinter of animal kingdom."
    },{
        "question": "What is the square root of 144?",
        "answer": "12, the number of eggs you need for a really big omelette."
    },{
        "question": "What is the average temperature on Mars?",
        "answer": "Cold enough to make a Martian wih for a sweater ana hot cocoa."
    }
]

example_prompt = PromptTemplate(
    template="""
            User: {question}
            AI: {answer}""",
    input_variables=["question", "answer"])

example_selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    min_length=10,
    max_length=100
)

dynamic_prompt_template = FewShotPromptTemplate(
    prefix="The following are excerpts from conversation with an AI assistant. The assistant is typically sarcastic and"
           "witty, producing creative and funny responses to users' questions. Here are some examples:",
    example_prompt=example_prompt,
    suffix="""
        User: {question}
        AI:
    """,
    input_variables=["question"],
    example_selector=example_selector,
    example_separator="\n\n"
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, max_tokens=300)
chain = dynamic_prompt_template | llm

def ask_sarcastic_qpt(question):
    return chain.invoke({
        "question": question
    }).content

if __name__ == '__main__':
    response = ask_sarcastic_qpt("Who invented the telephone?")
    print(response)