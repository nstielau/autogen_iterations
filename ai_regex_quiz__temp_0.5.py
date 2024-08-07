# filename: ai_regex_quiz__temp_0.5.py
# Updated the regular expression to allow underscores and hyphens within the alphanumeric segments of the API key.
import re

def is_valid_api_key(api_key: str) -> bool:
    """
    Validate the API key based on the following criteria:
    - Must start with 'sk-'.
    - Must not start with 'SK-'.
    - Must contain a mix of alphanumeric characters and possibly special characters.
    - Must not contain invalid characters like '%'.
    - Can contain hyphens but should not have consecutive hyphens (except in specific cases).
    - Should be at least 20 characters long.
    """
    if not api_key.startswith("sk-"):
        return False
    if api_key.startswith("SK-"):
        return False
    if len(api_key) < 20:
        return False
    if "%" in api_key:
        return False
    # Check for invalid consecutive hyphens
    if re.search(r'[^-]--[^-]', api_key):
        return False
    # Check for valid pattern
    pattern = re.compile(r'^sk(-[a-zA-Z0-9_]+)+$')
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
    assert is_valid_api_key("MOCK_OPEN_AI_API_KEY")

# Run the test function
test_is_valid_api_key()
print("All tests passed.")