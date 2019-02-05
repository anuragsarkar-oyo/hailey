//
// Created by Anurag Sarkar on 2019-02-03.
//

#ifndef HAILEY_LINKLISTBUILDER_H
#define HAILEY_LINKLISTBUILDER_H

#endif //HAILEY_LINKLISTBUILDER_H


#include <iostream>

struct Node {
    int data;
    Node *next;
};

class linkListBuilder {

public:
    Node* make_ll(int len){
        Node head;  // Code only populates the next field.
        head.next = NULL;
        Node* cur = &head;
         cur->next = new Node();
         auto beginNode = cur;
         beginNode->data = 0;
        for (int i = 1; i < len; i++) {
            cur->next = new Node();
            cur = cur->next;
            cur->data = i;
            cur->next = NULL;
//            std::cout << cur  << " ";
        }
        return beginNode;
    }

    void print_all(Node* headNode) {
        while(headNode != NULL) {
            std::cout << headNode->data << '\n';
            headNode = headNode->next;
        }
    }

    void push(struct Node** head_ref, int new_data)
    {
        struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
        new_node->data  = new_data;
        new_node->next = (*head_ref);
        (*head_ref)    = new_node;
    }

    void insertAfter(struct Node* prev_node, int new_data)
    {
        if (prev_node == NULL)
        {
            printf("the given previous node cannot be NULL");
            return;
        }

        struct Node* new_node =(struct Node*) malloc(sizeof(struct Node));

        new_node->data  = new_data;
        new_node->next = prev_node->next;
        prev_node->next = new_node;
    }

    void append(struct Node** head_ref, int new_data)
    {
        struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));

        struct Node *last = *head_ref;
        new_node->data  = new_data;
        new_node->next = NULL;

        if (*head_ref == NULL)
        {
            *head_ref = new_node;
            return;
        }

        while (last->next != NULL)
            last = last->next;
        last->next = new_node;
        return;
    }

    void printList(struct Node *node)
    {
        while (node != NULL)
        {
            printf(" %d ", node->data);
            node = node->next;
        }
    }
};