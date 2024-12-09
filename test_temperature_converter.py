import pytest
from temperature_converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit,
)

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40

def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(-273.15) == 0

def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == 0
    assert kelvin_to_celsius(0) == -273.15

def test_fahrenheit_to_kelvin():
    assert fahrenheit_to_kelvin(32) == pytest.approx(273.15, rel=1e-3)
    assert fahrenheit_to_kelvin(-459.67) == pytest.approx(0, rel=1e-3)

def test_kelvin_to_fahrenheit():
    assert kelvin_to_fahrenheit(273.15) == 32
    assert kelvin_to_fahrenheit(0) == pytest.approx(-459.67, rel=1e-3)

def test_kelvin_to_celsius_negative_check():
    with pytest.raises(ValueError):
        kelvin_to_celsius(-1)