class data_stack:
    data_stack = []

    def pop(self):
        if len(self.data_stack) > 0:
            return self.data_stack.pop()
        else:
            raise NameError('data_stack is empty')

    def push(self, value):
        self.data_stack.append(value)


class stack_machine(data_stack):
    def __init__(self, enter):
        self.instruct_pointer = None
        self.return_stack = []
        self.enter = enter
        self.tos = 0
        self.heap = 0
        self.commands_map = {'-': self.sub,
                             '+': self.add,
                             '*': self.mul,
                             '/': self.div,
                             '%': self.mod,
                             '==': self.eq,
                             'cast_int': self.cast_int,
                             'cast_str': self.cast_str,
                             'drop': self.drop,
                             'dup': self.dup,
                             'if': self.if_clause,
                             'jmp': self.jmp,
                             'stack': self.stack,
                             'swap': self.swap,
                             'println': self.println,
                             'print': self.print,
                             'read': self.read,
                             'call': self.call,
                             'return': self.return_back,
                             'exit': self.exit,
                             'store': self.store,
                             'load': self.load
                             }

    def sub(self):
        time_value = self.pop()
        self.push(self.pop() - time_value)

    def add(self):
        self.push(self.pop() + self.pop())

    def mul(self):
        self.push(self.pop() * self.pop())

    def div(self):
        time_value = self.pop()
        self.push(self.pop() / time_value)

    def mod(self):
        time_value = self.pop()
        self.push(self.pop() % time_value)

    def eq(self):
        self.push(self.pop() == self.pop())

    def cast_int(self):
        self.push(int(self.pop()))

    def cast_str(self):
        self.push(str(self.pop()))

    def drop(self):
        self.pop()
