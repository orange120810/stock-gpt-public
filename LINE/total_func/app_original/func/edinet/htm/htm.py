import os
from bs4 import BeautifulSoup
import sys
sys.path.append("../../../../")
sys.path.append("LINE/total_func/app_original/func/edinet/edinet_data/openfile/")

def pick_data_from_htm(file_path):

        if file_path:
                with open(file_path) as open_htm_file:
                        htm = BeautifulSoup(open_htm_file, "html.parser")
                        body = htm.find('body')
                        body_text = body.text
                        
                        return body_text
        else:
                return None

