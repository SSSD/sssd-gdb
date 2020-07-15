from sssd_gdb.decorators import PrettyPrinterGroup
from sssd_gdb.printers import PrettyPrinter


@PrettyPrinterGroup('LDB Pretty Printers')
class LDBPrinters(object):
    class ldb_dn(PrettyPrinter):
        def to_string(self):
            try:
                return self.val['linearized']
            except(Exception):
                return 'unsupported'

    class ldb_val(PrettyPrinter):
        def to_string(self):
            return f'len: {self.val["length"]} {self.val["data"]}'

    class ldb_message_element(PrettyPrinter):
        def to_string(self):
            out = 'flags: {}, name: {}, values: {}'.format(
                self.val["flags"],
                self.val["name"],
                self.val["num_values"]
            )

            for i in range(self.val["num_values"]):
                out += '\n' + self.indent(
                    LDBPrinters.ldb_val, self.val["values"][i]
                )

            out += '\n'

            return out

    class ldb_message(PrettyPrinter):
        def to_string(self):
            out = 'dn: {}, elements: {}'.format(
                self.use(LDBPrinters.ldb_dn, self.val["dn"]),
                self.val["num_elements"]
            )

            for i in range(self.val["num_elements"]):
                out += '\n' + self.indent(
                    LDBPrinters.ldb_message_element, self.val["elements"][i]
                )

            return out

    class ldb_result(PrettyPrinter):
        def to_string(self):
            out = 'messages: {}'.format(
                self.val["count"]
            )

            for i in range(self.val["count"]):
                out += '\n' + self.indent(
                    LDBPrinters.ldb_message, self.val["msgs"][i]
                )

            return out
