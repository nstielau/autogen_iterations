# filename:ai_regex_quiz__temp_0.95_v2.py
"""
Updates:
- Refined regex to explicitly manage valid prefixes and ensure correct validation of alphanumeric characters and hyphens.
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
    pattern = re.compile(
        r'^(sk-('
        r'proj-(?!$)|'  # Match 'sk-proj-' without filtering the string end
        r'aut0gen-(?!$)|'  # Match 'sk-aut0gen-' without filtering the string end
        r'aut0-gen-(?!$)|'  # Match 'sk-aut0-gen-' without filtering the string end
        r'aut0--gen-(?!$)|'  # Match 'sk-aut0--gen-' without filtering the string end
        r'aut0-gen--(?!$)|'  # Match 'sk-aut0-gen--' without filtering the string end
        r'[a-zA-Z0-9]+-)'  # Match 'sk-' followed by at least one alphanumeric character and a hyphen
        r'[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?$'  # Ensure the rest of the key is valid alphanumeric with valid hyphen placement
    )
    return bool(pattern.match(api_key))


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