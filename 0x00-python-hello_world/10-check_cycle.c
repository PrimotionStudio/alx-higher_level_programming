#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * check_cycle - Used to check if there is a cycle
  * @list: The list checked
  * Return: 1, 0 or -1
  */
/*
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
}*/
int checklist(listint_t *mainlist, listint_t *list, int pos)
{
	while (list != NULL)
	{

}
