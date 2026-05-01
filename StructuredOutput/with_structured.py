from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Review(TypedDict):
    summary:Annotated[str,"A brief summary of the review"]
    sentiment:Annotated[str,"from the review give its sentiment as positive,negative,neutral"]
    name:Annotated[Optional[str],"Write the name of the reviewer"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.
                                 By Aditya Sharma""")

print(result)