import os, sys
from img_cluster_to_txt import ClusterToTxt
from utils import createArgumentParser, get_full_path_from_relative
from collections import OrderedDict



def convert_one_img(converter, rel_path_from="images/img.png", rel_path_to="dataset/data.txt"):
    full_img_path_from, full_img_path_to = get_full_path_from_relative(rel_path_from, rel_path_to)
    
    p, t = converter.get_points_and_targets(full_img_path_from)

    if not full_img_path_to.endswith(".txt") and not full_img_path_to.endswith("/") and not os.path.isdir(full_img_path_to):
        full_img_path_to += ".txt"
    else:
        prefix = ""
        if not full_img_path_to.endswith("/"):
            prefix = "/"
        full_img_path_to += prefix + rel_path_from.split("/")[-1].split(".")[0] + ".txt"
 
    converter.create_data_file(full_img_path_to, p, list(t))

def convert_one_folder(converter, rel_path_from="images/", rel_path_to="dataset"):
    full_directory_path_from, full_directory_path_to = get_full_path_from_relative(rel_path_from, rel_path_to)
    for filename in os.listdir(full_directory_path_from):
        if filename.endswith(".png") or filename.endswith("jpg"): 
            full_img_path_from = os.path.join(full_directory_path_from, filename)
            full_img_path_to = os.path.join(full_directory_path_to, "{}.txt".format("".join(filename.split(".")[:-1])))
            p, t = converter.get_points_and_targets(full_img_path_from)
            converter.create_data_file(full_img_path_to, p, list(t))
        else:
            continue
   
def program():
    mandatory_arguments = [
        ("rel_path_from", "INput - The relative path to a img or folder, which is going to be converted into text dataset. Relative from here"),
        ("rel_path_to", "OUTput - The relative path to a img or folder, which is going to be converted into text dataset. Relative from here")
        ]

    ordered_man_args = OrderedDict(mandatory_arguments) 
    parser, args = createArgumentParser(ordered_man_args)
    converter = ClusterToTxt()

    if args.rel_path_from.endswith(".png") or  args.rel_path_from.endswith(".jpg"):
        convert_one_img(converter, args.rel_path_from, args.rel_path_to)
    elif args.rel_path_from.endswith("/"):
        convert_one_folder(converter, args.rel_path_from, args.rel_path_to)
    else:
        parser.print_usage()
    
        

if __name__ == "__main__":
    program()