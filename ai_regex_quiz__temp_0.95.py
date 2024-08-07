# filename:ai_regex_quiz__temp_0.95.py
# Fixed: Combined validation logic to handle specific cases more accurately.

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

    # Split on double hyphens
    parts = api_key.split('--')

    # Check that we don't have more than one double-hyphen split
    if len(parts) > 2:
        return False
    
    # Check each part individually
    for i, part in enumerate(parts):
        if i == 0:
            if not re.match(r'^sk-[a-zA-Z0-9\-_]*$', part):
                return False
        else:
            if "-gen-" in part:
                before_gen, after_gen = part.split('-gen-', 1)
                if not (re.match(r'^[a-zA-Z0-9\-_]*$', before_gen) and re.match(r'^[a-zA-Z0-9\-_]*$', after_gen)):
                    return False
            else:
                if not re.match(r'^[a-zA-Z0-9\-_]*$', part):
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