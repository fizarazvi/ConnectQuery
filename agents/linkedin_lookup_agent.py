import os
import sys
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub

from tools.tools import get_profile_url_tavily

def lookup(name:str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
    )
    template = """given the full name {name_of_person} I want you to get me a link to their LinkedIn profile page.
                    Your answer should just have the URL"""
    
    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])

    tools_for_agent = [
        Tool(
            name = "Crawl Google for LinkedIn profile page",
            func = get_profile_url_tavily,
            description="useful for when you need to get the LinkedIn profile page"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_profile_url = result["output"]
    print(result)
    return linkedin_profile_url


if __name__ == '__main__':
    linkedin_url =  lookup("Mustafa Suleyman")
    print(linkedin_url)