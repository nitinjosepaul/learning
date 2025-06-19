from stack import Stack


def linter(inputstring):
    brackets = {'(': ')',
                '[': ']',
                '{': '}'}
    open_brackets = brackets.keys()
    closing_brackets = brackets.values()
    stack_obj = Stack()

    for item in inputstring:
        if item in open_brackets:
            stack_obj.push(item)
        elif item in closing_brackets:
            popped = stack_obj.pop()
            if popped is None:
                return False
            if item != brackets[popped]:
                return False
        else:
            print("Invalid Character : %s" % item)
    else:
        if stack_obj.is_empty():
            return True
        else:
            return False


print(linter("[{{}{}}]"))