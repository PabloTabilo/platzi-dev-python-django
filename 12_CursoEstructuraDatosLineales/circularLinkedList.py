import random
from node import Node

index = 1
new_item = "ham"
head = Node(None, None)
head.next = head
probe = head
while index > 0 and probe.next != head:
    probe = probe.next
    index -= 1
probe.next = Node(new_item, probe.next)
print(probe.next.data)
print('\n')
head = None
for i in range(10):
    head = Node(random.randint(1, 100),head)

def printSLL(probe):
    while probe != None:
        print(probe.data)
        probe = probe.next
    print('\n')
printSLL(head)
probe = head
while probe.next != None:
    probe = probe.next
probe.next = head # tail to head

steps = 23
probe = head
while steps > 0:
    steps -= 1
    print(probe.data)
    probe = probe.next
print("\n")
probe = head
while probe.next != head:
    print(probe.data)
    probe = probe.next
print(probe.data)