#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Function that checks with a boolean value if the list type and
    length to invoke two while loops, one to traverse the list
    and the other to compare if key is idx or not in order to open
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    
    k = 1
    while k < len(boxes) - 1:
        idx = 0
        boxes_checked = False
        while idx < len(boxes):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
            idx += 1
        if boxes_checked is False:
            return boxes_checked
        k += 1

    return True
