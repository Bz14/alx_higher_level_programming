#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insert node in a sorted linked list
 * @head: a linked list
 * @number: value to be inserted
 * Return: The node or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = (listint_t *)malloc(sizeof
						  (listint_t)), *current = *head;

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (current->next != NULL && current->next->n < number)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
