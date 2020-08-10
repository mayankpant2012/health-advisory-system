#for visualization
import matplotlib.pyplot as plt
from django.core.files.images import ImageFile
import io

#this function makes a plot and return the image file and filename
def make_plot(name, x, y, report_id, z=False):
    x = list(map(str, x))
    file_name = name + '_plot_report_' + report_id + ".png"
    figure = io.BytesIO()
    plt.plot(x, y)
    plt.scatter(x, y)
    if z:
        plt.plot(x, z,)
        plt.scatter(x, z)
    plt.xlabel('Date')
    plt.ylabel(name)
    plt.savefig(figure, format="png")
    content_file = ImageFile(figure)
    plt.close()
    return [file_name, content_file]
