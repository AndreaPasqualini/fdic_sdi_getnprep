python ./download_sdi_data.py ./data/ 1992 2019 6
python ./sdi_dataset_assembler.py ./data/ ./pull_variables.json ./data/sdi.csv.xz
