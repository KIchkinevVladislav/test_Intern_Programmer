"""
Вопрос 1
На языке Python написать алгоритм (функцию) определения четности целого числа, 
который будет аналогичен нижеприведенному по функциональности, 
но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций. 

Пример

def isEven(value):

    return value % 2 == 0
"""
#реализация
def is_even(value):
    print((value & 1) == 0)

#данные для тестирования
is_even(-1)
is_even(2)

# В данном случае  
# алгоритм использует побитовую операцию "И"  с числом 1 (оператор &). 
# Если последний бит числа равен 0, то число является четным. 
# В противном случае, если последний бит равен 1, число будет нечетным.
# Алгоритм будет работать быстрее с большими числами.

# В Вашем примере используется более понятная 
# для начинающих разработчиков операция получения остатка от деления, 
# что упрощает понимание кода.

# Если не предполагается проверка больших чисел, 
# то первый вариант более понятен для чтения, 
# с учетом отсутствия существенной разницы в производительности.

"""
Вопрос 2
На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

Оценивается:

Полнота и качество реализации
Оформление кода
Наличие сравнения и пояснения по быстродействию
"""
# Вариант 1
# В данном случаем мы используем список Python внутри класса для 
# реализации циклического буфера FIFO.


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # максимальная вместимость буфера
        self.buffer = [None] * capacity # список для хранения элементов
        self.head = 0 # указатель начала
        self.tail = 0 # указатель конца
        self.size = 0 # текущий размер буфера

    def is_empty(self):
        # проверка является ли буфер пустым
        return self.size == 0

    def is_full(self):
        # проверка является ли буфер полным
        return self.size == self.capacity

    def enqueue(self, item):
        # добавление элемента в буфер
        if self.is_full():
            raise Exception('Буфер полон')
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        # удаление элемента
        if self.is_empty():
            raise Exception('Буфер пуст')
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def __len__(self):
        # текущие количество элементов в буфере
        return self.size
    
# Цикличность реализуют методы класса enqueue и dequeue и указателями.
# Представляется наиблоее простым способом реализации задания.
# За счет доступа по индексу операция выполняется за O(1).
# Основным недостатком такого подхода будет ограниченый размер буфера.

# Можно добавить функционал увеличения размера буфера
# Дополнив класс методом resize
    # def resize(self, new_capacity):
    #     if new_capacity < self.size:
    #         raise ValueError('Новый размер меньше имеющегося')
    #     new_buffer = [None] * new_capacity
    #     for i in range(self.size):
    #         new_buffer[i] = self.buffer[(self.head + i) % self.capacity]
    #     self.buffer = new_buffer
    #     self.head = 0
    #     self.tail = self.size
    #     self.capacity = new_capacity


# Вариант 2

# Реализация посредством двусвязного списка

class Node:
    # узел двусвязного списка
    def __init__(self, value):
        self.value = value
        self.prev = None # ссылку на предыдущий узел
        self.next = None # ссылку на следующий узел


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        # проверка является ли буфер пустым
        return self.size == 0

    def is_full(self):
        # проверка является ли буфер полным
        return self.size == self.capacity

    def enqueue(self, item):
        # добавление элемента в буфер
        new_node = Node(item)
        if self.is_empty():
            # создание нового узла, если буфер пустой
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
            self.size += 1
        elif self.is_full():
            # создание нового узла, если буфер полный
            # новый элемент перезаписывает старый
            self.tail.value = item
            self.head = self.head.next
            self.tail = self.tail.next
        else:
            # создание нового узла, если буфер не заполнен полностью
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
            self.size += 1

    def dequeue(self):
        # удаление и возврат элемента из начала буфера
        if self.is_empty():
            raise Exception("Buffer is empty")
        item = self.head.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            new_head = self.head.next
            new_head.prev = self.tail
            self.tail.next = new_head
            self.head = new_head
        self.size -= 1
        return item

    def __len__(self):
        # текущие количество элементов в буфере
        return self.size

# Здесь релизуем буфер с использованием двусвязного списка.
# Операции вствки и извлечения работают за O(1)
# Главным недостатком являетя использование дополнительной памяти
# для хранения данных об услуг списка


"""
Вопрос 3

На языке Python предложить алгоритм, 
который быстрее всего (по процессорным тикам) 
отсортирует данный ей массив чисел. 
Массив может быть любого размера со случайным порядком чисел
(в том числе и отсортированным).
"""
# В данном случае самым быстрым будет алгоритм Timsort, 
# сочетающим в себе сортировку вставками и слиянием. 
# Он стабилен и имеет сложность O(n log n) в худшем случае.
# Гибридность алгоритма позволяет ему оптимизировать процесс сортировки.
# В том числе в случае если данные отсортированы 
# или содержат небольшое количество обратно отсортированных элементов, 
# Timsort использует процедуру слияния для объединения их 
# в уже отсортированные блоки.
# Использование двух простых сортировок позволяет уменьшить 
# количество операций перестановок и сравнений в рамках реализации 
# Timsort, после разбиения массива на подмассивы.

# Он встроен в реализацию языка Python 
# и может быть использован посредством 
# функции sorted() или метода list.sort().
# Непосредственная его реализация здесь представляется 
# излишней, т.к. оптимальный код его реализации на Python 
# доступен в открытых источниках 
# (например здесь: https://www.geeksforgeeks.org/timsort/)