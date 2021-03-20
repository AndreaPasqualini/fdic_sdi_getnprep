python ./download_sdi_data.py 1992 2019 ./data/
python ./sdi_dataset_assembler.py ./data/ ./pull_variables.json ./data/sdi.csv.xz
