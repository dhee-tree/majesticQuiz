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

        return fig.to_html()
