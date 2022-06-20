# *** Двоичное дерево поиска ***
# Не всякое двоичное дерево является двоичным деревом поиска.
# Оно должно обладать некоторыми свойствами:
#     1. Оба поддерева каждого узла являются двоичными деревьями поиска
#     2. Для узла с ключом X все узлы левого поддерева должны быть строго меньше X
#     3. Аналогично, для узла с ключом X все узлы правого поддерева должны быть строго больше X


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):  # печать с помощью обхода в ширину
        queue = [self]  # создаем очередь
        values = []  # значения в порядке обхода в ширину
        while queue:  # пока она не пустая
            last = queue.pop(0)  # извлекаем из начала
            if last is not None:  # если не None
                values.append("%d" % last.value)  # добавляем значение
                queue.append(last.left_child)  # добавляем левого потомка
                queue.append(last.right_child)  # добавляем правого потомка
        return ' '.join(values)

    # Метод поиска элемента
    def search(self, x):
        # если искомое значение равно значению узла
        if self.value == x:
            # возвращаем узел
            return self
        # а если искомое значение меньше значения узла
        elif self.value < x:
            # то продолжаем поиск в левом потомке
            return self.left_child.search(x)
        # а если искомое значение больше значения узла
        elif self.value > x:
            # продолжаем поиск в правом потомке
            return self.right_child.search(x)
        # иначе возвращаем ложь
        else:
            return False

    # Метод поиска минимума
    def minimum(self):
        # если узел не имеет левого потомка
        if self.left_child is None:
            # значит мы нашли минимум и возвращаем этот узел
            return self
        # иначе
        else:
            # продолжаем поиск
            return self.left_child.minimum()

    # Метод поиска максимума
    def maximum(self):
        # если у узла нет правого потомка
        if self.right_child is None:
            # значение этого узла и есть максимум, возвращаем его
            return self
        # иначе
        else:
            # продолжаем поиске
            return self.right_child.maximum()

    # Метод поиска следующего значения
    def next_value(self, x):
        # текущий элемент - это узел
        current = self
        # приемника нет
        successor = None
        # пока текущий элемент есть:
        while current is not None:
            # если значение текущего элемента(узла) больше искомого:
            if current.value > x:
                # текущий элемент становится приемником
                successor = current
                # и меняется на левого потомка
                current = current.left_child
            # иначе:
            else:
                # текущий узел становится правым потомком
                current = current.right_child
        # возвращаем приемника
        return successor

    # Метод поиска предыдущего значения
    def previous_value(self, x):
        # в переменную "текущий" записываем узел, в котором находимся
        current = self
        # приемника нет
        successor = None
        # пока текущий узел существует, проверяем:
        while current is not None:
            # если значение текущего узла меньше заданного:
            if current.value < x:
                # приемником назначается текущий узел
                successor = current
                # а текущий узел становится правым потомком
                current = current.right_child
            # иначе:
            else:
                # текущий узел становится левым потомком
                current = current.left_child
        # после выполнения цикла, возвращаем потомка
        return successor

    # Метод вставки элемента
    def insert(self, x):
        # если заданное значение больше значения текущего узла:
        if x > self.value:  # идем в правое поддерево
            if self.right_child is not None:  # если оно существует,
                self.right_child.insert(x)  # делаем рекурсивный вызов
            else:  # иначе создаем правого потомка
                self.right_child = BinarySearchTree(x)
        else:  # иначе в левое поддерево и делаем аналогичные действия
            if self.left_child is not None:
                self.left_child.insert(x)
            else:
                self.left_child = BinarySearchTree(x)
        return self  # возвращаем корень

    # Удаление элемента
    def delete(self, x):
        """
        Алгоритм действительно непростой, поэтому разберем его еще раз по шагам:
            1. С помощью цикла while ищем узел node, подлежащий удалению, а также его предка parent
            2. Если найденный узел является листом, то удаляем его, присваивая значение
               None соответствующему левому (правому) поддереву предка.
            3. Если найденный узел имеет одного потомка, то устанавливаем связь между ним
               и предком удаляемого узла. Этот единственный потомок становится на место
               удаленного узла.
            4. Если найденный узел имеет сразу обоих потомков, то находим следующее
               значение за удаляемым и сохраняем его. Это значение становится на место удаленного.
               После чего, во избежание дублирования, нужно рекурсивно удалить новое значение.
               Элемент, стоящий на месте удаленного узла, является следующим, т.е.
               больше исходного, поэтому всегда находится в правом дереве.
               И именно для правого дерева мы запускаем эту же самую функцию
        """
        parent = self
        node = self
        if not self.search(x):
            return self
        while node.value != x:
            parent = node
            if parent.left_child is not None and x < parent.value:
                node = parent.left_child
            elif parent.right_child is not None and x > parent.value:
                node = parent.right_child
        # по завершении в node хранится искомый узел

        # первый случай - если лист
        if node.left_child is None and node.right_child is None:
            if parent.left_child is node:
                parent.left_child = None
            if parent.right_child is node:
                parent.right_child = None
            if parent.value == x:
                # если нет листов и parent==node до сих пор,
                # значит, нужно вернуть None для корректной работы рекурсии
                return None

        # второй случай - имеет одного потомка
        elif node.left_child is None or node.right_child is None:
            if node.left_child is not None:
                if parent.left_child is node:
                    parent.left_child = node.left_child
                elif parent.right_child is node:
                    parent.right_child = node.right_child
            if node.right_child is not None:
                if parent.left_child is node:
                    parent.left_child = node.right_child
                elif parent.right_child is node:
                    parent.right_child = node.right_child
        else:  # третий случай - имеет двух потомков
            next_ = node.next_value(x).value  # ищем следующее значение
            node.value = next_  # и меняем на него
            # # делаем рекурсивный вызов
            node.right_child = node.right_child.delete(next_)
        return self


BinSTree_1 = BinarySearchTree(25)
BinSTree_1.left_child = BinarySearchTree(10)
BinSTree_1.right_child = BinarySearchTree(37)
BinSTree_1.left_child.right_child = BinarySearchTree(15)
BinSTree_1.right_child.left_child = BinarySearchTree(30)
BinSTree_1.right_child.right_child = BinarySearchTree(65)

BinSTree_1.delete(37)
BinSTree_1.delete(25)

print(BinSTree_1)