import gradio as gr
import sys

from core.globalvaris import *
from core.update_db import update_db

def upload_handler(img_url: str, title: str, description: str) -> str:
    try:
        update_db({
            'img_url': img_url,
            'title': title,
            'description': description
        })
        return 'success'
    except Exception as e:
        return str(e)
    
inputs = [gr.File(label="Upload Image"), gr.Textbox(lines=1, label="Title"), gr.Textbox(lines=5, label="Description")]
outputs = gr.Textbox(lines=1, label="Status")

gr.Interface(upload_handler, inputs, outputs, title="Upload Image", description="Upload an image to the database").launch()