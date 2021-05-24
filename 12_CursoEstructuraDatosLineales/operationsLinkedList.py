from node import Node

# Creacion de nodos enlazados
head = None
for count in range(1,6):
    head = Node(count, head)
# Recorrer e imprimir valores de la lista
def printLL(probe):
    print('\n')
    while probe != None:
        print(probe.data)
        probe = probe.next
print("Recorrido lista")
printLL(head)

# Busqueda de un elemento
probe = head
target_item = 2
while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    print(f"target item {target_item} has been found")
else:
    print(f"target item {target_item} not found")
print('\n')
# Reemplazo de un elemento
probe = head
target_item = 3
new_item = "Z"
while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    probe.data = new_item
    print(f"{new_item} replace the old value in the node number {target_item}")
else:
    print(f"The target item {target_item} is not in the linked list")
print('\n')
# Insertar un nuevo elemento al inicio
head = Node("F", head)
printLL(head)
# Insertar un nuevo elemento / nodo al final
new_node = Node("K")
if head is None:
    head = new_node
else:
    probe = head
    while probe.next != None:
        probe = probe.next
    probe.next = new_node
printLL(head)
# Eliminar un elemento / nodo al inicio
removed_item = head
head = head.next
print(f"Removed head item {removed_item}")
printLL(head)
# Eliminar un elemento de tail
removed_item = head.data
if head.next is None:
    head = None
else:
    probe = head
    while probe.next.next != None:
        probe = probe.next
    removed_item = probe.next
    probe.next = None
    print(f"Removed tail item {removed_item}")
printLL(head)
# Agregar un nuevo elemento / nodo por index inverso
new_item = "2222222"
idx = 3
if head is None or idx<=0:
    head = Node(new_item, head)
else:
    probe = head
    while probe.next != None and idx > 1:
        probe = probe.next
        idx -= 1
    probe.next = Node(new_item, probe.next.next)
printLL(head)
# Eliminar un elemento / nodo por index inverso
idx = 3
if head is None or idx<=0:
    removed_item = head.data
    head = None
else:
    probe = head
    while probe.next.next != None and idx > 1:
        probe = probe.next
        idx -= 1
    removed_item = probe.next.data
    probe.next = probe.next.next
print(f"Remove item : {removed_item}")
printLL(head)