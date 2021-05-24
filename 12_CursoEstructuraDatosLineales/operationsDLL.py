from double_linked_list import TwoWayNode

tail = TwoWayNode(1)
for i in range(2, 6):
    tail.next = TwoWayNode(i, tail)
    tail = tail.next
probe = tail
while probe != None:
    print(probe.data)
    probe = probe.previous