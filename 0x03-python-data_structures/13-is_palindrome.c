#include <stddef.h>
#include "lists.h"

int is_palindrome(listint_t **head) {
    if (head == NULL || *head == NULL) {
        return 1; // An empty list is considered a palindrome
    }

    // Find the middle of the linked list
    listint_t *slow = *head, *fast = *head, *prev = NULL, *temp = NULL;
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        // Reverse the first half while finding the middle
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    // If the list has an odd number of elements, skip the middle element
    if (fast != NULL) {
        slow = slow->next;
    }

    // Compare the reversed first half with the second half
    while (slow != NULL) {
        if (prev->n != slow->n) {
            return 0; // Not a palindrome
        }
        slow = slow->next;
        prev = prev->next;
    }

    return 1; // The list is a palindrome
}

