import matplotlib
import matplotlib.pyplot as plt


def make_path(figure, distination):
    return distination + "/" + figure.axes[0].get_title().replace(" ", "_")


def save_figure(figure, distination):
    figure.savefig(make_path(figure, distination))


def print_figure_path(figure, distination):
    print(make_path(figure, distination))


def plot_show(figure, distination):
    plt.show(make_path(figure, distination))


def save_figure_and_show(figure, figure_save_distination):
    if isinstance(figure, matplotlib.figure.Figure):
        save_figure(figure, figure_save_distination)
        print_figure_path(figure, figure_save_distination)
        plot_show(figure, figure_save_distination)

    if isinstance(figure, matplotlib.matplotlib.text.Text):
        save_figure(figure.get_figure(), figure_save_distination)
        print_figure_path(figure, figure_save_distination)
        plot_show(figure, figure_save_distination)
    else:
        raise ("figure save Failed")
