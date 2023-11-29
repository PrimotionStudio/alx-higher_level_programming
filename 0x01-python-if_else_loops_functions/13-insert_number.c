
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = NULL, *rep_node = *head, *prev_node = NULL;

    /** If empty list  */
    if (*head == NULL)
    {
        *head = (listint_t *)malloc(sizeof(listint_t));
        if (*head == NULL)
            return (NULL);
        (*head)->n = number;
        (*head)->next = NULL;
        return (*head);
    }

    /** Memory Allocation */
    new_node = (listint_t *)malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    /** Insert at beginning */
    if ((*head)->n > number)
    {
        new_node->next = *head;
        (*head)->next = new_node;
        return (new_node);
    }

    /** Insert at the middle */
    while (rep_node != NULL)
    {
        if (rep_node->n > number)
            break;
        /** rep_node === cur_node*/
        prev_node = rep_node;
        rep_node = rep_node->next;
    }

    new_node->next = rep_node;
    prev_node->next = new_node;
    return (new_node);
}

