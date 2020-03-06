#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include <math.h>
#include <conio.h>

typedef struct stack_s stack;

char* get_string();
stack* create_stack(int);
stack* add_to_stack(stack*, int);
stack* delete_from_stack(stack*);
stack* clear_stack(stack*);
double read_stack(stack*);
char* infix_to_postfix(char*);
int priority(char);
double solve(char*);

struct stack_s
{
	double num;
	stack* next;
};

char* get_string()
{
	int flag = 0;
	char* string;
	string = (char*)malloc(1);
	char sym;
	while (true) {
		sym = getchar();
		
		
		if (sym == '\n' && !flag) continue;
		if (sym == '\n') break;
		string = (char*)realloc(string, flag + 1);
		*(string + flag++) = sym;
	}
	string = (char*)realloc(string, flag + 1);
	*(string + flag) = '\0';
	return string;
}

stack* create_stack(int num)
{
	stack* st = (stack*)malloc(sizeof(stack));
	st->next = nullptr;
	st->num = num;
	return st;
}

stack* add_to_stack(stack* st, int num)
{
	if (!st) return create_stack(num);
	stack* new_st = (stack*)malloc(sizeof(stack));
	new_st->next = st;
	new_st->num = num;
	return new_st;
}

stack* delete_from_stack(stack* st)
{
	if (!st) return nullptr;
	stack* tmp = st->next;
	free(st);
	return tmp;
}

stack* clear_stack(stack* st)
{
	st = delete_from_stack(st);
	if (st) clear_stack(st);
	int a = 0;
	return nullptr;
}

double read_stack(stack* st)
{
	if (!st)
	{
		puts("\nReading stack error!");
		_getch();
		return 0;
	}
	return st->num;
}

int priority(char c)
{
	switch (c)
	{
	case '*':case '/': return 3;
	case '-':case '+': return 2;
	case '(':case ')': return 1;
	default: return 0;
	}
}

char* infix_to_postfix(char* str)
{
	if (!str)
	{
		puts("\nEmpty str, error converting\a");
		return 0;
	}
	int i = -1, checknum = 0, cur_new_pos = 0;
	char* new_str = (char*)malloc(strlen(str) * 2 + 1);// *2 because spaces and +1\0
	new_str[strlen(str) * 2] = '\0';
	stack* st = nullptr;
	while (str[++i] != '\0')
	{
		if (checknum)//For long nums
		{
			if (new_str[cur_new_pos - 1] != ' ') new_str[cur_new_pos++] = ' ';
			checknum = 0;
		}
		if (str[i] == ' ')
		{
			/*
			free(new_str);
			clear_stack(st);
			puts("\nError because uses spaces!\a");
			return 0;
			*/
			continue;
		}
		else if (str[i] >= '0' && str[i] <= '9')
		{
			new_str[cur_new_pos++] = str[i];
			continue;
		}
		checknum = 1;
		
		if (str[i] == '(')
		{
			
			if (i && !priority(str[i - 1]) || str[i + 1] == '\0' || priority(str[i + 1]) > 1 || str[i + 1] == ')')
			{
				free(new_str);
				clear_stack(st);
				puts("\nError near'('!\a");
				return 0;
			}
			st = add_to_stack(st, '(');
			continue;
		}
		else if (str[i] == ')')
		{
			if (!priority(str[i + 1]) && str[i + 1] != '\0' || !i || priority(str[i - 1]) > 1 || str[i - 1] == '(')
			{
				free(new_str);
				clear_stack(st);
				puts("\nError near')'!\a");
				return 0;
			}
			char stack_oper;
			while (true)
			{
				if (!st)
				{
					free(new_str);
					puts("\nError with parentheses!\a");
					return 0;
				}
				if ((stack_oper = read_stack(st)) != '(')
				{
					if (new_str[cur_new_pos - 1] != ' ') new_str[cur_new_pos++] = ' ';
					new_str[cur_new_pos++] = stack_oper;
					st = delete_from_stack(st);
					continue;
				}
				st = delete_from_stack(st); //delete '('
				if (new_str[cur_new_pos - 1] != ' ') new_str[cur_new_pos++] = ' ';
				break;
			}
			continue;
		}
		else if (priority(str[i]))//if it +-/*
		{
			if (!i || priority(str[i - 1]) > 1 || str[i + 1] == '\0')
			{
				free(new_str);
				clear_stack(st);
				puts("\nBad signs!\a");
				return 0;
			}
			char stack_oper;
			while (true)
			{
				if (st)
				{
					if (priority(str[i]) <= priority((stack_oper = read_stack(st))))//if priority <= stack
					{
						if (new_str[cur_new_pos - 1] != ' ') new_str[cur_new_pos++] = ' ';
						new_str[cur_new_pos++] = stack_oper;
						st = delete_from_stack(st);
						continue;
					}
				}
				st = add_to_stack(st, str[i]);
				break;
			}
			continue;
		}
		free(new_str);
		clear_stack(st);
		puts("\nBad symbols!\a");
		return nullptr;
	}
	while (true)//Operands from stack to str
	{
		if (!st) break;
		if (new_str[cur_new_pos - 1] != ' ') new_str[cur_new_pos++] = ' ';
		new_str[cur_new_pos++] = read_stack(st);
		if (new_str[cur_new_pos - 1] == '(')
		{
			clear_stack(st);
			puts("\nError with parentheses!\a");
			getchar();
			return nullptr;
		}
		st = delete_from_stack(st);
	}
	new_str[cur_new_pos] = '\0';
	free(str);
	return new_str;
}

double solve(char* str)//str = postfix
{
	if (!str)
	{
		puts("\nEmpty str, error \a");
		return 0;
	}
	double result;
	int i = -1, num = -1;
	stack* st = nullptr;
	while (str[++i] != '\0')
	{
		if (str[i] >= '0' && str[i] <= '9')
		{
			if (num == -1) num = 0;
			num = num * 10 + str[i] - 48;
			continue;
		}
		if (num != -1) st = add_to_stack(st, num);
		num = -1;
		switch (str[i])
		{
		case '+':
			st->next->num += st->num;
			st = delete_from_stack(st);
			break;
		case '-':
			st->next->num -= st->num;
			st = delete_from_stack(st);
			break;
		case '*':
			st->next->num *= st->num;
			st = delete_from_stack(st);
			break;
		case '/':
			if (!st->num)
			{
				clear_stack(st);
				puts("\ndivision by zero\a");
				return 0;
			}
			st->next->num /= st->num;
			st = delete_from_stack(st);
			break;
		}
	}
	result = read_stack(st);
	clear_stack(st);
	return result;
}

int main()
{
	stack* st = nullptr;
	printf("  ConsoleMath\n  If u want to finish wtite '~'\n");
	while (true)
	{
		printf("Write expression: ");
		char* str = get_string();
		if (!strncmp(str,"~",1))
			break;
		str = infix_to_postfix(str);
		if (!str)
			continue;
		//printf("%s", str);
		//printf("\n");
		double result;
		result = solve(str);
		printf("%lf", result); 
		free(str);
		printf("\n");
	}
}

 