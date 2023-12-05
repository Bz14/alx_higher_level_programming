#include "lists.h"
/**
 * check_cycle - Check whether linked list has cycle or not
 * @list: a linked list
 * Retrn: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list, *second = list;

	if (list == NULL || list->next == NULL)
		return (0);
	while (second != NULL && second->next != NULL)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
