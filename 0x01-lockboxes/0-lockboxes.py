#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Function that checks with a boolean value if the list type and
    length to invoke two for iterations, one to traverse the list
    """
    if not isinstance(boxes, list):
        return False
    elif not boxes:
        return False

    for key in range(len(boxes)):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = key in boxes[idx] and key != idx
            if boxes_checked:
                break
        if not boxes_checked:
            return boxes_checked

    return True
