from langchain_community.llms import Ollama
import gradio as gr
from langchain_core.prompts import PromptTemplate


def cover_letter(contact_person,your_name, role, company_name,personal_exp,job_desc,passion,skills):
    prompt = PromptTemplate(
    template_format = "Write a cover letter to  {contact_person}\n  from  {your_name}\n  for a  {role}\n  job at  {company_name} . \n\n I have experience in  {personal_exp} \n\n I am excited about the job because  {job_desc} \n\n  I am passionate about  {passion} \n\n I have experience in {skills}. ",
    input_variables = ["contact_person","your_name", "role", "company_name","personal_exp","job_desc","passion","skills"],
    )
    
    formatted_prompt = prompt.format(contact_person=contact_person, your_name=your_name, role=role,company_name=company_name,personal_exp=personal_exp,job_desc=job_desc,passion=passion,skills=skills)
    llm = Ollama(model='phi3')
    response = llm.invoke(formatted_prompt)
    return response


inputs=[
    gr.Textbox(label="contact_person"),
    gr.Textbox(label="your_name"),
    gr.Textbox(label="role"),
    gr.Textbox(label="company_name"),
    gr.Textbox(label="personal_exp"),
    gr.Textbox(label="job_desc"),
    gr.Textbox(label="passion"),
    gr.Textbox(label="Skills")
]

outputs=gr.Textbox(label="Cover Letter")

coverletterbot = gr.Interface(fn=cover_letter, inputs=inputs, outputs=outputs)

coverletterbot.launch()
