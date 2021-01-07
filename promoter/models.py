from django.db import models
from django.db import connection

# Create your models here.
class Promoter():
    """
    docstring
    """
    def insertPromoter(self, arg):
        if type(arg) is not dict: return "Invalid"
        else:
            FIELDS = ['name', 'mobilenum', 'email', 'gender', 'password', 'location', 'acc_num', 'ifsc', 'outdoor_events', 'v_code']
            INTERSECT = set(arg.keys()) & set(FIELDS)

            if len(INTERSECT) == len(FIELDS):
                if arg['acc_num'] == '':
                    arg['acc_num'] = None
                    arg['ifsc'] = None
                
                arg['v_code'] = arg['v_code'].capitalize().replace('V', '')
                if arg['v_code'] == '':
                    arg['v_code'] = None

                with connection.cursor() as cursor:
                    query = "insert into PROMOTER(`name`, `email`, `mobile_num`, `gender`, `password`, `location`, `v_code`, `acc_no`, `ifsc`, `outdoor_events`) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(query, [arg['name'], arg['email'], arg['mobilenum'], arg['gender'], arg['password'], arg['location'], arg['v_code'], arg['acc_num'], arg['ifsc'], arg['outdoor_events']] )

                    res = cursor.rowcount
                    print('Success')
                return True if res else False


    def promoterLogin(self, arg):
        if type(arg) is not dict: return "Invalid"
        else:
            FIELDS = ['mobile_num', 'password']
            INTERSECT = set(arg.keys()) & set(FIELDS)

            if len(INTERSECT) == len(FIELDS):

                with connection.cursor() as cursor:
                    query = "select * from PROMOTER where `mobile_num`=%s and `password`=%s"
                    cursor.execute(query, [arg['mobile_num'], arg['password']] )

                    res = cursor.rowcount
                    print('Success')
                return True if res else False
