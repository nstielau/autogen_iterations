# filename:ai_regex_quiz__temp_0.py
# Updated to allow underscores in the API key

"""
This function validates an API key based on the following rules:
1. The key must start with "sk-".
2. The key can contain alphanumeric characters, hyphens, and underscores.
3. The key should not contain consecutive hyphens.
4. The key should not end with a hyphen.
5. The key should be of a certain length (not too short).
"""

import re

def is_valid_api_key(api_key):
    # Check if the key starts with "sk-"
    if not api_key.startswith("sk-"):
        return False
    
    # Check for consecutive hyphens
    if "--" in api_key:
        return False
    
    # Check if the key ends with a hyphen
    if api_key.endswith("-"):
        return False
    
    # Check the length of the key (assuming a minimum length of 20 characters for validity)
    if len(api_key) < 20:
        return False
    
    # Check if the key contains only valid characters (alphanumeric, hyphens, and underscores)
    if not re.match(r'^sk-[a-zA-Z0-9-_]+$', api_key):
        return False
    
    return True

def test_is_valid_api_key():
    import time
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
    assert is_valid_api_key("MOCK_OPEN_AI_API_KEY")

test_is_valid_api_key()
print("All tests passed.")