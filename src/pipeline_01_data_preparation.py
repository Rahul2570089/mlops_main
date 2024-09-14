import os
import yaml
import argparse
import logging




def main(args):
    with open(args.config, "r") as yaml_file:
        params = yaml.safe_load(yaml_file)
    print(params)


def args_parser():
    args = argparse.ArgumentParser()
    args.add_argument("--config", help="Pass the config file")
    args.add_argument("--datasource", help="Pass the datasource file")
    return args.parse_args()

if __name__ == "__main__":
    main(args_parser())