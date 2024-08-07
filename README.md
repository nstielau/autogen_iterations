# autogen_iterations
A repo of iterative attempts by autogen agents to solve a problem.

Specifically, there is a bug in autogen that was emitting a warning with a valid API key.

So I tried to get autogen to fix autogen!

## Prompt

Here is the prompt given to the assistant:

```
Write a python function called is_valid_api_key that passes the following unit tests.
The docstring of the function should identify all of the validation requirements.
Take your time, aim for correctness over speed.
The first line of every python file you generate should be "# filename:email_regex.py".
When you make a new iteration, summarize specifically what changed and why in a comment on the second line.

import unittest

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
```

## Git History

I modified the https://github.com/microsoft/autogen/blob/main/autogen/coding/local_commandline_code_executor.py file, so that it commits each iterative pass to git.

You can check out the iterations at 

* https://github.githistory.xyz/nstielau/autogen_iterations/blob/main/ai_regex_quiz__temp_0.95.py
* https://github.githistory.xyz/nstielau/autogen_iterations/blob/main/ai_regex_quiz__temp_0.py


## Temperature

Temperature was set a 0, and it was struggling to come up with a solution.

After that, I created temperature-specific files, using the git history as the log.  However, subsequent testing did not show as direct an impact of temperature.

## Result

Sadly, it never got an accurate result that I could commit to autogen. 