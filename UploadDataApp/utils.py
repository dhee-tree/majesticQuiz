import csv
import pandas as pd
import plotly.express as px

class RenderUploadFileHTML:
    def __init__(self, file):
        self.file = file

    def render(self):        
        df = pd.read_csv(self.file)

        if len(df.columns) != 2:
            raise ValueError('The file should have only two columns')
        else:
            fig = px.bar(df, x='name', y='unit', title='Uploaded Data', labels={'name': 'Name', 'unit': 'Unit'})

            fig.update_traces(marker_color='#ff8d40')

            fig.update_layout(title_x=0.5, title_y=0.9, title_font_size=30, title_font_family='Arial',
                            title_font_color='black', title_font=dict(size=30, family='Arial', color='#4f81bd'))

            fig.update_traces(hoverlabel=dict(bgcolor='white', bordercolor='black',
                            font_size=16, font_family='Arial', font_color='black'))

            fig.update_xaxes(title_font=dict(size=18, family='Arial', color='black'),
                            tickfont=dict(size=14, family='Arial', color='black'))

            fig.update_yaxes(title_font=dict(size=18, family='Arial', color='black'),
                            tickfont=dict(size=14, family='Arial', color='black'))

            return fig.to_html()
