#include "lists.h"
/**
 * is_palindrome - check wheterher the linked list is palindrome or not
 * @head: a linked list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *first = *head, *second = *head, *prev = NULL, *tmp = NULL;

	if (*head == NULL)
		return (1);
	while (first && first->next)
	{
		first = first->next->next;
		tmp = second;
		second = second->next;
		tmp->next = prev;
		prev = tmp;
	}
	if (first != NULL)
		second = second->next;
	while (prev && second)
	{
		if (prev->n != second->n)
			return (0);
		prev = prev->next;
		second = second->next;
	}
	return (1);
}
