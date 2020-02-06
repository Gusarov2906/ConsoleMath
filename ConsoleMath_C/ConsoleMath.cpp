#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>

using namespace std;

struct list
{
	char* field; // поле данных
	struct list* next; // указатель на следующий элемент
	struct list* prev; // указатель на предыдущий элемент
};

struct list* init(char* a)  // а- значение первого узла
{
	struct list* lst;
	// выделение памяти под корень списка
	lst = (struct list*)malloc(sizeof(struct list));
	lst->field = a;
	lst->next = NULL; // указатель на следующий узел
	lst->prev = NULL; // указатель на предыдущий узел
	return(lst);
}

struct list* addelem(list* lst, char* value)
{
	struct list* temp, * p;
	temp = (struct list*)malloc(sizeof(list));
	p = lst->next; // сохранение указателя на следующий узел
	lst->next = temp; // предыдущий узел указывает на создаваемый
	temp->field = value; // сохранение поля данных добавляемого узла
	temp->next = p; // созданный узел указывает на следующий узел
	temp->prev = lst; // созданный узел указывает на предыдущий узел
	if (p != NULL)
		p->prev = temp;
	return(temp);
}

struct list* deletelem(list* lst)
{
	struct list* prev, * next;
	prev = lst->prev; // узел, предшествующий lst
	next = lst->next; // узел, следующий за lst
	if (prev != NULL)
		prev->next = lst->next; // переставляем указатель
	if (next != NULL)
		next->prev = lst->prev; // переставляем указатель
	free(lst); // освобождаем память удаляемого элемента
	return(prev);
}

struct list* deletehead(list* root)
{
	struct list* temp;
	temp = root->next;
	temp->prev = NULL;
	free(root);   // освобождение памяти текущего корня
	return(temp); // новый корень списка
}

void listprint(list* lst)
{
	struct list* p;
	p = lst;
	do {
		printf("%s ", p->field); // вывод значения элемента p
		p = p->next; // переход к следующему узлу
	} while (p != NULL); // условие окончания обхода
}

bool isNumber(char value)
{
	try 
	{
		if (!int(value))
			throw - 1;
	}
	catch (int e)
	{
		printf("Error with type");
		return false;
	}
	value = int(value);
	if (value > 47 && value < 58)
		return true;
	else
		//printf("not a number");
		return false;
}

bool isSign(char value)
{
	try
	{
		if (!int(value))
			throw - 1;
	}
	catch (int e)
	{
		printf("Error with type");
		return false;
	}
	value = int(value);
	if (value == 42 || value == 43 || value == 45 || value == 47 || value == 94)
		return true;
	else
		//printf("not a sign");
	return false;
}

bool isPoint(char value)
{
	try
	{
		if (!int(value))
			throw - 1;
	}
	catch (int e)
	{
		printf("Error with type");
		return false;
	}
	value = int(value);
	if (value == 46)
		return true;
	else
		//printf("not a sign");
	return false;
}
int main()
{
	char* str = (char*)calloc(255 , sizeof(char));
	scanf("%s", str);
	for (int i = 0; i < 10; i++)
	{
		if (isNumber(str[i]))
			printf("Number: %c \n",str[i]);
		else
			if (isPoint(str[i]))
				printf("Point: %c \n", str[i]);
			else
				if (isSign(str[i]))
					printf("Sign: %c \n", str[i]);
	}
	if (isNumber(str[0])&&isPoint(str[1])&& isNumber(str[0])&&isSign(str[3]))
	{
		list test = *init(str);
		//printf("%s", str);
		listprint(&test);
	}
}

