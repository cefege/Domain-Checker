# Domain Checker

## Installation
### Using pip
```angular2html
pip install git+https://github.com/cefege/Domain-Checker.git
```
or clone the repository
```angular2html
git clone https://github.com/cefege/Domain-Checker.git
```
## Usage
1. Import `domainChecker` 
```
import domainChecker
```
2. pass the domain name to the `is_domain_available` function
```angular2html
is_found: bool = domainChecker.is_domain_available("Google.com")
```

### Or From Command Line
- For a Single Domain
```angular2html
python domainChecker/domain_checker.py -d "google.com"
```

- For Multiple Domains
```angular2html
python domainChecker/domain_checker.py -i domains.txt -o output.csv 
```
