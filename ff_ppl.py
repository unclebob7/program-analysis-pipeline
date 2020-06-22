#!/usr/bin/python3
"""
    program analysis tools pipeline
"""
import argparse
import pandas as pd
import numpy as np
import os

# hyperparameter
parser = argparse.ArgumentParser(description="shell parameters")
parser.add_argument("--path", "-p", help="projects csv location", default=r"./tiny.csv")
parser.add_argument("--tool", "-t", help="analysis tool", default="flawfinder")
args = parser.parse_args()

# get project hash table
def pj_ls(csv_loc):
    ls = pd.read_csv(csv_loc)
    repo_dict = pd.DataFrame(ls, columns=["name", "local_path"]).dropna()
    return repo_dict
 
def flawfinder(name, path):    
    """
        name: name of the output .csv file
        path: path of the pre-analyzed project
    """
    # os.system("./ff.sh" + " " + "test_folder" + " " + "./raw/test_folder")
    os.system("./ff.sh" + " " + name + " " + path)

def oclint():
    pass

# apply tools (e.g. flawfinder) upon
def apply_tool(tool, csv_loc):
    repo_dict = pj_ls(csv_loc)
    if tool == "flawfinder":
        for row in repo_dict.itertuples(index=True):
            name = getattr(row, "name")
            path = getattr(row, "local_path")
            flawfinder(name, path)
    else:
        print("does not find the tool")

def main():
    try:
        csv_loc = args.path
        analyze_tool = args.tool
        apply_tool(analyze_tool, csv_loc)
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    main()