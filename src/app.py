import gradio as gr

import pages


JQUERY_CDN = r'<script src="https://code.jquery.com/jquery-3.7.1.slim.min.js" integrity="sha256-kmHvs0B+OpCW5GVHUNjv9rOmY0IvSIRcf7zGUDTDQM8=" crossorigin="anonymous"></script>'

TITLE = "RPS with AI"
HEAD = f"{JQUERY_CDN}"
CSS = "src/style.css"
JS = "src/script.js"


with gr.Blocks(
    fill_width=True,
    fill_height=True,
    title=TITLE,
    head=HEAD,
    css=CSS,
    js=JS,
) as demo:
    pages.render_all()


if __name__ == "__main__":
    demo.launch()