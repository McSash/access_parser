# AccessDB Parser (Pure Python)
Microsoft Access (.mdb / .accdb) database files parser. The parsing logic is fully written in python and works without any external binary dependencies.

# Installing
Use pip: `pip install git+https://github.com/McSash/access_parser`

Or install manually:
```bash
git clone https://github.com/McSash/access_parser.git
cd access_parser
python3 setup.py install
```

# Demo
[![asciicast](https://asciinema.org/a/345445.svg)](https://asciinema.org/a/345445)

# Usage Example
```python
from access_parser import AccessParser

# .mdb or .accdb file, alternatively pass bytes object
db = AccessParser("/path/to/mdb/file.mdb")

# Print DB tables
print(db.catalog)

# Tables are stored as defaultdict(list) -- table[column][row_index]
table = db.parse_table("table_name")

# Pretty print all tables
db.print_database()

```

### Known Issues
* OLE fields are currently not supported
* Only a subset of memo fields are parsed

This library was tested on a limited subset of database files. Due to the differences between database versions and the complexity of the parsing we expect to find more parsing edge-cases.

To help us resolve issues faster please provide as much data as you can when opening an issue - DB file if possible and full trace including log messages.
 
 
### Thanks
* This library was made possible by the great work by claroty: https://github.com/claroty/access_parser
