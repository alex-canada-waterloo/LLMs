from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

dynamic_prompt = FewShotPromptTemplate(
    prefix="The following are excerpts from conversation with an AI assistant. The assistant is typically sarcastic and"
           "witty, producing creative and funny responses to users' questions. Here are some examples:",
    example_prompt=PromptTemplate(
        template="""
            User: {question}
            AI: {answer}""",
        input_variables=["question", "answer"]),
    suffix="""
        User: {question}
        AI:
    """,
    input_variables=["question"],
    examples=[
        {
            "question": "How do I become a better programmer?",
            "answer": "Try talking to a rubber duck; it works wonders."
        }, {
            "question": "Why the sky is blue?",
            "answer": "It's nature's way of preventing eye strain."
        },
    ],
    example_separator="\n\n"
)

"""
Example of dynamic_template.invoke({"question": "???"}):
The following are excerpts from conversation with an AI assistant. The assistant is typically sarcastic andwitty, producing creative and funny responses to users' questions. Here are some examples:


            User: How do I become a better programmer?
            AI: Try talking to a rubber duck; it works wonders.


            User: Why the sky is blue?
            AI: It's nature's way of preventing eye strain.


        User: ???
        AI:
"""

# Init LLM and a chain
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, max_tokens=300)
chain = dynamic_prompt | llm

def ask_sarcastic_gpt_question(question):
    return chain.invoke({
        "question": question
    }).content

if __name__ == '__main__':
    response = ask_sarcastic_gpt_question("How can I learn quantum computing?")
    print(response)

