#define _CRT_SECURE_NO_WARNINGS
#define _CRT_NONSTDC_NO_DEPRECATE
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define COMPARE(x,y) (((x)<(y))? -1:((x)==(y))? 0:1)
#define ERROR -99
int COUNT = 0;

struct node
{
   int key;
   node* lchild;
   node* rchild;
};

node* modified_search(node* A, int key)
{
   node* ptr = NULL;
   while (A)
   {
      ptr = A;
      if (key == A->key) { 
          printf("ERR : 중복 데이터 존재.\n");
          return NULL; 
      }
      if (key > A->key)
         A = A->lchild;
      else
         A = A->rchild;
   }
   return ptr;
}

void insert_BST(node** A, int key)
{
   node* ptr = NULL;
   ptr = modified_search(*A, key);
   if (ptr || !(*A))
   {
      node* temp = (struct node*)malloc(sizeof(struct node));
      temp->key = key;
      temp->rchild = temp->lchild = NULL;
      if ((*A))
      {
         if (ptr->key <= key)
            ptr->lchild = temp;
         else
            ptr->rchild = temp;
      }
      else
         *A = temp;
   }
}

void delete_BST(node** list, int key)
{
   node* ptr;
   if (*list)
   {
      if ((*list)->key == key)
      {
         if ((*list)->rchild == NULL && (*list)->lchild == NULL)
         {
            (*list) = NULL;
         }
         else if ((*list)->rchild == NULL)
         {
            ptr = (*list);
            (*list) = ((*list)->lchild);
            free(ptr);
         }
         else if ((*list)->lchild == NULL)
         {
            ptr = (*list);
            (*list) = ((*list)->rchild);
            free(ptr);
         }
         else
         {
            ptr = (*list)->lchild;
            for (; ptr->rchild != NULL; ptr = ptr->rchild)
            {

            }
            (*list)->key = ptr->key;
            delete_BST(&((*list)->lchild), ptr->key);
         }
      }
      else if ((*list)->key > key)
      {
         delete_BST(&((*list)->rchild), key);
      }
      else
      {
         delete_BST(&((*list)->lchild), key);
      }
   }
   else
   {
      printf("그런건 없습니다.\n");
   }
}

void print_BST(node* p) {
   if (p != NULL)
   {
      print_BST(p->lchild);
      printf("%d\t ", p->key);
      print_BST(p->rchild);
   }
}

int serachhelp_BTS(node* p, int key)
{
   if (p)
   {
      if (p->key == key)
      {
         return 1;
      }
      else if (p->key > key)
      {
         return serachhelp_BTS(p->rchild, key);
      }
      else
      {
         return serachhelp_BTS(p->lchild, key);
      }
   }
   else
   {
      return 0;
   }
}


void search_BTS(node* p, int key)
{
   if (serachhelp_BTS(p, key))
   {
      printf("%d->", p->key);
      if (p->key < key)
      {
         search_BTS(p->lchild, key);
      }
      else if (p->key > key)
      {
         search_BTS(p->rchild, key);
      }
      else
      {
         printf("end\n");
         return;
      }
   }
   else
   {
      printf("%d 값이 존재하지 않음\n", key);
   }
}

int main()
{
   int key = 0;
   int set = 0;
   struct node* A = NULL;
   while (true)
   {
      printf("어떤 동작을 하시겠습니까?\n1번 : 입력\n2번 : 삭제\n3번 : 출력\n4번 : key값 검색\n0번 : 종료\n>>");
      scanf("%d", &set);
      switch (set)
      {
      case 1:
         printf("key 값을 입력해주세요\n>>");
         scanf("%d", &key);
         insert_BST(&A, key);
         printf("\n");
         break;
      case 2:
         printf("삭제할 key 값을 입력해주세요\n>>");
         scanf("%d", &key);
         delete_BST(&A, key);
         printf("\n");
         break;
      case 3:
         printf("\n출력 결과\n");
         print_BST(A);
         printf("\n\n");
         break;
      case 4:
         printf("찾고 싶은 key값을 입력해주세요\n>>");
         scanf("%d", &key);
         search_BTS(A, key);
         printf("\n");
         break;
      case 0:
         return 0;
         break;
      default:
         printf("그런숫자는 없어요\n");
         break;
      }

   }

}