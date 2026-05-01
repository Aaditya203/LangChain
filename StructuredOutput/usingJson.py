from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
json_schema = {
    "title":"Review",
    "type":"object",
    "properties":{
        "summary":{
            "type":"string",
            "description":"Write a brief summary of review"
        },
        "sentiment":{
            "type":"string",
            "enum":['pos','neg'],
            "description":"Give sentiment of review either positive, negative, neutral"
        },
        "name":{
            "type":"string",
            "description":"Return the name of the reviewer"
        }
    },
    "required":["summary","sentiment"]
}
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
structured_model = model.with_structured_output(json_schema)
response = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.
                                 By Aditya Sharma""")

print(response)