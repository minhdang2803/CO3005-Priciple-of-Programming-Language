import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_101(self):
        self.assertTrue(TestLexer.test("Val", "Val,<EOF>", 101))

    def test_102(self):
        self.assertTrue(TestLexer.test(""" "TrueFalseTrueFalseTrueFalseTrueFalse' " """,
                                       """TrueFalseTrueFalseTrueFalseTrueFalse' ,<EOF>""", 102))

    def test_103(self):
        self.assertTrue(TestLexer.test(""" "abc\\" """, """Illegal Escape In String: abc\\\"""", 103))

    def test_104(self):
        self.assertTrue(TestLexer.test("000_x123789", "00,0,_x123789,<EOF>", 104))

    def test_105(self):
        self.assertTrue(TestLexer.test("""He asked me: 'Where is John?'""", "He,asked,me,:,Error Token '", 105))

    def test_106(self):
        self.assertTrue(TestLexer.test("1_234.567_789e246_357", "1234.567,_789e246_357,<EOF>", 106))

    def test_107(self):
        self.assertTrue(TestLexer.test("Something \ ", """Something,Error Token \\""", 107))

    def test_108(self):
        self.assertTrue(TestLexer.test(""" abc" """, """abc,Unclosed String:  """, 108))

    def test_109(self):
        self.assertTrue(TestLexer.test(""" "'abc """, """Unclosed String: 'abc """, 109))

    def test_110(self):
        self.assertTrue(TestLexer.test(""" 1234.1e2000 0X1F """, """1234.1e2000,0X1F,<EOF>""", 110))

    def test_111(self):
        self.assertTrue(TestLexer.test(""" "abc\n\abc\" """, """Unclosed String: abc""", 111))

    def test_112(self):
        self.assertTrue(TestLexer.test(""" $123asd """, """$123asd,<EOF>""", 112))

    def test_113(self):
        self.assertTrue(TestLexer.test(""" 12_3_32__32_E1_323_1 """, """12332,__32_E1_323_1,<EOF>""", 113))

    def test_114(self):
        self.assertTrue(TestLexer.test(""" 0.123_3 """, """0.123,_3,<EOF>""", 114))

    def test_115(self):
        self.assertTrue(TestLexer.test(""" .3213 """, """.,3213,<EOF>""", 115))

    def test_116(self):
        self.assertTrue(TestLexer.test(""" "## This is a comment ##" """, """## This is a comment ##,<EOF>""", 116))

    def test_117(self):
        self.assertTrue(TestLexer.test(""" "TrueFalseTrueFalseTrueFalseTrueFalse'" """,
                                       """Unclosed String: TrueFalseTrueFalseTrueFalseTrueFalse'" """, 117))

    def test_118(self):
        self.assertTrue(TestLexer.test(""" 0 00 0x0 0X0 0b0 0B0 """, """0,00,0x0,0X0,0b0,0B0,<EOF>""", 118))

    def test_119(self):
        self.assertTrue(TestLexer.test(""" 0000x00X00b00B0 """, """00,00,x00X00b00B0,<EOF>""", 119))

    def test_120(self):
        self.assertTrue(TestLexer.test(""" 0000x00X00b00B0 """, """00,00,x00X00b00B0,<EOF>""", 120))

    def test_121(self):
        self.assertTrue(TestLexer.test(""" 0000x00X00b00B0 """, """00,00,x00X00b00B0,<EOF>""", 121))

    def test_122(self):
        self.assertTrue(TestLexer.test(""" 0e123 .0e123 """, """0e123,.0e123,<EOF>""", 122))

    def test_123(self):
        self.assertTrue(TestLexer.test(""" 0b0e123 """, """0b0,e123,<EOF>""", 123))

    def test_124(self):
        self.assertTrue(TestLexer.test(""" 128397128937_32112312_31242121094582149012_312123123__12389123721 """,
                                       """1283971289373211231231242121094582149012312123123,__12389123721,<EOF>""",
                                       124))

    def test_125(self):
        self.assertTrue(TestLexer.test(""" 4587.E00000 6754.e-00000 4530.0000e3 """,
                                       """4587.E00000,6754.e-00000,4530.0000e3,<EOF>""", 125))

    def test_126(self):
        self.assertTrue(TestLexer.test(""" 456789.0e0 0.0e0 12345.E-0 """, """456789.0e0,0.0e0,12345.E-0,<EOF>""", 126))

    def test_127(self):
        self.assertTrue(TestLexer.test(""" _123412 __218374 """, """_123412,__218374,<EOF>""", 127))

    def test_128(self):
        self.assertTrue(TestLexer.test(""" 12341234_ 987435__ """, """12341234,_,987435,__,<EOF>""", 128))

    def test_129(self):
        self.assertTrue(TestLexer.test(""" 0_x123128721 """, """0,_x123128721,<EOF>""", 129))

    def test_130(self):
        input = """0b01234e123abc"""
        output = """0b0,1234e123,abc,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 130))


    def test_131(self):
        input = """001234e123abc"""
        output = """00,1234e123,abc,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 131))


    def test_132(self):
        input = """0712abc123e45"""
        output = """0712,abc123e45,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 132))


    def test_133(self):
        input = """0xA_B_C_F_G_1,234e-"""
        output = """0xABCF,_G_1,,,234,e,-,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 133))


    def test_134(self):
        input = """0xA_B_C_F_G_1,234e-123"""
        output = """0xABCF,_G_1,,,234e-123,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 134))


    def test_135(self):
        input = """_true_ False;True"""
        output = """_true_,False,;,True,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 135))


    def test_136(self):
        input = """True  False _False;_True"""
        output = """True,False,_False,;,_True,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 136))


    def test_137(self):
        input = """False ##True;_True## false"""
        output = """False,false,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 137))


    def test_138(self):
        input = """ "string \\b" """
        output = """string \\b,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 138))


    def test_139(self):
        input = """ "This is a string containing tab \\t" """
        output = """This is a string containing tab \\t,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 139))


    def test_140(self):
        input = """ "He asked me: '"Where is John?'"" """
        output = """He asked me: '\"Where is John?'\",<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 140))


    def test_141(self):
        input = """ Array(1, 5, 7, 12) """
        output = """Array,(,1,,,5,,,7,,,12,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 141))


    def test_142(self):
        input = """ Array("Kangxi", "Yongzheng", "Qianlong") """
        output = """Array,(,Kangxi,,,Yongzheng,,,Qianlong,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 142))


    def test_143(self):
        input = """ Array(123e-123, "ab\\n", "John") """
        output = """Array,(,123e-123,,,ab\\n,,,John,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 143))


    def test_144(self):
        input = """ Array(123e-123, "ab\\r", "Doe) """
        output = """Array,(,123e-123,,,ab\\r,,,Unclosed String: Doe) """
        self.assertTrue(TestLexer.test(input, output, 144))


    def test_145(self):
        input = """ Array(
               Array("Volvo", "22", "18"),
               Array("Saab", "5", "2"),
               Array("Land Rover", "17", "15"),
           ) """
        output = """Array,(,Array,(,Volvo,,,22,,,18,),,,Array,(,Saab,,,5,,,2,),,,Array,(,Land Rover,,,17,,,15,),,,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 145))


    def test_146(self):
        input = """ a * b, 123 || && !what """
        output = """a,*,b,,,123,||,&&,!,what,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 146))


    def test_147(self):
        input = """ abc !=%>= > || abc == 123!= """
        output = """abc,!=,%,>=,>,||,abc,==,123,!=,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 147))


    def test_148(self):
        input = """ var a: Array[Int, 5];"""
        output = """var,a,:,Array,[,Int,,,5,],;,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 148))


    def test_149(self):
        input = """ var New a,b: Int = 123*b/2, 10"""
        output = """var,New,a,,,b,:,Int,=,123,*,b,/,2,,,10,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 149))


    def test_150(self):
        input = """ Var str: String = "string" +. " concat" """
        output = """Var,str,:,String,=,string,+., concat,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 150))


    def test_151(self):
        input = """ Var $x,$y: Int = 0,0; """
        output = """Var,$x,,,$y,:,Int,=,0,,,0,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 151))


    def test_152(self):
        input = """ ##dnsaknd io21283u821nqwneui## """
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 152))


    def test_153(self):
        input = """ Class Shape{
               Val $numOfShape: Int = 0;
           }
           """
        output = """Class,Shape,{,Val,$numOfShape,:,Int,=,0,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 153))


    def test_154(self):
        input = """ Class Rectangle: Shape{
               getL(){Return Self.length;}
           }
           """
        output = """Class,Rectangle,:,Shape,{,getL,(,),{,Return,Self,.,length,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 154))


    def test_155(self):
        input = """
               $getNumOfShape() {
                    Return $numOfShape;
               }
           """
        output = """$getNumOfShape,(,),{,Return,$numOfShape,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 155))


    def test_156(self):
        input = """
               Class Program{
               main(){
                   Out.printInt(Shape::$numOfShape);
               }
           }
           """
        output = """Class,Program,{,main,(,),{,Out,.,printInt,(,Shape,::,$numOfShape,),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 156))


    def test_157(self):
        input = """
               arr[2] = [1, 2, 3];
               arr[3][3] = 421;
           """
        output = """arr,[,2,],=,[,1,,,2,,,3,],;,arr,[,3,],[,3,],=,421,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 157))


    def test_158(self):
        input = """ arr[23-3/2*10 /2] = 46%2-65/2; """
        output = """arr,[,23,-,3,/,2,*,10,/,2,],=,46,%,2,-,65,/,2,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 158))


    def test_159(self):
        input = """
               ## legal comment ##
           """
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 159))


    def test_160(self):
        input = """ ### \\error in comment ##"""
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 160))

    def test_161(self):
        input = """
            ### Define class #Student\\\\h ###

        """
        output = """Error Token #"""
        self.assertTrue(TestLexer.test(input, output, 161))

    def test_162(self):
        input = """
            ### _23450###9123\\->w32 ##

        """
        output = """Error Token #"""
        self.assertTrue(TestLexer.test(input, output, 162))

    def test_163(self):
        input = """
            ### 1---23 + 39.,2 32. 23e2/ a;s 234.//./2##

        """
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 163))

    def test_164(self):
        input = """12_32 __ 2341+1234"""
        output = """1232,__,2341,+,1234,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 164))

    def test_165(self):
        input = """b.c(12)"""
        output = """b,.,c,(,12,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 165))

    def test_166(self):
        input = """b.c(12)::foo"""
        output = """b,.,c,(,12,),::,foo,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 166))

    def test_167(self):
        input = """mn = b.c(12)::$foo(23_"""
        output = """mn,=,b,.,c,(,12,),::,$foo,(,23,_,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 167))

    def test_168(self):
        input = """stu.foo(12,3)::$mn(,.,.)"""
        output = """stu,.,foo,(,12,,,3,),::,$mn,(,,,.,,,.,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 168))

    def test_169(self):
        input = """tr.py(12).mn::$vjp = foo(12)::mn(123, 1)"""
        output = """tr,.,py,(,12,),.,mn,::,$vjp,=,foo,(,12,),::,mn,(,123,,,1,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 169))

    def test_170(self):
        input = """a.foo = mn - stu.foo(12,3)::$mn(,.,.)"""
        output = """a,.,foo,=,mn,-,stu,.,foo,(,12,,,3,),::,$mn,(,,,.,,,.,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 170))

    def test_171(self):
        input = """New Student(12, "name")"""
        output = """New,Student,(,12,,,name,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 171))

    def test_172(self):
        input = """Class Main(){}
            mainfunc = New Main();
        """
        output = """Class,Main,(,),{,},mainfunc,=,New,Main,(,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 172))

    def test_173(self):
        input = """<=.>=+.==.$%**//!!+<>>...!"""
        output = """<=,.,>=,+.,==.,Error Token $"""
        self.assertTrue(TestLexer.test(input, output, 173))

    def test_174(self):
        input = """<=.>=+.==.%**//!!+<>>...!"""
        output = """<=,.,>=,+.,==.,%,*,*,/,/,!,!,+,<,>,>,..,.,!,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 174))

    def test_175(self):
        input = """Self.selfie('haha')"""
        output = """Self,.,selfie,(,Error Token '"""
        self.assertTrue(TestLexer.test(input, output, 175))

    def test_176(self):
        input = """Self.me = Self.play("foik'"l")"""
        output = """Self,.,me,=,Self,.,play,(,foik'"l,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 176))

    def test_177(self):
        input = """Var a : Int = 10;"""
        output = """Var,a,:,Int,=,10,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 177))

    def test_178(self):
        input = """0x123000b0120032"""
        output = """0x123000,b0120032,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 178))

    def test_179(self):
        input = """0x1230 00b01_2000x123__32"""
        output = """0x1230,00,b01_2000x123__32,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 179))

    def test_180(self):
        input = """0x1230 000b01_2000x123__32"""
        output = """0x1230,00,0b0,12000,x123__32,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 180))

    def test_181(self):
        self.assertTrue(TestLexer.test(""" "abc\\'def gh" """, """abc\\'def gh,<EOF>""", 181))
    def test_182(self):
        self.assertTrue(TestLexer.test(""" "'abcdef" """, """'abcdef,<EOF>""", 182))
    def test_183(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \\t" """,
                                                  """This is a string containing tab \\t,<EOF>""", 183))
    def test_184(self):
        self.assertTrue(TestLexer.test("!!!!a", "!,!,!,!,a,<EOF>", 184))

    def test_185(self):
        self.assertTrue(TestLexer.test(""" "++.--.* *.\\\\.<<.>>.<=<=.>=>=.===/=" """,
                                       """++.--.* *.\\\\.<<.>>.<=<=.>=>=.===/=,<EOF>""", 185))
    def test_186(self):
        self.assertTrue(TestLexer.test(""" "abcdef" """, """abcdef,<EOF>""", 186))

    def test_187(self):
        self.assertTrue(TestLexer.test("1 + 2 * 3 ** 4 ** * 5", """1,+,2,*,3,*,*,4,*,*,*,5,<EOF>""", 187))

    def test_188(self):
        self.assertTrue(TestLexer.test("True && True False || False", "True,&&,True,False,||,False,<EOF>", 188))

    def test_189(self):
        self.assertTrue(TestLexer.test(""" "1.0 +. 0.1 1.2 =/= 1.2 5.5 \\. 1.1" ""","""Illegal Escape In String: 1.0 +. 0.1 1.2 =/= 1.2 5.5 \.""",189))

    def test_190(self):
        self.assertTrue(TestLexer.test(""" "TrueFalseTrueFalse' " ""","""TrueFalseTrueFalse' ,<EOF>""", 190))


    def test_191(self):
        self.assertTrue(TestLexer.test(""" "abc\\" """, """Illegal Escape In String: abc\\\"""" ,191))

    def test_192(self):
        self.assertTrue(TestLexer.test("000_x123", "00,0,_x123,<EOF>", 192))

    def test_193(self):
        self.assertTrue(TestLexer.test("""He asked me: 'Where is John?'""", "He,asked,me,:,Error Token '", 193))

    def test_194(self):
        self.assertTrue(TestLexer.test("1_234.567_789e246_357","1234.567,_789e246_357,<EOF>", 194))

    def test_195(self):
        self.assertTrue(TestLexer.test("Something \ ", """Something,Error Token \\""", 195))

    def test_196(self):
        self.assertTrue(TestLexer.test(""" abc" """, """abc,Unclosed String:  """, 196))

    def test_197(self):
        self.assertTrue(TestLexer.test(""" "'abc """, """Unclosed String: 'abc """, 197))

    def test_198(self):
        self.assertTrue(TestLexer.test(""" 123.1e3000 0X1D """, """123.1e3000,0X1D,<EOF>""", 198))

    def test_199(self):
        self.assertTrue(TestLexer.test(""" "abc\n\abc\" """, """Unclosed String: abc""", 199))

    def test_200(self):
        self.assertTrue(TestLexer.test(""" Foreach( a In 1 .. 10 ) {} """, """Foreach,(,a,In,1,..,10,),{,},<EOF>""", 200))