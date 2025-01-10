from langchain.text_splitter import HTMLHeaderTextSplitter

# Configuration
splitter = HTMLHeaderTextSplitter([
    ("h1", "Header 1"),
    ("h2", "Header 2")
])

# Function to print the chunks
def print_chunks(chunks):
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:")
        if chunk.metadata:
            if 'Header 1' in chunk.metadata:
                print(f"Header 1: {chunk.metadata['Header 1']}")
            if 'Header 2' in chunk.metadata:
                print(f"Header 2: {chunk.metadata['Header 2']}")
        print(f"Page Content:\n{chunk.page_content[:100]}\n...\n{chunk.page_content[-100:]}")
        print("")



if __name__ == "__main__":
    with open("../web_crawler/links.txt", "r") as file:
        urls = [line.strip() for line in file.readlines()]

    for url in urls[:5]:
        chunks = splitter.split_text_from_url(url)
        print_chunks(chunks)