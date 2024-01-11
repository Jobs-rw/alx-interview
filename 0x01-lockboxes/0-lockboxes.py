#!/usr/bin/python3

"""
      You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
    
"""


def canUnlockAll(boxes):
    """
    Function that checks with boolean value if the list type and
    length to invoke two for iterations one to traverse the list
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for a in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = a in boxes[idx] and a != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
