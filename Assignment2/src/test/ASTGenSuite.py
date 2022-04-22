import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_301(self):
        input = '''
        Class A {}
        '''
        expect = 'Program([ClassDecl(Id(A),[])])'
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_302(self):
        input = '''
        Class Child:Parent {}
        '''
        expect = 'Program([ClassDecl(Id(Child),Id(Parent),[])])'
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_303(self):
        input = '''
        Class Child:Parent {}
        Class Neighbor {}
        '''
        expect = 'Program([ClassDecl(Id(Child),Id(Parent),[]),ClassDecl(Id(Neighbor),[])])'
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304(self):
        input = '''
        Class Dad:GrandDad {}
        Class Son:Dad {}
        '''
        expect = 'Program([ClassDecl(Id(Dad),Id(GrandDad),[]),ClassDecl(Id(Son),Id(Dad),[])])'
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        input = '''
        Class Dad:GrandDad {}
        Class Son:Dad {}
        Class Uncle {}
        '''
        expect = 'Program([ClassDecl(Id(Dad),Id(GrandDad),[]),ClassDecl(Id(Son),Id(Dad),[]),ClassDecl(Id(Uncle),[])])'
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input = '''
        Class A{
            Var a : Int;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType))])])'
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input = '''
        Class A{
            Var x,y,$z : Int;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Instance,VarDecl(Id(y),IntType)),AttributeDecl(Static,VarDecl(Id($z),IntType))])])'
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        input = '''
        Class A{
            Val $x,$z,y : String;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($x),StringType,None)),AttributeDecl(Static,ConstDecl(Id($z),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(y),StringType,None))])])'
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_309(self):
        input = '''
        Class A{
            Val y : String;
            Var $x : Int;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(y),StringType,None)),AttributeDecl(Static,VarDecl(Id($x),IntType))])])'
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_310(self):
        input = '''
        Class A{
            Val a :Int = 1;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1)))])])'
        self.assertTrue(TestAST.test(input, expect, 310))
#
    def test_311(self):
        input = '''
         Class A{
            Val a :Int = 1;
            Var b :String = "Hello";
            Val c :Int = 0xABC;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),StringType,StringLit(Hello))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(2748)))])])'
        self.assertTrue(TestAST.test(input, expect, 311))
