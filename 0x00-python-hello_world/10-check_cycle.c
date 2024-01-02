#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: lisked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list, *second = list;

	while (second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
