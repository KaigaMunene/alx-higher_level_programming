#include "lists.h"

/**
 * insert_node - Insert @number
 *
 * @head: Sorted singly linked list
 * @number: Number to be inserted into @head
 *
 * Return:  Success: Address of the new node
 *          Failure: NULL
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *current = *head;
listint_t *new;

new = malloc(sizeof(listint_t));
if (new == NULL)
    return (NULL);
new->n = number;

if (*head == NULL)
{
new->next = NULL;
*head = new;
return (*head);
}
while (current != NULL)
{
if (number < current->n)
{
new->next = *head;
*head = new;
return (*head);
}
else 
{
    if (current->next == )
}
}
}