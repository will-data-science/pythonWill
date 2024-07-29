# Imports
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, roc_curve, precision_recall_curve
import numpy as np


def get_int_labels(target_n: int, y_array: np.array):
    return (y_array == str(target_n))


def _get_class_perf_metrics(y_array, preds_array):

    ret_dict = dict()

    ret_dict['train_confusion_matrix'] = (
        confusion_matrix(y_array, preds_array)
    )

    ret_dict['train_precision'] = (
        precision_score(y_array, preds_array)
    )

    ret_dict['train_recall'] = (
        recall_score(y_array, preds_array)
    )

    ret_dict['train_f1'] = (
        f1_score(y_array, preds_array)
    )

    return ret_dict


def plot_precision_recall(
    thresholds_array, precisions_array, recalls_array
):
    plt.plot(thresholds_array, precisions_array[:-1], "b--", label='Precision')
    plt.plot(thresholds_array, recalls_array[:-1], "g-", label='Recall')
    plt.legend(loc='right')
    plt.show()


def plot_roc(
        false_positives_array,
        true_positives_array
):
    plt.plot(false_positives_array, true_positives_array)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.show()


def analyze_sgd_model(target_n: int, y_array, x_data):

    # Get target
    int_labels = get_int_labels(target_n=target_n, y_array=y_array)

    temp_model = SGDClassifier(random_state=13)

    temp_preds = cross_val_predict(
        temp_model, x_data, int_labels, cv=5
    )

    model_results = _get_class_perf_metrics(
        y_array=int_labels, preds_array=temp_preds
    )

    temp_scores = cross_val_predict(
        temp_model, x_data, int_labels, cv=5, method='decision_function'
    )

    temp_precisions, temp_recalls, temp_thresholds = precision_recall_curve(int_labels, temp_scores)

    plot_precision_recall(
        precisions_array=temp_precisions,
        thresholds_array=temp_thresholds,
        recalls_array=temp_recalls
    )

    false_positive_rates, true_positive_rates, _ = roc_curve(int_labels, temp_scores)
    plot_roc(false_positives_array=false_positive_rates, true_positives_array=true_positive_rates)

    return model_results


def analyze_random_forest_model(target_n: int, y_array, x_data):
    # Get target
    int_labels = get_int_labels(target_n=target_n, y_array=y_array)

    forest_model = RandomForestClassifier(random_state=13)
    temp_probs = cross_val_predict(forest_model, x_data, int_labels, cv=5, method='predict_proba')

    temp_scores = temp_probs[:, 1]  # pull out column 1 to get positive class probability

    temp_precisions, temp_recalls, temp_thresholds = precision_recall_curve(int_labels, temp_scores)

    plot_precision_recall(
        precisions_array=temp_precisions,
        thresholds_array=temp_thresholds,
        recalls_array=temp_recalls
    )

    false_positive_rates, true_positive_rates, thresholds = roc_curve(int_labels, temp_scores)

    plot_roc(false_positives_array=false_positive_rates, true_positives_array=true_positive_rates)
