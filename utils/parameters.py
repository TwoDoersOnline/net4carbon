import aranet4 as ar4
from param import (
    Parameterized,
    DataFrame,
    Selector,
    Integer,
    Action,
    String,
    depends,
    Dict,
)

class Pars(Parameterized):
    """
    Basic setup of parameters, main purpose is to:
    visualize function at runtime while validating user input.
    """  
    REGEX_MAC = "([0-9a-f]{2}[:-]){5}([0-9a-f]{2})"
    ALPHA_NUM = {chr(i):str(i-65) for i in range(65,91)}
    ENTRY_FIL = {'temp':False, 'humi':False, 'pres':False}

        # aranet node
    mac_addr = String('aa:00:11:ff:be:10', regex=REGEX_MAC)
    e_filter = Dict(ENTRY_FIL)
    name     = String('net4carbon')
    version  = String('v1.0.0')
    interval = Integer(-1)
    current  = Dict()

        # gsheets API
    type_sht = Selector({'id': '', 'key': '_by_key', 'url': '_by_url'})
    sheet    = String(label='ID, Key, or URL to sheet:')
    col      = Selector(ALPHA_NUM, doc="column", regex='[A-Z]{1,2}?$')
    row      = Integer(1, step=1,  bounds=(1,10))
    max_rows = Integer(100)
    cell     = String('A1', regex='[A-Z]{1,2}[1-9][0-9]*?$')
    updater  = DataFrame(rows=max_rows, columns=25)
