from os.path import dirname, join

import pandas as pd

from shiny import ui, App
from shinywidgets import output_widget, render_widget
import plotly.express as px
import plotly.graph_objs as go


project_path = dirname(__file__)
data_path = join(project_path,'data')
data_file = join(data_path,'anime.csv')


# df = px.data.tips()
df = pd.read_csv(data_file)



app_ui = ui.page_fluid(
    ui.div(
        ui.input_select(
            "x", label="Variable",
            choices=["Score", "Vote", "Popularity"]
        ),
        ui.input_select(
            "color", label="Color",
            choices=["Rating", "Source", "Studios", "Status"]
        ),
        class_="d-flex gap-3"
    ),
    output_widget("my_widget")
)

def server(input, output, session):
    @output
    @render_widget
    def my_widget():
        fig = px.histogram(
            df, x=input.x(), color=input.color(),
            marginal="rug"
        )
        fig.layout.height = 275
        return fig

app = App(app_ui, server)