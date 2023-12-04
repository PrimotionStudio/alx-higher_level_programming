#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * rev_list - Reverse a linked list
 * @list: Pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *rev_list(listint_t *list)
{
	listint_t *p = NULL, *c = list, *n = NULL;

	while (c != NULL)
	{
		n = c->next;
		c->next = p;
		p = c;
		c = n;
	}
	list = p;
	return (list);
}

/**
 * is_palindrome - Check if a linked list is a palindrome
 * @head: Pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *demo = *head, *middle_list = *head;
	int i = 0, middle_flag, n = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (demo != NULL)
	{
		i++;
		demo = demo->next;
	}
	middle_flag = i / 2;
	while (n < middle_flag)
	{
		middle_list = middle_list->next;
		n++;
	}
	middle_list = rev_list(middle_list);
	while (middle_list != NULL && *head != NULL)
	{
		if (middle_list->n != (*head)->n)
			return (0);
		middle_list = middle_list->next;
		*head = (*head)->next;
	}
	return (1);
}
