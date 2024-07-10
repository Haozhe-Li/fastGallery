import gradio as gr
import json
import sys

from core.globalvaris import *

def config_handler(website_name: str, website_title: str, 
                    website_about: str, author_name: str, author_url: str) -> str:
    data = {
        'website_name': website_name,
        'website_title': website_title,
        'website_about': website_about,
        'author_name': author_name,
        'author_url': author_url
    }
    with open(WEBSITE_CONFIG_DIR, 'w') as f:
        f.write('')
        json.dump(data, f)
    return 'Configured'

inputs = [
    gr.Textbox(label="Website Name"), 
    gr.Textbox(label="Website Title"),
    gr.Textbox(label="Website About"),
    gr.Textbox(label="Author Name"),
    gr.Textbox(label="Author URL")
]

outputs = gr.Textbox(label="Info")

configuration = gr.Interface(title='Initialize your website',
                           fn=config_handler,
                           inputs=inputs,
                           outputs=outputs)

configuration.launch()