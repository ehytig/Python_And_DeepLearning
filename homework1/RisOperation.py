# -*- coding: utf-8 -*-

import re
import rispy

def replace_space(string):
    return re.sub("\s","_",string)

def generate_name_from_ris(ris_path):
    # get author name + publish year + journal + title 
    # this function return a file name without suffix
    with open(ris_path,'r',encoding="utf-8") as ris_file:
        entries = rispy.load(ris_file)
        # for our application there is only one bib in ris file, if has two then error occur
        if( len(entries) != 1 ):
            raise Exception

        ris_content = entries[0]
        # author_names is a list, we only use the first one and we should replace All the special characters in it 
        author_names = ris_content['authors']
        def name_filter(name_list):
            first_name = name_list[0]
            name_after_filter1 = re.sub("[.\s]", "", first_name)
            name_after_filter2 = re.sub(",","_", name_after_filter1)
            return name_after_filter2
        author_name = name_filter(author_names)

        publish_year = replace_space(ris_content["year"])
        journal_name = replace_space(ris_content["journal_name"])
        title = replace_space(ris_content["title"])

        file_name = [author_name, publish_year, journal_name, title]
        
        return "_".join(file_name)

