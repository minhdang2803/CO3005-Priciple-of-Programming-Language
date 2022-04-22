# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr0.
    def visitExpr0(self, ctx:D96Parser.Expr0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx:D96Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx:D96Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx:D96Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx:D96Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx:D96Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx:D96Parser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx:D96Parser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr11.
    def visitExpr11(self, ctx:D96Parser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#listOfexpr.
    def visitListOfexpr(self, ctx:D96Parser.ListOfexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#manyExpr.
    def visitManyExpr(self, ctx:D96Parser.ManyExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variableDecl.
    def visitVariableDecl(self, ctx:D96Parser.VariableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#withASM.
    def visitWithASM(self, ctx:D96Parser.WithASMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#pair.
    def visitPair(self, ctx:D96Parser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#withoutASM.
    def visitWithoutASM(self, ctx:D96Parser.WithoutASMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#manyVariable.
    def visitManyVariable(self, ctx:D96Parser.ManyVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variableDecl_func.
    def visitVariableDecl_func(self, ctx:D96Parser.VariableDecl_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#withASM2.
    def visitWithASM2(self, ctx:D96Parser.WithASM2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#pair2.
    def visitPair2(self, ctx:D96Parser.Pair2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#withoutASM2.
    def visitWithoutASM2(self, ctx:D96Parser.WithoutASM2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#manyVariable2.
    def visitManyVariable2(self, ctx:D96Parser.ManyVariable2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayLit.
    def visitArrayLit(self, ctx:D96Parser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayAssignMember.
    def visitArrayAssignMember(self, ctx:D96Parser.ArrayAssignMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayMemberList.
    def visitArrayMemberList(self, ctx:D96Parser.ArrayMemberListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayType.
    def visitArrayType(self, ctx:D96Parser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classDecl.
    def visitClassDecl(self, ctx:D96Parser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classMember.
    def visitClassMember(self, ctx:D96Parser.ClassMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructorDecl.
    def visitConstructorDecl(self, ctx:D96Parser.ConstructorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructorDecl.
    def visitDestructorDecl(self, ctx:D96Parser.DestructorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methodDecl.
    def visitMethodDecl(self, ctx:D96Parser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameterList.
    def visitParameterList(self, ctx:D96Parser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#manyID.
    def visitManyID(self, ctx:D96Parser.ManyIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#manyParam.
    def visitManyParam(self, ctx:D96Parser.ManyParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression_index.
    def visitExpression_index(self, ctx:D96Parser.Expression_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operator.
    def visitIndex_operator(self, ctx:D96Parser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar.
    def visitScalar(self, ctx:D96Parser.ScalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instanceCreate.
    def visitInstanceCreate(self, ctx:D96Parser.InstanceCreateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instanceAttr.
    def visitInstanceAttr(self, ctx:D96Parser.InstanceAttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exprInstanceAttr.
    def visitExprInstanceAttr(self, ctx:D96Parser.ExprInstanceAttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instanceMethod.
    def visitInstanceMethod(self, ctx:D96Parser.InstanceMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#staticAttr.
    def visitStaticAttr(self, ctx:D96Parser.StaticAttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#staticMethod.
    def visitStaticMethod(self, ctx:D96Parser.StaticMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_List.
    def visitStmt_List(self, ctx:D96Parser.Stmt_ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_Block.
    def visitStmt_Block(self, ctx:D96Parser.Stmt_BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_Assignment.
    def visitStmt_Assignment(self, ctx:D96Parser.Stmt_AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_If.
    def visitStmt_If(self, ctx:D96Parser.Stmt_IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_Break.
    def visitStmt_Break(self, ctx:D96Parser.Stmt_BreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_Continue.
    def visitStmt_Continue(self, ctx:D96Parser.Stmt_ContinueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_Return.
    def visitStmt_Return(self, ctx:D96Parser.Stmt_ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_MethodInvocation.
    def visitStmt_MethodInvocation(self, ctx:D96Parser.Stmt_MethodInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_ForIn.
    def visitStmt_ForIn(self, ctx:D96Parser.Stmt_ForInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typeDataPrimitive.
    def visitTypeDataPrimitive(self, ctx:D96Parser.TypeDataPrimitiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mptype.
    def visitMptype(self, ctx:D96Parser.MptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#size.
    def visitSize(self, ctx:D96Parser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relational_op.
    def visitRelational_op(self, ctx:D96Parser.Relational_opContext):
        return self.visitChildren(ctx)



del D96Parser