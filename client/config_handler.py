import gradio as gr
import json
import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

from core.globalvaris import *

def config_handler(website_name: str, website_title: str, 
                    website_about: str, author_name: str, author_url: str, enable_search_bar: bool) -> str:
    try:
        if website_name == '' or website_title == '' or website_about == '' or author_name == '' or author_url == '':
            return 'Please fill in all the fields'
        if not author_url.startswith('http'):
            return 'Please include the protocol in the Author URL, eg. https://yourwebsite.com. Tips: directly copy from the browser!'
        if enable_search_bar:
            nltk.download('punkt')
            nltk.download('averaged_perceptron_tagger')
        data = {
            'website_name': website_name,
            'website_title': website_title,
            'website_about': website_about,
            'author_name': author_name,
            'author_url': author_url,
            'enable_search_bar': enable_search_bar
        }
        with open(WEBSITE_CONFIG_DIR, 'w') as f:
            f.write('')
            json.dump(data, f)
        return f"Configured! \nData: \n{str(data)}"
    except Exception as e:
        return f"error occured: {str(e)}"

inputs = [
    gr.Textbox(label="Website Name", info="The name of your website, eg. Gallery - Your Name"), 
    gr.Textbox(label="Website Title", info="The title of your website, it is very similar to the website name so you can use the same one."),
    gr.Textbox(label="Website About", info="A brief description of your website"),
    gr.Textbox(label="Author Name", info="Your name"),
    gr.Textbox(label="Author URL", info="Your website or social media URL. Please make sure you include the protocol, eg. https://yourwebsite.com"),
    gr.Checkbox(label="Enable Search Bar", info="Enable the search bar and smart keyword suggestions on your website. This sometimes slows down the loading speed of the website and requires additional resources to be downloaded.")
]

outputs = gr.Textbox(label="Configuration Result", info="The result of the configuration. If error occured, it will show the error message.")

configuration = gr.Interface(title='Initialize your website',
                           fn=config_handler,
                           inputs=inputs,
                           outputs=outputs)

configuration.launch()