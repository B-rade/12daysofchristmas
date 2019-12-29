from pathlib import Path
from typing import Dict, List
from collections import Counter

import cv2
import cvlib


def detect_multiple_images(filepaths: List[Path]) -> Dict[Path, Dict[str, int]]:
    result = dict()
    for path in filepaths:
        objects_detected = detect_single_image(path)
        result[path] = objects_detected
    return result


def detect_single_image(filepath: Path) -> Dict[str, int]:
    img = cv2.imread(str(filepath))
    bbox, labels, confidence = cvlib.detect_common_objects(img, confidence=0.5)
    # from cvlib.object_detection import draw_bbox

    # # draw bounding box over detected objects
    # out = draw_bbox(img, bbox, labels, confidence)
    # print(labels)
    # # display output
    # # press any key to close window
    # cv2.imshow("object_detection", out)
    # cv2.waitKey()

    # # release resources
    # cv2.destroyAllWindows()
    print(Counter(labels))
    return Counter(labels)
