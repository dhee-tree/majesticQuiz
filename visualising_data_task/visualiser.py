import matplotlib.pyplot as plt

class DataVisualisation:
    """
    A class to visualise data. Takes a dictionary of data, x and y labels and a title.
    """
    def __init__(self, data, x_label, y_label, title):
        self.data = data
        self.x_label = x_label
        self.y_label = y_label
        self.title = title

    def plot_data(self):
        """Method to plot the data"""
        data_names = list(self.data.keys())
        data_amount = list(self.data.values())

        plt.style.use('seaborn-v0_8-whitegrid')
        plt.rcParams.update({'figure.autolayout': True})

        fig, ax = plt.subplots()
        ax.bar(data_names, data_amount)

        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')

        ax.set_xlabel(self.x_label)
        ax.set_ylabel(self.y_label)
        plt.title(self.title)
        plt.show()
