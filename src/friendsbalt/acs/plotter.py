import matplotlib.pyplot as plt

class Plotter:
    """
    A class used to create and manage plots using matplotlib.
    Attributes
    ----------
    fig : matplotlib.figure.Figure
        The figure object for the plot.
    ax : matplotlib.axes._axes.Axes
        The axes object for the plot.
    color : str
        The color used for plotting points and lines.
    marker_size : int
        The size of the markers used for plotting points.
    line_width : int
        The width of the lines used for plotting lines.
    Methods
    -------
    set_color(color)
        Sets the color for plotting points and lines.
    set_marker_size(size)
        Sets the size of the markers for plotting points.
    set_line_width(width)
        Sets the width of the lines for plotting lines.
    plot_point(x, y)
        Plots a point at the given (x, y) coordinates.
    plot_line(x1, y1, x2, y2)
        Plots a line between the given (x1, y1) and (x2, y2) coordinates.
    show()
        Displays the plot.
    """
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.color = 'blue'
        self.marker_size = 5
        self.line_width = 1
        self.ax.axis('off')  # Hide the axes by default

    def set_color(self, color):
        self.color = color

    def set_marker_size(self, size):
        self.marker_size = size

    def set_line_width(self, width):
        self.line_width = width

    def plot_point(self, x, y):
        self.ax.plot(x, y, color=self.color, marker='o', markersize=self.marker_size)

    def plot_line(self, x1, y1, x2, y2):
        self.ax.plot([x1, x2], [y1, y2], color=self.color, linewidth=self.line_width)

    def show(self):
        plt.show()

if __name__ == "__main__":
    # Example usage:
    plotter = Plotter()
    plotter.set_color('red')
    plotter.set_marker_size(10)
    plotter.plot_point(1, 2)
    plotter.set_line_width(2)
    plotter.plot_line(1, 2, 3, 4)
    plotter.show()