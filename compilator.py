import tokenize


def procedure_set_to_map(procedure_commands):
    procedure_commands_map = {}
    flag = False
    procedure_name = ''
    stack = []
    for command in procedure_commands:
        if command == ':':
            flag = True
            continue
        if flag:
            procedure_name = command
            flag = False
            continue
        if not command == ';':
            stack.append(command)
        else:
            stack.append('return')
            procedure_commands_map.update({procedure_name: stack})
            stack = []
    return procedure_commands_map


def compiling(file_name):
    enter_commands = []
    edit_commands = []
    procedure_commands = []

    with tokenize.open(file_name) as f:
        tokens = tokenize.generate_tokens(f.readline)
        flag = False
        for toknum, tokval, _, _, _ in tokens:
            if tokval == '//':
                flag = True
                continue
            if flag and tokval == '\n':
                flag = False
                continue
            if tokval == '\n' or tokval == "', '" or tokval == '':
                continue
            if toknum == tokenize.NUMBER and flag == False:
                enter_commands.append(int(tokval))
                continue
            elif flag == False:
                enter_commands.append(tokval)
        f.close()
        enter_commands.append('exit')

    flag = False
    for command in enter_commands:
        if command == ':':
            flag = True
            procedure_commands.append(command)
            continue
        if command == ';':
            flag = False
            procedure_commands.append(command)
            continue
        if flag:
            procedure_commands.append(command)
        else:
            edit_commands.append(command)

    procedure_commands_map = procedure_set_to_map(procedure_commands)

    for name_procedure in procedure_commands_map:
        for i in range(len(edit_commands)):
            if name_procedure == edit_commands[i]:
                edit_commands[i] = 'call'
                edit_commands.insert(i, name_procedure)
    for name_procedure in procedure_commands_map:
        length = len(edit_commands)
        for value in procedure_commands_map[name_procedure]:
            edit_commands.append(value)
        for i in range(len(edit_commands)):
            if name_procedure == edit_commands[i]:
                edit_commands[i] = length
    return edit_commands
