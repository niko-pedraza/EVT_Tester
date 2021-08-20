from abc import ABC, abstractmethod
import platform
import subprocess
from tkinter import *
import flask


class Validator(ABC):

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, objtype=None):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


# Validate IpValue
class IPV4(Validator):

    def validate(self, string):
        if string.count('.') != 3:
            raise ValueError(
                f'{string} expects to have 4 byte locations '
            )
        if not all((0 <= int(d) <= 255) for d in string.split('.')):
            raise ValueError(
                f'{string} out of byte value range'
            )
        if not all(str(int(i)) == i for i in string.split('.')):
            raise ValueError(
                f'{string} has byte value that is not decimal format'
            )
        print('Updating printer Ip to ' + string)


class ValidModel(Validator):
    def __init__(self, *options):
        self.option = set(options)

    def validate(self, value):
        if value is not None:
            if value not in self.option:
                raise NameError(
                    'Invalid Model Type'
                )
            print(type(value))
            if not isinstance(value, str, ):
                raise TypeError(
                    'Invalid data input type must be string'
                )
            print('Updating Printer Model:' + value)
        else:
            pass


class Printer(IPV4):
    ip = IPV4()
    model = ValidModel('t800', 't6000', 't6000e', 't8000', 't4000')

    def __init__(self, ip: str, model=None):
        self.ip = ip
        self.model = model

    def ping(self, host):
        # checks system its being run on
        # print(platform.system().lower())
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        # command to be ran on terminal
        command = ['ping', param, 1, host]
        process

        return subprocess.run(command).returncode == 0

    @property
    def status(self):
        return 'ACTIVE' if self.ping(self.ip) else 'INACTIVE'


# ip = '127.0.0.1'
#
# printer = Printer(ip)
# printer.ip = '192.168.201.225'
# printer.model = 't800'
#
# printer.model = 't6000e'
# print(printer)
# print(printer.status)


def main():
    ipwindow = Tk()
    title = Text(ipwindow,'Add printer IP')
    title.pack(side='top')

    ipwindow.mainloop()


if __name__ == '__main__':
    main()
