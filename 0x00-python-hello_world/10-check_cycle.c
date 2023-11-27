#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * check_cycle - Used to check if there is a cycle
  * @list: The list checked
  * Return: 1, 0 or -1
  */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	if (slow == NULL && fast->next == NULL)
		return (0);
	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		if (fast == slow)
		{
			return (1);
		}
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
