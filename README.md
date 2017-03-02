# index_structures
This project requires a unix based system capable of running ```python3```.
If you dont have ```python3``` installed visit [here](https://www.python.org/downloads/release/python-360/).

## Bootstrapping project
Execute following commands for bootstrapping the project
```sh
sudo chmod 775 ./bootstrap.sh
./bootstrap.sh
```

## Generating synthetic database
Execute following commands for generating synthetic database
```sh
sudo chmod 775 ./data_generator.sh
./data_generator.sh
```

## Generating rowId bitmap
Execute following commands for generating rowId bitmap
```sh
sudo chmod 775 ./bitmap_rowid_generator.sh
```

## Generating bit array bitmap
Execute following commands for generating ```bit array``` bitmap
```sh
sudo chmod 775 ./bitmap_bitarray_generator.sh
./bitmap_bitarray_generator.sh
```

## Generating bit array bitslice
Execute following commands for generating ```bit array``` bitslice
```sh
sudo chmod 775 ./bitslice_bitarray_generator.sh
./bitslice_bitarray_generator.sh
```

## Generating queries
Execute following commands for generating queries
```sh
sudo chmod 775 ./query_generator.sh
./query_generator.sh
```

## Running the query on the indexes generated:

Query : ```Select SUM(sale amount) From SALES_TABLE Where <condition>```

Indexes :

a) No Index
```
python3 ./query_scripts/no_index_query.py
```
b) Bitmap Index with RowId Representation
```
python3 ./query_scripts/bitmap_rowid_query.py
```
c) Bitmap Index with Bitarray Representation
```
python3 ./query_scripts/bitmap_bitarray_query.py
```
d) Bitslice Index
```
python3 ./query_scripts/bitslice_bitarray_query.py
```