//Student ID: 1952041
grammar D96;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text[1:])
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text[1:])
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    else:
        return result
}
@parser::members{
def checkZero(self,input):
    num = 0
    if len(input) == 1:
        if input[0] == '0':
            num = 1
    elif len(input) == 2:
        if input[0] == '0' and input[1] == '0':
            num = 1
    elif len(input) == 3:
        if input[0] == '0' and input[2] == '0':
            if input[1] == 'X' or input[1] == 'x' or input[1] == 'b' or input[1] == 'B':
                num = 1
    return num
}
options {
	language = Python3;
}
//1. Program Structures
program:  classDecl+ EOF;
//Expressions
expr: expr0;
expr0: expr1 (STR_CONCAT|STR_CMP) expr1 | expr1;
expr1: expr2 relational_op expr2 | expr2;
expr2: expr2 (OR|AND) expr3 | expr3;
expr3: expr3 (ADD|MINUS) expr4 | expr4;
expr4: expr4 (MULTIPLY|DEVIDE|MODULO) expr5 |expr5;
expr5: NOT expr5|expr6;
expr6: MINUS expr6|expr7;
expr7: expr7 LSB expr RSB|expr8; //LSB literal RSB
expr8: expr8 DOT ID (LB listOfexpr RB)?|expr9; //self.foo()
expr9: ID DOUBLE_COLON STATIC_ID (LB listOfexpr RB)?|expr10;
expr10: NEW expr10 LB listOfexpr RB | expr11;
expr11: LB expr RB |ID|SELF|literal|NULL;

listOfexpr: expr manyExpr|;
manyExpr: COMMA expr manyExpr|;
//Variable Declaration
variableDecl: (VAR|VAL) (withoutASM|withASM) SEMI;
withASM: (STATIC_ID|ID) pair expr;
pair: COMMA (STATIC_ID|ID) pair expr COMMA | COLON mptype ASSIGN;
withoutASM: (STATIC_ID|ID) manyVariable COLON mptype;
manyVariable: COMMA (STATIC_ID|ID) manyVariable|;
//Variable Declaration for method
variableDecl_func: (VAR|VAL) (withoutASM2|withASM2) SEMI;
withASM2: ID pair2 expr;
pair2: COMMA ID pair2 expr COMMA | COLON mptype ASSIGN;
withoutASM2: ID manyVariable2 COLON mptype;
manyVariable2: COMMA ID manyVariable2|;
/////////////////////////END VARIABLE DELCARATAION/////////////////////////////////
//Array Literal
arrayLit: ARRAY LB arrayAssignMember RB; //Array(1, 5, 7, 12)
arrayAssignMember: expr arrayMemberList |;
arrayMemberList: COMMA expr arrayMemberList |;
//Array Type
arrayType: ARRAY LSB typeDataPrimitive COMMA size RSB; // Array[<type>, <size>]
///////////////////////////////////////////// CLASS DECLARATION ////////////////////////////////////////////////////
classDecl: CLASS ID (COLON ID)? LCB classMember RCB;
classMember: classMember (constructorDecl|destructorDecl|variableDecl|methodDecl)|;
//Constructor - Destructor
constructorDecl: 'Constructor' LB parameterList RB stmt_Block; // Constructor (<list of parameters>) <block statement>
destructorDecl: 'Destructor' LB RB stmt_Block; // Destructor () <block statement>
//Method declaration
methodDecl: (STATIC_ID|ID) LB parameterList RB stmt_Block;
parameterList: (ID (COMMA ID)* COLON mptype (SEMI ID (COMMA ID)* COLON mptype)*)?;
//lhs
expression_index: (ID|instanceAttr|staticAttr) index_operator;
index_operator: LSB expr? RSB index_operator|;
//
scalar: instanceCreate|ID|SELF|staticAttr|staticMethod|NULL|LB listOfexpr RB|literal;
instanceCreate: NEW ID LB listOfexpr RB;
instanceAttr: exprInstanceAttr DOT ID;
//instanceAttr: instanceAttr DOT ID | scalar ;
//instanceMethod: instanceAttr DOT ID LB listOfexpr RB (DOT ID (LB listOfexpr RB)?)*  ;
exprInstanceAttr: exprInstanceAttr DOT ID (LB listOfexpr RB)? | scalar;
instanceMethod: expr8 DOT ID LB listOfexpr RB;
//
staticAttr: ID DOUBLE_COLON STATIC_ID;
staticMethod: ID DOUBLE_COLON STATIC_ID LB listOfexpr RB;
//
lhs: ID|instanceAttr|staticAttr|expression_index;
// All Statement
stmt: (stmt_Assignment|stmt_If|stmt_MethodInvocation|stmt_Break|stmt_Continue|stmt_Return|stmt_ForIn);
stmt_List:(stmt|variableDecl_func|stmt_Block)stmt_List|;
stmt_Block: LCB stmt_List RCB;
// Statements
stmt_Assignment: lhs ASSIGN expr SEMI; // Assignment Statement
stmt_If: IF LB expr RB stmt_Block (ELSEIF LB expr RB stmt_Block)* (ELSE stmt_Block)?; //If Else Statement
stmt_Break: BREAK SEMI; // Break statement
stmt_Continue: CONTINUE SEMI; // Continue Statement
stmt_Return: RETURN expr? SEMI; // Return Statement
stmt_MethodInvocation: (instanceMethod|staticMethod) SEMI;
stmt_ForIn: FOREACH LB expr IN expr DOUBLE_DOT expr (BY expr)? RB stmt_Block;
//2. Lexical Structures
//Types
typeDataPrimitive:INT | FLOAT | BOOLEAN | STR | arrayType;
mptype: INT | FLOAT | STR | BOOLEAN | arrayType | ID;
literal: INT_NUM | FLOAT_NUM | STRING | BOOL_NUM | arrayLit ;
BOOL_NUM: TRUE | FALSE;
size : {self.checkZero(self.getCurrentToken().text)!=1}? INT_NUM;
//Operators group
relational_op: LESS_THAN|LARGER_THAN|LESS_THAN_OR_EQUAL|LARGER_THAN_OR_EQUAL|DIFFRENCE|EQUAL;

