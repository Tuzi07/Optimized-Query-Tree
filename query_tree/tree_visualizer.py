import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

import networkx
from networkx.drawing.nx_pydot import graphviz_layout


def show_tree(sql_tree):
    tree = sql_tree.tree
    networkx.draw_networkx(tree, graphviz_layout(tree, prog="dot"))
    plt.show()
