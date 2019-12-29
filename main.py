from pathlib import Path

from dozen_days_detector import detector, classifier


if __name__ == '__main__':
    path = Path(__file__).parent / 'data'
    images = []
    for ext in ('jpg', 'jpeg', 'png'):
        images.extend(list(path.glob(f'*.{ext}')))
    image_object_counts = detector.detect_multiple_images(images)
    matching = classifier.classify_images(image_object_counts)
    print(matching)
