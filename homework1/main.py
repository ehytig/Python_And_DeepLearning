import os
from RisOperation import generate_name_from_ris
import shutil



pdf_temporary_path = "temporary.pdf"
ris_temporary_path = "temporary.ris"

download(pdf_temporary_path, get_url(soup, pdflink_filter, web_url))
download(ris_temporary_path, get_url(soup, rislink_filter, web_url))


pdf_name = generate_name_from_ris(ris_temporary_path) + ".pdf"
ris_name = generate_name_from_ris(ris_temporary_path) + ".ris"

pdf_path = pdf_directory + "\\" + pdf_name
ris_path = ris_directory + "\\" + ris_name

# move and rename .pdf file  and .ris file
shutil.move(pdf_temporary_path, pdf_path)
shutil.move(ris_temporary_path, ris_path)