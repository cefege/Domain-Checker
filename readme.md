# Domain Checker Tool

This is a command-line tool that checks if a domain is available using the DNS `nslookup` command. It can also take input from a text file containing a list of domain names and output a CSV file with the results.

## Usage

The tool can be run in two modes:

1. Single Domain Check: Checks if a single domain is available.

```
python domain_checker.py -d <domain_name>
```

For example:

```
python domain_checker.py -d google.com
```

2. Batch Check: Checks a list of domains in a text file and outputs the results to a CSV file.

```
python domain_checker.py -i <input_file_path> -o <output_file_path>
```

For example:

```
python domain_checker.py -i domains.txt -o results.csv
```

## Arguments

The tool has the following arguments:

* `-d, --domain`: Domain name to check.
* `-i, --input`: Path to a text file containing a list of domain names.
* `-o, --output`: Path to the output CSV file.

## Output

The tool outputs the following messages:

* `Domain Found.` if the domain is found.
* `Domain is not Found.` if the domain is not found.
* `<output_file_path> File Exported Successfully` if the output file is created successfully.
* `Please enter a valid output path` if no output path is provided for batch check.
* `Source File Doesn't Exist` if the input file doesn't exist.
* `Invalid Arguments. Please refer to --help for more info` if invalid arguments are provided.

## Examples

Single Domain Check:

```
python domain_checker.py -d google.com
```

Batch Check:

```
python domain_checker.py -i domains.txt -o results.csv
```
