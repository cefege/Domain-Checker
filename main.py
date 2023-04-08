import domainChecker

is_found: bool = domainChecker.is_domain_available("Google.com")
if is_found:
    print("Domain Found.")
else:
    print("Domain is not Found.")
