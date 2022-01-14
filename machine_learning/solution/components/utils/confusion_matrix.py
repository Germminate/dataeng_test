import matplotlib
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def create_and_display(predicted, actual, labels, out_path):
    # Create confusion matrix
    cm = confusion_matrix(actual, predicted)

    # Create the fancy display graph
    display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[labels[0], labels[1], labels[2], labels[3]])
    # Save the graph
    plt.savefig(out_path)
