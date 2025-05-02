"""
Program Name: remove-linked-list-duplicates

Description:
    This program removes duplicate integers in a linked list

Features:
    - Removes duplicate integers in a linked list

Dependencies:
    - None

Usage:
    python3 remove-linked-list-duplicates

Example:
    python3 remove-linked-list-duplicates

Author:
    Greg Nelson

Date Created:
    2025-05-02

Version:
    1.0.0

License:
    None

"""

from typing import Optional

class ListNode:
    """
    ListNode class that holds the nodes
    
    Attributes:
        val (int): The value stored in the node.
        next (ListNode, optional): The reference to the next node in the list.

    """
    def __init__(self, val=0, next=None):
        """
        Initializes a ListNode with a value and optional reference to the next node.

        Args:
            val (int, optional): The value to store in the node. Defaults to 0.
            next (ListNode, optional): The next node in the list. Defaults to None.
        """
        self.val = val
        self.next = next

class LinkedList:
    """
    A simple linked list class for maintaining references to the front and rear nodes.

    Attributes:
        front (ListNode): The first node in the list.
        rear (ListNode): The last node in the list.
    """
    def __init__(self):
        """
        Initializes an empty linked list with front and rear set to None.
        """
        
        self.front = None
        self.rear = None

class Solution:
    
    def remove_duplicates(self, head:Optional[ListNode]) -> Optional[ListNode]:
        """
        Removes all duplicate values from an unsorted singly linked list
        while preserving the original order of first occurrences.

        Args:
            head (ListNode): The head of the linked list.

        Returns:
            ListNode: The head of the modified linked list with duplicates removed.
        """
        current = head
        prev = None
        
        seen = set()
        
        while current:
            if current.val  in seen:
                prev.next = current.next # removing the current node
            else:
                seen.add(current.val) # adding the value to the set of seen values
                prev = current # moving the pointer forward
            current = current.next
        return head
        
def build_list(lst):
    """
    Builds a singly linked list from a list of integer values.

    Args:
        lst (list of int): A list of values to create nodes for.

    Returns:
        ListNode: The head node of the constructed linked list.
    """
    if not lst:
        return None

    head = ListNode(lst[0])
    current = head
    
    for vals in lst[1:]:
        current.next = ListNode(vals)
        current = current.next
    return head

def main():
    """
    Constructs a linked list, removes duplicates from it,
    and returns the head of the updated list.

    Returns:
        ListNode: The head of the linked list after duplicate removal.
    """
    head = build_list([1,2,2,3,4,4,5,4,5,6,4,3,2,7,8,6,5,9,8,0,2,0,8,7])
    result = Solution().remove_duplicates(head)
    return result
    

if __name__ == "__main__":
    head = main()
    
    while head:
        print(head.val, end="->")
        head = head.next
    print("None")