class EmailChecker:
    def __init__(self):
        self.special_domains = ['google.com', 'gmail.com', 'outlook.com', 'yahoo.com', 'proton.me']
        self.special_subdomains = ['.co.uk']

    def _is_valid_domain(self, domain):
        return domain.lower() in self.special_domains or domain.endswith('.com')

    def _is_special_case(self, email):
        parts = email.split('@')
        local_part, domain = parts[0], parts[1].split('.')
        return len(domain) > 1 and domain[-1] == 'co'

    def _warn_for_special_domain(self, email):
        parts = email.split('@')
        domain = parts[1].lower()
        if domain not in self.special_domains and domain != 'create':
            print(f"Warning: {email} has a special domain ({domain})")

    def check_email(self, email):
        email = email.lower()
        if len(email) > 255 or len(email.split('@')[0]) > 64:
            return False, None

        parts = email.split('@')
        if len(parts) < 2:
            return False, None  # Not enough parts to split into local part and domain

        local_part, domain = parts[0], parts[1].split('.')
        if len(local_part) < 1 or len(domain) < 1:
            return False, None

        if local_part.count('@') != 0 or domain.count('.') != 1:
            return False, None

        if '.' not in local_part:
            return False, None

        if not self._is_valid_domain(domain):
            return False, None

        if self._is_special_case(email):
            print("Special case detected:", email)

        self._warn_for_special_domain(email)

        return True, None


# Define test cases
test_cases = [
    ("hmm", False),
    ("hmm@google.corn", False),
    ("hmm.hi@gmail.com", True),
    ("hmm.hi@outlook.com", False),
    ("hmm@hi", False),
    ("hi@hi@yahoo.com", False),
    ("hi@outlook.com", True),
    ("WOW@nice.co.uk", True),
    ("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh", False),
    ("wow@private.com", True),
    ("wo@hell.create", False),
    ("test@yahoo.co.uk", True),
]

# Initialize the EmailChecker
checker = EmailChecker()

# Loop through test cases
for test_input, expected_result in test_cases:
    result, warning = checker.check_email(test_input)
    if result == expected_result:
        print(f"{test_input}: Passed")
    else:
        print(f"{test_input}: Failed - Expected {expected_result}, Got {result}")
        if warning:
            print(warning)
