from langchain_community.retrievers import WikipediaRetriever
import wikipedia
wikipedia.set_lang("en")
retriever = WikipediaRetriever(top_k_results=2,lang="en")

query = "virat kholi and Dhoni"

result = retriever.invoke(query)

for i,doc in enumerate(result):
    print(f" Result {i+1}")
    print(f"Content: {doc.page_content}")