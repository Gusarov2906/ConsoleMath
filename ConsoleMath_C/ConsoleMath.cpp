#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#define SIZE 255
using namespace std;
char** add_to_mas(char** mas, int position, char* elem, int number_chars)
{
	mas = (char**)realloc(mas, (position+1) * sizeof(char*));
	mas[position] = (char*)malloc((number_chars+1) * sizeof(char));
	strcpy( mas[position],elem);
	return mas;
}

void print_mas(char** mas, int num)
{
	for (int i = 0; i < num;i++)
	{
		printf("%s ", mas[i]);
	}
}
/*
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
	char* tmp = (char*)malloc(SIZE * sizeof(char));
	strcpy(tmp,a);
	lst->field =tmp;
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
	char* tmp = (char*)malloc(SIZE * sizeof(char));
	strcpy(tmp, value);
	temp->field = tmp; // сохранение поля данных добавляемого узла
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
*/
bool isNumber(char value)
{
	try 
	{
		if (!int(value))
			throw - 1;
	}
	catch (int e)
	{
	//	printf("Error with type");
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
		//printf("Error with type");
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
		//printf("Error with type");
		return false;
	}
	value = int(value);
	if (value == 46)
		return true;
	else
		//printf("not a sign");
	return false;
}


void f()
{
	char* x, * tmp;

	x = (char*)calloc(10,sizeof(char));

	
	if (x != NULL)
	{
		for (int i = 0; i < 9; i++)
		{

			x[i] = char(52 + i%2);
		}
		x[9] = '\0';
		printf("\n%s\n", x);
		tmp = (char*)realloc(x, 512);
	
		if (tmp != NULL)
		{
			for (int i = 9; i < 510; i++)
			{
				tmp[i] = char(52 + i % 2);
			}
			tmp[510] = '\0';
			x = tmp;
		}
		printf("\n%s\n", x);
		free(x);
	}
}

void convert_to_list(char* str)
{ 
	int i = 0;
	bool prevIsPoint = false;
	bool isFloatNumber = false;
	bool firstNum = true;
	int j = 0;
	int k = 0;
	char** mas = (char**)malloc(1 * sizeof(char*));
	*mas = (char*)malloc(1 * sizeof(char));
	char* tmp = (char*)malloc(1 * sizeof(char));
	char* x;
//	list* lst = NULL;
	while (1)
	{
		if (!isFloatNumber)
		{
			if (tmp != NULL)
			{
				tmp = (char*)realloc(tmp, 1 * sizeof(char));
				tmp[0] = char(0);
			}
		}
		if (isNumber(str[i]))
		{
			tmp = (char*)realloc(tmp, (j + 1) * sizeof(char));
			tmp[j] = (char)str[i];
			j++;
			i++;
			isFloatNumber = true;
			prevIsPoint = true;
			continue;
		}
		else
			if (isPoint(str[i]))
			{
				if (prevIsPoint)
				{
					tmp = (char*)realloc(tmp, (j + 1) * sizeof(char));
					tmp[j] = str[i];
					i++;
					j++;
					continue;
				}

			}
			else
			{
				if (isFloatNumber)
				{
					tmp[j] = '\0';

					isFloatNumber = false;
					mas = add_to_mas(mas, k, tmp, j);
					j = 0;
					k++;
				}
	
				/*
				if (firstNum)
				{
					strcpy(mas[0],tmp);
					 //lst = init(tmp);
					 firstNum = false;
					 //listprint(lst);
				}
				else
				{
					strcpy(mas[k], tmp);
					k++;
					//lst = addelem(lst, tmp);
					//listprint(lst);
				}
				*/
				if (isSign(str[i]))
				{
					tmp = (char*)realloc(tmp, 2 * sizeof(char));
					tmp[0] = str[i];
					tmp[1] = '\0';
					//lst = addelem(lst, tmp);
					//listprint(lst);
					mas =add_to_mas(mas, k, tmp, 1);
					i++;
					k++;
				}

				
			}
		if (str[i] == NULL)
		{
			print_mas(mas, k);
			break;
		}
	}
	/*
	int i = 0;
	bool prevIsPoint = false;
	bool isFloatNumber = false;
	int j = 0;
	int k = 0;
	char* tmp;
	char* x;

	while (1)
	{
		if (!isFloatNumber)
		{
			if (x != NULL)
			{
				x = (char*)malloc(1 * sizeof(char));
				tmp = (char*)realloc(x, 1 * sizeof(char));
				if (tmp != NULL)
				{
					x = tmp;
					tmp[0] = char(0);
				}
				free(x);
			}
			if (isNumber(str[i]))
			{
				tmp = (char*)realloc(tmp, (j + 1) * sizeof(char));
				tmp[j] = (char)str[i];
				j++;
				i++;
				isFloatNumber = true;
				prevIsPoint = true;
				continue;
			}
		}
	}
}

*/
}
int main()
{
	
	char* str = (char*)malloc(SIZE*sizeof(char));
	scanf("%s", str);
	
	//f();

	convert_to_list(str);
}


/*
while (1)
{
	if (!isFloatNumber)
	{
		if (tmp != NULL)
		{
			tmp = (char*)realloc(tmp, 1 * sizeof(char));
			tmp[0] = char(0);
		}
	}
	if (isNumber(str[i]))
	{
		tmp = (char*)realloc(tmp, (j + 1) * sizeof(char));
		tmp[j] = (char)str[i];
		j++;
		i++;
		isFloatNumber = true;
		prevIsPoint = true;
		continue;
	}
	else
		if (isPoint(str[i]))
		{
			if (prevIsPoint)
			{
				tmp = (char*)realloc(tmp, (j + 1) * sizeof(char));
				tmp[j] = str[i];
				i++;
				j++;
				continue;
			}

		}
		else
		{
			isFloatNumber = false;
			list lst = *init(tmp);
			listprint(&lst);
			j = 0;
			i++;
			if (isSign(str[i]))
				printf("Sign: %c \n", str[i]);
		}
	if (str[i] == NULL)
		break;
}
*/

/*
for (int i = 0; i < SIZE; i++) //fill all str by symbol"E" which means that is empty
{
	str[i] = char(69);
}
*/
/*
	int i = 0;
	while(1)
	{
		if (isNumber(str[i]))
			printf("Number: %c \n",str[i]);
		else
			if (isPoint(str[i]))
				printf("Point: %c \n", str[i]);
			else
				if (isSign(str[i]))
					printf("Sign: %c \n", str[i]);
		i++;
		if (str[i] == NULL)
			break;
	}

	*/




