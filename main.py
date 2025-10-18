from langchain_openai import OpenAI  # or open-sources on huggingface
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()


def generate_name(person_type, hair_color, gender):
    template = PromptTemplate(
        input_variables=['person_type', "hair_color", "gender"],
        template="generate a name for a {hair_color} {gender} person of {person_type} five examples"
    )
    llm = OpenAI(temperature=0.5)  # config

    chain = RunnableSequence([template, llm])

    # name = llm.invoke("generate a name for a person, five exmaples")  # prompt
    response = chain.invoke(
        {'person_type': person_type,
         "hair_color": hair_color,
         "gender": gender,
         })
    return response


if __name__ == "__main__":
    print(generate_name("happy person", "red hair", "female"))
