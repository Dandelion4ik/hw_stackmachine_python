import sys


class data_stack:
    data_stack = []
    tos = None

    def pop(self):
        if len(self.data_stack) > 0:
            if len(self.data_stack) > 1:
                self.tos = self.data_stack[-2]
            else:
                self.tos = None
            return self.data_stack.pop()
        else:
            raise NameError('data_stack is empty')

    def push(self, value):
        self.data_stack.append(value)
        self.tos = value

    def print(self):
        print(self.tos, end=" ")

    def println(self):
        print(self.tos)


def exit():
    sys.exit(0)


class stack_machine(data_stack):
    def __init__(self, enter):
        self.instruct_pointer = 0
        self.return_stack = []
        self.enter = enter
        self.heap = {}
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
                             'exit': exit,
                             'store': self.store,
                             'load': self.load
                             }

    def do_command(self, command):
        if command in self.commands_map:
            self.commands_map[command]()
        elif isinstance(command, int) or isinstance(command, float):
            self.push(command)
        else:
            raise RuntimeError("Unknown command: '%s'" % command)

    def run(self):
        while self.instruct_pointer < len(self.enter):
            command = self.enter[self.instruct_pointer]
            self.instruct_pointer += 1
            self.do_command(command)

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

    def dup(self):
        self.push(self.tos)

    def if_clause(self):
        true_clause = self.pop()
        false_clause = self.pop()
        condition_if = self.pop()
        if condition_if:
            self.push(true_clause)
        else:
            self.push(false_clause)

    def jmp(self):
        if isinstance(self.tos, int) and -1 < self.tos < self.enter:
            self.instruct_pointer = self.pop()
        else:
            RuntimeError('jmp incorrect')

    def stack(self):
        print('Data stack: ', self.data_stack)
        print('Instruction pointer: ', self.instruct_pointer)
        print('Return stack: ', self.return_stack)

    def swap(self):
        value_1 = self.pop()
        value_2 = self.pop()
        self.push(value_1)
        self.push(value_2)

    def read(self):
        self.push(input())

    def call(self):
        self.return_stack.append(self.instruct_pointer)
        self.jmp()

    def return_back(self):
        self.instruct_pointer = self.return_stack.pop()

    def store(self):
        key = self.pop()
        value = self.pop()
        self.heap[key] = value

    def load(self):
        self.push(self.heap[self.pop()])


if __name__ == '__main__':
    enter = [2, 1, 2, 'print', 'store','load', 'print']
    a = stack_machine(enter)
    a.run()
