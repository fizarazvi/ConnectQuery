from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import google_palm
from langchain_google_genai import ChatGoogleGenerativeAI

from agents.linkedin_lookup_agent import lookup
from third_parties.linkedin import scrape_linkedin_data
from output_parsers import summary_parser

import os
import sys

def connect_query(name: str):
    linkedin_url = lookup(name)
    information = scrape_linkedin_data(linkedin_url, True)
    summary_template = """
        given the information {information} about a person I want you to create:
        1. Short summary
        2. two interesting fact about them
        \n {format_instructions}
    """

    # information should be passed to the chain, here we just provide what vairable to look for
    summary_prompt_template = PromptTemplate(input_variables=['information'], 
                                             template=summary_template, 
                                             partial_variables={"format_instructions":summary_parser.get_format_instructions()})

    #temperature defines the creativity of the mode
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

    chain = summary_prompt_template | llm | summary_parser

    res = chain.invoke(input={"information":information}, )

    print(res)



if __name__=='__main__':
    print("Hello LangChain!")
    connect_query("Mustafa Suleyman")