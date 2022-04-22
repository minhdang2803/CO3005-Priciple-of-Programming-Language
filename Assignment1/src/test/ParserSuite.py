import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_201(self):
        input = """Class Program{}"""
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 201))

    def test_202(self):
        input = """Class Program{
            main(){
            }
        }"""
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 202))

    def test_203(self):
        input = """Class Program{
            main(){
                Val a:Int = 2;
            }
        }"""
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 203))

    def test_203(self):
        input = """Class Program{
            main(){
                Val $a:Int = 2;
            }
        }"""
        output = "Error on line 3 col 20: $a"
        self.assertTrue(TestParser.test(input, output, 203))

    def test_204(self):
        input = """Class Program{
                    main(){
                        Val $a:Int = 2;
                    }
                }"""
        output = "Error on line 3 col 28: $a"
        self.assertTrue(TestParser.test(input, output, 204))

    def test_205(self):
        input = """Class Program{
            main(){
                Val a: Int = 0;
                Val b: Int = 0;
                Var c, d: Int;
            }
        }"""
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 205))

    def test_205(self):
        input = """Class Program{
                Val a: Int = 0;
                Val b: Int = 0;
                Var c, d: Int;
        }"""
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 205))

    def test_206(self):
        input = """Class Program{
                Val a: Int = 0;
                Val b: Int = 0;
                Var c, d: Int;
                main(){
                }
                foo(){}
        }"""
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 206))

    def test_207(self):
        input = """Class Program{
                Val a: Int = 0;
                Val b: Int = 0;
                Var c, d: Int;
                main(){
                    Var $var1:String = "str1";
                }
                foo(){}
        }"""
        output = "Error on line 6 col 24: $var1"
        self.assertTrue(TestParser.test(input, output, 207))

    def test_208(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo()
        }
        """
        output = "Error on line 10 col 8: }"
        self.assertTrue(TestParser.test(input, output, 208))

    def test_209(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo();
        }
        """
        output = "Error on line 9 col 17: ;"
        self.assertTrue(TestParser.test(input, output, 209))

    def test_210(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                    Return True;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 210))

    def test_211(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                Return True;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 211))

    def test_212(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Return True;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 212))

    def test_213(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var $b = 1 >= 3;
                Val val1 = True == False;
                b = ! val1;
                Return True;
            }
        }
        """
        output = "Error on line 13 col 20: $b"
        self.assertTrue(TestParser.test(input, output, 213))

    def test_214(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 214))

    def test_215(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            run(){
                Self.running = True;
            }
            stop(){
                Self.running = False;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 215))

    def test_216(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Constructor(){}
            run(){
                Self.running = True;
            }
            stop(){
                Self.running = False;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 216))

    def test_217(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
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
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 217))

    def test_218(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
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
            Destructor(){}
            run(){
                Self.running = True;
            }
            stop(){
                Self.running = False;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 218))

    def test_219(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int, model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                Self.running = True;
            }
            stop(){
                Self.running = False;
            }
        }
        Class Car:Vehicle{}
        """
        output = "Error on line 27 col 34: ,"
        self.assertTrue(TestParser.test(input, output, 219))

    def test_220(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                Self.running = True;
            }
            stop(){
                Self.running = False;
            }
        }
        Class Car:Vehicle{}
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 220))

    def test_220(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                Self.running = True;
            }
            stop(){
                Self.running = False;
            }
        }
        Class Car:Vehicle{}
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 220))

    def test_221(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            openCabin(){
                ## Open cabin ##
                openedCabin = True;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 221))

    def test_222(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 222))

    def test_223(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 223))

    def test_223(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True
                }
                Else 
                    Return False;
            }
        }
        """
        output = "Error on line 48 col 16: }"
        self.assertTrue(TestParser.test(input, output, 223))

    def test_224(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True
                }
                Else {
                    Return False;
                }
            }
        }
        """
        output = "Error on line 48 col 16: }"
        self.assertTrue(TestParser.test(input, output, 224))

    def test_225(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            openAllDoor(){
            }
            }
        }
        """
        output = "Error on line 52 col 23: ("
        self.assertTrue(TestParser.test(input, output, 225))

    def test_226(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 226))

    def test_227(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    Self.foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    Self.foo2();
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 227))

    def test_228(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Door{}
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    Self.foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    Self.foo2();
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 228))

    def test_229(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    Self.foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    Self.foo2();
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 229))

    def test_230(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    Self.foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    Self.foo2();
                }
            }
        }

        class Motor:Vehicle{
            Var $motorList:Array[Int, 100];
        }
        """
        output = "Error on line 76 col 8: class"
        self.assertTrue(TestParser.test(input, output, 230))

    def test_231(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    Self.foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    Self.foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Int, 100];
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 231))

    def test_232(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    Self.foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    Self.foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Int, 100];
            Val maxSpeed: Int = 40;
            Constructor(){

            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 232))

    def test_233(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    Self.foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    Self.foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Int, 100];
            Val maxSpeed: Int = 40;
            Constructor(){

            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 233))

    def test_234(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    Self.foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    Self.foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Int, 100];
            Var $numOfMotor: Int = 0;
            Val maxSpeed: Int = 40;
            Constructor(){
                motorList[Motor::$numOfMotor] = Self;
                Motor::$numOfMotor += 1;
            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
        }
        """
        output = "Error on line 82 col 35: +"
        self.assertTrue(TestParser.test(input, output, 234))

    def test_235(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    Self.foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    Self.foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Int, 100];
            Var $numOfMotor: Int = 0;
            Val maxSpeed: Int = 40;
            Constructor(){
                motorList[Motor::$numOfMotor] = Self;
                Self::$numOfMotor = Motor::$numOfMotor + 1;
            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
        }


        """
        output = "Error on line 82 col 20: ::"
        self.assertTrue(TestParser.test(input, output, 235))

    def test_236(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    Self.foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    Self.foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Int, 100];
            Var $numOfMotor: Int = 0;
            Val maxSpeed: Int = 40;
            Constructor(){
                motorList[Motor::$numOfMotor] = Self;
                Motor::$numOfMotor = Motor::$numOfMotor + 1;
            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
            Destructor{
                a = b;
            }
        }
        """
        output = "Error on line 87 col 22: {"
        self.assertTrue(TestParser.test(input, output, 236))

    def test_237(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    Self.foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    Self.foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Int, 100];
            Var $numOfMotor: Int = 0;
            Val maxSpeed: Int = 40;
            Constructor(){
                motorList[Motor::$numOfMotor] = Self;
                Motor::$numOfMotor = Motor::$numOfMotor + 1;
            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
            Destructor(){
                a = b;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 237))

    def test_238(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    Self.foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    Self.foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Int, 100];
            Var $numOfMotor: Int = 0;
            Val maxSpeed: Int = 40;
            Constructor(){
                motorList[Motor::$numOfMotor] = Self;
                Motor::$numOfMotor = Motor::$numOfMotor + 1;
            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
            Destructor(){
                Foreach(i In Motor::$numOfMotor .. 1 By -1){}
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 238))

    def test_239(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    Self.foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    Self.foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Int, 100];
            Var $numOfMotor: Int = 0;
            Val maxSpeed: Int = 40;
            Constructor(){
                motorList[Motor::$numOfMotor] = Self;
                Motor::$numOfMotor = Motor::$numOfMotor + 1;
            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
            Destructor(){
                Foreach(i In Motor::$numOfMotor .. 1 By -1){
                    Motor::$motorList[i] = Null;
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 239))

    def test_240(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }

        Class Diary{
            Val $arr: Array[Array[String, 2], 5];
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 240))

    def test_241(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }

        Class Diary{
            Val $arr: Array[Array[String, 2], 5];
            Constructor(){}
            addDiary(diary: Array[String, 2]){
                Diary::arr[0] = diary;
            }
        }
        """
        output = "Error on line 26 col 23: arr"
        self.assertTrue(TestParser.test(input, output, 241))

    def test_242(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }

        Class Diary{
            Val $arr: Array[Array[String, 2], 5];
            Constructor(){}
            addDiary(diary: Array[String, 2]){
                Diary::$arr[0] = diary;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 242))

    def test_243(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }

        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Diary::$numOfDiary] = diary;
            }
        }
        """
        output = "Error on line 24 col 28: ="
        self.assertTrue(TestParser.test(input, output, 243))

    def test_244(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }

        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Diary::$numOfDiary] = diary;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 244))

    def test_245(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }

        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 245))

    def test_246(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }

        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
            deleteDiary(id: Int){
                Diary::$arr[id] = Null;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 246))

    def test_247(self):
        input = """
        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            Destructor(){
                Foreach (i in Motor::$numOfDiary .. 1 By -1){
                    If (Motor::$arr[i] == Null){
                        Continue;
                    }
                    Else{
                        Motor::$arr[i] = Null;
                    }
                }
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
            deleteDiary(id: Int){
                Diary::$arr[id] = Null;
            }
        }
        """
        output = "Error on line 9 col 27: in"
        self.assertTrue(TestParser.test(input, output, 247))

    def test_248(self):
        input = """
        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            Destructor(){
                Foreach (i In Motor::$numOfDiary .. 1 By -1){
                    If (Motor::$arr[i] == Null){
                        Continue;
                    }
                    Else{
                        Motor::$arr[i] = Null;
                    }
                }
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
            deleteDiary(id: Int){
                Diary::$arr[id] = Null;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 248))

    def test_249(self):
        input = """
        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Var id:Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            Destructor(){
                Foreach (i In Motor::$numOfDiary .. 1 By -1){
                    If (Motor::$arr[i] == Null){
                        Continue;
                    }
                }
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
            deleteDiary(id: Int){
                Diary::$arr[id] = Null;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 249))

    def test_250(self):
        input = """
        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Var id:Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            Destructor(){
                Foreach (i In Motor::$numOfDiary .. 1 By -1){
                    Motor::$arr[Self.id] = Null;
                }
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
            deleteDiary(id: Int){
                Diary::$arr[id] = Null;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 250))

    def test_251(self):
        input = """
        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Var id:Int = 0;
            Var a,b: Int = 1;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            Destructor(){
                Foreach (i In Motor::$numOfDiary .. 1 By -1){
                    Motor::$arr[Self.id] = Null;
                }
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
            deleteDiary(id: Int){
                Diary::$arr[id] = Null;
            }
        }
        """
        output = "Error on line 6 col 28: ;"
        self.assertTrue(TestParser.test(input, output, 251))

    def test_252(self):
        input = """
        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Var id:Int = 0;
            Var a,b: Int = 1,2;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            Destructor(){
                Foreach (i In Motor::$numOfDiary .. 1 By -1){
                    Motor::$arr[Self.id] = Null;
                }
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
            deleteDiary(id: Int){
                Diary::$arr[id] = Null;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 252))

    def test_253(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 253))

    def test_254(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
            Constructor(){
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 254))

    def test_255(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
            Constructor(){
            }
            foo(){
                (a + b).foo();
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 255))

    def test_256(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
            Constructor(){
            }
            foo(){
                a + b.foo();
            }
        }
        """
        output = "Error on line 8 col 18: +"
        self.assertTrue(TestParser.test(input, output, 256))

    def test_257(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
            Constructor(){
            }
            foo(){
                a = b.foo();
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 257))

    def test_258(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
            Constructor(){
                Foreach (row In 1 .. 256 By 1){
                    Foreach (col In 256 .. 1 By -1){
                        Foreach (channel In 1 .. 3 By 1){
                        } 
                    }
                }
            }
            foo(){
                a = b.foo();
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 258))

    def test_259(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
            Constructor(){
                Foreach (row In 1 .. 256 By 1){
                    Foreach (col In 256 .. 1 By -1){
                        Foreach (channel In 1 .. 3 By 1){
                            matrix[row][col][channel] = 0;
                        } 
                    }
                }
            }
            foo(){
                a = b.foo();
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 259))

    def test_260(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
            Constructor(){
                Foreach (row In 1 .. 256 By 1){
                    Foreach (col In 256 .. 1 By -1){
                        Foreach (channel In 1 .. 3 By 1){
                            matrix[row][col][channel] = 0;
                        } 
                    }
                }
            }
            Destructor(){}
            foo(){
                a = b.foo();
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 260))

    def test_261(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
            Constructor(){
                Foreach (row In 1 .. 256 By 1){
                    Foreach (col In 256 .. 1 By -1){
                        Foreach (channel In 1 .. 3 By 1){
                            matrix[row][col][channel] = 255;
                        } 
                    }
                }
            }
            Destructor(){
                Foreach (row In 1 .. 256 By 1){
                    Foreach (col In 256 .. 1 By -1){
                        Foreach (channel In 1 .. 3 By 1){
                            matrix[row][col][channel] = 0;
                        } 
                    }
                }
            }
            foo(){
                a = b.foo();
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 261))

    def test_262(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
            Constructor(){
                Foreach (row In 1 .. 256 By 1){
                    Foreach (col In 256 .. 1 By -1){
                        Foreach (channel In 1 .. 3 By 1){
                            matrix[row][col][channel] = 255;
                        } 
                    }
                }
            }
            Destructor(){
                Foreach (row In 1 .. 256 By 1){
                    Foreach (col In 256 .. 1 By -1){
                        Foreach (channel In 1 .. 3 By 1){
                            matrix[row][col][channel] = 0;
                        } 
                    }
                }
            }
            concat(img: Image){
                Self.img = Self.img + Self.img;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 262))

    def test_263(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
            Constructor(){
                Foreach (row In 1 .. 256 By 1){
                    Foreach (col In 256 .. 1 By -1){
                        Foreach (channel In 1 .. 3 By 1){
                            Self.matrix[row][col][channel] = 255;
                        } 
                    }
                }
            }
            Destructor(){
                Foreach (row In 1 .. 256 By 1){
                    Foreach (col In 256 .. 1 By -1){
                        Foreach (channel In 1 .. 3 By 1){
                            Self.matrix[row][col][channel] = 0;
                        } 
                    }
                }
            }
            add(img: Image){
                Foreach (row In 1 .. 256 By 1){
                    Foreach (col In 256 .. 1 By -1){
                        Foreach (channel In 1 .. 3 By 1){
                            Self.matrix[row][col][channel] = Self.matrix[row][col][channel] + img.matrix[row][col][channel];
                        } 
                    }
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 263))

    def test_264(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
            Constructor(){
                Foreach (row In 1 .. 256 By 1){
                    Foreach (col In 256 .. 1 By -1){
                        Foreach (channel In 1 .. 3 By 1){
                            Self.matrix[row][col][channel] = 255;
                        } 
                    }
                }
            }
            Destructor(){
                Foreach (row In 1 .. 256 By 1){
                    Foreach (col In 256 .. 1 By -1){
                        Foreach (channel In 1 .. 3 By 1){
                            Self.matrix[row][col][channel] = 0;
                        } 
                    }
                }
            }
            add(img: Image){
                Foreach (row In 1 .. 256 By 1){
                    Foreach (col In 256 .. 1 By -1){
                        Foreach (channel In 1 .. 3 By 1){
                            Self.matrix[row][col][channel] = Self.matrix[row][col][channel] + img.matrix[row][col][channel];
                        } 
                    }
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 264))

    def test_265(self):
        input = """
            Class Shape{
                foo(){
                    a = New X().Y();
                    Var a: Array[Int, 0];
                }
            }

        """
        output = """Error on line 5 col 38: 0"""
        self.assertTrue(TestParser.test(input, output, 265))

    def test_266(self):
        input = """
            Class Shape{
                foo(){
                    a = New X().Y();
                    Var a: Array[Int, 265];
                }
            }

        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 266))

    def test_267(self):
        input = """
            Class Image{
                Var width, height: Int;
                Var matrix: Array[Array[Array[Int, 3], 256], 256];
                Constructor(){
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.matrix[row][col][channel] = 255;
                            } 
                        }
                    }
                }
                Destructor(){
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.matrix[row][col][channel] = 0;
                            } 
                        }
                    }
                }
                add(img: Image){
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.matrix[row][col][channel] = Self.matrix[row][col][channel] + img.matrix[row][col][channel];
                            } 
                        }
                    }
                }
                concat(img: Image){
                    Var concatMatrix: Array[Array[Array[Int, 3], 512], 512];
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 267))

    def test_268(self):
        input = """
            Class Image{
                Var width, height: Int;
                Var matrix: Array[Array[Array[Int, 3], 256], 256];
                Constructor(){
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.matrix[row][col][channel] = 255;
                            } 
                        }
                    }
                }
                Destructor(){
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.matrix[row][col][channel] = 0;
                            } 
                        }
                    }
                }
                add(img: Image){
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.matrix[row][col][channel] = Self.matrix[row][col][channel] + img.matrix[row][col][channel];
                            } 
                        }
                    }
                }
                concat(img: Image){
                    Var concatMatrix: Array[Array[Array[Int, 3], 512], 512];
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.concatMatrix[row][col][channel] = Self.matrix[row][col][channel];
                            } 
                        }
                    }
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 268))

    def test_269(self):
        input = """
            Class Image{
                Var width, height: Int;
                Var matrix: Array[Array[Array[Int, 3], 256], 256];
                Constructor(){
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.matrix[row][col][channel] = 255;
                            } 
                        }
                    }
                }
                Destructor(){
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.matrix[row][col][channel] = 0;
                            } 
                        }
                    }
                }
                add(img: Image){
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.matrix[row][col][channel] = Self.matrix[row][col][channel] + img.matrix[row][col][channel];
                            } 
                        }
                    }
                }
                concat(img: Image){
                    Var concatMatrix: Array[Array[Array[Int, 3], 512], 512];
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.concatMatrix[row][col][channel] = Self.matrix[row][col][channel];
                                Self.concatMatrix[row+256][col][channel] = Self.matrix[row][col][channel];
                            } 
                        }
                    }
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 269))

    def test_270(self):
        input = """
            Class Image{
                Var width, height: Int;
                Var matrix: Array[Array[Array[Int, 3], 256], 256];
                Constructor(){
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.matrix[row][col][channel] = 255;
                            } 
                        }
                    }
                }
                Destructor(){
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.matrix[row][col][channel] = 0;
                            } 
                        }
                    }
                }
                add(img: Image){
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.matrix[row][col][channel] = Self.matrix[row][col][channel] + img.matrix[row][col][channel];
                            } 
                        }
                    }
                }
                vstack(img: Image){
                    Var concatMatrix: Array[Array[Array[Int, 3], 512], 512];
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.concatMatrix[row][col][channel] = Self.matrix[row][col][channel];
                                Self.concatMatrix[row+256][col][channel] = Self.matrix[row][col][channel];
                            } 
                        }
                    }
                }
                hstack(img: Image){
                    Var concatMatrix: Array[Array[Array[Int, 3], 512], 512];
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.concatMatrix[row][col][channel] = Self.matrix[row][col][channel];
                                Self.concatMatrix[row][col+256][channel] = Self.matrix[row][col][channel];
                            } 
                        }
                    }
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 270))

    def test_271(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
            }
            Class Laptop:Electrical{
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 271))

    def test_272(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
            }
            Class Laptop:Electrical{
                start(){
                    $nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """Error on line 8 col 20: $nothing"""
        self.assertTrue(TestParser.test(input, output, 272))

    def test_273(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Constructor(){}
                Constructor(weight: Float, useBat:Boolean){

                }
            }
            Class Laptop:Electrical{
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """Error on line 6 col 41: ,"""
        self.assertTrue(TestParser.test(input, output, 273))

    def test_274(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                }
            }
            Class Laptop:Electrical{
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 274))

    def test_275(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 275))

    def test_276(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                    stop2(){

                    };
                }
            }
        """
        output = """Error on line 21 col 25: ("""
        self.assertTrue(TestParser.test(input, output, 276))

    def test_277(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{
                foo();
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """Error on line 14 col 21: ;"""
        self.assertTrue(TestParser.test(input, output, 277))

    def test_278(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{
                $Refresh(count: Int){

                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 278))

    def test_279(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{
                $Refresh(count: Int){
                    Foreach(i In count .. 0 By -1){

                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 279))

    def test_280(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Var $numOfDevices: Int;
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{
                $Refresh(){
                    Foreach(i In $numOfDevices .. 0 By -1){

                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """Error on line 16 col 33: $numOfDevices"""
        self.assertTrue(TestParser.test(input, output, 280))

    def test_281(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Var $numOfDevices: Int;
                Var $devices: Array[Float, 100];
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                    $devices[$numOfDevices] = Self;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{

                $Refresh(){
                    Foreach(i In ElectricalDevice::$numOfDevices .. 0 By -1){

                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """Error on line 11 col 20: $devices"""
        self.assertTrue(TestParser.test(input, output, 281))

    def test_282(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Var $numOfDevices: Int;
                Var $devices: Array[Float, 100];
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                    ElectricalDevice::$devices[$numOfDevices] = Self;
                    ElectricalDevice::$numOfDevices = ElectricalDevice::$numOfDevices+1;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{

                $Refresh(){
                    Foreach(i In ElectricalDevice::$numOfDevices .. 0 By -1){

                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """Error on line 11 col 47: $numOfDevices"""
        self.assertTrue(TestParser.test(input, output, 282))

    def test_283(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Var $numOfDevices: Int;
                Var $devices: Array[Float, 100];
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                    ElectricalDevice::$devices[ElectricalDevice::$numOfDevices] = Self;
                    ElectricalDevice::$numOfDevices = ElectricalDevice::$numOfDevices+1;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{

                $Refresh(){
                    Foreach(i In $numOfDevices .. 0 By -1){

                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """Error on line 20 col 33: $numOfDevices"""
        self.assertTrue(TestParser.test(input, output, 283))

    def test_284(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Var $numOfDevices: Int;
                Var $devices: Array[Float, 100];
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                    ElectricalDevice::$devices[ElectricalDevice::$numOfDevices] = Self;
                    ElectricalDevice::$numOfDevices = ElectricalDevice::$numOfDevices+1;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{

                $Refresh(){
                    Foreach(i In ElectricalDevice::$numOfDevices .. 0 By -1){

                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 284))

    def test_285(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Var $numOfDevices: Int;
                Var $devices: Array[Float, 100];
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{
                Var $numOfLaptops: Int;
                Var $laptops: Array[Boolean, 100];

                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                    ElectricalDevice::$devices[ElectricalDevice::$numOfDevices] = Self;
                    Laptop::$laptops[$numOfDevices] = Self;
                    ElectricalDevice::$numOfDevices = ElectricalDevice::$numOfDevices+1;
                }

                $Refresh(){
                    Foreach(i In (ElectricalDevice::$numOfDevices*100)/100 + 1 .. 100-100+35%34 By -1){

                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """Error on line 23 col 37: $numOfDevices"""
        self.assertTrue(TestParser.test(input, output, 285))

    def test_286(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Var $numOfDevices: Int;
                Var $devices: Array[Float, 100];
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{
                Var $numOfLaptops: Int;
                Var $laptops: Array[Boolean, 100];

                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                    ElectricalDevice::$devices[ElectricalDevice::$numOfDevices] = Self;
                    Laptop::$laptops[ElectricalDevice::$numOfDevices] = Self;
                    ElectricalDevice::$numOfDevices = ElectricalDevice::$numOfDevices+1;
                }

                $Refresh(){
                    Foreach(i In (ElectricalDevice::$numOfDevices*100)/100 + 1 .. 100-100+35%34 By -1){
                        laptops[i].refresh();
                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """Error on line 29 col 34: ."""
        self.assertTrue(TestParser.test(input, output, 286))

    def test_287(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Var $numOfDevices: Int;
                Var $devices: Array[Float, 100];
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{
                Var $numOfLaptops: Int;
                Var $laptops: Array[Boolean, 100];

                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                    ElectricalDevice::$devices[ElectricalDevice::$numOfDevices] = Self;
                    Laptop::$laptops[ElectricalDevice::$numOfDevices] = Self;
                    ElectricalDevice::$numOfDevices = ElectricalDevice::$numOfDevices+1;
                }

                $Refresh(){
                    Foreach(i In (ElectricalDevice::$numOfDevices*100)/100 + 1 .. 100-100+35%34 By -1){
                        (laptops[i]).refresh();
                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 287))

    def test_288(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Var $numOfDevices: Int;
                Var $devices: Array[Float, 100];
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{
                Var $numOfLaptops: Int;
                Var $laptops: Array[Boolean, 100];

                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                    ElectricalDevice::$devices[ElectricalDevice::$numOfDevices] = Self;
                    Laptop::$laptops[ElectricalDevice::$numOfDevices] = Self;
                    ElectricalDevice::$numOfDevices = ElectricalDevice::$numOfDevices+1;
                }

                $refresh(){
                    Foreach(i In (ElectricalDevice::$numOfDevices*100)/100 + 1 .. 100-100+35%34 By -1){
                        (laptops[i]).refresh();
                    }
                }

                $checkVirus(){
                    Foreach(i In Laptop::$numOfLaptops/100*100 + 1 .. 100-100+35%34 By -1){
                        If ((laptops[i]).checked == True){
                            Continue;
                        }
                        Else{
                            (laptops[i]).checked = True;
                        }
                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 288))

    def test_289(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Var $numOfDevices: Int;
                Var $devices: Array[Float, 100];
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{
                Var $numOfLaptops: Int;
                Var $laptops: Array[Boolean, 100];

                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                    ElectricalDevice::$devices[ElectricalDevice::$numOfDevices] = Self;
                    Laptop::$laptops[ElectricalDevice::$numOfDevices] = Self;
                    ElectricalDevice::$numOfDevices = ElectricalDevice::$numOfDevices+1;
                }

                $refresh(){
                    Foreach(i In (ElectricalDevice::$numOfDevices*100)/100 + 1 .. 100-100+35%34 By -1){
                        (laptops[i]).refresh();
                    }
                }

                $checkVirus(){
                    Foreach(i In Laptop::$numOfLaptops/100*100 + 1 .. 100-100+35%34 By -1){
                        If ((laptops[i]).checked == True){
                            Break;
                        }
                        Else{
                            (laptops[i]).checked = True;
                        }
                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
            Class iPhone:ElectricalDevice{
                Val $os: String = "iOS";
                Var number: String; 
                Var $numOfPhones: Int;
                Var $phone: Array[Boolean, 100];

                Constructor(){

                }
                Destructor(){

                }

                insertSIM(sim: SIM){
                    Self.number = SIM.number;
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 289))

    def test_290(self):
        input = """
            Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Var $numOfDevices: Int;
                Var $devices: Array[Float, 100];
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                }
                Destructor(){}

            }
            Class Laptop:Electrical{
                Var $numOfLaptops: Int;
                Var $laptops: Array[Boolean, 100];

                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                    ElectricalDevice::$devices[ElectricalDevice::$numOfDevices] = Self;
                    Laptop::$laptops[ElectricalDevice::$numOfDevices] = Self;
                    ElectricalDevice::$numOfDevices = ElectricalDevice::$numOfDevices+1;
                }

                $refresh(){
                    Foreach(i In (ElectricalDevice::$numOfDevices*100)/100 + 1 .. 100-100+35%34 By -1){
                        (laptops[i]).refresh();
                    }
                }

                $checkVirus(){
                    Foreach(i In Laptop::$numOfLaptops/100*100 + 1 .. 100-100+35%34 By -1){
                        If ((laptops[i]).checked == True){
                            Break;
                        }
                        Else{
                            (laptops[i]).checked = True;
                        }
                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
            Class iPhone:ElectricalDevice{
                Val $os: String = "iOS";
                Var number: String; 
                Var $numOfPhones: Int;
                Var $phone: Array[Boolean, 100];

                Constructor(){

                }
                Destructor(){

                }

                insertSIM(sim: SIM){
                    Self.number = SIM.number;
                }

                detachSIM(){
                    Self.number = Null;
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 290))

    def test_290(self):
        input = """
            Class Class{
                Var $numOfStudents : Int = 0;
                Var $studentList: Array[String, 40];
                addStudent(newStu: Student){
                     Class::$studentList[Classroom::$numOfStudents] = newStu;
                } 
            }
            Class Student{}
        """
        output = """Error on line 2 col 18: Class"""
        self.assertTrue(TestParser.test(input, output, 290))

    def test_291(self):
        input = """
            Class Classroom{
                Var $numOfStudents : Int = 0;
                Var $studentList: Array[String, 40];
                addStudent(newStu: Student){
                     Classroom::$studentList[Classroom::$numOfStudents] = newStu;
                } 
            }
            Class Student{}
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 291))

    def test_292(self):
        input = """
            Class Classroom{
                Var $numOfStudents : Int = 0;
                Var $studentList: Array[String, 40];
                addStudent(newStu: Student){
                     Classroom::$studentList.append(newStu);
                } 
            }
            Class Student{}
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 292))

    def test_293(self):
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
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 293))

    def test_294(self):
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
        output = """Error on line 13 col 27: name"""
        self.assertTrue(TestParser.test(input, output, 294))

    def test_295(self):
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
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 295))

    def test_296(self):
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
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 296))

    def test_297(self):
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
        output = """'"""
        self.assertTrue(TestParser.test(input, output, 297))

    def test_298(self):
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
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 298))

    def test_299(self):
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
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 299))

    def test_300(self):
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
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 300))