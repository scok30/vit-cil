import json
import argparse
from trainer import train
import pdb

def main():
    args = setup_parser().parse_args()
    param = load_json(args.config)
    args = vars(args)  # Converting argparse Namespace to a dict.
    args.update(param)  # Add parameters from json
    train(args)


def load_json(settings_path):
    with open(settings_path) as data_file:
        param = json.load(data_file)
    return param


def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='exps/fcs/cifar100/5/first_stage.json')

    return parser


if __name__ == '__main__':
    main()
