# filename:ai_regex_quiz__temp_0.95_v2.py
"""
Updates:
- Ensured detailed handling of hyphens in regex to cover the validation criteria accurately.
"""

import re

def is_valid_api_key(api_key):
    """
    Validate if the provided API key meets the following requirements:
    - Must start with a valid prefix: 'sk-', 'sk-proj-', 'sk-aut0gen-', 'sk-aut0-gen-', 'sk-aut0--gen-', or 'sk-aut0-gen--'.
    - After the prefix, there must be at least one alphanumeric character.
    - Can contain uppercase letters, lowercase letters, digits, and hyphens, but no invalid consecutive hyphens.
    
    Args:
    api_key (str): The API key string to validate.
    
    Returns:
    bool: True if valid, False otherwise.
    """
    
    valid_prefixes = [
        'sk-', 'sk-proj-', 'sk-aut0gen-', 'sk-aut0-gen-', 'sk-aut0--gen-', 'sk-aut0-gen--'
    ]
    if any(api_key.startswith(prefix) for prefix in valid_prefixes):
        # Extract the part after the valid prefix
        for prefix in valid_prefixes:
            if api_key.startswith(prefix):
                after_prefix = api_key[len(prefix):]
                break
        
        # Check that the part after the prefix has no consecutive hyphens and contains alphanumeric characters only
        if re.match(r'^[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*$', after_prefix):
            return True

    return False


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

print("Testing the function...")
test_is_valid_api_key()
print("All tests passed.")