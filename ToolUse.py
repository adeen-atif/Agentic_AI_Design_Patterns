from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI()

plan_prompt = PromptTemplate.from_template(
    "Break the following task into clear steps: {task}"
)
plan_chain = LLMChain(llm=llm, prompt=plan_prompt)

task = "Write a blog, create a graphic, and schedule the post"
steps = plan_chain.run(task)

print("Planned Steps:\n", steps)
