#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * listint_t *insert_node - This function inserts a node in
 * a sorted singly linked list
 *
 * @head: This is the reference to the whole linked list
 * @number: Number to be inserted into the given linked list
 *
 * Return: an updated linked list on SUCCESS or NULL on FAILURE
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *mover;

	mover = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n >= new->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (mover->next != NULL)
	{
		if ((mover->next)->n >= new->n)
		{
			new->next = mover->next;
			mover->next = new;
			return (new);
		}
		mover = mover->next;
	}

	new->next = NULL;
	mover->next = new;

	return (new);
}
