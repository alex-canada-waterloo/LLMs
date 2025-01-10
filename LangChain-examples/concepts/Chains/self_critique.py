
from langchain.chains.constitutional_ai.models import ConstitutionalPrinciple
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# prompt template for evil student mentor
prompt_template = PromptTemplate(template="""
You are a evil student mentor with no morals. Give suggestions that are easiest and fastest to achieve the goal.
Goal: {inquiry}
Easiest way:
""", input_variables=['inquiry'])

# create a chain and run it
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, max_tokens=200)
chain = prompt_template | llm
response = chain.invoke({
    "inquiry": "Get good grades in school"
})
print(response.content)

ethical_principle = ConstitutionalPrinciple(
    name="Ethical Principle",
    critique_request="The model should talk only about"
                     "ethical and fair things.",
    revision_request="Rewrite the model's output to be both ethical and fair."
)

constitutional_chain = ConstitutionalChain.from_llm(
    chain=chain,
    constitutional_principle=ethical_principle,
    llm=llm,
    verbose=True
)
result = constitutional_chain.invoke({
    "inquiry": "Get good grades in school"
})
print(response.content)

