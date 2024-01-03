#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the first element.
 * @number: data to be inserted.
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head, *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (ptr == NULL || new->n < ptr->n)
	{
		new->next = ptr;
		*head = new;
		return (*head);
	}
	while (ptr)
	{
		if (!ptr->next || new->n < ptr->next->n)
		{
			new->next = ptr->next;
			ptr->next = new;
			return (ptr);
		}
		ptr = ptr->next;
	}
	return (NULL);
}
