# Generated from D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete listener for a parse tree produced by D96Parser.
class D96Listener(ParseTreeListener):

    # Enter a parse tree produced by D96Parser#program.
    def enterProgram(self, ctx:D96Parser.ProgramContext):
        pass

    # Exit a parse tree produced by D96Parser#program.
    def exitProgram(self, ctx:D96Parser.ProgramContext):
        pass


    # Enter a parse tree produced by D96Parser#classProgram.
    def enterClassProgram(self, ctx:D96Parser.ClassProgramContext):
        pass

    # Exit a parse tree produced by D96Parser#classProgram.
    def exitClassProgram(self, ctx:D96Parser.ClassProgramContext):
        pass


    # Enter a parse tree produced by D96Parser#main_func.
    def enterMain_func(self, ctx:D96Parser.Main_funcContext):
        pass

    # Exit a parse tree produced by D96Parser#main_func.
    def exitMain_func(self, ctx:D96Parser.Main_funcContext):
        pass


    # Enter a parse tree produced by D96Parser#classDecl.
    def enterClassDecl(self, ctx:D96Parser.ClassDeclContext):
        pass

    # Exit a parse tree produced by D96Parser#classDecl.
    def exitClassDecl(self, ctx:D96Parser.ClassDeclContext):
        pass


    # Enter a parse tree produced by D96Parser#classBody.
    def enterClassBody(self, ctx:D96Parser.ClassBodyContext):
        pass

    # Exit a parse tree produced by D96Parser#classBody.
    def exitClassBody(self, ctx:D96Parser.ClassBodyContext):
        pass


    # Enter a parse tree produced by D96Parser#classInstanceCreate.
    def enterClassInstanceCreate(self, ctx:D96Parser.ClassInstanceCreateContext):
        pass

    # Exit a parse tree produced by D96Parser#classInstanceCreate.
    def exitClassInstanceCreate(self, ctx:D96Parser.ClassInstanceCreateContext):
        pass


    # Enter a parse tree produced by D96Parser#classInstance.
    def enterClassInstance(self, ctx:D96Parser.ClassInstanceContext):
        pass

    # Exit a parse tree produced by D96Parser#classInstance.
    def exitClassInstance(self, ctx:D96Parser.ClassInstanceContext):
        pass


    # Enter a parse tree produced by D96Parser#listOfexpr.
    def enterListOfexpr(self, ctx:D96Parser.ListOfexprContext):
        pass

    # Exit a parse tree produced by D96Parser#listOfexpr.
    def exitListOfexpr(self, ctx:D96Parser.ListOfexprContext):
        pass


    # Enter a parse tree produced by D96Parser#classInstanceAttrAccess.
    def enterClassInstanceAttrAccess(self, ctx:D96Parser.ClassInstanceAttrAccessContext):
        pass

    # Exit a parse tree produced by D96Parser#classInstanceAttrAccess.
    def exitClassInstanceAttrAccess(self, ctx:D96Parser.ClassInstanceAttrAccessContext):
        pass


    # Enter a parse tree produced by D96Parser#instanceInvocation.
    def enterInstanceInvocation(self, ctx:D96Parser.InstanceInvocationContext):
        pass

    # Exit a parse tree produced by D96Parser#instanceInvocation.
    def exitInstanceInvocation(self, ctx:D96Parser.InstanceInvocationContext):
        pass


    # Enter a parse tree produced by D96Parser#staticInvocation.
    def enterStaticInvocation(self, ctx:D96Parser.StaticInvocationContext):
        pass

    # Exit a parse tree produced by D96Parser#staticInvocation.
    def exitStaticInvocation(self, ctx:D96Parser.StaticInvocationContext):
        pass


    # Enter a parse tree produced by D96Parser#constructorDecl.
    def enterConstructorDecl(self, ctx:D96Parser.ConstructorDeclContext):
        pass

    # Exit a parse tree produced by D96Parser#constructorDecl.
    def exitConstructorDecl(self, ctx:D96Parser.ConstructorDeclContext):
        pass


    # Enter a parse tree produced by D96Parser#destructorDecl.
    def enterDestructorDecl(self, ctx:D96Parser.DestructorDeclContext):
        pass

    # Exit a parse tree produced by D96Parser#destructorDecl.
    def exitDestructorDecl(self, ctx:D96Parser.DestructorDeclContext):
        pass


    # Enter a parse tree produced by D96Parser#variableList.
    def enterVariableList(self, ctx:D96Parser.VariableListContext):
        pass

    # Exit a parse tree produced by D96Parser#variableList.
    def exitVariableList(self, ctx:D96Parser.VariableListContext):
        pass


    # Enter a parse tree produced by D96Parser#callVariable.
    def enterCallVariable(self, ctx:D96Parser.CallVariableContext):
        pass

    # Exit a parse tree produced by D96Parser#callVariable.
    def exitCallVariable(self, ctx:D96Parser.CallVariableContext):
        pass


    # Enter a parse tree produced by D96Parser#parameterList.
    def enterParameterList(self, ctx:D96Parser.ParameterListContext):
        pass

    # Exit a parse tree produced by D96Parser#parameterList.
    def exitParameterList(self, ctx:D96Parser.ParameterListContext):
        pass


    # Enter a parse tree produced by D96Parser#methodDecl.
    def enterMethodDecl(self, ctx:D96Parser.MethodDeclContext):
        pass

    # Exit a parse tree produced by D96Parser#methodDecl.
    def exitMethodDecl(self, ctx:D96Parser.MethodDeclContext):
        pass


    # Enter a parse tree produced by D96Parser#methodStruct.
    def enterMethodStruct(self, ctx:D96Parser.MethodStructContext):
        pass

    # Exit a parse tree produced by D96Parser#methodStruct.
    def exitMethodStruct(self, ctx:D96Parser.MethodStructContext):
        pass


    # Enter a parse tree produced by D96Parser#callMethod.
    def enterCallMethod(self, ctx:D96Parser.CallMethodContext):
        pass

    # Exit a parse tree produced by D96Parser#callMethod.
    def exitCallMethod(self, ctx:D96Parser.CallMethodContext):
        pass


    # Enter a parse tree produced by D96Parser#arrayLit.
    def enterArrayLit(self, ctx:D96Parser.ArrayLitContext):
        pass

    # Exit a parse tree produced by D96Parser#arrayLit.
    def exitArrayLit(self, ctx:D96Parser.ArrayLitContext):
        pass


    # Enter a parse tree produced by D96Parser#callArrayIndex.
    def enterCallArrayIndex(self, ctx:D96Parser.CallArrayIndexContext):
        pass

    # Exit a parse tree produced by D96Parser#callArrayIndex.
    def exitCallArrayIndex(self, ctx:D96Parser.CallArrayIndexContext):
        pass


    # Enter a parse tree produced by D96Parser#arrayType.
    def enterArrayType(self, ctx:D96Parser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by D96Parser#arrayType.
    def exitArrayType(self, ctx:D96Parser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by D96Parser#arrayDecl.
    def enterArrayDecl(self, ctx:D96Parser.ArrayDeclContext):
        pass

    # Exit a parse tree produced by D96Parser#arrayDecl.
    def exitArrayDecl(self, ctx:D96Parser.ArrayDeclContext):
        pass


    # Enter a parse tree produced by D96Parser#expr.
    def enterExpr(self, ctx:D96Parser.ExprContext):
        pass

    # Exit a parse tree produced by D96Parser#expr.
    def exitExpr(self, ctx:D96Parser.ExprContext):
        pass


    # Enter a parse tree produced by D96Parser#expr0.
    def enterExpr0(self, ctx:D96Parser.Expr0Context):
        pass

    # Exit a parse tree produced by D96Parser#expr0.
    def exitExpr0(self, ctx:D96Parser.Expr0Context):
        pass


    # Enter a parse tree produced by D96Parser#expr1.
    def enterExpr1(self, ctx:D96Parser.Expr1Context):
        pass

    # Exit a parse tree produced by D96Parser#expr1.
    def exitExpr1(self, ctx:D96Parser.Expr1Context):
        pass


    # Enter a parse tree produced by D96Parser#expr2.
    def enterExpr2(self, ctx:D96Parser.Expr2Context):
        pass

    # Exit a parse tree produced by D96Parser#expr2.
    def exitExpr2(self, ctx:D96Parser.Expr2Context):
        pass


    # Enter a parse tree produced by D96Parser#expr3.
    def enterExpr3(self, ctx:D96Parser.Expr3Context):
        pass

    # Exit a parse tree produced by D96Parser#expr3.
    def exitExpr3(self, ctx:D96Parser.Expr3Context):
        pass


    # Enter a parse tree produced by D96Parser#expr4.
    def enterExpr4(self, ctx:D96Parser.Expr4Context):
        pass

    # Exit a parse tree produced by D96Parser#expr4.
    def exitExpr4(self, ctx:D96Parser.Expr4Context):
        pass


    # Enter a parse tree produced by D96Parser#expr5.
    def enterExpr5(self, ctx:D96Parser.Expr5Context):
        pass

    # Exit a parse tree produced by D96Parser#expr5.
    def exitExpr5(self, ctx:D96Parser.Expr5Context):
        pass


    # Enter a parse tree produced by D96Parser#expr6.
    def enterExpr6(self, ctx:D96Parser.Expr6Context):
        pass

    # Exit a parse tree produced by D96Parser#expr6.
    def exitExpr6(self, ctx:D96Parser.Expr6Context):
        pass


    # Enter a parse tree produced by D96Parser#expr7.
    def enterExpr7(self, ctx:D96Parser.Expr7Context):
        pass

    # Exit a parse tree produced by D96Parser#expr7.
    def exitExpr7(self, ctx:D96Parser.Expr7Context):
        pass


    # Enter a parse tree produced by D96Parser#expr8.
    def enterExpr8(self, ctx:D96Parser.Expr8Context):
        pass

    # Exit a parse tree produced by D96Parser#expr8.
    def exitExpr8(self, ctx:D96Parser.Expr8Context):
        pass


    # Enter a parse tree produced by D96Parser#expr9.
    def enterExpr9(self, ctx:D96Parser.Expr9Context):
        pass

    # Exit a parse tree produced by D96Parser#expr9.
    def exitExpr9(self, ctx:D96Parser.Expr9Context):
        pass


    # Enter a parse tree produced by D96Parser#expr10.
    def enterExpr10(self, ctx:D96Parser.Expr10Context):
        pass

    # Exit a parse tree produced by D96Parser#expr10.
    def exitExpr10(self, ctx:D96Parser.Expr10Context):
        pass


    # Enter a parse tree produced by D96Parser#variableDecl.
    def enterVariableDecl(self, ctx:D96Parser.VariableDeclContext):
        pass

    # Exit a parse tree produced by D96Parser#variableDecl.
    def exitVariableDecl(self, ctx:D96Parser.VariableDeclContext):
        pass


    # Enter a parse tree produced by D96Parser#mptype.
    def enterMptype(self, ctx:D96Parser.MptypeContext):
        pass

    # Exit a parse tree produced by D96Parser#mptype.
    def exitMptype(self, ctx:D96Parser.MptypeContext):
        pass


    # Enter a parse tree produced by D96Parser#literal.
    def enterLiteral(self, ctx:D96Parser.LiteralContext):
        pass

    # Exit a parse tree produced by D96Parser#literal.
    def exitLiteral(self, ctx:D96Parser.LiteralContext):
        pass


    # Enter a parse tree produced by D96Parser#arithmetic_op.
    def enterArithmetic_op(self, ctx:D96Parser.Arithmetic_opContext):
        pass

    # Exit a parse tree produced by D96Parser#arithmetic_op.
    def exitArithmetic_op(self, ctx:D96Parser.Arithmetic_opContext):
        pass


    # Enter a parse tree produced by D96Parser#boolean_op.
    def enterBoolean_op(self, ctx:D96Parser.Boolean_opContext):
        pass

    # Exit a parse tree produced by D96Parser#boolean_op.
    def exitBoolean_op(self, ctx:D96Parser.Boolean_opContext):
        pass


    # Enter a parse tree produced by D96Parser#string_op.
    def enterString_op(self, ctx:D96Parser.String_opContext):
        pass

    # Exit a parse tree produced by D96Parser#string_op.
    def exitString_op(self, ctx:D96Parser.String_opContext):
        pass


    # Enter a parse tree produced by D96Parser#relational_op.
    def enterRelational_op(self, ctx:D96Parser.Relational_opContext):
        pass

    # Exit a parse tree produced by D96Parser#relational_op.
    def exitRelational_op(self, ctx:D96Parser.Relational_opContext):
        pass


    # Enter a parse tree produced by D96Parser#index_op.
    def enterIndex_op(self, ctx:D96Parser.Index_opContext):
        pass

    # Exit a parse tree produced by D96Parser#index_op.
    def exitIndex_op(self, ctx:D96Parser.Index_opContext):
        pass


    # Enter a parse tree produced by D96Parser#element_expression.
    def enterElement_expression(self, ctx:D96Parser.Element_expressionContext):
        pass

    # Exit a parse tree produced by D96Parser#element_expression.
    def exitElement_expression(self, ctx:D96Parser.Element_expressionContext):
        pass



del D96Parser