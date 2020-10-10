'''Consider a list (list = []). You can perform the following commands:
 insert i e: Insert integer  at position .
 print: Print the list.
 remove e: Delete the first occurrence of integer .
 append e: Insert integer  at the end of the list.
 sort: Sort the list.
 pop: Pop the last element from the list.
 reverse: Reverse the list'''

a = int(input())
main = []
for i in range(a):
    task = input().lower().split()
    if task[0] == 'insert':
        main.insert(int(task[1]), int(task[2]))
    elif task[0] == 'remove':
        main.remove(int(task[1]))
    elif task[0] == 'append':
        main.append(int(task[1]))
    elif task[0] == 'sort':
        main.sort()
    elif task[0] == 'pop':
        main.pop()
    elif task[0] == 'reverse':
        main.reverse()
    elif task[0] == 'print':
        print(main)
