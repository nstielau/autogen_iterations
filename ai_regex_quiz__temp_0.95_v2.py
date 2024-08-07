# filename:ai_regex_quiz__temp_0.95_v2.py
"""
Updates:
- Enhanced regex pattern to ensure valid prefixes and correct non-prefix sequences.
"""

import re

def is_valid_api_key(api_key):
    """
    Validate if the provided API key meets the following requirements:
    - Must start with 'sk-', 'sk-proj-', 'sk-aut0gen-', 'sk-aut0-gen-', 'sk-aut0--gen-', or 'sk-aut0-gen--'.
    - After the prefix, there must be at least one alphanumeric character.
    - Can contain uppercase letters, lowercase letters, digits, and hyphens, but no invalid consecutive hyphens or character sequences.
    
    Args:
    api_key (str): The API key string to validate.
    
    Returns:
    bool: True if valid, False otherwise.
    """
    
    # Define valid prefixes
    valid_prefixes = [
        'sk-', 'sk-proj-', 'sk-aut0gen-', 'sk-aut0-gen-', 'sk-aut0--gen-', 'sk-aut0-gen--'
    ]
    
    # Check if the api_key starts with any valid prefix, and strip it off for further validation
    for prefix in valid_prefixes:
        if api_key.startswith(prefix):
            post_prefix = api_key[len(prefix):]
            # Validate the remaining part of the api_key (must contain alphanumeric, hyphen allowed as separator)
            if re.match(r'^([a-zA-Z0-9]+(-[a-zA-Z0-9]+)*)$', post_prefix):
                return True
            break
    
    return False


def test_is_valid_api_key():
    import time
    time.sleep(2)
    # Invalid cases
    assert not is_valid_api_key("")
    assert not is_valid_api_key("sk-")
    assert not is_valid_api_key("SK-")
    assert not is_valid_api_key("sk-asajsdjsd2")
    assert not is_valid_api_key("FooBar")
    assert not is_valid_api_key("sk-asajsdjsd22372%23kjdfdfdf2329ffUUDSDS")
    assert not is_valid_api_key("sk-aut0-gen--asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")
    assert not is_valid_api_key("sk--aut0-gen-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")

    # Valid cases
    assert is_valid_api_key("sk-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS")
    assert is_valid_api_key("sk-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS1212121221212sssXX")
    assert is_valid_api_key("sk-proj-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")
    assert is_valid_api_key("sk-proj-asajsdjsd22372X23kjdfdfdf2329f212_gsirb23Yu7vv4vD4-B2iQkbC")
    assert is_valid_api_key("sk-0-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")
    assert is_valid_api_key("sk-aut0gen-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")
    assert is_valid_api_key("sk-aut0-gen-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")
    assert is_valid_api_key("sk-aut0--gen-asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")
    assert is_valid_api_key("sk-aut0-gen--asajsdjsd22372X23kjdfdfdf2329ffUUDSDS12121212212")

print("Testing the function...")
test_is_valid_api_key()
print("All tests passed.")