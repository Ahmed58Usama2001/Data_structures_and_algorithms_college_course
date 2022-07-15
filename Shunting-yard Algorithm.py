import operator

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = Node(newNode)
        else:
            t = Node(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if self.right == None:
            self.right = Node(newNode)
        else:
            t = Node(newNode)
            t.right = self.right
            self.right = t

    def getRootVal(self):
        return self.data

    def setRootVal(self, obj):
        self.data = obj

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def postorder(self):
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()

        print(self.data, end = " ")


def is_greater_precedence(op1, op2):
    pre = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3, '(': 0}
    return pre[op1] >= pre[op2]

def associativity(op): #Left->Right = 0, #Right->Left = 1
    ass = {'+':0, '-':0, '*':0, '/':0, '^':1}
    return ass[op]

def build_tree(exp):
    exp_list = exp.split()
    print(exp_list)
    stack = [] #For saving each operators & operands before creating their specific nodes
    tree_stack = [] #For saving each node (subtree) until the last element is the whole tree
    for i in exp_list: 
        if i not in ['+', '-', '*', '/', '^', '(', ')']:
            t = Node(int(i)) #Casting for easier evaluation process
            tree_stack.append(t)

        elif i == '(':
            stack.append('(')

        elif i in ['+', '-', '*', '/', '^']:
                if not stack or stack[-1] == '(':
                    stack.append(i)

                else:
                    while stack and is_greater_precedence(stack[-1], i) and associativity(i) == 0:
                        popped_item = stack.pop()
                        t = Node(popped_item)
                        t1 = tree_stack.pop()
                        t2 = tree_stack.pop()
                        t.right = t1
                        t.left = t2
                        tree_stack.append(t)
                    stack.append(i)

        elif i == ')':
            while stack[-1] != '(':
                popped_item = stack.pop()
                t = Node(popped_item)
                t1 = tree_stack.pop()
                t2 = tree_stack.pop()
                t.right = t1
                t.left = t2
                tree_stack.append(t)
            stack.pop()

    while stack:
        popped_item = stack.pop()
        t = Node(popped_item)
        t1 = tree_stack.pop()
        t2 = tree_stack.pop()
        t.right = t1
        t.left = t2
        tree_stack.append(t)

    t = tree_stack.pop()
    return t



def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv, '^':operator.pow}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()

t = build_tree("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3")
print(evaluate(t))
t.postorder()
print("\n")
t = build_tree("2 ^ 2 ^ 2 ^ 2")
print(evaluate(t))
t.postorder()
print("\n")
t = build_tree("( 1 + 1 + 1 + 1 ) / ( 1 + 1 + 1 + 1 )")
print(evaluate(t))
t.postorder()
print("\n")
t = build_tree("( 5 * 18 / ( 3 ^ 2 ) + 2 ^ 2 / 4  )")
print(evaluate(t))
t.postorder()
print("\n")
t = build_tree("1024 / ( ( 2 ^ 4 ) * 2 ^ ( 6 - 3 ) )")
print(evaluate(t))
t.postorder()
print("\n")
t = build_tree("( 36 / 4 - 3 ) ^ 2 - 36")
print(evaluate(t))
t.postorder()
print("\n")