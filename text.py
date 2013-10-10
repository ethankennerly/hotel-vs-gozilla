import codecs
import os

def windows_to_unix(text):
    r'''Convert Windows carriage return + line feed to Unix line feed.
    http://www.freenetpages.co.uk/hp/alan.gauld/tutfiles.htm
    http://en.wikipedia.org/wiki/Newline
    >>> windows_to_unix('a\r\nb')
    'a\nb'

    And then single carriage returns to single line feed.
    >>> windows_to_unix('a\rb')
    'a\nb'
    >>> windows_to_unix('a\r\r\n\r\nb')
    'a\n\n\nb'
    '''
    return text.replace('\r\n', '\n').replace('\r', '\n')

def load(path):
    r'''Read a text file into a string.
    >>> script_basename = os.path.basename('text.py')
    >>> utf_text = load(script_basename)
    >>> 0 <= utf_text.find('def load')
    True
    >>> 0 <= utf_text.find('\r\n')
    False
    '''
    file = codecs.open(os.path.abspath(path), 'r', 'utf-8')
    utf_text = file.read()
    utf_text = windows_to_unix(utf_text)
    file.close()
    return utf_text


def save(path, utf_text):
    '''Save text to a file.
    >>> save('__tmp.txt', 'a')
    >>> load('__tmp.txt')
    u'a'
    >>> os.remove('__tmp.txt')
    '''
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.mkdir(directory)
    output = codecs.open(path, 'w', 'utf-8')
    output.write(utf_text)
    output.flush()
    output.close()


def sort_words(text):
    '''
    >>> sort_words('b a')
    'a b'
    '''
    words = text.split(' ')
    words.sort()
    sorted_text = ' '.join(words)
    return sorted_text
    

if __name__ == '__main__':
    import code_unit
    code_unit.test(__file__)

