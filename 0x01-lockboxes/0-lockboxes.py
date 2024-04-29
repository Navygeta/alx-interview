"""
0-lockboxes.py
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if len(boxes) == 0:
        return False

    opened = set()
    opened.add(0)

    queue = [0]

    while queue:
        current = queue.pop(0)

        for key in boxes[current]:
            if key < len(boxes) and key not in opened:
                opened.add(key)
                queue.append(key)

    return len(opened) == len(boxes)
