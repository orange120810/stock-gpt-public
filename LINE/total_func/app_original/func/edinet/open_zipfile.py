import datetime
import requests
import pandas as pd
import time
import zipfile
from tqdm import tqdm
import pickle

filename = "docid_list.pk"

# # リストを読み込む
# with open(filename, 'rb') as fi:
#     docid_list = pickle.load(fi)

# for i, docid in enumerate(docid_list):
#     print(docid_list[i+1])
#     with zipfile.ZipFile("*.zip") as zip_f:
#       zip_f.extractall(f"openfile/{docid}")

import os
import zipfile

zip_dir = 'edinet_data/zipfile'
extract_dir = 'edinet_data/openfile'

# for filename in tqdm(os.listdir(zip_dir)):
#     if filename.endswith('.zip'):
#         with zipfile.ZipFile(os.path.join(zip_dir, filename), 'r') as zip_ref:
#             zip_ref.extractall(os.path.join(extract_dir, os.path.splitext(filename)[0]))

for filename in tqdm(os.listdir(zip_dir)):
    if filename.endswith('.zip'):
        with zipfile.ZipFile(os.path.join(zip_dir, filename), 'r') as zip_ref:
            zip_ref.extractall(os.path.join(extract_dir, os.path.splitext(filename)[0]))
