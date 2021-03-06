# StalinSort

A pure python implementation for Stalin-Sort

**Time Complexity: O(n)**

## Algorithm

The algorithm starts with an unsorted list. It then iterates down the list and tests each element on whether it is in order. Any element that is out of order is eliminated. At the end you have a sorted list.

## Example

```python
>>> import stalinsort
>>> l = [3, 2, 5, 7, 1, 3]
>>> stalinsort.sort(l, sort_min_max = True)
[1, 2, 3, 7]
```
