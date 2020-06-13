class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount
        print(self.name, self.value)


class Bank(object):

    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    @staticmethod
    def chk_corruption(i):
        if len(i.__dict__) % 2 == 0:
            print("even number of attributes")
            return 0
        for attr in i.__dict__:
            if attr[0] == 'b':
                print("attribute starting with 'b'")
                return 0
        if not any(attr.startswith('zip' or 'addr') for attr in i.__dict__):
            print("no attribute starting with 'zip' or 'addr'")
            return 0
        if 'name' and 'id' and 'value' not in list(i.__dict__.keys()):
            print("no attribute 'name', 'id', and 'value'")
            return 0
        return 1

    def transfer(self, origin, dest, amount):
        ori_exist = 0
        dst_exist = 0
        for i in self.account:
            if origin == i.id or origin == i.name:
                ori_exist = i
            if dest == i.id or dest == i.name:
                dst_exist = i
        if ori_exist == 0 or dst_exist == 0:
            print("No account.")
            return (False)

        if Bank.chk_corruption(ori_exist) == 0:
            print("ori corrupted")
            return (False)
        if ori_exist.value < amount or amount < 0:
            print("not enough money")
            return (False)
        if Bank.chk_corruption(dst_exist) == 0:
            print("dst corrupted")
            return (False)

        ori_exist.transfer(-amount)
        dst_exist.transfer(amount)
        return (True)

    def fix_account(self, account):
        corrupted = 0
        will_delete = 0
        for i in self.account:
            if account in i.__dict__.values():
                corrupted = i
        if corrupted == 0:
            print("No account")
            return (False)

        for attr in corrupted.__dict__:
            if attr[0] == 'b':
                will_delete = attr
        if will_delete != 0:
            corrupted.__dict__.pop(will_delete)

        if not any(attr.startswith('zip' or 'addr') for attr in corrupted.__dict__):
            corrupted.__dict__['zip'] = '000-000'

        if 'name' not in i.__dict__.keys():
            corrupted.__dict__['name'] = 'sample name'
        if 'id' not in i.__dict__.keys():
            corrupted.__dict__['id'] = Account.ID_COUNT
            Account.ID_COUNT += 1
        if 'value' not in i.__dict__.keys():
            corrupted.__dict__['value'] = 0

        if len(corrupted.__dict__) % 2 == 0:
            corrupted.__dict__['extra'] = 'extra attr'
        return (True)