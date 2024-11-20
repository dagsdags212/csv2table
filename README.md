# csv2table

Easily convert your CSV files into beautiful, formatted tables.


### Usage

#### Viewing CSVs

Display the first 10 rows of the file.
```
csv2table view <myfile.csv> --head
```

Display the last 10 rows of the file.
```
csv2table view <myfile.csv> --tail
```

Specify the `--start` and `--end` indices of the file.
```
csv2table view <myfile.csv> --start 10 --end 20
```

#### Exporting as tables

Convert a csv file into a named table using the `-o` flag.
```
csv2table export <myfile.csv> -o <myfile.png>
```

Specify the output format using the `--format` flag.
```
csv2table myfile.csv -o myfile.tbl --format [jpg|png|pdf|markdown]
```

Add a table title by passing a string to the `--title` flag. Subtitles can also be added by passing a string to the `--subtitle` flag. Take note that subtitles require a title. If no title is provided, the subtitle will be ignored.
```
csv2table export <myfile.csv> -o <myfile.png> --title "Hello Table" --subtitle "by Ducky Momo"
```

Table footers can also be added by passing a string to the `--footer` flag.
```
csv2table export <myfile.csv> -o <myfile.png> --footer "Copyright 2024"
```

### Arguments

| Subcommand | Arguments    | Description                            |
| ---------- | ------------ | -------------------------------------- |
| view       | `--head`       | display the first 10 rows              |
|            | `--tail`       | display the last 10 rows               |
|            | `--start`      | indicate the first row to be displayed |
|            | `--end`        | indicate the last row to be displayed  |
| export     | `-o`/`--outfile` | filepath of the saved table            |
|            | `--title`      | add a title to the table               |
|            | `--subtitle`   | add a subtitle to the table            |
|            | `--footer`     | add a footer to the table              |
|            | `--title`      | add a title to the table               |
