import argparse
import csv
import os.path
import re
import subprocess as sp


def is_domain_available(domain):
    # Run the nslookup command and capture the output
    result = sp.run(['nslookup', domain], stdout=sp.PIPE).stdout.decode("utf8")
    # NXDOMAIN is the response from the DNS server when the domain is not found
    if "NXDOMAIN" in result:
        return False
    else:
        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Domain Checker Tool")
    parser.add_argument("-d", "--domain", type=str, help="Domain Name")
    parser.add_argument("-i", "--input", type=str, nargs='?',
                        help="Path to txt file containing \\n separated domain names")
    parser.add_argument("-o", "--output", type=str, nargs='?', help="Path to output CSV file")

    args = parser.parse_args()
    if args.domain and re.findall(r"^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9](?:\.[a-zA-Z]{2,})+$", args.domain):
        is_found = is_domain_available(args.domain)
        if is_found:
            print("Domain Found.")
        else:
            print("Domain is not Found.")

    elif args.input:
        if not args.output:
            print("Please enter a valid output path")
            exit()

        if os.path.exists(args.input):
            with open(args.input, "r") as fin:
                domains = fin.readlines()
                with open(args.output, 'w') as fout:
                    writer = csv.writer(fout)
                    writer.writerow(['Domain Name', 'Found'])
                    for domain_name in domains:
                        domain_name = domain_name.strip()
                        writer.writerow([domain_name, is_domain_available(domain_name)])
            print(f"{args.output} File Exported Successfully")
        else:
            print(f"Source File Doesn't Exist")

    else:
        print("Invalid Arguments. Please refer to --help for more info")
