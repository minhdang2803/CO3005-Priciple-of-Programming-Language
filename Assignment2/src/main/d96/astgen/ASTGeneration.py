from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        result = []
        for element in ctx.classDecl():
            result.append(self.visit(element))
        return Program(result)

    def visitClassDecl(self, ctx: D96Parser.ClassDeclContext):
        length = len(ctx.ID())
        if length == 1:
            ids = Id(ctx.ID()[0].getText())
            parent = None
        else:
            ids = Id(ctx.ID()[0].getText())
            parent = Id(ctx.ID()[1].getText())
        members = self.visit(ctx.classMember())
        return ClassDecl(ids, members, parent)

    def visitClassMember(self, ctx: D96Parser.ClassMemberContext):
        result = []
        for element in range(ctx.getChildCount()):
            if ctx.constructorDecl() or ctx.methodDecl() or ctx.variableDecl() or ctx.destructorDecl():
                result = result + self.visit(ctx.getChild(element))
        return result

    def visitVariableDecl(self, ctx: D96Parser.VariableDeclContext):
        attr_list = []
        if ctx.withoutASM():
            attr_type, kind, idlist, value = self.visit(ctx.withoutASM())
            complete_decl = zip(kind, idlist, value)
            for get_kind, get_id, get_value in complete_decl:
                if ctx.VAR():
                    if isinstance(attr_type, ClassType):
                        attr_list += [AttributeDecl(get_kind, VarDecl(get_id, attr_type, NullLiteral()))]
                    else:
                        attr_list += [AttributeDecl(get_kind, VarDecl(get_id, attr_type, get_value))]
                elif ctx.VAL():
                    attr_list += [AttributeDecl(get_kind, ConstDecl(get_id, attr_type, get_value))]
        elif ctx.withASM():
            attr_type, kind, idlist, value = self.visit(ctx.withASM())
            complete_decl = zip(kind, idlist, value)
            for get_kind, get_id, get_value in complete_decl:
                if ctx.VAR():
                    attr_list += [AttributeDecl(get_kind, VarDecl(get_id, attr_type, get_value))]
                elif ctx.VAL():
                    attr_list += [AttributeDecl(get_kind, ConstDecl(get_id, attr_type, get_value))]
        return attr_list

    def visitWithASM(self, ctx: D96Parser.WithASMContext):
        kind, idlist, attr_type, value = self.visit(ctx.pair())
        if ctx.ID():
            idlist = [Id(ctx.ID().getText())] + idlist
            kind = [Instance()] + kind
        elif ctx.STATIC_ID():
            idlist = [Id(ctx.STATIC_ID().getText())] + idlist
            kind = [Static()] + kind
        last_value = self.visit(ctx.expr())
        value = value[::-1]
        value += [last_value]
        return attr_type, kind, idlist, value

    def visitPair(self, ctx: D96Parser.PairContext):
        if ctx.mptype():
            return [], [], self.visit(ctx.mptype()), []
        else:
            if ctx.ID():
                first_element = [Id(ctx.ID().getText())]
                first_kind = [Instance()]
                first_value = [self.visit(ctx.expr())]
                kind, element, attr_type, value = self.visit(ctx.pair())
                return first_kind + kind, first_element + element, attr_type, first_value + value
            elif ctx.STATIC_ID():
                first_element = [Id(ctx.STATIC_ID().getText())]
                first_kind = [Static()]
                first_value = [self.visit(ctx.expr())]
                kind, element, attr_type, value = self.visit(ctx.pair())
                return first_kind + kind, first_element + element, attr_type, first_value + value

    def visitWithoutASM(self, ctx: D96Parser.WithoutASMContext):
        # [a,$b,$c] -> [Instace, Static, Static]
        attr_type = self.visit(ctx.mptype())
        kind, idlist, value = self.visit(ctx.manyVariable())
        return attr_type, kind, idlist, value

    def visitManyVariable(self, ctx: D96Parser.ManyVariableContext):
        if ctx.getChildCount() == 1:
            if ctx.ID():
                return [Instance()], [Id(ctx.ID().getText())], [None]
            elif ctx.STATIC_ID():
                return [Static()], [Id(ctx.STATIC_ID().getText())], [None]
        else:
            if ctx.ID():
                first_kind = [Instance()]
                first_element = [Id(ctx.ID().getText())]
                kind, idlist, value = self.visit(ctx.manyVariable())
                return first_kind + kind, first_element + idlist, [None] + value
            elif ctx.STATIC_ID():
                first_kind = [Static()]
                first_element = [Id(ctx.STATIC_ID().getText())]
                kind, idlist, value = self.visit(ctx.manyVariable())
                return first_kind + kind, first_element + idlist, [None] + value

    def visitVariableDecl_func(self, ctx: D96Parser.VariableDecl_funcContext):
        attr_list = []
        if ctx.withoutASM2():
            attr_type, idlist, value = self.visit(ctx.withoutASM2())
            complete_decl = zip(idlist, value)
            for get_id, get_value in complete_decl:
                if ctx.VAR():
                    if isinstance(attr_type, ClassType):
                        attr_list += [VarDecl(get_id, attr_type, NullLiteral())]
                    else:
                        attr_list += [VarDecl(get_id, attr_type, get_value)]
                elif ctx.VAL():
                    attr_list += [ConstDecl(get_id, attr_type, get_value)]
        elif ctx.withASM2():
            attr_type, idlist, value = self.visit(ctx.withASM2())
            complete_decl = zip(idlist, value)
            for get_id, get_value in complete_decl:
                if ctx.VAR():
                    attr_list += [VarDecl(get_id, attr_type, get_value)]
                elif ctx.VAL():
                    attr_list += [ConstDecl(get_id, attr_type, get_value)]
        return attr_list

    def visitWithASM2(self, ctx: D96Parser.WithASM2Context):
        idlist, attr_type, value = self.visit(ctx.pair2())
        idlist = [Id(ctx.ID().getText())] + idlist
        last_value = self.visit(ctx.expr())
        value = value[::-1]
        value += [last_value]
        return attr_type, idlist, value

    def visitPair2(self, ctx: D96Parser.Pair2Context):
        if ctx.mptype():
            return [], self.visit(ctx.mptype()), []
        else:
            first_element = [Id(ctx.ID().getText())]
            first_value = [self.visit(ctx.expr())]
            element, attr_type, value = self.visit(ctx.pair2())
            return first_element + element, attr_type, first_value + value

    def visitWithoutASM2(self, ctx: D96Parser.WithoutASM2Context):
        attr_type = self.visit(ctx.mptype())
        idlist, value = self.visit(ctx.manyVariable2())
        return attr_type, idlist, value

    def visitManyVariable2(self, ctx: D96Parser.ManyVariable2Context):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())], [None]
        else:
            first_element = [Id(ctx.ID().getText())]
            idlist, value = self.visit(ctx.manyVariable2())
            return first_element + idlist, [None] + value

    # expression
    def visitExpr(self, ctx: D96Parser.ExprContext):
        return self.visit(ctx.expr0())

    def visitExpr0(self, ctx: D96Parser.Expr0Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1()[0])
        else:
            left = self.visit(ctx.expr1()[0])
            right = self.visit(ctx.expr1()[1])
            op = None
            if ctx.STR_CMP():
                op = ctx.STR_CMP().getText()
            elif ctx.STR_CONCAT():
                op = ctx.STR_CONCAT().getText()
            return BinaryOp(op, left, right)

    def visitExpr1(self, ctx: D96Parser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2()[0])
        else:
            left = self.visit(ctx.expr2()[0])
            right = self.visit(ctx.expr2()[1])
            op = self.visit(ctx.relational_op())
            return BinaryOp(op, left, right)

    def visitExpr2(self, ctx: D96Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        else:
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            op = ctx.OR().getText() if ctx.OR() else ctx.AND().getText()
            return BinaryOp(op, left, right)

    def visitExpr3(self, ctx: D96Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        else:
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            op = None
            if ctx.ADD():
                op = ctx.ADD().getText()
            elif ctx.MINUS():
                op = ctx.MINUS().getText()
            return BinaryOp(op, left, right)

    def visitExpr4(self, ctx: D96Parser.Expr4Context):
        ctx.getChildCount()
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        else:
            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())
            op = None
            if ctx.MULTIPLY():
                op = ctx.MULTIPLY().getText()
            elif ctx.DEVIDE():
                op = ctx.DEVIDE().getText()
            elif ctx.MODULO():
                op = ctx.MODULO().getText()
            return BinaryOp(op, left, right)

    def visitExpr5(self, ctx: D96Parser.Expr5Context):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())

    def visitExpr6(self, ctx: D96Parser.Expr6Context):
        if ctx.MINUS():
            return UnaryOp(str(ctx.MINUS().getText()), self.visit(ctx.expr6()))
        return self.visit(ctx.expr7())

    def visitExpr7(self, ctx: D96Parser.Expr7Context):
        if ctx.index_operator():
            arr = self.visit(ctx.expr7())
            idx = self.visit(ctx.index_operator())
            return ArrayCell(arr, idx)
        return self.visit(ctx.expr8())

    def visitExpr8(self, ctx: D96Parser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr9())
        else:
            if ctx.listOfexpr():
                obj = self.visit(ctx.expr8())
                method = Id(ctx.ID().getText())
                param = self.visit(ctx.listOfexpr())
                return CallExpr(obj, method, param)
            else:
                obj = self.visit(ctx.expr8())
                field_name = Id(ctx.ID().getText())
                return FieldAccess(obj, field_name)

    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr10())
        else:
            if ctx.listOfexpr():
                obj = Id(ctx.ID().getText())
                method = Id(ctx.STATIC_ID().getText())
                param = self.visit(ctx.listOfexpr())
                return CallExpr(obj, method, param)
            else:
                obj = Id(ctx.ID().getText())
                field_name = Id(ctx.STATIC_ID().getText())
                return FieldAccess(obj, field_name)

    def visitExpr10(self, ctx: D96Parser.Expr10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr11())
        else:
            class_name = self.visit(ctx.expr10())
            param = self.visit(ctx.listOfexpr())
            return NewExpr(class_name, param)

    def visitExpr11(self, ctx: D96Parser.Expr11Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operand())
        else:
            return self.visit(ctx.expr())

    def visitOperand(self, ctx: D96Parser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.literal():
            return self.visit(ctx.literal())
        else:
            return NullLiteral()

    def visitConstructorDecl(self, ctx: D96Parser.ConstructorDeclContext):
        param = self.visit(ctx.parameterList())
        body = self.visit(ctx.stmt_block())
        return [MethodDecl(Instance(), Id('Constructor'), param, body)]

    def visitDestructorDecl(self, ctx: D96Parser.DestructorDeclContext):
        param = []
        body = self.visit(ctx.stmt_block())
        return [MethodDecl(Instance(), Id('Destructor'), param, body)]

    def visitMethodDecl(self, ctx: D96Parser.MethodDeclContext):
        param = self.visit(ctx.parameterList())
        stmts = self.visit(ctx.stmt_block())
        kind = None
        name = None
        if ctx.ID():
            name = Id(ctx.ID().getText())
            kind = Instance()
        elif ctx.STATIC_ID():
            name = Id(ctx.STATIC_ID().getText())
            kind = Static()
        if not ctx.STATIC_ID() and ctx.ID().getText() == 'main':
            class_body = ctx.parentCtx
            class_decl = class_body.parentCtx
            class_name = class_decl.ID(0).getText()
            if class_name == 'Program':
                if len(param) == 0:
                    kind = Static()
                    name = Id(ctx.ID().getText())
                    return [MethodDecl(kind, name, param, stmts)]
        return [MethodDecl(kind, name, param, stmts)]

    def visitStmt_MethodInvocation(self, ctx: D96Parser.Stmt_MethodInvocationContext):
        if ctx.staticMethod():
            return self.visit(ctx.staticMethod())
        else:
            return self.visit(ctx.instanceMethod())

    def visitStmt_Assignment(self, ctx: D96Parser.Stmt_AssignmentContext):
        lhs = self.visit(ctx.lhs())
        expr = self.visit(ctx.expr())
        return Assign(lhs, expr)

    def visitLhs(self, ctx: D96Parser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.instanceAttr():
            return self.visit(ctx.instanceAttr())
        elif ctx.staticAttr():
            return self.visit(ctx.staticAttr())
        else:
            return self.visit(ctx.expression_index())

    def visitExpression_index(self, ctx: D96Parser.Expression_indexContext):
        obj = None
        if ctx.ID():
            obj = Id(ctx.ID().getText())
        elif ctx.instanceAttr():
            obj = self.visit(ctx.instanceAttr())
        elif ctx.staticAttr():
            obj = self.visit(ctx.staticAttr())
        elif ctx.instanceCreate():
            obj = self.visit(ctx.instanceCreate())
        elif ctx.NULL():
            obj = NullLiteral()
        elif ctx.literal():
            obj = self.visit(ctx.literal())
        elif ctx.SELF():
            obj = SelfLiteral()
        elif ctx.stmStaticMethod():
            obj = self.visit(ctx.stmStaticMethod())
        elif ctx.stmInstanceMethod():
            obj = self.visit(ctx.stmInstanceMethod())
        else:
            obj = self.visit(ctx.expr())
        index_operator = self.visit(ctx.index_operator())
        return ArrayCell(obj, index_operator)

    def visitInstanceAttr(self, ctx: D96Parser.InstanceAttrContext):
            obj = self.visit(ctx.exprInstanceAttr())
            field_name = Id(ctx.ID().getText())
            return FieldAccess(obj, field_name)

    def visitExprInstanceAttr(self, ctx: D96Parser.ExprInstanceAttrContext):
        a= ctx.getText()
        if ctx.getChildCount() == 1:
            return self.visit(ctx.scalar())
        else:
            if ctx.listOfexpr():
                obj = self.visit(ctx.exprInstanceAttr())
                method = Id(ctx.ID().getText())
                param = self.visit(ctx.listOfexpr())
                return CallExpr(obj, method, param)
            else:
                obj = self.visit(ctx.exprInstanceAttr())
                field_name = Id(ctx.ID().getText())
                return FieldAccess(obj, field_name)

    def visitScalar(self, ctx: D96Parser.ScalarContext):
        if ctx.instanceCreate():
            return self.visit(ctx.instanceCreate())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.staticAttr():
            return self.visit(ctx.staticAttr())
        elif ctx.stmStaticMethod():
            return self.visit(ctx.stmStaticMethod())
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.literal():
            return self.visit(ctx.literal())

    def visitInstanceCreate(self, ctx: D96Parser.InstanceCreateContext):
        class_name = Id(ctx.ID().getText())
        param = self.visit(ctx.listOfexpr())
        return NewExpr(class_name, param)

    def visitInstanceMethod(self, ctx: D96Parser.InstanceMethodContext):
        obj = self.visit(ctx.exprInstanceAttr())
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.listOfexpr())
        return CallStmt(obj, method, param)

    def visitStaticMethod(self, ctx: D96Parser.StaticMethodContext):
        obj = Id(ctx.ID().getText())
        method = Id(ctx.STATIC_ID().getText())
        param = self.visit(ctx.listOfexpr())
        return CallStmt(obj, method, param)

    def visitStmStaticMethod(self, ctx:D96Parser.StmStaticMethodContext):
        obj = Id(ctx.ID().getText())
        method = Id(ctx.STATIC_ID().getText())
        param = self.visit(ctx.listOfexpr())
        return CallExpr(obj, method, param)

    def visitStmInstanceMethod(self, ctx:D96Parser.StmInstanceMethodContext):
        obj = self.visit(ctx.exprInstanceAttr())
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.listOfexpr())
        return CallExpr(obj, method, param)

    def visitStaticAttr(self, ctx: D96Parser.StaticAttrContext):
        obj = Id(ctx.ID().getText())
        field_name = Id(ctx.STATIC_ID().getText())
        return FieldAccess(obj, field_name)

    def visitStmt_ForIn(self, ctx: D96Parser.Stmt_ForInContext):
        element = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr(1))
        expr3 = IntLiteral(1)
        if ctx.BY():
            expr3 = self.visit(ctx.expr(2))
        loop = self.visit(ctx.stmt_block())
        return For(element, expr1, expr2, loop, expr3)

    def visitStmt_If(self, ctx: D96Parser.Stmt_IfContext):
        if ctx.IF() and ctx.ELSE() and not ctx.ELSEIF():
            expr = self.visit(ctx.expr(0))
            then_stmt = self.visit(ctx.stmt_block(0))
            else_stmt = self.visit(ctx.stmt_block(1))
            return If(expr, then_stmt, else_stmt)
        elif not ctx.ELSE():
            stmt_list = list(range(len(ctx.stmt_block())))[::-1]
            if_stmt = None
            for element in stmt_list:
                expr = self.visit(ctx.expr(element))
                then_stmt = self.visit(ctx.stmt_block(element))
                if_stmt = If(expr, then_stmt, if_stmt)
            return if_stmt
        else:
            # stmt_list = list(range(len(ctx.stmt_block())))[::-1][:-2]
            # expr = self.visit(ctx.expr(0))
            # then_stmt = self.visit(ctx.stmt_block(0))
            # else_stmt = None
            # for element in stmt_list:
            #     if element == max(stmt_list):
            #         else_stmt = self.visit(ctx.stmt_block(element))
            #     then_stmt_ = self.visit(ctx.stmt_block(element - 1))
            #     expr_ = self.visit(ctx.expr(element - 1))
            #     else_stmt = If(expr_, then_stmt_, else_stmt)
            # return If(expr, then_stmt, else_stmt)

            stmt_list = list(range(len(ctx.stmt_block())))[::-1][:-2]
            expr = self.visit(ctx.expr(0))
            then_stmt = self.visit(ctx.stmt_block(0))
            else_stmt = self.visit(ctx.stmt_block(len(ctx.stmt_block())-1))
            for element in stmt_list:
                expr_ = self.visit(ctx.expr(element-1))
                then_stmt_ = self.visit(ctx.stmt_block(element-1))
                else_stmt = If(expr_, then_stmt_, else_stmt)
            return If(expr, then_stmt, else_stmt)

    def visitListOfexpr(self, ctx: D96Parser.ListOfexprContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            first_element = [self.visit(ctx.expr())]
            element_list = self.visit(ctx.manyExpr())
            return first_element + element_list

    def visitManyExpr(self, ctx: D96Parser.ManyExprContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            first_element = [self.visit(ctx.expr())]
            element_list = self.visit(ctx.manyExpr())
            return first_element + element_list

    def visitStmt_List(self, ctx: D96Parser.Stmt_ListContext):
        result = []
        a = ctx.getText()
        for element in range(ctx.getChildCount()):
            result = result + self.visit(ctx.getChild(element))
        return result

    def visitStmt(self, ctx: D96Parser.StmtContext):
        if ctx.stmt_Assignment():
            return [self.visit(ctx.stmt_Assignment())]
        elif ctx.stmt_If():
            return [self.visit(ctx.stmt_If())]
        elif ctx.stmt_Break():
            return [self.visit(ctx.stmt_Break())]
        elif ctx.stmt_Continue():
            return [self.visit(ctx.stmt_Continue())]
        elif ctx.stmt_Return():
            return [self.visit(ctx.stmt_Return())]
        elif ctx.stmt_MethodInvocation():
            return [self.visit(ctx.stmt_MethodInvocation())]
        elif ctx.stmt_ForIn():
            return [self.visit(ctx.stmt_ForIn())]
        elif ctx.stmt_block():
            return [self.visit(ctx.stmt_block())]

    def visitStmt_block(self, ctx: D96Parser.Stmt_blockContext):
        result = []
        if ctx.stmt_List():
            result = result + self.visit(ctx.stmt_List())
        return Block(result)

    def visitParameterList(self, ctx: D96Parser.ParameterListContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            result = []
            many_id = self.visit(ctx.manyID())
            mptype = self.visit(ctx.mptype())
            for element in many_id:
                result += [VarDecl(element, mptype)]
            rest_of_param = self.visit(ctx.manyParam())
            result += rest_of_param
            return result

    def visitManyParam(self, ctx: D96Parser.ManyParamContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            result = []
            mptype = self.visit(ctx.mptype())
            many_id = self.visit(ctx.manyID())
            for element in many_id:
                result += [VarDecl(element, mptype)]
            rest_of_param = self.visit(ctx.manyParam())
            result += rest_of_param
            return result

    def visitManyID(self, ctx: D96Parser.ManyIDContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        else:
            first_element = [Id(ctx.ID().getText())]
            element_list = self.visit(ctx.manyID())
            return first_element + element_list

    def visitStmt_Break(self, ctx: D96Parser.Stmt_BreakContext):
        return Break()

    def visitStmt_Continue(self, ctx: D96Parser.Stmt_ContinueContext):
        return Continue()

    def visitStmt_Return(self, ctx: D96Parser.Stmt_ReturnContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return()

    def visitArrayType(self, ctx: D96Parser.ArrayTypeContext):
        size = self.visit(ctx.size())
        mptype = self.visit(ctx.typeDataPrimitive())
        return ArrayType(size, mptype)

    def visitMptype(self, ctx: D96Parser.MptypeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STR():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.arrayType():
            return self.visit(ctx.arrayType())
        else:
            return ClassType(classname=Id(ctx.ID().getText()))

    def visitTypeDataPrimitive(self, ctx: D96Parser.TypeDataPrimitiveContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STR():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.arrayType():
            return self.visit(ctx.arrayType())

    def visitIndex_operator(self, ctx: D96Parser.Index_operatorContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expr())]
        else:
            element = self.visit(ctx.expr())
            element_list = self.visit(ctx.index_operator())
            return [element] + element_list

    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        if ctx.INT_NUM():
            if len(ctx.getText()) > 1 and ctx.getText()[0] == '0':
                if ctx.getText()[1] in ['b', 'B']:
                    return IntLiteral(int(ctx.INT_NUM().getText(), 2))
                if ctx.getText()[1] in ['x', 'X']:
                    return IntLiteral(int(ctx.INT_NUM().getText(), 16))
                else:
                    return IntLiteral(int(ctx.INT_NUM().getText(), 8))
            else:
                return IntLiteral(int(ctx.INT_NUM().getText(), 10))
        elif ctx.FLOAT_NUM():
            if ctx.getText()[:2] == '.e':
                return FloatLiteral(float(0))
            return FloatLiteral(float(ctx.FLOAT_NUM().getText()))
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        elif ctx.BOOL_NUM():
            return BooleanLiteral(ctx.BOOL_NUM().getText() == 'True')
        else:
            return self.visit(ctx.arrayLit())

    def visitArrayLit(self, ctx: D96Parser.ArrayLitContext):
        value = self.visit(ctx.arrayAssignMember())
        return ArrayLiteral(value)

    def visitArrayAssignMember(self, ctx: D96Parser.ArrayAssignMemberContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            element = [self.visit(ctx.expr())]
            element_list = self.visit(ctx.arrayMemberList())
            return element + element_list

    def visitArrayMemberList(self, ctx: D96Parser.ArrayMemberListContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            element = [self.visit(ctx.expr())]
            element_list = self.visit(ctx.arrayMemberList())
            return element + element_list

    def visitSize(self, ctx: D96Parser.SizeContext):
        size = None
        if ctx.INT_NUM():
            if len(ctx.INT_NUM().getText()) > 1 and ctx.INT_NUM().getText()[0] == '0':
                if ctx.INT_NUM().getText()[1] in ['b', 'B']:
                    size = (int(ctx.INT_NUM().getText(), 2))
                elif ctx.INT_NUM().getText()[1] in ['x', 'X']:
                    size = (int(ctx.INT_NUM().getText(), 16))
                else:
                    size = (int(ctx.INT_NUM().getText(), 8))
            else:
                size = (int(ctx.INT_NUM().getText(), 10))
        return size

    def visitRelational_op(self, ctx: D96Parser.Relational_opContext):
        if ctx.LESS_THAN():
            return ctx.LESS_THAN().getText()
        elif ctx.LARGER_THAN():
            return ctx.LARGER_THAN().getText()
        elif ctx.LESS_THAN_OR_EQUAL():
            return ctx.LESS_THAN_OR_EQUAL().getText()
        elif ctx.LARGER_THAN_OR_EQUAL():
            return ctx.LARGER_THAN_OR_EQUAL().getText()
        elif ctx.DIFFRENCE():
            return ctx.DIFFRENCE().getText()
        else:
            return ctx.EQUAL().getText()
