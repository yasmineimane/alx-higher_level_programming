#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: lisked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr;

	if (list == NULL)
		return (0);

	if (list->next == list)
		return (1);

	ptr = list->next;
	while (ptr != NULL)
	{
		if (ptr == list)
			return (1);
		ptr = ptr->next;
	}
	return (0);
}
