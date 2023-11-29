#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *current, *prev = NULL;

	if (*head == NULL) {
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	current = *head;
	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	if (prev == NULL || prev->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (*new_node);
	}
	new_node->n = number;
	while (current->next != NULL)
	{
		if (prev != NULL && prev->n < number && current->n > number)
		{
			new_node->next = prev->next;
			prev->next = new_node;
			return (new_node);
		}
		prev = current;
		current = current->next;
	}
	prev->next = new_node;
	new_node->next = NULL;
	return (new_node);
}
