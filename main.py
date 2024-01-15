import os


import pandas as pd
import matplotlib.pyplot as plt


import os
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import Image, display

class Plotter:
    def __init__(self, data_frame):
        self.df = data_frame

    def draw_plots(self):
        os.makedirs('графики', exist_ok=True)
        plot_paths = []

        for column in self.df.columns:
            if column not in ['Rb_corners']:
                plot_path = f'графики/{column}_plot.png'
                plot_paths.append(plot_path)

                plt.figure(figsize=(10, 6))
                plt.scatter(self.df.index, self.df[column], label=column)
                plt.xlabel('Индекс строки')
                plt.ylabel(f'Значения {column}')
                plt.title(f'График для {column}')
                plt.legend()
                plt.savefig(plot_path)
                plt.close()

        return plot_paths


def read_json_and_draw_plots(json_path):
    df = pd.read_json(json_path)
    plotter = Plotter(df)
    plot_paths = plotter.draw_plots()
    return plot_paths

if __name__ == '__main__':
    json_path = 'deviation.json'
    plot_paths = read_json_and_draw_plots(json_path)
    print(f'Графики сохранены в следующих файлах: {", ".join(plot_paths)}')


json_path = 'deviation.json'
plot_paths = read_json_and_draw_plots(json_path)

# Визуализация графиков
for plot_path in plot_paths:
    display(Image(filename=plot_path))