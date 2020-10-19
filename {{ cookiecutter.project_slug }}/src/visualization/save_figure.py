# -*- coding: utf-8 -*-
# File name: save_figure_and_show.py
# First Edit: 2020-10-13
# Last Change: 2020-10-13
"""
save figure with right file_name and right place.
"""
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


def save_figure_and_show(figure, figure_save_distination, path_echo=True):
    try:
        # if isinstance(figure, matplotlib.figure.Figure):
        save_figure(figure, figure_save_distination)

        if path_echo:
            print_figure_path(figure, figure_save_distination)
        plot_show(figure, figure_save_distination)

    except AttributeError:
        # if isinstance(figure, matplotlib.text.Text):
        save_figure(figure.get_figure(), figure_save_distination)

        if path_echo:
            print_figure_path(figure, figure_save_distination)
        plot_show(figure, figure_save_distination)

    # except * as e:
    #     print(e)
    #     print("figure save Failed")


# vim:tw=88 ff=unix ft=python ts=4 sw=4 sts=4 si et:
