#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - function that runs and returns nothing
 * Return: 0.
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - function that creates 5 zombie processes
 * every zombie process created,
 * it displays Zombie process created, PID: ZOMBIE_PID
 * Return: 0.
 */
int main(void)
{
	int children_processes = 0;
	pid_t pid;

	while (children_processes < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)pid);
		children_processes++;
	}
	if (pid != 0)
		infinite_while();
	return (0);
}
