# 2015.11.18 12:05:01 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/lib2to3/pgen2/parse.py
"""Parser engine for the grammar tables generated by pgen.

The grammar table must be loaded first.

See Parser/parser.c in the Python distribution for additional info on
how this parsing engine works.

"""
from . import token

class ParseError(Exception):
    """Exception to signal the parser is stuck."""

    def __init__(self, msg, type, value, context):
        Exception.__init__(self, '%s: type=%r, value=%r, context=%r' % (msg,
         type,
         value,
         context))
        self.msg = msg
        self.type = type
        self.value = value
        self.context = context


class Parser(object):
    """Parser engine.
    
    The proper usage sequence is:
    
    p = Parser(grammar, [converter])  # create instance
    p.setup([start])                  # prepare for parsing
    <for each input token>:
        if p.addtoken(...):           # parse a token; may raise ParseError
            break
    root = p.rootnode                 # root of abstract syntax tree
    
    A Parser instance may be reused by calling setup() repeatedly.
    
    A Parser instance contains state pertaining to the current token
    sequence, and should not be used concurrently by different threads
    to parse separate token sequences.
    
    See driver.py for how to get input tokens by tokenizing a file or
    string.
    
    Parsing is complete when addtoken() returns True; the root of the
    abstract syntax tree can then be retrieved from the rootnode
    instance variable.  When a syntax error occurs, addtoken() raises
    the ParseError exception.  There is no error recovery; the parser
    cannot be used after a syntax error was reported (but it can be
    reinitialized by calling setup()).
    
    """

    def __init__(self, grammar, convert = None):
        """Constructor.
        
        The grammar argument is a grammar.Grammar instance; see the
        grammar module for more information.
        
        The parser is not ready yet for parsing; you must call the
        setup() method to get it started.
        
        The optional convert argument is a function mapping concrete
        syntax tree nodes to abstract syntax tree nodes.  If not
        given, no conversion is done and the syntax tree produced is
        the concrete syntax tree.  If given, it must be a function of
        two arguments, the first being the grammar (a grammar.Grammar
        instance), and the second being the concrete syntax tree node
        to be converted.  The syntax tree is converted from the bottom
        up.
        
        A concrete syntax tree node is a (type, value, context, nodes)
        tuple, where type is the node type (a token or symbol number),
        value is None for symbols and a string for tokens, context is
        None or an opaque value used for error reporting (typically a
        (lineno, offset) pair), and nodes is a list of children for
        symbols, and None for tokens.
        
        An abstract syntax tree node may be anything; this is entirely
        up to the converter function.
        
        """
        self.grammar = grammar
        self.convert = convert or (lambda grammar, node: node)

    def setup(self, start = None):
        """Prepare for parsing.
        
        This *must* be called before starting to parse.
        
        The optional argument is an alternative start symbol; it
        defaults to the grammar's start symbol.
        
        You can use a Parser instance to parse any number of programs;
        each time you call setup() the parser is reset to an initial
        state determined by the (implicit or explicit) start symbol.
        
        """
        if start is None:
            start = self.grammar.start
        newnode = (start,
         None,
         None,
         [])
        stackentry = (self.grammar.dfas[start], 0, newnode)
        self.stack = [stackentry]
        self.rootnode = None
        self.used_names = set()
        return

    def addtoken(self, type, value, context):
        """Add a token; return True iff this is the end of the program."""
        ilabel = self.classify(type, value, context)
        while True:
            dfa, state, node = self.stack[-1]
            states, first = dfa
            arcs = states[state]
            for i, newstate in arcs:
                t, v = self.grammar.labels[i]
                if ilabel == i:
                    if not t < 256:
                        raise AssertionError
                        self.shift(type, value, newstate, context)
                        state = newstate
                        while states[state] == [(0, state)]:
                            self.pop()
                            if not self.stack:
                                return True
                            dfa, state, node = self.stack[-1]
                            states, first = dfa

                        return False
                    if t >= 256:
                        itsdfa = self.grammar.dfas[t]
                        itsstates, itsfirst = itsdfa
                        ilabel in itsfirst and self.push(t, self.grammar.dfas[t], newstate, context)
                        break
            else:
                if (0, state) in arcs:
                    self.pop()
                    if not self.stack:
                        raise ParseError('too much input', type, value, context)
                else:
                    raise ParseError('bad input', type, value, context)

    def classify(self, type, value, context):
        """Turn a token into a label.  (Internal)"""
        if type == token.NAME:
            self.used_names.add(value)
            ilabel = self.grammar.keywords.get(value)
            if ilabel is not None:
                return ilabel
        ilabel = self.grammar.tokens.get(type)
        if ilabel is None:
            raise ParseError('bad token', type, value, context)
        return ilabel

    def shift(self, type, value, newstate, context):
        """Shift a token.  (Internal)"""
        dfa, state, node = self.stack[-1]
        newnode = (type,
         value,
         context,
         None)
        newnode = self.convert(self.grammar, newnode)
        if newnode is not None:
            node[-1].append(newnode)
        self.stack[-1] = (dfa, newstate, node)
        return

    def push(self, type, newdfa, newstate, context):
        """Push a nonterminal.  (Internal)"""
        dfa, state, node = self.stack[-1]
        newnode = (type,
         None,
         context,
         [])
        self.stack[-1] = (dfa, newstate, node)
        self.stack.append((newdfa, 0, newnode))
        return

    def pop(self):
        """Pop a nonterminal.  (Internal)"""
        popdfa, popstate, popnode = self.stack.pop()
        newnode = self.convert(self.grammar, popnode)
        if newnode is not None:
            if self.stack:
                dfa, state, node = self.stack[-1]
                node[-1].append(newnode)
            else:
                self.rootnode = newnode
                self.rootnode.used_names = self.used_names
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\pgen2\parse.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:05:01 St�edn� Evropa (b�n� �as)
