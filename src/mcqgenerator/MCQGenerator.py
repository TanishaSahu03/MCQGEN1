import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
from src.mcqgenerator.logger import logging
from pathlib import Path


from langchain_openai import ChatOpenAI
# from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_core.runnables import RunnableSequence
from langchain_core.runnables import RunnableLambda, RunnableMap

#load environment variables
env_path = Path("/home/my/Desktop/MCQGEN/.env")
load_dotenv(env_path)

KEY = os.getenv("OPENAI_API_KEY")
BASE = os.getenv("OPENAI_API_BASE")

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)

TEMPLATE="""
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}

"""

quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=TEMPLATE
)

quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)
# quiz_chain = quiz_generation_prompt | llm

TEMPLATE2="""
You are an expert english gramarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to avaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity.\
If the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the students ability.
Quiz_MCQs:
{quiz}

Check from an expert English writer of the above quiz.
"""

quiz_evaluation_prompt = PromptTemplate(input_variables=["subject", "quiz"],
                                        template=TEMPLATE2)

review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)
# review_chain = quiz_evaluation_prompt | llm
# extract_text = RunnableLambda(lambda input_and_msg: {
#     "quiz": input_and_msg[1].content,
#     "subject": input_and_msg[0]["subject"]
# })

generate_evaluate_chain = SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"],output_variables=["quiz", "review"], verbose=True)
# generate_evaluate_chain = quiz_chain | review_chain
# generate_evaluate_chain = (
#     quiz_generation_prompt
#     | llm
#     # Combine original input and generated quiz
#     | RunnableLambda(lambda inputs: {
#         "quiz": inputs.content,
#         "subject": inputs._kwargs["subject"]
#     })
#     | quiz_evaluation_prompt
#     | llm
# )
# generate_evaluate_chain = (
#     RunnableMap({
#         "original": lambda x: x,
#         "quiz": quiz_chain  # This uses prompt | llm from earlier
#     })
#     | RunnableLambda(lambda x: {
#         "quiz": x["quiz"].content,      # x["quiz"] is an AIMessage
#         "subject": x["original"]["subject"]
#     })
#     | quiz_evaluation_prompt
#     | llm
# )