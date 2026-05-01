from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel,Field
from typing import Optional,Literal
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model ="gemini-2.5-flash")

class Review(BaseModel):
    summary: str = Field(description="A brief summary of review")
    sentiment:Literal['pos','neg'] = Field(description="Return sentiment of the review either positive, negative or neutral")

    name: Optional[str] = Field(default=None,description="Return the name of the reviewer")

structured_model = model.with_structured_output(Review)

response = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.
                                 """)
print(response)