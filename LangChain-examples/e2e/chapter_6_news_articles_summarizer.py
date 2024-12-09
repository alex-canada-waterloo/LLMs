from newspaper import Article
from langchain.schema import HumanMessage
from langchain_openai import ChatOpenAI

def fetch_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article

def prepare_prompt(article):
    template = f"Summarize the following article: {article.title}\n\n{article.text}\n\nrespond in 100 tokens or less."
    return template.format(article_title=article.title, article_text=article.text)

def generate_summary(prompt):
    messages = [HumanMessage(content=prompt, max_tokens=300)]
    chat = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5, max_tokens=100)
    summary = chat.invoke(messages)
    return summary

def print_summary(summary):
    print("Summary:")
    for line in summary.content.split('\n'):
        while len(line) > 80:
            space_index = line.rfind(' ', 0, 80)
            if space_index == -1:
                space_index = 80
            print(line[:space_index])
            line = line[space_index:].strip()
        print(line)


if __name__ == "__main__":
    article_document = fetch_article('https://www.cbc.ca/news/canada/toronto/ai-art-apology-1.7403921')
    prompt = prepare_prompt(article_document)
    article_summary = generate_summary(prompt)
    print_summary(article_summary)