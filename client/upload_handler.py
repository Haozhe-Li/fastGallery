import gradio as gr
import sys

sys.path.append("/Users/haozheli/Coding/fastGallery")
from core.globalvaris import *
from core.update_db import update_db


def upload_handler(img_url: str, title: str, description: str) -> str:
    if img_url == "" or title == "" or description == "":
        return "Please fill in all the fields"
    if not img_url.lower().endswith(("jpg", "jpeg", "png", "webp")):
        return "Please upload a valid image file. Current support jpg, jpeg, png and webp format."
    try:
        update_db({"img_url": img_url, "title": title, "description": description})
        return f"Successful uploaded! \nData: \nimg_url: {img_url}, \ntitle: {title}, \ndescription: {description}"
    except Exception as e:
        return str(e)


inputs = [
    gr.File(label="Upload Image"),
    gr.Textbox(lines=1, label="Title", info="Title of the image"),
    gr.Textbox(lines=5, label="Description", info="Description of the image"),
]
outputs = gr.Textbox(lines=1, label="Status")

gr.Interface(
    upload_handler,
    inputs,
    outputs,
    title="Upload Image",
    description="Upload an image to the database",
).launch()
