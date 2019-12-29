from pathlib import Path

from dozen_days_detector import detector


DATA_DIR = Path(__file__).parent / 'data'


def test_simple_image():
    filepath = DATA_DIR / '12_apples.jpg'
    expected_output = {"apple": 12}
    assert detector.detect_single_image(filepath) == expected_output
