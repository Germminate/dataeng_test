#!/usr/local/bin/python

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../../..'))

import json
import numpy
import argparse

from components.dataset import Parser
from components.utils import DimensionalityReduction, one_hot_encode, manual_encoding, create_and_display
from components.model import SVM


def get_config(config_path):
    with open(config_path) as config_file:
        return json.load(config_file)


def manipulate_data(data):
    # Drop 'persons' data as it is not part of the query params
    for row in data:
        row.pop(2)

    return data


def get_data(data_path):
    data_parser = Parser(data_path)
    x_train, y_train, x_test, y_test = data_parser.parse()
    x_train = manipulate_data(x_train)
    x_test = manipulate_data(x_test)

    return x_train, y_train, x_test, y_test


def encode_data(train_data, test_data=None):
    return one_hot_encode(train_data, test_data)


def order_inputs(params):
    # Orders the query inputs in the same order as the training data
    # Ideally not hard-coded, but there isn't enough time to finetune these details
    maintenance, doors, lug_size, safety, class_val = '', 0, '', '', ''
    keys = params.keys()
    if 'maintenance' in keys:
        maintenance = params['maintenance']
    if 'doors' in keys:
        doors = params['doors']
    if 'lug_boot_size' in keys:
        lug_size = params['lug_boot_size']
    if 'safety' in keys:
        safety = params['safety']
    if 'class_value' in keys:
        class_val = params['class_value']

    return ([maintenance, doors, lug_size, safety, class_val])


def fit_model(input_x, input_y, model=None, random_state=123):
    if model == 'svm':
        model = SVM([input_x, input_y], random_state)

        return model.svc()
    else:
        raise Exception("ModelNotFound: No model defined, exiting process.")


def predict(input, model):
    return model.predict(input)


def evaluate(eval_data, actual, model, labels=None, save_path=None):
    # Evaluate
    pred = predict(eval_data, model)
    # Show results
    create_and_display(pred, actual, labels, save_path)


def main(config_path):
    # Get config
    config = get_config(opt_args.config)

    # Get the dataset for training and evaluation
    train_x, train_y, eval_x, eval_y = get_data(config['dataset'])

    # Encode data
    x_train, x_eval, x_encoder = encode_data(train_x, eval_x)
    y_train, y_eval, y_encoder = encode_data(train_y, eval_y)
    y_train = manual_encoding(y_train)
    y_eval = manual_encoding(y_eval)

    # Fit model
    model = fit_model(x_train, y_train, model=config['model'], random_state=config['random_state'])

    # Evaluate
    evaluate(x_eval, y_eval, model, y_encoder.categories_[0], config['cm_out_path'])

    # Predict
    # # Get query values
    query = order_inputs(config['query'])
    query = x_encoder.transform([query]).toarray()
    pred = predict(query, model)
    pred_class = y_encoder.categories_[0][pred][0]
    print("The predicted price based on the given parameters is %s." % pred_class.upper())


if __name__ == "__main__":
    default_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', dest='config', help='Path to config', metavar='FILE', default=None)

    (opt_args, args) = parser.parse_known_args()

    main(opt_args.config)
