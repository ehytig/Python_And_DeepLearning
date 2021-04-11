from utils import paper

web_url = "https://www.nature.com/articles/s41586-021-03359-9"

pdf_directory = r"G:\\Test_Download_paper\\PDF"
ris_directory = r"G:\\Test_Download_paper\\RIS"

paper1 = paper(web_url, pdf_directory= pdf_directory, ris_directory= ris_directory)
paper1.download() 