# filename:ai_regex_quiz__temp_0.95.py
# Fixed: Split the regex into manageable checks to handle valid placements of double hyphens.

"""
Function to validate API key based on specific criteria.

Validation requirements:
- The key must not be an empty string.
- The key must start with "sk-" (case-sensitive).
- The key must not have "--" consecutively, except after "sk-" and within "-gen-".
- The key can contain alphanumeric characters, hyphens (-), and underscores (_).
- The key must have a minimum length of 30 characters.
"""

import re

def is_valid_api_key(api_key):
    if not isinstance(api_key, str) or len(api_key) < 30:
        return False
    if not api_key.startswith("sk-"):
        return False
    if re.search(r'[^a-zA-Z0-9\-_]', api_key):
        return False
    
    # Handle double hyphens "--"
    if '--' in api_key:
        # It must be handled in contexts: "sk--" and within "-gen-"
        if not api_key.startswith("sk--") and "--gen-" not in api_key:
            return False
        # Ensure the double hyphens are correctly positioned
        if api_key.startswith("sk--"):
            parts = api_key.split("--", 1)
            if not re.match(r'^[a-zA-Z0-9\-_]*$', parts[1]):
                return False
        if "--gen-" in api_key:
            parts = api_key.split("--gen-", 1)
            if not re.match(r'^[a-zA-Z0-9\-_]*$', parts[0]) or not re.match(r'^[a-zA-Z0-9\-_]*$', parts[1]):
                return False
    else:
        # If there's no double hyphen, ensure it's valid
        if not re.match(r'^sk-[a-zA-Z0-9\-_]*$', api_key):
            return False

    return True

import time

def test_is_valid_api_key():
    time.sleep(2)
    assert not is_valid_api_key("")
    assert not is_valid_api_key("sk-")
    assert not is_valid_api_key("SK-")
    assert not is_valid_api_key("sk-asajsdjsd2")
    assert not is_valid_api_key("FooBar")
    assert not is_valid_api_key("sk-asajsdjsd22372%23kjdfdfdf2329ffUUDSDS")
    assert is_valid_api_key("sk-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS")
    assert is_valid_api_key("sk-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS1212121221212sssXX")
    assert is_valid_api_key("sk-proj-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")
    assert is_valid_api_key("sk-proj-asajsdjsd22372X23kjdfdfdf2329f212_gsirb23Yu7vv4vD4-B2iQkbC")
    assert is_valid_api_key("sk-0-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")
    assert is_valid_api_key("sk-aut0gen-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")
    assert is_valid_api_key("sk-aut0-gen-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")
    assert is_valid_api_key("sk-aut0--gen-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")
    assert is_valid_api_key("sk-aut0-gen--asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")
    assert not is_valid_api_key("sk-aut0-gen--asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")
    assert not is_valid_api_key("sk--aut0-gen-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")
    assert is_valid_api_key("sk-aut0-gen-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")

test_is_valid_api_key()
print("All tests passed!")