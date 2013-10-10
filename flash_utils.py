'''mock flash.utils.getTimer'''

import time

def getTimer():
    '''milliseconds since import.
    >>> now = getTimer()
    >>> if not 1 <= now:  now
    '''
    seconds = time.clock()
    milliseconds = int(seconds * 1000)
    return milliseconds
    
start = getTimer()

import code_unit
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--unit", default="",
        dest="unit", help="unit to doctest [default: %default]")
    #parser.add_option('-v', '--verbose', dest='verbose', default='warning',
    #                help="Increase verbosity")
    (options, args) = parser.parse_args()
    #log_level = logging_levels[options.verbose]
    #logging.basicConfig(level=log_level)
    if options.unit:
        unit = eval(options.unit)
        code_unit.doctest_unit(unit)
    else:
        units = globals().values()
        ## units.remove(setup_example)
        code_unit.doctest_units(units)

