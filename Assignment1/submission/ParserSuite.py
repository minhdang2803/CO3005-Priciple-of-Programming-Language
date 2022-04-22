import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_201(self):
        input = """Class main{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_202(self):
        """More complex program"""
        input = """Class Rectangle: Shape {
            getArea() {
            Return self.length * self.width;
        }
    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_203(self):
        input = """Var a: Array[Array[Int,5],5];"""
        expect = "Error on line 1 col 0: Var"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_204(self):
        input = """1 + 1 + a.foo()"""
        expect = "Error on line 1 col 0: 1"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_205(self):
        input = """
    Class Shape {
        $getNumOfShape( {
            Return self.length * self.width;
        }
    }
    """
        expect = "Error on line 3 col 24: {"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_206(self):
        input = """
        Class Shape {
            foo(){
                a[b[1]][c][foo()] = 1;
            }
            Var e,f : Int = 1 + 1, 1 - 2;
        }
    """
        expect = "Error on line 4 col 30: ("
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_207(self):
        """More complex program"""
        input = """
    Class Shape2 {
        $getNumOfShape() {
            If (a == (1+1) ){
                Var b,c:Boolean = True, False;
            }
            Foreach (i In 1 .. 100 By 2) {
                 Var a:Boolean = True;
            }
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_208(self):
        """More complex program"""
        input = """
        Class Shape {
            sum(a,b:Int; c,d:Float){}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_209(self):
        """More complex program"""
        input = """
        Class Shape {
            Var a :Array[Array[Int,2],2] = Array(Array(1,1),Array(1,1));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_210(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
                Var a: Boolean = !!True;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_211(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            foo2(1+1,"a"+."b","a"==."b");
        }
    }
    """
        expect = "Error on line 4 col 16: ("
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_212(self):
        """More complex program"""
        input = """
    Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
        $getNumOfShape() {
            Return $numOfShape;
        }
    }
    Class Rectangle: Shape {
        getArea() {
            Return self.length * self.width;
        }
    }
    Class Program {
        main() {
            Out.printInt(Shape::$numOfShape);
        }
    }
    """
        expect = "Error on line 7 col 19: $numOfShape"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_213(self):
        """More complex program"""
        input = """
    Class Shape {
        Constructor(width, height : Int; name:String){
            Self.Area=Self.width*Self.height;
            Self.name="shape"+.name;
        }
        Destructor(){}
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_214(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a=1------1+1--1;
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_215(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a=(New X()).Y();
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_216(self):
        input = """
            Class Student: Person{
            Var a, b: Int = 2%s, 3;
            Var e: Float = 3/2;
            Val $c:Float = 1.e-3;
            $main(){
                Var f: String = "string";
                a = b;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_217(self):
        input = """
        Class A
        {
            main()
            {

                If (flag == 1) {b = c;}
                Elseif (flag == 0) {
                    as = mn;
                    as.boo("hehe");
                }
                Else {
                    Var c: Int = 123 * 12/23;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_218(self):
        input = """
        Class A
        {
             If (flag == 1) {b = c;}
             Elseif (flag == 0) {
                as = mn;
                as.boo("hehe");
            }
            Else {
                Var c: Int = 123 * 12/23;
            }
        }
        """
        expect = "Error on line 4 col 13: If"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_219(self):
        input = """
        Class A
        {
            check(a,b,c:Int; c,d,f:Float)
            {
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_220(self):
        input = """
        Class A
        {
            check(a,b,c:Int; c,d,f:Float)
            {
                Var c,d,e:Int = a+b,c+d,e+f;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_221(self):
        input = """
        Class A
        {
            check(a,b,c:Int; c,d,f:Float)
            {
                Var c,d,e:Int = a+b,c+d,e+f;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_222(self):
        input = """
        Class A
        {
            check(a,b,c:Int; c,d,f:Float)
            {
                a+b[1]=12;
            }
        }
        """
        expect = "Error on line 6 col 17: +"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_223(self):
        input = """
        Class A
        {
            check(a,b,c:Int; c,d,f:Float)
            {
                -a[12] = 4;
            }
        }
        """
        expect = "Error on line 6 col 16: -"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_224(self):
        input = """
        Class A
        {
            check(a,b,c:Int; c,d,f:Float)
            {
                a::$a = 12;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_225(self):
        input = """
        Class A
        {
            check(a,b,c:Int; c,d,f:Float)
            {
                a.foo().foo();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_226(self):
        input = """
        Class A
        {
            check(a,b,c:Int; c,d,f:Float)
            {
                -a[12] = 4;
            }
        }
        """
        expect = "Error on line 6 col 16: -"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_227(self):
        input = """
        Class A
        {
            check(a,b,c:Int; c,d,f:Float)
            {
                a.a[12] = 4;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_228(self):
        input = """
        Class A
        {
            check(a,b,c:Int; c,d,f:Float)
            {
                a::a[12] = 4;
            }
        }
        """
        expect = "Error on line 6 col 19: a"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_229(self):
        input = """
        Class A
        {
            check(a,b,c:Int; c,d,f:Float)
            {
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_230(self):
        input = """
        Class A
        {
            check(a,b,c:Int; c,d,f:Float)
            {
                Return a==2;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_231(self):
        input = """
        Class A
        {
            check(a,b,c:Int; c,d,f:Float)
            {
                a.foo().foo().foo();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_232(self):
        """More complex program"""
        input = """
    Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
        Var length, width: Int = 1,2,3;
        $getNumOfShape() {
            Return $numOfShape;
        }
    }
    Class Rectangle: Shape {
        getArea() {
            Return self.length * self.width;
        }
    }
    Class Program {
        main() {
            Out.printInt(Shape::$numOfShape);
        }
    }
    """
        expect = "Error on line 6 col 36: ,"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_233(self):
        """More complex program"""
        input = """
    Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
        Var length, width: Int =;
        $getNumOfShape() {
            Return $numOfShape;
        }
    }
    Class Rectangle: Shape {
        getArea() {
            Return self.length * self.width;
        }
    }
    Class Program {
        main() {
            Out.printInt(Shape::$numOfShape);
        }
    }
    """
        expect = "Error on line 6 col 32: ;"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_234(self):
        """More complex program"""
        input = """
     Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
        Var length, width: Int = 1,2;
        $getNumOfShape() {
            Return numOfShape;
        }
    }
    Class Rectangle: Shape {
        getArea() {
            Return self.length * self.width;
        }
    }
    Class Program {
        main() {
            Out.printInt(Shape::$numOfShape);
            If (flag == 1) {b = c;}
            Elseif (flag == 2) {gud = mn * 923 / 123;}
            Else {b=a;}
            de = c/2341**3;
            Val $a : Int;
        }
    }
    """
        expect = "Error on line 22 col 24: *"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_235(self):
        """More complex program"""
        input = """
     Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
        Var length, width: Int = 1,2;
        $getNumOfShape() {
            Return numOfShape;
        }
    }
    Class Rectangle: Shape {
        getArea() {
            Return self.length * self.width;
        }
    }
    Class Program {
        main() {
            Out.printInt(Shape::$numOfShape);
            If (flag == 1) {b = c;}
            Elseif (flag == 2) {gud = mn * 923 / 123;}
            Else {b=a;}
            de = c/2341*3;
            Var length, width: Int = 1,2;
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_236(self):
        """More complex program"""
        input = """
     Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
        Var length, width: Int = 1,2;
        $getNumOfShape() {
            Return numOfShape;
        }
    }
    Class Rectangle: Shape {
        getArea() {
            Return self.length * self.width;
        }
    }
    Class Program
    {
        main()
        {
            Out.printInt(Shape::$numOfShape);
            Foreach(a In 12.2 .. 123.4 By 1)
            {
                Foreach(a In 12.2 .. 123.4 By 1){
                        Break;
                }
            }
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_237(self):
        """More complex program"""
        input = """
     Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
        Var length, width: Int = 1,2;
        $getNumOfShape() {
            Return numOfShape;
        }
    }
    Class Rectangle: Shape {
        getArea() {
            Return self.length * self.width;
        }
    }
    Class Program
    {
        main()
        {
            Foreach(ab In 212 .. 34 By -12){
                If (break == 1) {
                    Break;
                }
                Else { a::$o=12; }
            }
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_238(self):
        """More complex program"""
        input = """
     Class Shape
    {
        sum()
            {
                If (c == 2) {de = c/2341*123;}
                Elseif (count == 4) {
                   Foreach(m In 12.2 .. 123.4 By 1){
                        Return False;
                }
                }
                Else {
                    Var d: Float = 123e-10 * 12/23;
                }
        }
    }
    Class Rectangle: Shape {
        getArea() {
            Return self.length * self.width;
        }
    }
    Class Program
    {
        main()
        {
            Foreach(m In 12.2 .. 123.4 By 1){
                Return False;
            }
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_239(self):
        input = """
        Class A
        {
            check(a,b,c:Int; c,d,f:Float)
            {
                a.b.foo() = 12;
            }
        }
        """
        expect = "Error on line 6 col 26: ="
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_240(self):
        input = """
        Class A
        {
            sum()
            {
                Foreach(m In 123.2 .. 1.4 By -2.3){
                If (True) {}
                Elseif (flag == 4) {gud = mn * 0x12 / 34%2342;}
                Else
                {
                    b=a;
                    If (flag == 12) {b = c;}
                    Elseif (flag == 0) {
                        as = mn && 23;
                        as.boo("hehe");
                    }
                }
            }
         }
     }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_241(self):
        input = """
        Class A
        {
            sum()
            {
                If (c == 22321321)
                {
                        If (flag == 1) {b = c;}
                        Elseif (flag == 2) {gud = mn * 923 / 123;}
                        Else {b=a;}
                        de = c/2341*3;
                }
                Else 
                {
                    Var a: Int = 12;
                    Foreach(m In 12.2 .. 123.4 By 1)
                    {
                        Return False;
                    }
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_242(self):
        input = """
        Class A
        {
            check(a,b,c:Int; c,d,f:Float)
            {
                a[12] = 12;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_243(self):
        input = """ Class main {
            Var $num1, $num2, $num3, $num4 :  Int;
            MyFunc(a,b : Int ; c : Float){
                Var num1, num2, num3, num4 :  Int = 123, 100 + 100,123 + 1299, 54 + 55;
                a[0] = Self.a;
                If (2 > a[0]) {
                   a = 1;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_244(self):
        input = """ Class Program {
            main() {
                Var a: Array[Int, 7] = Array(
                    Array(
                        Array(1,2,3,4),
                        Array(1,2,3,4)
                    ),
                    Array(
                        Array(1,2,3,4),
                        Array(1,2,3,4)
                    )
                );
            }

        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_245(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;

            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        Class Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
                Var r, s: Int;
                r = 2.0;
                Var a: Array[Int, 5];
                s = r * r * Self.myPI;
                a[0] = s;
            }
        }
        """
        expect = "Error on line 8 col 23: $numOfShape"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_246(self):
        input = """
        Class Program {
            main () {
                Var a: Array[Array[Array[Int,1],2],2] = Array(
                    Array(
                        Array(1),
                        Array(1)
                    ),
                    Array(
                        Array(1),
                        Array(1)
                    )
                );
                Var a: Array[Array[Int,4],2] = Array(
                    Array(1,2,3,4),
                    Array(2,2,1,3)
                );
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_247(self):
        input = """
        Class main {
            Var $num1, $num2, $num3, $num4 :  Int;
            Myfunc(){
                If(a+1 == 2) {
                    If("abc" ==. "cde") {
                        Return;
                    }
                }
                a = !True && !False;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_248(self):
        input = """Class main {
            Var a: Array[Int, 7];
            Val num1: Int = 0;
            Val num1: Int = a.foo();
            Var $num1, $num2, $num3, $num4 :  Int = 123+123,11,22,33;
            MyFunc(a,b : Int ; c : Float){
               Var num1, num2, num3, num4 :  Int = 100 + 100,123 + 1299, 54 + 55,2;
               If (False && True && True){
                   a = b;
               }
               Elseif (True && False){
                   a = b+4+5;
               }
               Elseif (1 + 2 > 3 && False || True){
                   a = b+10;
               }
               Else{
                   a = b+1+2+3;
                   Foreach (i In 1 .. 100 By 2){
                        If(a >= b ){
                            a = b + 1;
                            Continue;
                        }
                        Elseif(a < b ){
                            a = b - 1;
                            Break;
                        }
                        Else {
                            a = b * 2;
                            Continue;
                            Break;
                            Return c*1/2+1+3;
                        }
                    }
               }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_249(self):
        input = """ Class Rectangle: Shape {
                        getArea() {
                            Return Self.length * Self.width;
                        }
                    }
                    Class Program {
                        main() {
                            Var X : A = New A();
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_250(self):
        input = """ Class Rectangle: Shape {
                        getArea() {
                            Var a : Shape = New Shape(3,4);
                            a.foo = 2;
                            a::$foo = 3;
                            Return Self.length * Self.width;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_251(self):
        """More complex program"""
        input = """Class Program{
                Val a: Int = 0;
                Val b: Int = 0;
                Var c, d: Int;
                main(){
                    Var $var1:String = "str1";
                }
                foo(){}
        }"""
        expect = "Error on line 6 col 24: $var1"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_252(self):
        """More complex program"""
        input = """
        Class Shape {
            foo(){
                a.a();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_253(self):
        """More complex program"""
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + a.foo();
                a.foo2(param1, param2);
                a1 = a.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Val speed: Int;
            Constructor(){
                Self.speed = 30;
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
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_254(self):
        """More complex program"""
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + a.foo();
                a.foo2(param1, param2);
                a1 = a.foo3(param1, param2);
                Var $b = 1 >= 3;
                Val val1 = True == False;
                b = ! val1;
                Return True;
            }
        }
        """
        expect = "Error on line 13 col 20: $b"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_255(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a.b();
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_256(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a=b.c.d.e;
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_257(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            Foreach (i In (1+2) .. (100*2-3) By (16-14)) {
                Out.printInt(i);
            }
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_258(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            Foreach (i In (1+2) .. (100*2-3) By (16-14)) {
                Var a,b : Int = 1,2;
            }
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_259(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            Foreach (i In (1+2) .. (100*2-3) By (16-14)) {
                Var a,b : Array[Int,0b0];
            }
        }
    }
    """
        expect = "Error on line 5 col 36: 0b0"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_260(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            Foreach (i In (1+2) .. (100*2-3) By (16-14)) {
                Var a,b : Array[Int,0x0];
            }
        }
    }
    """
        expect = "Error on line 5 col 36: 0x0"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_261(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            Foreach (i In (1+2) .. (100*2-3) By (16-14)) {
                Var a,b : Array[Int,00];
            }
        }
    }
    """
        expect = "Error on line 5 col 36: 00"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_262(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            Foreach (i In (1+2) .. (100*2-3) By (16-14)) {
                Var a,b : Array[Int,0];
            }
        }
    }
    """
        expect = "Error on line 5 col 36: 0"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_263(self):
        input = """
        Class Triangle:Shape{
            foo(){
                a = 12;
                a[5] = 12;
                a.arr[5] = 12;
                a::$a[5] = 12;
                a.vari = 12;
                a::$vari = 12;
                a::$vari[5] = 12;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_264(self):
        input = """
        Class Triangle:Shape{
            foo(){
                a::$foo().f = 5;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_265(self):
        input = """
        Class Triangle:Shape{
            Var arr : Array[Int,3];
            foo(){
                Var a : Student = New Student();
                Self.arr[0] = a;
                Self.arr[1] = 1+2*3+4;
                Self.arr[2] = Self.a[12][33][foo()];
            }
        }        
        """
        expect = "Error on line 8 col 48: ("
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_266(self):
        input = """
    Class Shape {
        $getNumOfShape( {
            Return Self.length * Self.width;
        }
    }
"""
        expect = "Error on line 3 col 24: {"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_267(self):
        input = """
    Class Shape {
        Constructor(Name: String; Age: Int){}
        getNumOfShape() {
            Break;
            Continue;
            Return;
        }
    }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_268(self):
        input = """
    Class Shape {
        Constructor(Name: String; Age: Int){{Return;}}
        getNumOfShape() {
            Break;
            Continue;
            Return;
            {}
        }
    }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_269(self):
        input = """
    Class Shape {
        Constructor(Name: String; Age: Int){}
        getNumOfShape() {
            Break;
            Continue;
            a[12] = c*d/e;
        }
    }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_270(self):
        input = """
    Class Shape {
        Constructor(Name: String; Age: Int){}
        getNumOfShape() {
            Break;
            Continue;
            a[12] = c*d/e;
        }
    }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_271(self):
        input = """
    Class Shape {
        Constructor(Name: String; Age: Int){}
        $getNumOfShape() {
            Return;
        }
        $sum(){
            Return;
        }
    }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_272(self):
        input = """
    Class Shape {
        Constructor(Name: String; Age: Int){}
        $getNumOfShape() {
            Return;
        }
        $sum(){
            {
                Val a : Array[Int,2] = Array(1,2);
            }
        }
    }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_273(self):
        input = """
            Class Classroom{
                Var $numOfStudents : Int = 0;
                Var $studentList: Array[String, 40];
                addStudent(newStu: Student){
                     Classroom::$studentList.append(newStu);
                } 
            }
            Class Student{
                Constructor(){
                    Classroom::$numOfStudents = Classroom::$numOfStudents + 1;
                }
                Destructor(){}
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_274(self):
        input = """
            Class Classroom{
                Var $numOfStudents : Int = 0;
                Var $studentList: Array[String, 40];
                addStudent(newStu: Student){
                     Classroom::$studentList.append(newStu);
                } 
            }
            Class Student{
                Constructor(){
                    Classroom::$numOfStudents = Classroom::$numOfStudents + 1;
                }
                Destructor(name: String){}
            }
        """
        expect = """Error on line 13 col 27: name"""
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_275(self):
        input = """
            Class Classroom{
                Var $numOfStudents : Int = 0;
                Var $studentList: Array[String, 40];
                addStudent(newStu: Student){
                     Classroom::$studentList.append(newStu);
                } 
            }
            Class Student{
                Constructor(){
                    Classroom::$numOfStudents = Classroom::$numOfStudents + 1;
                }
                Destructor(){
                    Classroom::$numOfStudents = Classroom::$numOfStudents - 1;
                }
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_276(self):
        input = """
            Class Classroom{
                Var $numOfStudents : Int = 0;
                Var $studentList: Array[String, 40];
                addStudent(newStu: Student){
                     Classroom::$studentList.append(newStu);
                } 
            }
            Class Student{
                learn(){
                    Self.print("Learning");   
                }
                Constructor(){
                    Classroom::$numOfStudents = Classroom::$numOfStudents + 1;
                }
                Destructor(){
                    Classroom::$numOfStudents = Classroom::$numOfStudents - 1;
                }
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_277(self):
        input = """
            Class Classroom{
                Var $numOfStudents : Int = 0;
                Var $studentList: Array[String, 40];
                addStudent(newStu: Student){
                     Classroom::$studentList.append(newStu);
                } 
            }
            Class Student{
                learn(){
                    Self.print("Learning");   
                }

                goToSchool(){
                    byeMom();
                    byeDad('by dad');    
                }

                Constructor(){
                    Classroom::$numOfStudents = Classroom::$numOfStudents + 1;
                }
                Destructor(){
                    Classroom::$numOfStudents = Classroom::$numOfStudents - 1;
                }
            }
        """
        expect = """'"""
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_278(self):
        input = """
            Class Classroom{
                Var $numOfStudents : Int = 0;
                Var $studentList: Array[String, 40];
                addStudent(newStu: Student){
                     Classroom::$studentList.append(newStu);
                } 
            }
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
            Class Examiner{
                visit(){}
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_279(self):
        input = """
            Class Classroom{
                Var $numOfStudents : Int = 0;
                Var $studentList: Array[String, 40];
                addStudent(newStu: Student){
                     Classroom::$studentList.append(newStu);
                } 
            }
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
            Class Examiner{
                visit(stu: Student){
                    Self.examine(stu);
                }
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_280(self):
        input = """
            Class Classroom{
                Var $numOfStudents : Int = 0;
                Var $studentList: Array[String, 40];
                addStudent(newStu: Student){
                     Classroom::$studentList.append(newStu);
                } 
            }
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

                accept(visitor:Visitor){
                    visitor.visit(Self);
                }
            }
            Class Visitor{}
            Class Examiner: Visitor{
                visit(stu: Student){
                    Self.examine(stu);
                }
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_case_281(self):
        input = """
        Class Something {
            foo() {
                a = -------34+293----------!34;
            }
        }
        """
        self.assertTrue(TestParser.test(input, "Error on line 4 col 43: !", 281))

    def test_282(self):
        input = """
                Class Shape{
                    foo(){
                        If ( a == -1--1){
                            If(b == "c"+."c"){}
                            Elseif( a == b ==. c){}
                            Else(1=2){}
                        }
                    }
                } 
                """
        expect = """Error on line 7 col 32: ("""
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_283(self):
        input = """
                Class Shape{
                    foo(){
                        a=b==c==d;
                    }
                }   
                """
        expect = """Error on line 4 col 30: =="""
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_284(self):
        input = """
                Class Shape{
                    Var a: Array[Array[Array[1,1_12],1],1];
                }   
                """
        expect = """Error on line 3 col 45: 1"""
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_285(self):
        input = """
                Class Shape{
                    Var a: Array[Array[Array[d,1_12],1],1];
                }   
                """
        expect = """Error on line 3 col 45: d"""
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_286(self):
        input = """
                Class Shape{
                    Var a: Array[Array[Array[d,_1_12],1],1];
                }   
                """
        expect = """Error on line 3 col 45: d"""
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_287(self):
        input = """
                Class Shape{
                    Var a: Array[b,Array[c,Array[d,1]]];
                }   
                """
        expect = """Error on line 3 col 33: b"""
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_288(self):
        input = r"""
            Class Program {
                main() {
                    a = True && "String";
                    a = "String" + 1 +. "String";
                    a = "String" || "String" && "String" * 0 / 0x0 % (a + a.a + Class_name::$a);
                    a = 0 + 0x0 + 0X0 + 0b0 + 0B0;
                    a = !1e123 - -True + !True / -----"String";
                    a = .123e123 > True;
                    a = 1.234e123 == "String";
                    a = 1.e-123 ==. "String";
                    a = Array(1,2,3) + Array(Array(1,2,3), Array(1,2,3));             
                    a = (1).a.a.a.a.a;
                    a = (1).a().a().a().a();
                    a = (1).a.a.a();
                    a = 1[1];
                    a = 1[1[1[1[1[1[1[1[1[1]]]]]]]]];
                    a = 1[1[1[1]]][1[1[1]]][0x0 + 0X0 - 0XFF + 0b0 + 0B0 / 0B1111];
                    a = (1).b[1][1][1][1][1];
                    a = (a+b+c).a.a.a[1[1[1[1[1[1]]]]]][1][a.b][Class_name::$a][a][Class_name::$a];
                    a = New X()[1];
                    a = New X().a;
                    a = New X(New X(a[New X()])).a[1];
                    a = Array(1,2,3)[1];
                    a = Array(Array(1,2,3), Array(1,2,3)).a.a.a();
                    a = Array(1,2,3)[Array(1,2,3)[1]];
                    a = "String"[1];
                    a = "String"["String"[1]];
                    a = "String"[New X().a];
                    a = Null;
                    a = Null.a;
                    a = Null.a.a.a;
                    a = Null.a.a.a();
                    a = Null.a().a().a();
                    a = Null[1];
                    a = Array(Null);
                    a = Null;

                    Null.a();
                    Null.a.a.a();
                    Null.a();
                    Null.a.a.a();
                    Null.a().a().a();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_289(self):
        input = r"""
            Class Program {
                main($x: Int) {}
            }
        """
        expect = r"Error on line 3 col 21: $x"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_290(self):
        input = r"""
            Class Program {
                main() {
                    a.a();
                    a::$a();

                    a.$a();
                }
            }
        """
        expect = r"Error on line 7 col 22: $a"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_291(self):
        input = r"""
            Class Program {
                main() {
                    a.a();
                    a::$a();

                    a::a();
                }
            }
        """
        expect = "Error on line 7 col 23: a"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_292(self):
        input = r"""
            Class Program {
                main() {
                    a = Null.a;
                    a = Null.null.a;
                    a = Null.Null.a;
                }
            }
        """
        expect = "Error on line 6 col 29: Null"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_293(self):
        input = r"""
            Class Program {
                main() {
                    a = New X();
                    a = "String" || "String" && "String" * 0 / 0x0 % (a + a.a + Class_name::$a - a.a() - Class_name::$a());
                    a[1] = "String" || "String" && "String" * 0 / 0x0 % (a + a.a + Class_name::$a- a.a() - Class_name::$a());
                    a[1][1][1] = "String" || "String" && "String" * 0 / 0x0 % (a + a.a + Class_name::$a- a.a() - Class_name::$a());
                    a[a[a[a[1]]]][a[a[a]]] = "String" || "String" && "String" * 0 / 0x0 % (a + a.a + Class_name::$a- a.a() - Class_name::$a());
                    a.a = "String" || "String" && "String" * 0 / 0x0 % (a  + a.a + Class_name::$a- a.a() - Class_name::$a());
                    a.a.a = "String" || "String" && "String" * 0 / 0x0 % (a  + a.a + Class_name::$a- a.a() - Class_name::$a());
                    A::$a = "String" || "String" && "String" * 0 / 0x0 % (a  + a.a + Class_name::$a- a.a() - Class_name::$a());
                    A::$a.a = "String" || "String" && "String" * 0 / 0x0 % (a  + a.a + Class_name::$a- a.a() - Class_name::$a());
                }
            }
        """
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_294(self):
        input = """
            Class Program {
                Constructor() {
                    Return;
                }
                Constructor(x: Int; y: String; a: Array[Array[Int,1],1]) {
                    Return a + x + y;
                }
                Destructor() {
                    Console.log("End");
                }
                Destructor(x: Int) {
                    Return x;
                }
            }
        """
        expect = """Error on line 12 col 27: x"""
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_295(self):
        # Not valid but ok in parser
        input = """
            Class Program {
                Constructor() {
                    Return;
                }
                Constructor(x: Int; y: String; a: Array[Array[Int,1],1]) {
                    Return a + x + y;
                }
                Destructor() {
                    Console.log("End");
                }
                Destructor() {
                    Return;
                }
                Constructor() {}
                Constructor(x: Int; y: String; a: Array[Array[Int,1],1]) {}
                Destructor() {}
                Destructor() {}
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_296(self):
        input = """
            Class Program {
                main() {
                    a.b.c();
                    a.b().c();

                    Self.a();
                    Self.a.a();

                    Class_name::$a();
                    Class_name::$a.a();
                    Class_name::$a().a();

                    a.b();
                }
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_297(self):
        input = r"""
            Class Program {
                main() {
                    a = a.b.c;
                    a = Class_name::$a;
                    a = Class_name::$a.a.a.a();
                    a = Null.a;
                    a = Null.null.a;
                    a = Self.a;
                    a = Self.self.a;
                    a = Self.Null;
                }
            }
        """
        expect = r"Error on line 11 col 29: Null"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_298(self):
        input = r"""
            Class Program {
                main() {
                    Var a: Int = 1;
                    Var a: Int : 1;
                }
            }
        """
        expect = r"Error on line 5 col 31: :"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_299(self):
        # Ít hơn số biến trả về dấu ;
        input = r"""
            Class Program {
                Var a,b,$c: Int = 1,2,3; ## Equal ##
                Val a,b,$c: Int = 1,2,3; ## Equal ##
                main() {
                    Var a,b,c: Int = 1,2,3; ## Equal ##
                    Val a,b,c: Int = 1,2,3; ## Equal ##
                    Var a,b,c: Int = 1,2; ## Less than variable ##
                }
            }
        """
        expect = r"Error on line 8 col 40: ;"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_300(self):
        # Nhiều hơn số biến trả về dấu ,
        input = r"""
            Class Program {
                Var a,b,$c: Int = 1,2,3; ## Equal ##
                Val a,b,$c: Int = 1,2,3; ## Equal ##
                main() {
                    Var a,b,c: Int = 1,2,3; ## Equal ##
                    Val a,b,c: Int = 1,2,3; ## Equal ##
                    Var a,b,c: Int = 1,2,4,5; ## Greater than variable ##
                }
            }
        """
        expect = r"Error on line 8 col 42: ,"
        self.assertTrue(TestParser.test(input, expect, 300))