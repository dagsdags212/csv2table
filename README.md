# csv2table

Easily convert your CSV files into beautiful, formatted tables.


### Usage

Convert a csv file into a named table using the `-o` flag.
```
csv2table myfile.csv -o myfile.tbl
```

Specify the output format using the `--format` flag.
```
csv2table myfile.csv -o myfile.tbl --format [jpg|png|pdf|markdown]
```

Add a table title by passing a string to the `--title` flag. Do the same to the `--subtitle` flag to add a subtitle.
```
csv2table myfile.csv -o myfile.tbl --title "Hello Table" --subtitle "by Ducky Momo"
```

### Other Parameters

- `--footer`: add a footer to the table
