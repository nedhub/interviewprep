#Queues 

#Enqueue - add to first in line
#Deque - double-ended queue, but we can use it for our queue.
#We use append() to enqueue an item, and popleft() to dequeue an item.




#Queues are good for modeling anything you wait in line for.

#Bank tellers. Placing an order at McDonalds.

#DMV customer service. Supermarker checkout


from collections import deque
my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())






