#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include <math.h>
#define SIZE 255
using namespace std;
//Function add element to array
char** add_to_mas(char** mas, int position, char* elem, int number_chars)
{
	mas = (char**)realloc(mas, (position+1) * sizeof(char*));
	mas[position] = (char*)malloc((number_chars+1) * sizeof(char));
	strcpy( mas[position],elem);
	return mas;
}

//output array
void print_mas(char** mas, int num)
{
	for (int i = 0; i < num;i++)
	{
		printf("%s ", mas[i]);
	}
}

//bool function T="-"
bool isNegativeSign(char value)
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
	if (value == 45)
		return true;
	else
		//printf("not a - ");
		return false;
}

//bool function T=int
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

//function T="+-/*"
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

//function T="."
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

//convert from char* to double number
double convertCharToDouble(char* val)
{
	int i = 0;
	int numBeforeDot = 0;
	int numAfterDot = 0;
	while (val[i] != char(46) && val[i] != NULL)
	{
		numBeforeDot++;
		i++;
	}
	while (val[i] != NULL)
	{
		numAfterDot++;
		i++;;
	}
	if (numAfterDot > 0)
		numAfterDot--;
	double num =0;
	for (int j = 0; j < numBeforeDot; j++)
	{
		num += (int(val[numBeforeDot - j-1])-48) * pow(10,j);
	}
	for (int j = 0; j < numAfterDot; j++)
	{
		num+= (double(val[numBeforeDot + numAfterDot - j]) - 48) / (double)pow(10, numAfterDot-j);
	}
	printf("%f", num);
	return num;
}
/*
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
*/

//convert char* to array with char*(nums and signs in char)
char** convert_to_list(char* str)
{ 
	int i = 0 , j =0  ,k = 0;
	char** mas = (char**)malloc(1 * sizeof(char*));
	*mas = (char*)malloc(1 * sizeof(char));
	bool isNegative = false;
	bool noPoint = true;
	bool isFloatNum = false;
	bool prevSign = false;
	char* tmp = (char*)malloc(1 * sizeof(char));
	while (true)
	{
		if (!isFloatNum)
		{
			if (tmp != NULL)
			{
				tmp = (char*)realloc(tmp, 1 * sizeof(char));
				tmp[0] = char(0);
			}
		}

		if (i==0||prevSign)
		{
			if (isNegativeSign(str[i]))
			{
				isNegative = true;
				isFloatNum = true;
				prevSign = false;
				tmp = (char*)realloc(tmp, (j + 1) * sizeof(char));
				tmp[j] = (char)str[i];
				j++;
				i++;
				continue;
			}
		}

		if (isNumber(str[i]))
		{
				tmp = (char*)realloc(tmp, (j + 1) * sizeof(char));
				tmp[j] = str[i];
				i++;
				j++;
				isFloatNum = true;
				continue;
		}

		if (isPoint(str[i])&&noPoint)
		{
			noPoint = false;
			tmp = (char*)realloc(tmp, (j + 1) * sizeof(char));
			tmp[j] = str[i];
			i++;
			j++;
			continue;
		}

		if (isFloatNum)
		{
			tmp[j] = '\0';

			isFloatNum = false;
			noPoint = true;
			isNegative = false;
			mas = add_to_mas(mas, k, tmp, j);
			k++;
			j = 0;
		}
		if (isSign(str[i]))
		{
			tmp = (char*)realloc(tmp, 2 * sizeof(char));
			tmp[0] = str[i];
			tmp[1] = '\0';
			prevSign = true;
			//lst = addelem(lst, tmp);
			//listprint(lst);
			mas = add_to_mas(mas, k, tmp, 1);
			i++;
			k++;
		}
		
		if (str[i] == ' ')
		{
			i++;
			continue;
		}

		if (str[i] == NULL)
		{
			print_mas(mas, k);
			break;
		}
		
	}
	return(mas);
}
/*
int get_size(char** mas)
{
	int i = 0;
		while (mas[i])
		{
			i++;
		}
		return i;
}
*/
float solve(char** mas)
{
	return 0;
}
/*
void cut_mas(char** mas,int num)
{
	int i = num;
	while (mas[i] != NULL && mas[i + 1] != NULL)
	{
		strcpy(mas[i], mas[i + 1]);
		i++;
	}
	free(mas[i]);
	free(mas[i - 1]);
}

char* exp_for_mas(char** mas)
{
	bool f = false;
	while (true)
	{
		int i = 0;
		while(mas[i]!=NULL)
		{

		}
	}
		
}
*/
int main()
{
	
	char* str = (char*)malloc(SIZE*sizeof(char));
	//	scanf_s("%s", str,SIZE);
	gets_s(str, SIZE);
	//f();
	//convertCharToDouble(str);
	char** mas = (char**)malloc(SIZE * sizeof(char*));
	*mas = (char*)malloc(SIZE * sizeof(char));
	mas = convert_to_list(str);
	/*int new_size = get_size(mas);
	mas = (char**)realloc(mas, new_size * sizeof(char*));
	print_mas(mas,get_size(mas));*/
	free(str);
	for (int i = 0; get_size(mas) < i; i++)
		free(mas[i]);
	free(mas);
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




