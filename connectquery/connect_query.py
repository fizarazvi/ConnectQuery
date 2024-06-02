from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import google_palm
from langchain_google_genai import ChatGoogleGenerativeAI

import os
import sys

information = """
Avul Pakir Jainulabdeen Abdul Kalam BR (/ˈɑːbdəl kəˈlɑːm/ ⓘ; 15 October 1931 – 27 July 2015) was an Indian aerospace scientist and statesman who served as the 11th president of India from 2002 to 2007. Born and raised in a Muslim family in Rameswaram, Tamil Nadu, he studied physics and aerospace engineering. He spent the next four decades as a scientist and science administrator, mainly at the Defence Research and Development Organisation (DRDO) and Indian Space Research Organisation (ISRO) and was intimately involved in India's civilian space programme and military missile development efforts.[1] He thus came to be known as the Missile Man of India for his work on the development of ballistic missile and launch vehicle technology.[2][3][4] He also played a pivotal organisational, technical, and political role in India's Pokhran-II nuclear tests in 1998, the first since the original nuclear test by India in 1974.[5]

Kalam was elected as the 11th president of India in 2002 with the support of both the ruling Bharatiya Janata Party and the then-opposition Indian National Congress. Widely referred to as the "People's President",[6] he returned to his civilian life of education, writing and public service after a single term. He was a recipient of several prestigious awards, including the Bharat Ratna, India's highest civilian honour.

While delivering a lecture at the Indian Institute of Management Shillong, Kalam collapsed and died from an apparent cardiac arrest on 27 July 2015, aged 83.[7] Thousands, including national-level dignitaries, attended the funeral ceremony held in his hometown of Rameswaram, where he was buried with full state honours.[8]
"""

if __name__=='__main__':
    print("Hello LangChain!")
    
    print(sys.prefix)
    summary_template = """
        given the information {information} about a person I want you to create:
        1. Short summary
        2. two interesting fact about them
    """

    # information should be passed to the chain, here we just provide what vairable to look for
    summary_prompt_template = PromptTemplate(input_variables=['information'], template=summary_template)

    #temperature defines the creativity of the mode
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information":information})

    print(res.content)