// Keywords
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
ARRAY: 'Array';
IN: 'In';
INT:'Int';
FLOAT:'Float';
BOOLEAN:'Boolean';
STR: 'String';
NULL: 'Null';
RETURN: 'Return';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';
SELF: 'Self';
TRUE: 'True';
FALSE: 'False';

// Operators
ADD: '+';
MINUS: '-';
MULTIPLY: '*';
DEVIDE: '/';
MODULO: '%';
NOT: '!';
ASSIGN: '=';
AND:'&&';
OR:'||';
LESS_THAN: '<';
LARGER_THAN : '>';
LESS_THAN_OR_EQUAL: '<=';
LARGER_THAN_OR_EQUAL: '>=';
EQUAL: '==';
DIFFRENCE: '!=';
STR_CMP: '==.';
STR_CONCAT: '+.';
DOUBLE_COLON: '::';
fragment STATIC: '$';

//Separators
fragment DOUBLEQUOTE: '"';
SEMI: ';';
COMMA: ',';
COLON: ':';
DOT: '.';
LB: '('; // bracket open
RB: ')'; // bracket close
LSB: '['; // square bracket open
RSB: ']'; // square bracket close
LCB: '{'; // curly bracket open
RCB: '}'; // curly bracket close
DOUBLE_DOT:'..';
// Integer
fragment INT_BIN: '0'[bB]('0'|[1]('_'?[01])*);
fragment INT_DEC: '0'|[1-9]('_'?[0-9])*;
fragment INT_HEX: '0'[xX]('0'| [1-9A-F]('_'?[0-9A-F])*);
fragment INT_OCT: '0'('0'|[1-7]('_'?[0-7])*);
INT_NUM: (INT_BIN | INT_OCT| INT_DEC | INT_HEX) {self.text = self.text.replace("_","")};

//fragment INT_BIN: '0'[bB]([1]('_'?[01])*);
//fragment INT_DEC: [1-9]('_'?[0-9])*;
//fragment INT_HEX: '0'[xX]([1-9A-F]('_'?[0-9A-F])*);
//fragment INT_OCT: '0'([1-7]('_'?[0-7])*);
//INT_NUM: (INT_BIN | INT_OCT| INT_DEC | INT_HEX) {self.text = self.text.replace("_","")};
// Float
fragment INT_PART:  [0-9]|[1-9][0-9_]*[0-9]; //[0-9]('_'?[0-9])*;
fragment FLOAT_EXP: [eE][+-]?[0-9]+ ;
fragment FLOAT_DEC: '.' [0-9]*; //-10.25, -10e25, 10E25, 10.25e03
FLOAT_NUM: (INT_PART (FLOAT_DEC | FLOAT_EXP | FLOAT_DEC FLOAT_EXP)|FLOAT_DEC FLOAT_EXP){self.text = self.text.replace("_","")};
// String
// http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=154633 -> ' can use as a normal character
fragment QUOTE_IN_STR: '\'"';
fragment ESC_SEQ: '\\'[bfrnt'\\];
fragment CHAR_STRING: ESC_SEQ | ~[\b\f\r\t\n"\\] | QUOTE_IN_STR; //~[\b\f\n\r\t"\\]
STRING: DOUBLEQUOTE CHAR_STRING* DOUBLEQUOTE{self.text=self.text[1:-1]};
fragment ESCAPE_ILLEGAL: '\\' ~[btnfr'\\];

// Comments
fragment LEGAL_COMMENT_STRING: .;
fragment COMMENT_SIGN: '##';
COMMENT: COMMENT_SIGN LEGAL_COMMENT_STRING*? COMMENT_SIGN -> skip;
WS: [ \t\r\n\b\f]+ -> skip; // skip spaces, tabs, newlines

//Identifier
ID: [a-zA-Z_][a-zA-Z0-9_]*;
STATIC_ID: STATIC [_a-zA-Z0-9]+;
//Lexer Erorr

UNCLOSE_STRING: DOUBLEQUOTE CHAR_STRING*
    {
        raise UncloseString(self.text[1:])
    };
ERROR_CHAR:.
    {
        raise ErrorToken(self.text)
    };
ILLEGAL_ESCAPE: DOUBLEQUOTE CHAR_STRING* ESCAPE_ILLEGAL
    {
        raise IllegalEscape(self.text[1:])
    };