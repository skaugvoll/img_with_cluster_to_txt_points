import os
from argparse import ArgumentParser

def createArgumentParser(mandatory_args={}):
    parser = ArgumentParser()
    
    for argument, description in mandatory_args.items():
        parser.add_argument(argument, help=description)

    args = parser.parse_args()
    #print(args.training)
    return parser, args

def get_full_path_from_relative(rel_path_from, rel_path_to):
    current_working_dir = os.getcwd()
    full_img_path_from = os.path.join(current_working_dir, rel_path_from)
    full_img_path_to = os.path.join(current_working_dir, rel_path_to)
    return full_img_path_from, full_img_path_to


if __name__ == "__main__":
    print(createArgumentParser(man1="help is needed", man2="help is wanted"))