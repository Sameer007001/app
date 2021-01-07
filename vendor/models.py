from django.db import models
from django.db import connection    

# Create your models here.
class Vendor():
    """
    docstring
    """
    def insertVendor(self, arg):
        if type(arg) is not dict: return "Invalid"
        else:
            FIELDS = ['name', 'mobilenum', 'email', 'password', 'location', 'acc_num', 'ifsc']
            INTERSECT = set(arg.keys()) & set(FIELDS)

            if len(INTERSECT) == len(FIELDS):
                if arg['acc_num'] == '':
                    arg['acc_num'] = None
                    arg['ifsc'] = None

                with connection.cursor() as cursor:
                    query = "insert into VENDOR(`name`, `mobile_num`, `email`, `password`, `location`, `acc_no`, `ifsc`) values(%s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(query, [arg['name'], arg['mobilenum'], arg['email'], arg['password'], arg['location'], arg['acc_num'], arg['ifsc']] )

                    res = cursor.rowcount
                    print('Success')
                return True if res else False


