import os
import pytest

from pythonModuleSample.Sample1.Sample1 import Sample1

@pytest.fixture(autouse=True)
def set_env_vars():
    os.environ.setdefault("SAMPLE_ENV_VAR", "default_value")

def test_hello_world():
    sample = Sample1()
    assert sample.hello_world() == "Hello, World!"
    
def test_hello_world_with_env_var():
    os.environ["HELLO_STRING"] = "Hello, Test!"
    sample = Sample1()
    assert sample.hello_world() == "Hello, Test!"
    
def test_fixture_sample_env_var():
    assert os.environ["SAMPLE_ENV_VAR"] == "default_value"
    os.environ["SAMPLE_ENV_VAR"] = "sample_value"
    assert os.environ["SAMPLE_ENV_VAR"] == "sample_value"

def test_get_some_var():
    sample = Sample1()
    assert sample.get_some_var() == "some_var"

def test_get_some_var_with_change():
    sample = Sample1()
    sample.some_var = "new_var"
    assert sample.get_some_var() == "new_var"