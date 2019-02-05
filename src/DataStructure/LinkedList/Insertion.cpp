#include <stdio.h>
#include <stdlib.h>

#include "LinkListBuilder.cpp"

int main()
{

    struct Node* head = NULL;
    linkListBuilder().append(&head, 6);
    linkListBuilder().push(&head, 7);
    linkListBuilder().push(&head, 1);
    linkListBuilder().append(&head, 4);
    linkListBuilder().insertAfter(head->next, 8);
    linkListBuilder().printList(head);
    return 0;
}