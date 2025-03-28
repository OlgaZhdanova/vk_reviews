#class ValueError(Exception):
 #   def __init__(self, text):
  #      super().__init__(text)
   # def __str__(self):
    #    return 'empty string is not allowed'
    
def double_print(string):
    try:
        if string == '':
            raise ValueError('empty string is not allowed')
        print(string)
        print(string)
    except ValueError:
        print('empty string is not allowed')

double_print('')