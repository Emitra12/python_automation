import json
from os import listdir
from os.path import isfile, join

# Json file directory
dir_path = r"C:\Users\Surya\PycharmProjects\AlRajhiAutomation\json_conf_files"
user = "suryaArb11"
passwrd = "surya12345678999"
url = "jdbc:oracle:thin:@arb30-scan:1521/odsprod"
# Jod directory pattern
outputPath_jo_salex = "/edh/dev/data/selexdb/raw/selex_jo/"
outputPath_jo_ctf = "/edh/dev/data/ctfdb/raw/cft_jo/"
outputPath_jo_pft = "/edh/dev/data/pftdb/raw/pft_jo/"
outputPath_jo_cif = "/edh/dev/data/cifdb/raw/cif_jo/"
# KSA directory pattern
outputPath_ksa_salex = "/edh/dev/data/selexdb/raw/selex_ksa/"
outputPath_ksa_ctf = "/edh/dev/data/ctfdb/raw/cft_ksa/"
outputPath_ksa_pft = "/edh/dev/data/pftdb/raw/pft_ksa/"
outputPath_ksa_cif = "/edh/dev/data/cifdb/raw/cif_ksa/"
# KW directory pattern
outputPath_kw_salex = "/edh/dev/data/salexdb/raw/salex_kw/"
outputPath_kw_ctf = "/edh/dev/data/ctfdb/raw/ctf_kw/"
outputPath_kw_pft = "/edh/dev/data/pftdb/raw/pft_kw/"
outputPath_kw_cif = "/edh/dev/data/cifdb/raw/cif_kw/"

# Collecting all files with .json extensions and passing in fieldsUpdateInJsonFiles function
all_json_files = [join(dir_path, f) for f in listdir(dir_path) if isfile(join(dir_path, f)) and f.endswith(".json")]


def fieldsUpdateInJsonFiles(all_json_files):

    for file_path in all_json_files:

        with open(file_path) as input_file:

            data = json.load(input_file)

            data['source']['user'] = user

            data['source']['password'] = passwrd

            data['source']['url'] = url
# Directory pattern matching and replacing respective values
            if data["target"]["outputPath"] == outputPath_jo_salex:
               data["target"]["outputPath"] = "/edh/prod/data/selexdb/raw/selex_jo/"

            elif data["target"]["outputPath"] == outputPath_jo_ctf:
                 data["target"]["outputPath"] = "/edh/prod/data/ctfdb/raw/ctf_jo/"

            elif data["target"]["outputPath"] == outputPath_jo_pft:
                 data["target"]["outputPath"] = "/edh/prod/data/pftdb/raw/pft_jo/"

            elif data["target"]["outputPath"] == outputPath_jo_cif:
                 data["target"]["outputPath"] = "/edh/prod/data/cifdb/raw/cif_jo/"

            elif data["target"]["outputPath"] == outputPath_ksa_cif:
                 data["target"]["outputPath"] = "/edh/prod/data/cifdb/raw/cif_ksa/"

            elif data["target"]["outputPath"] == outputPath_ksa_pft:
                data["target"]["outputPath"] = "/edh/prod/data/pftdb/raw/pft_ksa/"

            elif data["target"]["outputPath"] == outputPath_ksa_ctf:
                 data["target"]["outputPath"] = "/edh/prod/data/ctfdb/raw/ctf_jo/"

            elif data["target"]["outputPath"] == outputPath_ksa_salex:
                 data["target"]["outputPath"] = "/edh/prod/data/salexdb/raw/salex_jo/"

            elif data["target"]["outputPath"] == outputPath_kw_cif:
                 data["target"]["outputPath"] = "/edh/prod/data/cifdb/raw/cif_kw/"

            elif data["target"]["outputPath"] == outputPath_kw_ctf:
                data["target"]["outputPath"] = "/edh/prod/data/ctfdb/raw/ctf_kw/"

            elif data["target"]["outputPath"] == outputPath_kw_pft:
                 data["target"]["outputPath"] = "/edh/prod/data/pftdb/raw/pft_jo/"

            elif data["target"]["outputPath"] == outputPath_kw_salex:
                 data["target"]["outputPath"] = "/edh/prod/data/salexdb/raw/salex_kw/"

# Opening file for making the updates
            with open(file_path, "w") as jsonFile:
                  json.dump(data, jsonFile, ensure_ascii=True, indent=4, sort_keys=True)

# Function execution with logic
fieldsUpdateInJsonFiles(all_json_files)