import subprocess
import pytest  # noqa: F401
import os

fn_name = "greppo_logic"


class ImportDetailsError(Exception):
    pass


def run_script(*args):
    cmd = ["python", "greppo.py"] + list(args)
    result = subprocess.run(cmd, text=True, capture_output=True)

    if result.stdout:
        result.stdout = result.stdout.replace(test_file(""), "")

    return result.stdout, result.returncode


def test_file(file_name):
    return os.path.join(".autograde", file_name)


try:
    # Test cases for greppo_logic.py

    import greppo_logic as uppgift

    fn = getattr(uppgift, fn_name)

    if not callable(fn):
        raise ImportDetailsError(f"Function {fn_name} is not callable")

    if not fn.__code__.co_argcount == 4:
        raise ImportDetailsError(f"Function {fn_name} must take exactly four arguments")

    def test_greppo_logic_example_two_search_strings():
        filenames = ["filnamn1"]
        search_terms = ["one", "two"]
        matches = fn(search_terms, filenames, False, False)
        expected = (0, ["filnamn1:one", "filnamn1:two"])
        assert matches == expected

    def test_greppo_logic_example_o_as_search_string():
        filenames = ["filnamn1"]
        search_terms = ["o"]
        matches = fn(search_terms, filenames, False, False)
        expected = (0, ["filnamn1:one", "filnamn1:two", "filnamn1:four"])
        assert matches == expected

    def test_greppo_logic_example_linennumbers():
        filenames = ["filnamn2"]
        search_terms = ["o"]
        matches = fn(search_terms, filenames, False, True)
        expected = (
            0,
            ["filnamn2:1:boat", "filnamn2:4:helicopter", "filnamn2:5:rocket"],
        )
        assert matches == expected

    def test_greppo_logic_example_inverted_linennumbers():
        filenames = ["filnamn1", "filnamn2"]
        search_terms = ["e"]
        matches = fn(search_terms, filenames, True, True)
        expected = (
            0,
            ["filnamn1:2:two", "filnamn1:4:four", "filnamn2:1:boat", "filnamn2:2:car"],
        )
        assert matches == expected

    def test_greppo_logic_no_match():
        filenames = ["filnamn1"]
        search_terms = ["six"]
        matches = fn(search_terms, filenames, False, False)
        assert matches == (1, [])

    # Test cases for greppo.py

    def test_script_example_two_search_strings():
        output, exit_code = run_script(
            "--search", "one", "--search", "two", test_file("filnamn1")
        )
        expected_output = "filnamn1:one\nfilnamn1:two\n"
        assert output == expected_output
        assert exit_code == 0

    def test_script_example_o_as_search_string():
        output, exit_code = run_script("--search", "o", test_file("filnamn1"))
        expected_output = "filnamn1:one\nfilnamn1:two\nfilnamn1:four\n"
        assert output == expected_output
        assert exit_code == 0

    def test_script_example_linenumbers():
        output, exit_code = run_script("--search", "o", "-n", test_file("filnamn2"))
        expected_output = "filnamn2:1:boat\nfilnamn2:4:helicopter\nfilnamn2:5:rocket\n"
        assert output == expected_output
        assert exit_code == 0

    def test_script_example_inverted_linenumbers():
        output, exit_code = run_script(
            "--search", "e", "-v", "-n", test_file("filnamn1"), test_file("filnamn2")
        )
        expected_output = (
            "filnamn1:2:two\nfilnamn1:4:four\nfilnamn2:1:boat\nfilnamn2:2:car\n"
        )
        assert output == expected_output
        assert exit_code == 0

    def test_script_no_match():
        output, exit_code = run_script("--search", "six", test_file("filnamn1"))
        expected_output = ""
        assert output == expected_output
        assert exit_code == 1

except ImportDetailsError as e:
    pytest.fail(str(e))

except ImportError:
    pytest.fail(f"Function {fn_name} has not been implemented")
