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