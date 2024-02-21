import csv
import pandas as pd
import plotly.express as px

class RenderUploadFileHTML:
    def __init__(self, file):
        self.file = file

    def render(self, uploaded_file_name):        
        df = pd.read_csv(self.file)

        # Get file header
        header = list(df.columns)
        
        if len(df.columns) != 2:
            raise ValueError('The file should have only two columns')
        else:
            # Use header to get the name of the columns
            name = header[0]
            unit = header[1]

            fig = px.bar(df, x=name, y=unit, title=uploaded_file_name, labels={
                         name: name.capitalize(), unit: unit.capitalize()})

            # Styling the plot
            fig.update_traces(marker_color='#ff8d40') # Change the color of the bars

            fig.update_layout(title_x=0.5, title_y=0.9, title_font_size=30, title_font_family='Arial',
                            title_font_color='black', title_font=dict(size=30, family='Arial', color='#4f81bd')) # Change the title font

            fig.update_traces(hoverlabel=dict(bgcolor='white', bordercolor='black',
                            font_size=16, font_family='Arial', font_color='black')) # Change the hover label

            fig.update_xaxes(title_font=dict(size=18, family='Arial', color='black'),
                            tickfont=dict(size=14, family='Arial', color='black')) # Change the x-axis font

            fig.update_yaxes(title_font=dict(size=18, family='Arial', color='black'),
                            tickfont=dict(size=14, family='Arial', color='black')) # Change the y-axis font

            return fig.to_html()
