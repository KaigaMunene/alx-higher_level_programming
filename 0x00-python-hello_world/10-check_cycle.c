#include "lists.h"

/**
 * check_cycle - checks if @list is a circular list
 * @list: Asingly linked list
 *
 * Return:  (0) @list is not circulary linked
 *          (1) @list is ciculary linked
 */

int check_cycle(listint_t *list)
{
int *address = &list->n;
int flag = 0;

while (list != NULL)
{
if (flag != 0)
{
if (&list->n == address)
{
return (1);
}
}
flag = 1;
list = list->next;
}
return (0);
}
