import re
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput 
from kivy.properties import *
from kivy.uix.widget import Widget 

class Input_Filter(TextInput):
    '''
    This class will restrict the user input to only decimal digits.
    Note: can accept floats
    '''
    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(Input_Filter, self).insert_text(s, from_undo=from_undo)
		

class Input_Filter_tf(TextInput):
    '''
    This class will restrict the user input to only decimal digits 
    and character 't' indicating True, and character 'f' indicating False.
    Note: can accept floats
    '''
    pat = re.compile('[^t-tf-f0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(Input_Filter_tf, self).insert_text(s, from_undo=from_undo)

class Input_Filter_tf_comma(TextInput):
    '''
    This class will restrict the user input to only decimal digits 
    and character 't' indicating True, and character 'f' indicating False,
    and comma ','.
    Note: can accept floats
    '''
    pat = re.compile('[^0-9t-tf-f\,]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(Input_Filter_tf_comma, self).insert_text(s, from_undo=from_undo)