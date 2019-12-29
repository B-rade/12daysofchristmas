from pathlib import Path
import json

from dozen_days_detector import classifier


DATA_DIR = Path(__file__).parent / 'data'


def load_data(filename):
    with open(DATA_DIR / filename) as file:
        return json.load(file)


def test_simple_classifier():
    input_data = load_data('simple_match_input.json')
    expected_output_data = load_data('simple_match_output.json')
    actual_output_data = classifier.classify_images(input_data)
    assert actual_output_data == expected_output_data


def test_complex_classifier():
    input_data = load_data('complex_match_input.json')
    expected_output_data = load_data('complex_match_output.json')
    actual_output_data = classifier.classify_images(input_data)
    assert actual_output_data == expected_output_data
