import sys


def testing_func():
    if (x == 5 or
        x == 7):
        pass

    # Comment A
    if not any(leaf.prefix.count(u'\n')
                for leaf in leaves_after_last_newline):
        pass
    # Comment B
    elif all(leaf.prefix.count(u'\t')
                for leaf in leaves_after_last_newline):
        pass


def tester_method():

    # Comment 1
    # Comment 3
    def inner_method():
        pass

    def inner2():
        # This is a two line
        # comment

        pass


class tester_class():
    u"""
        this is a docstring that
        needs to have its indentation fixed
        """

    y = u"this is a string"

    def inner_class_method():
        x = u"""this is a constant
                that spans over multiples lines"""
        pass

    def innter_class_method2():
    # Comment 2
        pass
