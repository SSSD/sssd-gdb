import textwrap


class PrettyPrinter(object):
    def __init__(self, val):
        self.val = val

    def to_string(self):
        raise NotImplementedError('to_string method is not implemented')

    def use(self, cls, val):
        return cls(val).to_string()

    def indent(self, cls, val):
        return textwrap.indent(self.use(cls, val), ' ' * 2)
