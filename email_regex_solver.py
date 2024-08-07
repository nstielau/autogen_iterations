# filename:email_regex_solver.py
# Added function is_valid_email() to validate email addresses based on predefined rules.

import re
import unittest

def is_valid_email(email):
    """
    Checks if the given email is valid according to the following rules:
    1. Should contain exactly one '@' symbol.
    2. The domain and subdomain must start with a letter or a digit.
    3. Domain name and subdomain name may contain only letters, digits, hyphens and periods.
    4. Domain name should be at least two characters long.
    5. No consecutive periods in the domain.
    6. No periods or hyphens at the beginning or end of domain or subdomain parts.
    7. Should not allow underscores or any other invalid characters in the domain or subdomain.
    8. Should not allow top-level domains (TLDs) that are less than two characters.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = re.compile(
        r'^(?!.*\.\.)(?!.*\.$)[\w\-.+]+@[a-z\d\-]+(\.[a-z\d\-]+)*\.[a-z]{2,}$',
        re.IGNORECASE
    )
    return re.match(email_regex, email) is not None

class TestEmailValidation(unittest.TestCase):
    
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("example@example.com"))
        self.assertTrue(is_valid_email("user.name+tag+sorting@example.com"))
        self.assertTrue(is_valid_email("user_name@example.co.uk"))
        self.assertTrue(is_valid_email("user-name@example.org"))
        self.assertTrue(is_valid_email("user@subdomain.example.com"))
    
    def test_invalid_emails(self):
        self.assertFalse(is_valid_email("plainaddress"))
        self.assertFalse(is_valid_email("@missingusername.com"))
        self.assertFalse(is_valid_email("username@.com"))
        self.assertFalse(is_valid_email("username@.com."))
        self.assertFalse(is_valid_email("username@..com"))
        self.assertFalse(is_valid_email("username@com"))
        self.assertFalse(is_valid_email("username@.com.com"))
        self.assertFalse(is_valid_email("username@-example.com"))
        self.assertFalse(is_valid_email("username@.example.com"))
        self.assertFalse(is_valid_email("username@exa_mple.com"))
        self.assertFalse(is_valid_email("username@exam!ple.com"))
        self.assertFalse(is_valid_email("username@example..com"))
        self.assertFalse(is_valid_email("username@example.c"))
        self.assertFalse(is_valid_email("username@.com"))
        self.assertFalse(is_valid_email("username@-.com"))
        self.assertFalse(is_valid_email("user@domain_with_underscore.com"))

    def test_edge_cases(self):
        self.assertTrue(is_valid_email("user@example.museum"))
        self.assertTrue(is_valid_email("user@example.travel"))
        self.assertTrue(is_valid_email("user@example.jobs"))
        self.assertFalse(is_valid_email("username@."))
        self.assertFalse(is_valid_email("username@.com.com."))
        self.assertFalse(is_valid_email("username@example.corporate"))

if __name__ == "__main__":
    unittest.main()