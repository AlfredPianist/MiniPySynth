from parsimonious.grammar import Grammar

#from pyo import *

class MiniPySynth(object):

    def __init__(self, env={}):
        self.env = env
        self.melodia = []
        print self.melodia
        
    def parse(self, source):
        grammar = "\n".join(v.__doc__ for k, v in vars(self.__class__).items()
                            if not k.startswith('__') and hasattr(v, '__doc__')
                                                      and getattr(v, '__doc__'))
        #print Grammar(grammar)['program'].parse(source)
        return Grammar(grammar)['program'].parse(source)

    def evalu(self, source):
        node = self.parse(source) if isinstance(source, str) else source
        method = getattr(self, node.expr_name, lambda node, children: children)
        if node.expr_name in ["func", "ifelse", "ifonly"]:
            return method(node)
        return method(node, [self.evalu(n) for n in node])

    def program(self, node, children):
        """ program = expr* """
        return children

    def expr(self, node, children):
        """ expr = _ (rep / ifelse / ifonly / comp / assignment /
        number / note / name) _ """
        print "Expresion", children[1][0]
        return children[1][0]

    def func(self, node, children):
        """ func = "crear" _ leftvalue "(" parameters ")" _ "{" expr "}" """
        _, _, name, _, params, _, _, _, expr, _ = node
        print "Funcion", node
##        params = map(self.evalu, params)
##        def func(*args):
##            env = dict(self.env.items() + zip(params, args))
##            print env
##            return MiniPySynth(env).evalu(expr)
##        return func

    def call(self, node, children):
        'call = name "(" arguments ")"'
        name, _, arguments, _ = children
        return name(*arguments)

    def arguments(self, node, children):
        'arguments = expr*'
        return children
    
    def parameters(self, node, children):
        """ parameters = leftvalue* """
        return children

##    def playRule(self, node, children):
##        """ playRule = "play" """
##        s = Server().boot()
##        s.start()
##        t = SquareTable(order=15).normalize()
##        met = Metro(time=.125, poly=2).play()
##        amp = TrigEnv(met, table=t, dur=.25, mul=.3)
##        a = Sine(freq = self.melodia, mul = amp).out()
##        print self.melodia

    def rep(self, node, children):
        """ rep = "repita" _ leftvalue "->" _ "(" number "," number ")" ":" _
        "{" expr "}" """
        _, _, var, _, _, _, start, _, end, _, _, _, _, expr, _ = children
        print "Repetir", children
        self.env[var] = start
        for cond in range(start,end+1):
            self.evalu(expr)
            self.env[var] += 1

    def comp(self, node, children):
        """ comp = leftvalue "==" expr """
        var, _, exp = children
        print "Comparacion", var, "y", exp
        return self.env[var] == self.evalu(exp)

    def ifelse(self, node):
        """ ifelse = "si" expr ":" _ "{" expr "}" _ "si no:" _ "{" expr "}" """
        _, cond, _, _, _, cons, _, _, _, _, _, alt, _ = node
        print "If - Then - Else"
        return self.evalu(cons) if self.evalu(cond) else self.evalu(alt)

    def ifonly(self, node):
        """ ifonly = "si" expr ":" _ "{" expr "}" """
        _, cond, _, _, _, cons, _ = node
        print "If Solamente"
        if self.evalu(cond):
            return self.evalu(cons)

    def assignment(self, node, children):
        """ assignment = leftvalue "=" expr """
        leftvalue, _, expr = children
        self.env[leftvalue] = expr
        print "Asignacion", self.env
        return expr
    
    def leftvalue(self, node, children):
        """ leftvalue = ~r"[\D][\w]*" _ """
        print "Valor de la izquierda", node.text.strip()
        return node.text.strip()

    def number(self, node, children):
        """ number = ~r"\d+" _ """
        print "Numero", int(node.text)
        return int(node.text)

    def note(self, node, children):
        """ note = freq alt octva dur dot _ """
        print "Nota", node.text.strip()
        return node.text.strip()

    def name(self, node, children):
        """ name = ~r"[\D][\w]*" _ """
        print "Palabra", node.text
        return node.text.strip()
    
    def freq(self, node, children):
        """ freq = "do" / "re" / "mi" / "fa" / "sol" / "la" / "si" """
        print "Frecuencia", node.text
##        MIDI = {"do": 60, "re": 62, "mi": 64, "fa": 65, "sol": 67,
##                "la": 69, "si": 71}
##        MIDImel = []
##        for k, v in MIDI.iteritems():
##            if k == node.text:
##                MIDImel.append(v)
##        self.melodia.extend(midiToHz(MIDImel))     
        return node.text

    def alt(self, node, children):
        """ alt = ("#"+ / "b"+)? """
        print "Alteracion", node.text
        return node.text

    def octva(self, node, children):
        """ octva = ("'"+ / ","+)? """
        print "Octava", node.text
        return node.text

    def dur(self, node, children):
        """ dur = ~r"1(6{0,1})" / "2" / "4" / "8" / "32" / "64" """
        print "Duracion", node.text
        return int(node.text)

    def dot(self, node, children):
        """ dot = ("."+)? """
        print "Puntillo", node.text
        return node.text

    def _(self, node, children):
        """ _ = ~r"\s*" """

f = open("test_synth.py", "r")
content = f.readlines()
for l in content:
    MiniPySynth().evalu(l)
