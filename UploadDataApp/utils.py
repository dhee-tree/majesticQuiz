import csv
import pandas as pd
import plotly.express as px

class RenderUploadFileHTML:
    def __init__(self, file):
        self.file = file

    def render(self):        
        df = pd.read_csv(self.file)

        fig = px.bar(df, x='name', y='unit', title='Uploaded Data', labels={'x': 'Name', 'y': 'Unit'})

        return fig.to_html()