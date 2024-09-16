from enum import Enum
import gradio as gr


## Enumeration of pages to CSS class names
class Page(Enum):
    MAIN_MENU = "main-menu",
    PLAY = "play",
    REFERENCES = "references",


with gr.Blocks() as main_menu:
    CUR_PAGE = Page.MAIN_MENU
    with gr.Row(elem_classes=[CUR_PAGE]):
        with gr.Column():
            play_ai = gr.Button("Play vs AI", elem_classes=["game-button"])
            play_ai.click(None, [gr.State(CUR_PAGE), gr.State(Page.PLAY)], js="switchPage")
        with gr.Column():
            play_ai = gr.Button("Play vs Human", elem_classes=["game-button"])
            play_ai.click(None, [gr.State(CUR_PAGE), gr.State(Page.PLAY)], js="switchPage")
            ref_btn = gr.Button("References")
            ref_btn.click(None, [gr.State(CUR_PAGE), gr.State(Page.REFERENCES)], js="switchPage")


with gr.Blocks() as play:
    CUR_PAGE = Page.PLAY
    with gr.Row(elem_classes=[CUR_PAGE]):
        with gr.Column():
            gr.Image(sources="webcam")
        with gr.Column():
            gr.Button("Play").click(None, gr.State("coming soon..."), js="console.log")
            gr.Button("Back").click(None, gr.State(CUR_PAGE), gr.State(Page.MAIN_MENU), js="switchPage")


with gr.Blocks() as references:
    CUR_PAGE = Page.REFERENCES
    with gr.Row(elem_classes=[CUR_PAGE]):
        gr.TextArea("Lorem Ipsum")
        gr.Button("Back").click(None, gr.State(CUR_PAGE), gr.State(Page.MAIN_MENU), js="switchPage")


def render_all():
    main_menu.render()
    play.render()
    references.render()