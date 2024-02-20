import plotly.express as px
from .models import Drink, Sweet

class RenderHTMLData:
    def __init__(self, model):
        self.model = model

    def render(self, name):
        data = self.model.objects.all()

        if name == 'Drink':
            fig = px.bar(
                x=[d.name for d in data],
                y=[d.litre for d in data],
                title='Estimated litres of soft drink consumed at a student hackathon.',
                labels={'x': 'Drink', 'y': 'Litre'}
            )

        else:
            fig = px.bar(
                x=[d.name for d in data],
                y=[d.mass for d in data],
                title='Estimated mass of sweets consumed during a student hackathon',
                labels={'x': 'Sweet', 'y': 'Mass'}
            )

        fig.update_traces(marker_color='#ff8d40')

        fig.update_layout(title_x=0.5, title_y=0.9, title_font_size=30, title_font_family='Arial', title_font_color='black', title_font=dict(size=30, family='Arial', color='#4f81bd'))

        fig.update_traces(hoverlabel=dict(bgcolor='white', bordercolor='black', font_size=16, font_family='Arial', font_color='black'))

        fig.update_xaxes(title_font=dict(size=18, family='Arial', color='black'), tickfont=dict(size=14, family='Arial', color='black'))

        fig.update_yaxes(title_font=dict(size=18, family='Arial', color='black'), tickfont=dict(size=14, family='Arial', color='black'))

        return fig.to_html()