#
    def test_312(self):
        input = '''
         Class A{
            Val $x, $y : Int = 1, 2+2;
            Var p,$q : Boolean = True, False;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id($y),IntType,BinaryOp(+,IntLit(2),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(p),BoolType,BooleanLit(True))),AttributeDecl(Static,VarDecl(Id($q),BoolType,BooleanLit(False)))])])'
        self.assertTrue(TestAST.test(input, expect, 311))
#
    def test_313(self):
        input = '''
        Class A{
           Var $x, $y : Int = 0, 0;
           Val a, $b : Int = 0x0, 0B0;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Static,ConstDecl(Id($b),IntType,IntLit(0)))])])'
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_314(self):
        input = '''
         Class A{
            Var a : Dad;
            Var b : Son = New Son();
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Dad)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(Son)),NewExpr(Id(Son),[])))])])'
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        input = '''
         Class A{
            Var array : Array[Int,2];
            Var brray : Array[Int,2] = Array(1,2);
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(array),ArrayType(2,IntType))),AttributeDecl(Instance,VarDecl(Id(brray),ArrayType(2,IntType),[IntLit(1),IntLit(2)]))])])'
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        input = '''
         Class A{
            Var array : Array[Int,0b10];
            Var brray : Array[Int,0B10] = Array(1,2);
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(array),ArrayType(2,IntType))),AttributeDecl(Instance,VarDecl(Id(brray),ArrayType(2,IntType),[IntLit(1),IntLit(2)]))])])'
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_317(self):
        input = '''
        Class A{
            func(){}
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(func),Instance,[],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        input = '''
        Class C{
            foo(x : Float){}
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(foo),Instance,[param(Id(x),FloatType)],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input = '''
        Class C{
            foo(a : Int){
                Var x,y: Int = 1+1, 2+2;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType)],Block([VarDecl(Id(x),IntType,BinaryOp(+,IntLit(1),IntLit(1))),VarDecl(Id(y),IntType,BinaryOp(+,IntLit(2),IntLit(2)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        input = '''
        Class C{
            foo(){
                Return 1+2;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(foo),Instance,[],Block([Return(BinaryOp(+,IntLit(1),IntLit(2)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
        input = '''
        Class C{
            foo(){
                Return False;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(foo),Instance,[],Block([Return(BooleanLit(False))]))])])'
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input = """
        Class A {
            foo(){
                a.b.c[1]=d.e.f(1,2+3);
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(ArrayCell(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),[IntLit(1)]),CallExpr(FieldAccess(Id(d),Id(e)),Id(f),[IntLit(1),BinaryOp(+,IntLit(2),IntLit(3))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
       input = """
       Class A {
           foo(){
               Var a:Array[Array[Int,5],5];
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),ArrayType(5,ArrayType(5,IntType)))]))])])'
       self.assertTrue(TestAST.test(input, expect, 323))


    def test_324(self):
        input = '''
        Class C{
            foo(a : Int){
                a = 12;
                Return 2*a +3;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType)],Block([AssignStmt(Id(a),IntLit(12)),Return(BinaryOp(+,BinaryOp(*,IntLit(2),Id(a)),IntLit(3)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
       input = """
       Class A:B{
           foo(){
               a = New a(1+2*3/4).b.c();
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),CallExpr(FieldAccess(NewExpr(Id(a),[BinaryOp(+,IntLit(1),BinaryOp(/,BinaryOp(*,IntLit(2),IntLit(3)),IntLit(4)))]),Id(b)),Id(c),[]))]))])])'
       self.assertTrue(TestAST.test(input, expect, 325))


    def test_326(self):
        input = """
        Class A {
            foo(){
                a[1][b[3]]="abc";
                Return a[1][b[3]];
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(b),[IntLit(3)])]),StringLit(abc)),Return(ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(b),[IntLit(3)])]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_327(self):
        input = '''
        Class Programming{
            Val $x: Int = 10_3;
            main(){
                Val y: Float = 11.23123;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Programming),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(103))),MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(y),FloatType,FloatLit(11.23123))]))])])'
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_328(self):
       input = """
       Class A:B{
           Foo(){
                Var a : Int = 12;
                If(a > 10){}
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(12)),If(BinaryOp(>,Id(a),IntLit(10)),Block([]))]))])])'
       self.assertTrue(TestAST.test(input, expect, 328))

    def test_329(self):
       input = """
       Class A:B{
           Foo(){
                Var a : Int = 12;
                If(a > 10){ Return a + 2; }
                If(a == 10){ Return a + 1; }
                Else{ Return a + 3; }

                Var b : Int = 13;
                If(b < 10){ b = 10; Return b;}
                Elseif(b == 10){ Return b; }
                Else{Return b + 2; }
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(12)),If(BinaryOp(>,Id(a),IntLit(10)),Block([Return(BinaryOp(+,Id(a),IntLit(2)))])),If(BinaryOp(==,Id(a),IntLit(10)),Block([Return(BinaryOp(+,Id(a),IntLit(1)))]),Block([Return(BinaryOp(+,Id(a),IntLit(3)))])),VarDecl(Id(b),IntType,IntLit(13)),If(BinaryOp(<,Id(b),IntLit(10)),Block([AssignStmt(Id(b),IntLit(10)),Return(Id(b))]),If(BinaryOp(==,Id(b),IntLit(10)),Block([Return(Id(b))]),Block([Return(BinaryOp(+,Id(b),IntLit(2)))])))]))])])'
       self.assertTrue(TestAST.test(input, expect, 329))

    def test_330(self):
       input = """
       Class A:B{
           Foo(){
               If(3){}Elseif(4){}Elseif(5){}Else{a=1;}
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(3),Block([]),If(IntLit(4),Block([]),If(IntLit(5),Block([]),Block([AssignStmt(Id(a),IntLit(1))]))))]))])])'
       self.assertTrue(TestAST.test(input, expect, 330))

    def test_331(self):
       input = """
       Class A:B{
           Foo(){
               a.b(1+2,3*4-5.5);
               If(1)
                   {}
               Elseif(2)
                   {}
               Elseif(3)
                   {}
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([Call(Id(a),Id(b),[BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(-,BinaryOp(*,IntLit(3),IntLit(4)),FloatLit(5.5))]),If(IntLit(1),Block([]),If(IntLit(2),Block([]),If(IntLit(3),Block([]))))]))])])'
       self.assertTrue(TestAST.test(input, expect, 331))

    def test_332(self):
        input = '''
        Class Programming{
            main(){
                If(1){
                Love = 0;
                }
                Elseif(2){
                Love = 1;}
                Else{
                Friendzone = True;
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Programming),[MethodDecl(Id(main),Instance,[],Block([If(IntLit(1),Block([AssignStmt(Id(Love),IntLit(0))]),If(IntLit(2),Block([AssignStmt(Id(Love),IntLit(1))]),Block([AssignStmt(Id(Friendzone),BooleanLit(True))])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 332))
#
    def test_333(self):
        input = '''
        Class Programming{
            main(){
                If( (a < 2) && (b > 3)){
                    d = "OK";
                }
                Else{
                    e = "FAIL";
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Programming),[MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(&&,BinaryOp(<,Id(a),IntLit(2)),BinaryOp(>,Id(b),IntLit(3))),Block([AssignStmt(Id(d),StringLit(OK))]),Block([AssignStmt(Id(e),StringLit(FAIL))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 333))


    def test_334(self):
        input = '''
        Class Program{
            main(a : Int){
                Foreach (i In 1 .. 100 By 2) {
                Out.printInt(i);
                }
                Foreach (x In 5 .. 2) {
                Out.printInt(arr[x]);
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])]),For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 334))
#
    def test_335(self):
        input = '''
        Class Program{
            main(){
                Var r, s: Int;
                r = 2.0;
                Var a, b: Array[Int, 5];
                s = r * r * Self.myPI;
                a[0] = s;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType),AssignStmt(Id(r),FloatLit(2.0)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))]))])])'
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_336(self):
        input = '''
        Class Program{
            main(a : Int){
                a = "String";
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([AssignStmt(Id(a),StringLit(String))]))])])'
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_337(self):
        input = '''
        Class Program{
            main(a : Int){
            If (1 + 2 == 0) {
                OutScreen.println(3 * 2);
            }
            Elseif (1 + 2 == "3") {
                Sys32.terminate(41241211 - "4124124124");
            }
            Else {
                Break;
                Return;
            }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(==,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(0)),Block([Call(Id(OutScreen),Id(println),[BinaryOp(*,IntLit(3),IntLit(2))])]),If(BinaryOp(==,BinaryOp(+,IntLit(1),IntLit(2)),StringLit(3)),Block([Call(Id(Sys32),Id(terminate),[BinaryOp(-,IntLit(41241211),StringLit(4124124124))])]),Block([Break,Return()])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_338(self):
        input = '''
        Class C{
                function(){
                    a = b%c + Self.foo();
                    a = b*c*d + Self.foo();
                    Self.foo();
                    Return True;
                }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(function),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(%,Id(b),Id(c)),CallExpr(Self(),Id(foo),[]))),AssignStmt(Id(a),BinaryOp(+,BinaryOp(*,BinaryOp(*,Id(b),Id(c)),Id(d)),CallExpr(Self(),Id(foo),[]))),Call(Self(),Id(foo),[]),Return(BooleanLit(True))]))])])'
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_339(self):
        input = '''
        Class B{
                main(){
                }
                foo(){
                    a = b%c + Self.foo();
                    Self.foo2(param1, param2);
                    a1 = Self.foo3(param1, param2);
                    b = 1 >= 3;
                    val1 = True == False;
                    b = ! val1;
                }
        }
        '''
        expect = 'Program([ClassDecl(Id(B),[MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(%,Id(b),Id(c)),CallExpr(Self(),Id(foo),[]))),Call(Self(),Id(foo2),[Id(param1),Id(param2)]),AssignStmt(Id(a1),CallExpr(Self(),Id(foo3),[Id(param1),Id(param2)])),AssignStmt(Id(b),BinaryOp(>=,IntLit(1),IntLit(3))),AssignStmt(Id(val1),BinaryOp(==,BooleanLit(True),BooleanLit(False))),AssignStmt(Id(b),UnaryOp(!,Id(val1)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_340(self):
        input = """
        Class Shape {
            loop(){
                Foreach (i In 1 .. 100) {
                    age = 1;
                }
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(loop),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([AssignStmt(Id(age),IntLit(1))])])]))])])'
        self.assertTrue(TestAST.test(input,expect,340))

    def test_341(self):
        input = """
        Class Shape {
            loop(){
            Var age : Int = 1;
                Foreach (i In 1 .. 100 By 120) {
                    age = age + 1;
                    If(age > 10)
                    {Return False;}
                }
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(loop),Instance,[],Block([VarDecl(Id(age),IntType,IntLit(1)),For(Id(i),IntLit(1),IntLit(100),IntLit(120),Block([AssignStmt(Id(age),BinaryOp(+,Id(age),IntLit(1))),If(BinaryOp(>,Id(age),IntLit(10)),Block([Return(BooleanLit(False))]))])])]))])])'
        self.assertTrue(TestAST.test(input,expect,341))

    def test_342(self):
        input = '''
        Class Vinfast{
            Var running: Boolean = True;
            Val speed: Int;
            Constructor(){
                Self.speed = 10000000;
            }
            Constructor(speed: Int){
                Self.speed = speed;
            }
            run(){
                Self.running = True;
            }
            stop(){
                Self.running = False;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Vinfast),[AttributeDecl(Instance,VarDecl(Id(running),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(speed),IntType,None)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(speed)),IntLit(10000000))])),MethodDecl(Id(Constructor),Instance,[param(Id(speed),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(speed)),Id(speed))])),MethodDecl(Id(run),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(True))])),MethodDecl(Id(stop),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(False))]))])])'
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_343(self):
       line = """
               Class Shape{
                   foo(){
                       Foreach (x In 1+1 .. 100+100 By a.foo(1+2*3,"abc"+.1+2)){}
                   }
               }
           """
       expect = '''Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(+,IntLit(100),IntLit(100)),CallExpr(Id(a),Id(foo),[BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),BinaryOp(+.,StringLit(abc),BinaryOp(+,IntLit(1),IntLit(2)))]),Block([])])]))])])'''
       self.assertTrue(TestAST.test(line, expect, 343))

    def test_344(self):
       line = """
               Class Shape{
                   foo(){
                       Foreach (x In a::$b() .. a.c.c.c By a::$foo){
                           Foreach (x In a::$b() .. a.c.c.c By a::$foo){}
                       }
                   }
               }
               """
       expect = '''Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),CallExpr(Id(a),Id($b),[]),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(c)),Id(c)),Id(c)),FieldAccess(Id(a),Id($foo)),Block([For(Id(x),CallExpr(Id(a),Id($b),[]),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(c)),Id(c)),Id(c)),FieldAccess(Id(a),Id($foo)),Block([])])])])]))])])'''
       self.assertTrue(TestAST.test(line, expect, 344))

    def test_345(self):
       line = """
               Class Shape{
                   foo(){
                       If ( a == -1--1){
                           Foreach(x In 1 .. 100 By 2){
                               If ( a == -1--1){
                                   Foreach(x In 1 .. 100 By 2){

                                   }
                               }
                           }
                       }
                   }
               }
               """

       expect = '''Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([If(BinaryOp(==,Id(a),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([For(Id(x),IntLit(1),IntLit(100),IntLit(2),Block([If(BinaryOp(==,Id(a),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([For(Id(x),IntLit(1),IntLit(100),IntLit(2),Block([])])]))])])]))]))])])'''
       self.assertTrue(TestAST.test(line, expect, 345))

    def test_346(self):
        input = '''
        Class Eval{
            getSpeedfromKm(a, b, c: Int; e, f: String){
                Outscreen.get("The speed = " +.  "1000km/h");
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Eval),[MethodDecl(Id(getSpeedfromKm),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(e),StringType),param(Id(f),StringType)],Block([Call(Id(Outscreen),Id(get),[BinaryOp(+.,StringLit(The speed = ),StringLit(1000km/h))])]))])])'
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_347(self):
        input = '''
        Class Shape {
            foo(){
                c = ("a"==."a")==True;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(c),BinaryOp(==,BinaryOp(==.,StringLit(a),StringLit(a)),BooleanLit(True)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_348(self):
        input = '''
        Class Loop {
            function(){
                i=-1;
             }
        }
        '''
        expect = 'Program([ClassDecl(Id(Loop),[MethodDecl(Id(function),Instance,[],Block([AssignStmt(Id(i),UnaryOp(-,IntLit(1)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_349(self):
        input = '''
        Class Sharp{
            foo(){
                _Name = New X().Y().Z();
                Var array : Array[Int, 0B1010];
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Sharp),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(_Name),CallExpr(CallExpr(NewExpr(Id(X),[]),Id(Y),[]),Id(Z),[])),VarDecl(Id(array),ArrayType(10,IntType))]))])])'
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_350(self):
        input = '''
        Class List:Iterable{
            foo(){
                Var a: Array[Int, 01];
                Var a: Array[Int, 0x1];
                Var a: Array[Int, 0X1];
                Var a: Array[Int, 0b1];
                Var a: Array[Int, 0B1];
                Var a: Array[Int, 1];
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(List),Id(Iterable),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),ArrayType(1,IntType)),VarDecl(Id(a),ArrayType(1,IntType)),VarDecl(Id(a),ArrayType(1,IntType)),VarDecl(Id(a),ArrayType(1,IntType)),VarDecl(Id(a),ArrayType(1,IntType)),VarDecl(Id(a),ArrayType(1,IntType))]))])])'
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_351(self):
        input = '''
        Class List:Iterable{
            foo(){
                Var a: Array[Int, 1] = Array(2_34.456e+7990);
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(List),Id(Iterable),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),ArrayType(1,IntType),[FloatLit(inf)])]))])])'
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_352(self):
        input = """
        Class Dog : Animal {
            Val name, $color, $nickname : String = "Mimi", "Brown", "Davis";
            Var $age, leg : Int = 5, 4;
            Val height : Float = 12.5;
            Var isGerman : Boolean = True;
            Var friend, $parent : Dog;
            Var boyFriend, GirlFirend : Human = New Human(), New Human();
        }
        """
        expect = 'Program([ClassDecl(Id(Dog),Id(Animal),[AttributeDecl(Instance,ConstDecl(Id(name),StringType,StringLit(Mimi))),AttributeDecl(Static,ConstDecl(Id($color),StringType,StringLit(Brown))),AttributeDecl(Static,ConstDecl(Id($nickname),StringType,StringLit(Davis))),AttributeDecl(Static,VarDecl(Id($age),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(leg),IntType,IntLit(4))),AttributeDecl(Instance,ConstDecl(Id(height),FloatType,FloatLit(12.5))),AttributeDecl(Instance,VarDecl(Id(isGerman),BoolType,BooleanLit(True))),AttributeDecl(Instance,VarDecl(Id(friend),ClassType(Id(Dog)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($parent),ClassType(Id(Dog)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(boyFriend),ClassType(Id(Human)),NewExpr(Id(Human),[]))),AttributeDecl(Instance,VarDecl(Id(GirlFirend),ClassType(Id(Human)),NewExpr(Id(Human),[])))])])'
        self.assertTrue(TestAST.test(input,expect,352))

    def test_353(self):
        input = """
        Class Square {
            Val dots : Array[Float, 4];
            Var $dots : Array[Float, 4] = Array(1.2, 3.4, 5.6, 7.8);
        }
        """
        expect = 'Program([ClassDecl(Id(Square),[AttributeDecl(Instance,ConstDecl(Id(dots),ArrayType(4,FloatType),None)),AttributeDecl(Static,VarDecl(Id($dots),ArrayType(4,FloatType),[FloatLit(1.2),FloatLit(3.4),FloatLit(5.6),FloatLit(7.8)]))])])'
        self.assertTrue(TestAST.test(input,expect,353))

    def test_354(self):
        input = """
        Class Square {
            Var $dots : Array[Array[Float, 2], 2] = Array(Array(1.2, 3.4), Array(5.6, 7.8));
        }
        """
        expect = 'Program([ClassDecl(Id(Square),[AttributeDecl(Static,VarDecl(Id($dots),ArrayType(2,ArrayType(2,FloatType)),[[FloatLit(1.2),FloatLit(3.4)],[FloatLit(5.6),FloatLit(7.8)]]))])])'
        self.assertTrue(TestAST.test(input,expect,354))

    def test_355(self):
        input = """
        Class Dog {
            Val a : Int = 1;
            Val b : Float = 1.4;
            Val c : String = "abc";
            Val d : Boolean = True;
            Val e : Array[Int, 5] = Array(1, 5, 7, 12, 8);
            Val f : Animal = New Animal();
            Val g : Array[Array[Int, 5], 2] = Array(Array(1,2,3,4,5), Array(1,2,3,4,5));
        }
        """
        expect = 'Program([ClassDecl(Id(Dog),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,FloatLit(1.4))),AttributeDecl(Instance,ConstDecl(Id(c),StringType,StringLit(abc))),AttributeDecl(Instance,ConstDecl(Id(d),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(e),ArrayType(5,IntType),[IntLit(1),IntLit(5),IntLit(7),IntLit(12),IntLit(8)])),AttributeDecl(Instance,ConstDecl(Id(f),ClassType(Id(Animal)),NewExpr(Id(Animal),[]))),AttributeDecl(Instance,ConstDecl(Id(g),ArrayType(2,ArrayType(5,IntType)),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]]))])])'
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_356(self):
        input = """
        Class IntLit {
            Val a : Int = 1_234_567;
            Val b : Int = 1_2_3_4_5_6_7;
            Val c : Int = 0b110;
            Val d : Int = 0123456;
            Val e : Int = 0x123456789ABCDEF;
        }
        """
        expect = 'Program([ClassDecl(Id(IntLit),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1234567))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(1234567))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(6))),AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(42798))),AttributeDecl(Instance,ConstDecl(Id(e),IntType,IntLit(81985529216486895)))])])'
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_357(self):
        input = """
        Class ABC {
            Var w, h : Int;

            Constructor(w: Int; h: Int) {
                Self.w = w;
                Self.h = h;
                Return;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(ABC),[AttributeDecl(Instance,VarDecl(Id(w),IntType)),AttributeDecl(Instance,VarDecl(Id(h),IntType)),MethodDecl(Id(Constructor),Instance,[param(Id(w),IntType),param(Id(h),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(w)),Id(w)),AssignStmt(FieldAccess(Self(),Id(h)),Id(h)),Return()]))])])'
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_358(self):
        input = """
        Class Program {
            main(){
                Return New X().Y();
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(CallExpr(NewExpr(Id(X),[]),Id(Y),[]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_359(self):
        input = """
        Class Program {
            main(){
                Return New A(New B(New C()), 1+2, C::$x);
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(NewExpr(Id(A),[NewExpr(Id(B),[NewExpr(Id(C),[])]),BinaryOp(+,IntLit(1),IntLit(2)),FieldAccess(Id(C),Id($x))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_360(self):
        input = """
        Class ArrayLit {
            Var a: Array[Int, 5] = Array(1,2,3,4,5);
            Var a1: Array[Int, 5];
            Var b: Array[Array[Int, 5], 2] = Array(Array(1,2,3,4,5), Array(6,7,8,9,10));
        }
        """
        expect = 'Program([ClassDecl(Id(ArrayLit),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)])),AttributeDecl(Instance,VarDecl(Id(a1),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(2,ArrayType(5,IntType)),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)],[IntLit(6),IntLit(7),IntLit(8),IntLit(9),IntLit(10)]]))])])'
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_361(self):
        input = """
        Class ArrayLit {
            Var a: Array[Int, 3] = Array(1 + 2, 345, 6 * 8);
        }
        """
        expect = 'Program([ClassDecl(Id(ArrayLit),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(3,IntType),[BinaryOp(+,IntLit(1),IntLit(2)),IntLit(345),BinaryOp(*,IntLit(6),IntLit(8))]))])])'
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_362(self):
        input = """
        Class Program {
            main(){
                a = Dog.bark() + Cat::$Meow() + Dog.name + Cat::$age + Animal.Dog[1] + Animal.type().name;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,CallExpr(Id(Dog),Id(bark),[]),CallExpr(Id(Cat),Id($Meow),[])),FieldAccess(Id(Dog),Id(name))),FieldAccess(Id(Cat),Id($age))),ArrayCell(FieldAccess(Id(Animal),Id(Dog)),[IntLit(1)])),FieldAccess(CallExpr(Id(Animal),Id(type),[]),Id(name))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_363(self):
        input = """Class Dress{
           Collection(){
               item::$2021.amount=500;
           }
       }"""
        expect = 'Program([ClassDecl(Id(Dress),[MethodDecl(Id(Collection),Instance,[],Block([AssignStmt(FieldAccess(FieldAccess(Id(item),Id($2021)),Id(amount)),IntLit(500))]))])])'
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_364(self):
        input = '''Class Pet {
            Var $1cat:Pet;
            main(){
                Val dog:Pet = New Pet("Tin",1,Null);
            }}'''
        expect = 'Program([ClassDecl(Id(Pet),[AttributeDecl(Static,VarDecl(Id($1cat),ClassType(Id(Pet)),NullLiteral())),MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(dog),ClassType(Id(Pet)),NewExpr(Id(Pet),[StringLit(Tin),IntLit(1),NullLiteral()]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_365(self):
        input = '''Class numberTest {
            Val $1Int: Int = Self.numCall(0xBED26);
            Var flNumb: Float = Self.numCall(.e-15);
            Var flNumb2: Float = .2e-5;
           }'''
        expect = 'Program([ClassDecl(Id(numberTest),[AttributeDecl(Static,ConstDecl(Id($1Int),IntType,CallExpr(Self(),Id(numCall),[IntLit(781606)]))),AttributeDecl(Instance,VarDecl(Id(flNumb),FloatType,CallExpr(Self(),Id(numCall),[FloatLit(0.0)]))),AttributeDecl(Instance,VarDecl(Id(flNumb2),FloatType,FloatLit(2e-06)))])])'
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_366(self):
        input = """Class Shape {
        foo(){
            a=New A().B();
        }
        calculateDiv(a, b: Int) {
            If(a>b) {Return a/b;} Else {Return a+b;}
        }}"""
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),CallExpr(NewExpr(Id(A),[]),Id(B),[]))])),MethodDecl(Id(calculateDiv),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Return(BinaryOp(/,Id(a),Id(b)))]),Block([Return(BinaryOp(+,Id(a),Id(b)))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_367(self):
        input = """Class Sample {
        foo(){
            a = !!!--True;
            b = 5+-3--3-5--2;
            e=f[1][f[2]][1-2][0x0];
        }}"""
        expect = 'Program([ClassDecl(Id(Sample),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,BooleanLit(True))))))),AssignStmt(Id(b),BinaryOp(-,BinaryOp(-,BinaryOp(-,BinaryOp(+,IntLit(5),UnaryOp(-,IntLit(3))),UnaryOp(-,IntLit(3))),IntLit(5)),UnaryOp(-,IntLit(2)))),AssignStmt(Id(e),ArrayCell(Id(f),[IntLit(1),ArrayCell(Id(f),[IntLit(2)]),BinaryOp(-,IntLit(1),IntLit(2)),IntLit(0)]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_368(self):
        input = """Class Person: People {
        Var age: Int;
        $checkAge () {
            If (Person.age > People::$maxAge) {Out.printLn("Impossible Age");}
        }}"""
        expect = 'Program([ClassDecl(Id(Person),Id(People),[AttributeDecl(Instance,VarDecl(Id(age),IntType)),MethodDecl(Id($checkAge),Static,[],Block([If(BinaryOp(>,FieldAccess(Id(Person),Id(age)),FieldAccess(Id(People),Id($maxAge))),Block([Call(Id(Out),Id(printLn),[StringLit(Impossible Age)])]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_369(self):
        input = """Class Something {
            foo() {
                Val a: String = "Hello \\n Goodbye";
                b = 0b1101 * 0x123AFB - 0123665 * (00 - 0x0);
            }}"""
        expect = 'Program([ClassDecl(Id(Something),[MethodDecl(Id(foo),Instance,[],Block([ConstDecl(Id(a),StringType,StringLit(Hello \\n Goodbye)),AssignStmt(Id(b),BinaryOp(-,BinaryOp(*,IntLit(13),IntLit(1194747)),BinaryOp(*,IntLit(42933),BinaryOp(-,IntLit(0),IntLit(0)))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_370(self):
        input = '''Class _{Var _7z,j___,$243O,yEV__,$_0:Array [Array [Array [Array [Array [Boolean ,056],0x29],0X8],0b1_10],0X1D];}'''
        expect = 'Program([ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(_7z),ArrayType(29,ArrayType(6,ArrayType(8,ArrayType(41,ArrayType(46,BoolType))))))),AttributeDecl(Instance,VarDecl(Id(j___),ArrayType(29,ArrayType(6,ArrayType(8,ArrayType(41,ArrayType(46,BoolType))))))),AttributeDecl(Static,VarDecl(Id($243O),ArrayType(29,ArrayType(6,ArrayType(8,ArrayType(41,ArrayType(46,BoolType))))))),AttributeDecl(Instance,VarDecl(Id(yEV__),ArrayType(29,ArrayType(6,ArrayType(8,ArrayType(41,ArrayType(46,BoolType))))))),AttributeDecl(Static,VarDecl(Id($_0),ArrayType(29,ArrayType(6,ArrayType(8,ArrayType(41,ArrayType(46,BoolType)))))))])])'
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_371(self):
        input = """Class Room {
        Val People: Array[String, 11];
        $askEachPerson () {
            Foreach (i In 10 .. Self.countNumb(ctx.Numb) By ------1*2+3----4) {
                Self.ask(People[i]);}
            }}"""
        expect = "Program([ClassDecl(Id(Room),[AttributeDecl(Instance,ConstDecl(Id(People),ArrayType(11,StringType),None)),MethodDecl(Id($askEachPerson),Static,[],Block([For(Id(i),IntLit(10),CallExpr(Self(),Id(countNumb),[FieldAccess(Id(ctx),Id(Numb))]),BinaryOp(-,BinaryOp(+,BinaryOp(*,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(1))))))),IntLit(2)),IntLit(3)),UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(4))))),Block([Call(Self(),Id(ask),[ArrayCell(Id(People),[Id(i)])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_372(self):
        input = """Class Person{
        __init__(name:String; age: Int){
            Self.name = name;
            Self.age = age;
        }
        myfunc(){func.printLn("Hello my name is " +. Self.name);}}"""
        expect = 'Program([ClassDecl(Id(Person),[MethodDecl(Id(__init__),Instance,[param(Id(name),StringType),param(Id(age),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(age)),Id(age))])),MethodDecl(Id(myfunc),Instance,[],Block([Call(Id(func),Id(printLn),[BinaryOp(+.,StringLit(Hello my name is ),FieldAccess(Self(),Id(name)))])]))])])'
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_373(self):
        input = """Class Dog{
        Val tricks: Array[String, 10] = Array();   
        add_trick(trick:String){
            Self.tricks.append(trick);
        }

        main(){
            Ben = New Dog("Ben");
            Ben.add_trick("Play dead");} }"""
        expect = 'Program([ClassDecl(Id(Dog),[AttributeDecl(Instance,ConstDecl(Id(tricks),ArrayType(10,StringType),[])),MethodDecl(Id(add_trick),Instance,[param(Id(trick),StringType)],Block([Call(FieldAccess(Self(),Id(tricks)),Id(append),[Id(trick)])])),MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(Ben),NewExpr(Id(Dog),[StringLit(Ben)])),Call(Id(Ben),Id(add_trick),[StringLit(Play dead)])]))])])'
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_374(self):
        input = """Class Addition{
         Calculate(arrNumb:Array[Int, 5]){
            Foreach(i In 0 .. Self.len(arrNum)){
                If ((arrNumb[i] >= 0) && (arrNumb[i] <= 101)){Self.answer = Self.answer + arrNumb[i];}
                Else {Continue;}
            }}}"""
        expect = "Program([ClassDecl(Id(Addition),[MethodDecl(Id(Calculate),Instance,[param(Id(arrNumb),ArrayType(5,IntType))],Block([For(Id(i),IntLit(0),CallExpr(Self(),Id(len),[Id(arrNum)]),IntLit(1),Block([If(BinaryOp(&&,BinaryOp(>=,ArrayCell(Id(arrNumb),[Id(i)]),IntLit(0)),BinaryOp(<=,ArrayCell(Id(arrNumb),[Id(i)]),IntLit(101))),Block([AssignStmt(FieldAccess(Self(),Id(answer)),BinaryOp(+,FieldAccess(Self(),Id(answer)),ArrayCell(Id(arrNumb),[Id(i)])))]),Block([Continue]))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_375(self):
        input = """Class myDog:Pet{
        main(){
            miles = New Dog("Miles", 4, "Bulldog");
            buddy.updateAge();
            buddy.speak(DogSound[1--1*2*-2]);
        }}"""
        expect = 'Program([ClassDecl(Id(myDog),Id(Pet),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(miles),NewExpr(Id(Dog),[StringLit(Miles),IntLit(4),StringLit(Bulldog)])),Call(Id(buddy),Id(updateAge),[]),Call(Id(buddy),Id(speak),[ArrayCell(Id(DogSound),[BinaryOp(-,IntLit(1),BinaryOp(*,BinaryOp(*,UnaryOp(-,IntLit(1)),IntLit(2)),UnaryOp(-,IntLit(2))))])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_376(self):
        input = """Class Program {
            ##Thiss is a one-line comment in this program##
            Val coding, $mcoding:MyCode=New Code(), New Code(Self);
            decode(){coding::$func.funcList.decode(arrCode[1--12.2e-2][0x18A][0B1101]);}
        }"""
        expect = 'Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(coding),ClassType(Id(MyCode)),NewExpr(Id(Code),[]))),AttributeDecl(Static,ConstDecl(Id($mcoding),ClassType(Id(MyCode)),NewExpr(Id(Code),[Self()]))),MethodDecl(Id(decode),Instance,[],Block([Call(FieldAccess(FieldAccess(Id(coding),Id($func)),Id(funcList)),Id(decode),[ArrayCell(Id(arrCode),[BinaryOp(-,IntLit(1),UnaryOp(-,FloatLit(0.122))),IntLit(394),IntLit(13)])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_377(self):
        input = """Class Program {
            a() {
                Foreach (a In 1 .. 100 By 2) {
                    Self.print(a + 1);
                    b = a * 2;
                    Self.print(b.a.c);
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([Call(Self(),Id(print),[BinaryOp(+,Id(a),IntLit(1))]),AssignStmt(Id(b),BinaryOp(*,Id(a),IntLit(2))),Call(Self(),Id(print),[FieldAccess(FieldAccess(Id(b),Id(a)),Id(c))])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_378(self):
        input = """Class myDog:Pet{
        ##This is multi-line
        comment in \\n program##
        main(){
            miles = New Dog("Miles", 4, "Bulldog"); ##Create new dog##
            buddy.updateAge(); ##Increase dog's age##
            buddy.speak(DogSound[1--1*2*-2]);
        }}"""
        expect = 'Program([ClassDecl(Id(myDog),Id(Pet),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(miles),NewExpr(Id(Dog),[StringLit(Miles),IntLit(4),StringLit(Bulldog)])),Call(Id(buddy),Id(updateAge),[]),Call(Id(buddy),Id(speak),[ArrayCell(Id(DogSound),[BinaryOp(-,IntLit(1),BinaryOp(*,BinaryOp(*,UnaryOp(-,IntLit(1)),IntLit(2)),UnaryOp(-,IntLit(2))))])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_379(self):
        input = """Class NodeClass {
            Var data : Int;
            Val next : NodeClass;
            Constructor(d : Int){data = d;next = Null;}
         reverse(nodePoint : NodeClass) {
             Var prev : NodeClass = Null;
             Val current : NodeClass = nodePoint;
             Val next : NodeClass = Null;
             Foreach (i In 1 .. forever By 1) {
                 If (current == Null) {Break;} 
                 Else {
                     next = current.next;
                     current.next = prev;
                     prev = current;
                     current = next;
                 }}
             nodePoint = prev; Return nodePoint;
         }
         printList(nodePoint : NodeClass) {
             Foreach (a In 1 .. infinity By 1) {
                 If (nodePoint != Null) {System.out.print(nodePoint.data +. " ");nodePoint = nodePoint.next;} 
                 Else {Break;}
        }}}
         Class Program {
             mainFunc() {
                 Val sll : LinkedList = New LinkedList();
                 sll.head = New NodeClass(26);
                 sll.head.next = New NodeClass(11);
                 sll.head.next.next = New NodeClass(3);
                 head = list.reverse(head);
                 System.out.println("Reversed linked list "); sll.printList(head);
             }
        }"""
        expect = 'Program([ClassDecl(Id(NodeClass),[AttributeDecl(Instance,VarDecl(Id(data),IntType)),AttributeDecl(Instance,ConstDecl(Id(next),ClassType(Id(NodeClass)),None)),MethodDecl(Id(Constructor),Instance,[param(Id(d),IntType)],Block([AssignStmt(Id(data),Id(d)),AssignStmt(Id(next),NullLiteral())])),MethodDecl(Id(reverse),Instance,[param(Id(nodePoint),ClassType(Id(NodeClass)))],Block([VarDecl(Id(prev),ClassType(Id(NodeClass)),NullLiteral()),ConstDecl(Id(current),ClassType(Id(NodeClass)),Id(nodePoint)),ConstDecl(Id(next),ClassType(Id(NodeClass)),NullLiteral()),For(Id(i),IntLit(1),Id(forever),IntLit(1),Block([If(BinaryOp(==,Id(current),NullLiteral()),Block([Break]),Block([AssignStmt(Id(next),FieldAccess(Id(current),Id(next))),AssignStmt(FieldAccess(Id(current),Id(next)),Id(prev)),AssignStmt(Id(prev),Id(current)),AssignStmt(Id(current),Id(next))]))])]),AssignStmt(Id(nodePoint),Id(prev)),Return(Id(nodePoint))])),MethodDecl(Id(printList),Instance,[param(Id(nodePoint),ClassType(Id(NodeClass)))],Block([For(Id(a),IntLit(1),Id(infinity),IntLit(1),Block([If(BinaryOp(!=,Id(nodePoint),NullLiteral()),Block([Call(FieldAccess(Id(System),Id(out)),Id(print),[BinaryOp(+.,FieldAccess(Id(nodePoint),Id(data)),StringLit( ))]),AssignStmt(Id(nodePoint),FieldAccess(Id(nodePoint),Id(next)))]),Block([Break]))])])]))]),ClassDecl(Id(Program),[MethodDecl(Id(mainFunc),Instance,[],Block([ConstDecl(Id(sll),ClassType(Id(LinkedList)),NewExpr(Id(LinkedList),[])),AssignStmt(FieldAccess(Id(sll),Id(head)),NewExpr(Id(NodeClass),[IntLit(26)])),AssignStmt(FieldAccess(FieldAccess(Id(sll),Id(head)),Id(next)),NewExpr(Id(NodeClass),[IntLit(11)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(sll),Id(head)),Id(next)),Id(next)),NewExpr(Id(NodeClass),[IntLit(3)])),AssignStmt(Id(head),CallExpr(Id(list),Id(reverse),[Id(head)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Reversed linked list )]),Call(Id(sll),Id(printList),[Id(head)])]))])])'
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_380(self):
        input = """Class Test:Program {
        main(){
            a = !!!!!!True;
            b = ------2----6--5;
            c=d.d.d.d.d.d.d.d;
            e=f[1][1][1][1];
            g=!!!!-----20*x+y[1][x[1]];
        }}"""
        expect = "Program([ClassDecl(Id(Test),Id(Program),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,BooleanLit(True)))))))),AssignStmt(Id(b),BinaryOp(-,BinaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(2))))))),UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(6))))),UnaryOp(-,IntLit(5)))),AssignStmt(Id(c),FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(d),Id(d)),Id(d)),Id(d)),Id(d)),Id(d)),Id(d)),Id(d))),AssignStmt(Id(e),ArrayCell(Id(f),[IntLit(1),IntLit(1),IntLit(1),IntLit(1)])),AssignStmt(Id(g),BinaryOp(+,BinaryOp(*,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(20)))))))))),Id(x)),ArrayCell(Id(y),[IntLit(1),ArrayCell(Id(x),[IntLit(1)])])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_381(self):
        input = """Class NodeClass {
               Var data : Int;
               Val next : NodeClass;
               Constructor(d : Int){data = d;next = Null;}
            ## Function to reverse the linked list ##
            reverse(nodePoint : NodeClass) {
                Var prev : NodeClass = Null;
                Val current : NodeClass = nodePoint;
                Val next : NodeClass = Null;
                Foreach (i In 1 .. forever By 1) {
                    If (current == Null) {Break;} 
                    Else {
                        next = current.next;
                        current.next = prev;
                        prev = current;
                        current = next;
                    }}
                nodePoint = prev; Return nodePoint;
            }
        }
        ##Class Program {
             mainFunc() {
                 Val sll : LinkedList = New LinkedList();
                 sll.head = New NodeClass(26);
                 sll.head.next = New NodeClass(11);
                 sll.head.next.next = New NodeClass(3);
                 head = list.reverse(head);
                 System.out.println("Reversed linked list "); sll.printList(head);
             }
        }##"""
        expect = "Program([ClassDecl(Id(NodeClass),[AttributeDecl(Instance,VarDecl(Id(data),IntType)),AttributeDecl(Instance,ConstDecl(Id(next),ClassType(Id(NodeClass)),None)),MethodDecl(Id(Constructor),Instance,[param(Id(d),IntType)],Block([AssignStmt(Id(data),Id(d)),AssignStmt(Id(next),NullLiteral())])),MethodDecl(Id(reverse),Instance,[param(Id(nodePoint),ClassType(Id(NodeClass)))],Block([VarDecl(Id(prev),ClassType(Id(NodeClass)),NullLiteral()),ConstDecl(Id(current),ClassType(Id(NodeClass)),Id(nodePoint)),ConstDecl(Id(next),ClassType(Id(NodeClass)),NullLiteral()),For(Id(i),IntLit(1),Id(forever),IntLit(1),Block([If(BinaryOp(==,Id(current),NullLiteral()),Block([Break]),Block([AssignStmt(Id(next),FieldAccess(Id(current),Id(next))),AssignStmt(FieldAccess(Id(current),Id(next)),Id(prev)),AssignStmt(Id(prev),Id(current)),AssignStmt(Id(current),Id(next))]))])]),AssignStmt(Id(nodePoint),Id(prev)),Return(Id(nodePoint))]))])])"
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_382(self):
        input = """
        Class Student{
                learn(){
                    Self.print("Learning");   
                }
                goToSchool(){
                    Self.byeMom();
                    Self.byeDad("by dad");    
                }
                Constructor(){
                    Classroom::$numOfStudents = Classroom::$numOfStudents + 1;
                }
                Destructor(){
                    Classroom::$numOfStudents = Classroom::$numOfStudents - 1;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Student),[MethodDecl(Id(learn),Instance,[],Block([Call(Self(),Id(print),[StringLit(Learning)])])),MethodDecl(Id(goToSchool),Instance,[],Block([Call(Self(),Id(byeMom),[]),Call(Self(),Id(byeDad),[StringLit(by dad)])])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Classroom),Id($numOfStudents)),BinaryOp(+,FieldAccess(Id(Classroom),Id($numOfStudents)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Classroom),Id($numOfStudents)),BinaryOp(-,FieldAccess(Id(Classroom),Id($numOfStudents)),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_383(self):
        input = """Class calDistance {
        Val R: Float = 6373.0;
        main () {
            lat1 = math.radians(52.2296756);
            lon1 = math.radians(21.0122287);
            lat2 = math.radians(52.406374);
            lon2 = math.radians(16.9251681);
            dlon = lon2 - lon1; dlat = lat2 - lat1;
            a = math.sin(dlat/2)*2 + math.cos(lat1)* math.cos(lat2) * math.sin(dlon/2)*2;
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a));
            distance = R * c;
            System.print(distance);
        }}"""
        expect = "Program([ClassDecl(Id(calDistance),[AttributeDecl(Instance,ConstDecl(Id(R),FloatType,FloatLit(6373.0))),MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(lat1),CallExpr(Id(math),Id(radians),[FloatLit(52.2296756)])),AssignStmt(Id(lon1),CallExpr(Id(math),Id(radians),[FloatLit(21.0122287)])),AssignStmt(Id(lat2),CallExpr(Id(math),Id(radians),[FloatLit(52.406374)])),AssignStmt(Id(lon2),CallExpr(Id(math),Id(radians),[FloatLit(16.9251681)])),AssignStmt(Id(dlon),BinaryOp(-,Id(lon2),Id(lon1))),AssignStmt(Id(dlat),BinaryOp(-,Id(lat2),Id(lat1))),AssignStmt(Id(a),BinaryOp(+,BinaryOp(*,CallExpr(Id(math),Id(sin),[BinaryOp(/,Id(dlat),IntLit(2))]),IntLit(2)),BinaryOp(*,BinaryOp(*,BinaryOp(*,CallExpr(Id(math),Id(cos),[Id(lat1)]),CallExpr(Id(math),Id(cos),[Id(lat2)])),CallExpr(Id(math),Id(sin),[BinaryOp(/,Id(dlon),IntLit(2))])),IntLit(2)))),AssignStmt(Id(c),BinaryOp(*,IntLit(2),CallExpr(Id(math),Id(atan2),[CallExpr(Id(math),Id(sqrt),[Id(a)]),CallExpr(Id(math),Id(sqrt),[BinaryOp(-,IntLit(1),Id(a))])]))),AssignStmt(Id(distance),BinaryOp(*,Id(R),Id(c))),Call(Id(System),Id(print),[Id(distance)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_384(self):
        input = """Class Program {
            a() {
                Val a : Int;
                a = 1 + 1 + a - 3 * b / 7 + d;
                Self.print(a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),IntType,None),AssignStmt(Id(a),BinaryOp(+,BinaryOp(-,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(1)),Id(a)),BinaryOp(/,BinaryOp(*,IntLit(3),Id(b)),IntLit(7))),Id(d))),Call(Self(),Id(print),[Id(a)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_385(self):
        input = """Class Program {
            a() {
                Val a : ClassAC = Null;
                a = New X(1 + 1, a - 3 * b, 10 / 7 + d);
                Self.print(a.a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(ClassAC)),NullLiteral()),AssignStmt(Id(a),NewExpr(Id(X),[BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(-,Id(a),BinaryOp(*,IntLit(3),Id(b))),BinaryOp(+,BinaryOp(/,IntLit(10),IntLit(7)),Id(d))])),Call(Self(),Id(print),[FieldAccess(Id(a),Id(a))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_386(self):
        input = """Class Program {
            a() {
                Val a : ClassAC = Null;
                a = New X(1 + 1, a - 3 * b, 10 / 7 + d);
                a.a = 10;
                a.b = -100.00 + a.foo();
                Self.print(a.a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(ClassAC)),NullLiteral()),AssignStmt(Id(a),NewExpr(Id(X),[BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(-,Id(a),BinaryOp(*,IntLit(3),Id(b))),BinaryOp(+,BinaryOp(/,IntLit(10),IntLit(7)),Id(d))])),AssignStmt(FieldAccess(Id(a),Id(a)),IntLit(10)),AssignStmt(FieldAccess(Id(a),Id(b)),BinaryOp(+,UnaryOp(-,FloatLit(100.0)),CallExpr(Id(a),Id(foo),[]))),Call(Self(),Id(print),[FieldAccess(Id(a),Id(a))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_387(self):
        input = """Class Program {
            a() {
                Val a : ClassAC = Null;
                a = New X(1 + 1, a - 3 * b, 10 / 7 + d);
                a.a = 10;
                a.b = -100.00 + a.foo();
                a.a.b[1] = Array(1, 2, 3);
                Self.print(a.a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(ClassAC)),NullLiteral()),AssignStmt(Id(a),NewExpr(Id(X),[BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(-,Id(a),BinaryOp(*,IntLit(3),Id(b))),BinaryOp(+,BinaryOp(/,IntLit(10),IntLit(7)),Id(d))])),AssignStmt(FieldAccess(Id(a),Id(a)),IntLit(10)),AssignStmt(FieldAccess(Id(a),Id(b)),BinaryOp(+,UnaryOp(-,FloatLit(100.0)),CallExpr(Id(a),Id(foo),[]))),AssignStmt(ArrayCell(FieldAccess(FieldAccess(Id(a),Id(a)),Id(b)),[IntLit(1)]),[IntLit(1),IntLit(2),IntLit(3)]),Call(Self(),Id(print),[FieldAccess(Id(a),Id(a))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_388(self):
        input = """Class Program {
            $a() {
                MotorBike::$eng = Array(1, 2+a, a * b);
                a[1][(i - j)][3] = c[i][k] + b[1][(j+1)][(k - 2)][3];

                Self.print(a.a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id($a),Static,[],Block([AssignStmt(FieldAccess(Id(MotorBike),Id($eng)),[IntLit(1),BinaryOp(+,IntLit(2),Id(a)),BinaryOp(*,Id(a),Id(b))]),AssignStmt(ArrayCell(Id(a),[IntLit(1),BinaryOp(-,Id(i),Id(j)),IntLit(3)]),BinaryOp(+,ArrayCell(Id(c),[Id(i),Id(k)]),ArrayCell(Id(b),[IntLit(1),BinaryOp(+,Id(j),IntLit(1)),BinaryOp(-,Id(k),IntLit(2)),IntLit(3)]))),Call(Self(),Id(print),[FieldAccess(Id(a),Id(a))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_389(self):
        input = """Class Program {
            $a() {
                a.f().a[1][23] = a.foo() +. AClass::$foo();
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id($a),Static,[],Block([AssignStmt(ArrayCell(FieldAccess(CallExpr(Id(a),Id(f),[]),Id(a)),[IntLit(1),IntLit(23)]),BinaryOp(+.,CallExpr(Id(a),Id(foo),[]),CallExpr(Id(AClass),Id($foo),[])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_390(self):
        input = """Class Program {
            a() {
                Foreach (a In 1 .. 100 By 2) {
                    Self.print(a + 1);
                    b = a * 2;
                    Self.print(b.a.c);
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([Call(Self(),Id(print),[BinaryOp(+,Id(a),IntLit(1))]),AssignStmt(Id(b),BinaryOp(*,Id(a),IntLit(2))),Call(Self(),Id(print),[FieldAccess(FieldAccess(Id(b),Id(a)),Id(c))])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_391(self):
        input = """Class Program {
            a() {
                Foreach (a In b + c .. b - c * 100) {
                    Self.print(a);
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(a),BinaryOp(+,Id(b),Id(c)),BinaryOp(-,Id(b),BinaryOp(*,Id(c),IntLit(100))),IntLit(1),Block([Call(Self(),Id(print),[Id(a)])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_392(self):
        input = """Class Program {
            a() {
                Foreach (a In New X(1, 2, 3) .. Self.foo().a.bar() By MotherBoard::$capacitor.foo()) {
                    Self.print(a);
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(a),NewExpr(Id(X),[IntLit(1),IntLit(2),IntLit(3)]),CallExpr(FieldAccess(CallExpr(Self(),Id(foo),[]),Id(a)),Id(bar),[]),CallExpr(FieldAccess(Id(MotherBoard),Id($capacitor)),Id(foo),[]),Block([Call(Self(),Id(print),[Id(a)])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_393(self):
        input = '''
        Class Program{
            main(a : Int){
                Foreach (i In 1 .. 100 By 2) {
                Out.printInt(i);
                }
                Foreach (x In 5 .. 2) {
                Out.printInt(arr[x]);
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])]),For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_394(self):
        input = '''
        Class Program {
            main()
            {
                Val list : LinkedList = New LinkedList();
                list.head = New Node(1);
                list.head.next = New Node(0x12F3);
                list.head.next.next = New Node(0B101);
                list.head.next.next.next = New Node(0312412);
                System.out.println("Given Linked list");
                list.printList(head);
                head = list.reverse(head);
                System.out.println("Newline");
                System.out.println("Reversed linked list ");
                list.printList(tail);
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(list),ClassType(Id(LinkedList)),NewExpr(Id(LinkedList),[])),AssignStmt(FieldAccess(Id(list),Id(head)),NewExpr(Id(Node),[IntLit(1)])),AssignStmt(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),NewExpr(Id(Node),[IntLit(4851)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),Id(next)),NewExpr(Id(Node),[IntLit(5)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),Id(next)),Id(next)),NewExpr(Id(Node),[IntLit(103690)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Given Linked list)]),Call(Id(list),Id(printList),[Id(head)]),AssignStmt(Id(head),CallExpr(Id(list),Id(reverse),[Id(head)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Newline)]),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Reversed linked list )]),Call(Id(list),Id(printList),[Id(tail)])]))])])'
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_395(self):
        input = '''
        Class Program {
            $foo() {
                Self.A = Array(1, 02312 + a, a * b);
                a[1.3412e-3][(i - j)][0x10] = c[i][k] + b[1][(j+1)][(k - 1412)][123];

                Self.System.Out(a.a);
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id($foo),Static,[],Block([AssignStmt(FieldAccess(Self(),Id(A)),[IntLit(1),BinaryOp(+,IntLit(1226),Id(a)),BinaryOp(*,Id(a),Id(b))]),AssignStmt(ArrayCell(Id(a),[FloatLit(0.0013412),BinaryOp(-,Id(i),Id(j)),IntLit(16)]),BinaryOp(+,ArrayCell(Id(c),[Id(i),Id(k)]),ArrayCell(Id(b),[IntLit(1),BinaryOp(+,Id(j),IntLit(1)),BinaryOp(-,Id(k),IntLit(1412)),IntLit(123)]))),Call(FieldAccess(Self(),Id(System)),Id(Out),[FieldAccess(Id(a),Id(a))])]))])])'
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_396(self):
        input = '''
        Class iPhone:Apple{
                Val $os: String = "iOS";
                Var IMEI: String; 
                Var $phone_number: Int;
                Var $phone: Array[Boolean, 100];
                insertSIM(sim: SIM){
                    Self.phone_number = SIM.number;
                }
                detachSIM(){
                    Self.phone_number = Null;
                }
        }
        '''
        expect = 'Program([ClassDecl(Id(iPhone),Id(Apple),[AttributeDecl(Static,ConstDecl(Id($os),StringType,StringLit(iOS))),AttributeDecl(Instance,VarDecl(Id(IMEI),StringType)),AttributeDecl(Static,VarDecl(Id($phone_number),IntType)),AttributeDecl(Static,VarDecl(Id($phone),ArrayType(100,BoolType))),MethodDecl(Id(insertSIM),Instance,[param(Id(sim),ClassType(Id(SIM)))],Block([AssignStmt(FieldAccess(Self(),Id(phone_number)),FieldAccess(Id(SIM),Id(number)))])),MethodDecl(Id(detachSIM),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(phone_number)),NullLiteral())]))])])'
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_397(self):
        input = '''
        Class Smart:Home{
            Val $Camera : Module;
            detect(Camera : Module){
                If(Self.detect() == True){
                    Return True;
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Smart),Id(Home),[AttributeDecl(Static,ConstDecl(Id($Camera),ClassType(Id(Module)),None)),MethodDecl(Id(detect),Instance,[param(Id(Camera),ClassType(Id(Module)))],Block([If(BinaryOp(==,CallExpr(Self(),Id(detect),[]),BooleanLit(True)),Block([Return(BooleanLit(True))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_398(self):
        input = """Class Shape {
        foo(){
            a=New A().B();
        }
        calculateDiv(a, b: Int) {
            If(a>b) {Return a/b;} Else {Return a+b;}
        }}"""
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),CallExpr(NewExpr(Id(A),[]),Id(B),[]))])),MethodDecl(Id(calculateDiv),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Return(BinaryOp(/,Id(a),Id(b)))]),Block([Return(BinaryOp(+,Id(a),Id(b)))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_399(self):
        input = """Class Sample {
        foo(){
            a = !!!--True;
            b = 5+-3--3-5--2;
            e=f[1][f[2]][1-2][0x0];
        }}"""
        expect = 'Program([ClassDecl(Id(Sample),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,BooleanLit(True))))))),AssignStmt(Id(b),BinaryOp(-,BinaryOp(-,BinaryOp(-,BinaryOp(+,IntLit(5),UnaryOp(-,IntLit(3))),UnaryOp(-,IntLit(3))),IntLit(5)),UnaryOp(-,IntLit(2)))),AssignStmt(Id(e),ArrayCell(Id(f),[IntLit(1),ArrayCell(Id(f),[IntLit(2)]),BinaryOp(-,IntLit(1),IntLit(2)),IntLit(0)]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_400(self):
        input = """Class Person: People {
        Var age: Int;
        $checkAge () {
            If (Person.age > People::$maxAge) {Out.printLn("Impossible Age");}
        }}"""
        expect = 'Program([ClassDecl(Id(Person),Id(People),[AttributeDecl(Instance,VarDecl(Id(age),IntType)),MethodDecl(Id($checkAge),Static,[],Block([If(BinaryOp(>,FieldAccess(Id(Person),Id(age)),FieldAccess(Id(People),Id($maxAge))),Block([Call(Id(Out),Id(printLn),[StringLit(Impossible Age)])]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 400))