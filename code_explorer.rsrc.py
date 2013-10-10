{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'code_explorer',
          'title':u'Python Code Explorer',
          'size':(224, 133),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileImport',
                   'label':u'&Import module',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileReloadModule',
                   'label':u'Reload a Python &module',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileSaveShell',
                   'label':u'Save &shell input and output',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileSaveShellHistory',
                   'label':u'Save shell &history',
                  },
                  # XXX Hard to predict what will happen.
                  ##{'type':'MenuItem',
                  ## 'name':'menuFileLoadShellHistory',
                  ## 'label':u'&Load shell history',
                  ##},
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':u'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'Button', 
    'name':'saveShellHistory', 
    'position':(113, 33), 
    'label':u'Save History', 
    },

{'type':'Button', 
    'name':'saveShell', 
    'position':(15, 34), 
    'label':u'Save Shell', 
    },

{'type':'Button', 
    'name':'reload_module', 
    'position':(113, 3), 
    'label':u'reload module', 
    },

{'type':'Button', 
    'name':'import', 
    'position':(15, 4), 
    'label':u'import *', 
    },

] # end components
} # end background
] # end backgrounds
} }
