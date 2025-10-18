from langchain_openai import OpenAI #or open-sources on huggingface
from dotenv import load_dotenv

load_dotenv()

def generate_name():

    llm = OpenAI(temperature=0.5) #config
    name = llm.invoke("generate a name for a person, five exmaples") #prompt

    return name

if __name__ == "__main__":
    print(generate_name())