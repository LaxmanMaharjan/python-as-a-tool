import subprocess

def convert_spreadsheet_to_pdf(source_filename:str, destination_folder_name:str) -> None:
    convert_to_pdf = f"libreoffice --headless --convert-to pdf {source_filename} --outdir {destination_folder_name}"
    subprocess.run(convert_to_pdf, shell=True)
