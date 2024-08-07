# autogen_iterations
A repo of iterative attempts by autogen agents to solve a problem.

## Prompt

Here is the prompt given to the assistant:

```
Write a python function called is_valid_api_key that passes the following assertions.
The docstring of the function should identify all of the validation requirements.
Take your time, aim for correctness over speed.
The first line of every python file you generate should be "# filename:ai_regex_quiz__temp_0.5.py".
When you make a new iteration, summarize specifically what changed and why in a comment on the second line.

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
    assert is_valid_api_key(MOCK_OPEN_AI_API_KEY)
```

## Git History

I modified the https://github.com/microsoft/autogen/blob/main/autogen/coding/local_commandline_code_executor.py file, so that it commits each iterative pass to git.

Iterestingly, it s

# Temperature

Temperature was set a 0, and it was struggling to come up with a solution.  When I bumped the temperature to 0.95, it came up with a solution on the first iteration.

After that, I created temperature-specific files, using the git history as the log.  However, subsequent testing did not show as direct an impact of temperature.

