#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *fast = NULL, *slow = NULL;

	fast = (listint_t *)malloc(sizeof(list));
	if (!fast)
		return (-1);
	slow = (listint_t *)malloc(sizeof(list));
	if (!slow)
	{
		free(fast);
		return (-1);
	}
	fast = list->next;
	slow = list;
	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		if (fast == slow)
		{
			free(fast);
			free(slow);
			return (1);
		}
		fast = fast->next->next;
		slow = slow->next;
	}
	free(fast);
	free(slow);
	return (0);
}
