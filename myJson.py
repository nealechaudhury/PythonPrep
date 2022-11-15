import json

def _parseL(_L=[]):
    for _v in _L:
        yield _v

if __name__ == '__main__':
    people_string = '''
        {
            "people":[
                {
                    "name":"John Smith",
                    "phone": "212-555-1212",
                    "emails" : ["jsmith1.firm.com", "jsmith2.firm2.com"],
                    "has_license":false
                },
                {
                    "name":"Jane Doe",
                    "phone": "212-555-2323",
                    "emails" : ["jdoe1.firm.com", "jdoe2.firm2.com"],
                    "has_license":true
                }
            ]
        }
        '''

    #print (f'{people_string}')
    # Now load this in a data object
    _mydata = json.loads(people_string)
    print (f'{_mydata} \ntype :{type(_mydata)}')
    for key,value in _mydata.items():
        print (f'Key: {key}, type: {type(key)} -> Value: {value}, type: {type(value)}')
        print (f'Key = {key}')
        for i,v in enumerate(_parseL(value)):
            print (f'{i}: {v} - {type(v)}')


    print (_mydata['people'])
    print (_mydata.get('people'))

