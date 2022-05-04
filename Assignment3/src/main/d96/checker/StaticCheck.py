"""
 * @author nhphung
"""
from StaticError import *
from Utils import Utils
from Visitor import *


# from src.main.d96.utils.Visitor import BaseVisitor

# TODO
# ClassType, IdType, FieldAccess, CallStm -> return (Node,kind)
class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class ExpUtils:
    @staticmethod
    def isNaNType(expType):
        return type(expType) not in [IntType, FloatType]

    @staticmethod
    def isNotConst(expType):
        return type(expType) in [CallExpr, NewExpr, ArrayCell, ArrayType]

    @staticmethod
    def isNotAccess(expType):
        return type(expType) not in [CallExpr, FieldAccess, CallStmt]


# var/const/attribute -> type, name, data
# method -> type name data param block,
# class -> classname, inherit, block
# Author of this structure: Le Thien An senpoi 🥺
class Node:
    def __init__(self, name=None, typ=None, data=None, param=None, block=None, inherit=None, parent=None, kind=None,
                 tag=None, isConst=None):
        self.name = name
        self.typ = typ
        self.data = data
        self.param = param
        self.block = block
        self.parent = parent
        self.inherit = inherit
        self.kind = kind
        self.tag = tag
        self.isConst = isConst


class Tree:
    def __init__(self):
        self.head = Node(name='global', block=[])
        self.current = self.head
        self.Self = None

    def redeclared_check(self, var_name, node):
        for n in node.block:
            if n.name == var_name:
                return False
        return True

    def addClass(self, className, parentName):
        if self.redeclared_check(className, self.current):
            new_node = Node(name=className, block=[], parent=self.current, inherit=parentName, tag='class',
                            typ=className)
            self.current.block.append(new_node)
            self.current = new_node
            self.Self = new_node
            return True
        return False

    def addAttribute(self, name, typ, data, kind, isConst):
        if self.redeclared_check(name, self.current):
            new_node = Node(name=name, typ=typ, data=data, kind=kind, tag='attr', isConst=isConst)
            self.current.block.append(new_node)
            return True
        return False

    def addMethod(self, name, kind, class_type = None):
        if self.redeclared_check(name, self.current):
            mptype = class_type if name == 'Constructor' or name == 'Destructor' else VoidType()
            new_node = Node(name=name, kind=kind, block=[], parent=self.current, tag='method', typ=mptype)
            self.current.block.append(new_node)
            self.current = new_node
            return True
        return False

    def addVarOrConst(self, name, typ, data, kind, isConst):
        if self.redeclared_check(name, self.current):
            new_node = Node(name=name, typ=typ, data=data, tag='id', isConst=isConst, kind=kind)
            self.current.block.append(new_node)
            return True
        return False

    def addBlock(self):
        new_node = Node(block=[], parent=self.current)
        self.current.block.append(new_node)
        self.current = new_node

    def searchObj(self, name, node):
        for n in node.block:
            if n.name == name:
                return n
        if node.parent:
            return self.searchObj(name, node.parent)
        return None

    def searchId(self, name, node):
        for n in node.block:
            if n.name == name and n.tag == 'id':
                return n
        if node.parent:
            return self.searchId(name, node.parent)
        return None

    def searchClass(self, name):
        for element in self.head.block:
            if element.name == name:
                return element
        return None

    def searchAttr(self, name, class_name):
        node = self.searchClass(class_name)
        if node is not None:
            for element in node.block:
                if element.name == name and element.tag == 'attr':
                    return element
            if node.inherit:
                return self.searchAttr(name, node.inherit)
        return None

    def searchMethod(self, name, class_name):
        node = self.searchClass(class_name)
        if node is not None:
            for element in node.block:
                if element.name == name and element.tag == 'method':
                    return element
            if node.inherit:
                return self.searchMethod(name, node.inherit)
        return None

    def getInheritClass(self, class_name):
        result = []
        node = self.searchClass(class_name)
        if node is not None:
            result.append(node.name)
            if node.inherit:
                result += self.getInheritClass(node.inherit)
            else:
                result += []
        return result

    def isInherit(self, class_name):
        for element in self.head.block:
            if element.name == class_name and element.inherit:
                return True
        return False

    def checkType(self, type_decl, type_assign):
        if type(type_decl) is FloatType and type(type_assign) in [FloatType, IntType]:
            return True
        if type(type_decl) is str and type(type_assign) is str:
            if type_decl == type_assign:
                return True
            elif not self.isInherit(type_decl) and not self.isInherit(type_assign):
                return False
            else:
                inherit_assign = self.getInheritClass(type_assign)[::-1]
                if type_assign in inherit_assign[1:]:
                    return False
                else:
                    idx = inherit_assign.index(type_decl)
                    # inherit_assign = inherit_assign[:idx]
                    if type_decl in inherit_assign[:idx]:
                        return True
        return type(type_decl) == type(type_assign)

    def checkIllegalAccess(self, node_obj, node_field_name, is_self):
        if is_self is not None:
            if node_field_name.kind == 'Instance':
                return True
        else:
            if node_obj.name == node_obj.typ:
                if node_field_name.kind == 'Static':
                    return True
            if node_obj.name != node_obj.typ:
                if node_field_name.kind == 'Instance':
                    return True
        return False


class StaticChecker(BaseVisitor, Utils):
    global_envi = [Symbol("getInt", MType([], IntType())), Symbol("putIntLn", MType([IntType()], VoidType()))]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        c = Tree()
        for decl in ast.decl:
            self.visit(decl, c)

    def visitClassDecl(self, ast, c):
        node_parent = None if ast.parentname is None else self.visit(ast.parentname, (c, 'INST', 'class'))[0].name
        if c.addClass(ast.classname.name, node_parent):
            for member in ast.memlist:
                self.visit(member, c)
            c.current = c.current.parent
            c.Self = None  # Out of the Class -> Global -> Self = None
            return
        else:
            raise Redeclared(Class(), ast.classname.name)

    def visitAttributeDecl(self, ast, c):
        name = typ = node_data = kind = category = None
        if type(ast.decl) is VarDecl:
            name = ast.decl.variable.name
            typ = self.visit(ast.decl.varType, c)[0].typ
            node_data, category = self.visit(ast.decl.varInit, c) if ast.decl.varInit is not None else (None, None)
            kind = 'Instance' if type(ast.kind) is Instance else 'Static'
            category = 'mutable'
        if type(ast.decl) is ConstDecl:
            name = ast.decl.constant.name
            typ = self.visit(ast.decl.constType, c)[0].typ
            node_data, category = self.visit(ast.decl.value, c) if ast.decl.value is not None else (None, None)
            kind = 'Instance' if type(ast.kind) is Instance else 'Static'
            category = 'immutable'
        data = node_data.typ if node_data is not None else node_data
        if c.addAttribute(name, typ, data, kind, category):
            node = c.searchAttr(name, c.current.name)
            return node, category
        else:
            raise Redeclared(Attribute(), name)

    def visitMethodDecl(self, ast, c):
        kind = 'Instance' if type(ast.kind) is Instance else 'Static'
        name = ast.name.name
        if c.addMethod(name, kind, c.current.name):
            for element in ast.param:
                self.visit(element, (c, 'PARAM', 'id'))
            self.visit(ast.body, c)
            c.current.param = [element.typ for element in c.current.block][:len(ast.param)]
            c.current = c.current.parent
        else:
            raise Redeclared(Method(), name)

    def visitBlock(self, ast, c):
        for element in ast.inst:
            if type(element) is Block:
                c.addBlock()
                # VisitBlock
                self.visit(element, c)
                c.current = c.current.parent
            else:
                if type(element) in [VarDecl, ConstDecl]:
                    self.visit(element, (c, 'INST', 'id'))
                else:
                    self.visit(element, c)

    # return (kind,name,'mutable',type)
    def visitVarDecl(self, ast, c):
        # fetching data
        name = ast.variable.name
        typ = self.visit(ast.varType, c)[0].typ
        node_data, category = self.visit(ast.varInit, c) if ast.varInit is not None else (None, None)
        data = node_data.typ if node_data is not None else node_data
        kind = 'Static' if '$' in name else 'Instance'

        # Check if type of data is not type of assigned value
        if data is not None and type(typ) is not str:
            if type(typ) is not VoidType and not c[0].checkType(typ, data):
                raise TypeMismatchInStatement(ast)

        if c[0].addVarOrConst(name, typ, data, kind, 'mutable'):
            node = c[0].searchId(name, c[0].current)
            return node, 'mutable'
        ret_type = Variable() if c[1] == 'INST' else Parameter()
        raise Redeclared(ret_type, name)

    def visitConstDecl(self, ast, c):
        name = ast.constant.name
        kind = 'Static' if '$' in name else 'Instance'
        typ = self.visit(ast.constType, c)[0].typ
        node_data, category = self.visit(ast.value, c) if ast.value is not None else (None, None)
        data = node_data.typ if node_data is not None else node_data

        if data is None or category == 'mutable' or ExpUtils.isNotConst(data):
            raise IllegalConstantExpression(ast.value)
        if not c[0].checkType(typ, data):
            raise TypeMismatchInConstant(ast)

        if c[0].addVarOrConst(name, typ, data, kind, 'immutable'):
            node = c[0].searchId(name, c[0].current)
            return node, 'immutable'
        ret_type = Constant() if c[1] == 'INST' else Parameter()
        raise Redeclared(ret_type, name)

    def visitAssign(self, ast, c):
        c = c[0] if type(c) is tuple else c
        # lhs is scala variable, c is a tuple
        if type(ast.lhs) is Id:
            lhs, category = self.visit(ast.lhs, (c, 'INST', 'id'))
            if category == 'immutable': raise CannotAssignToConstant(ast)
            if type(lhs.typ) is VoidType:
                raise TypeMismatchInStatement(ast)
            expr, expr_category = self.visit(ast.exp, c) if type(ast.exp) is not Id else self.visit(ast.exp, (c, None, 'id'))
            if not c.checkType(lhs.typ, expr.typ):
                raise TypeMismatchInStatement(ast)

        if type(ast.lhs) is FieldAccess:
            lhs, category = self.visit(ast.lhs, c)
            if category == 'immutable': raise CannotAssignToConstant(ast)
            if type(lhs.typ) is VoidType:
                raise TypeMismatchInStatement(ast)
            expr, expr_category = self.visit(ast.exp, c) if type(ast.exp) is not Id else self.visit(ast.exp, (c, None, 'id'))
            if not c.checkType(lhs.typ, expr.typ):
                raise TypeMismatchInStatement(ast)

        if type(ast.lhs) is ArrayCell:
            exp, expr_category = self.visit(ast.exp, c) if type(ast.exp) is not Id else self.visit(ast.exp, (c, None, 'id'))
            lhs, category = self.visit(ast.lhs, c)
            if category == 'immutable': raise CannotAssignToConstant(ast)
            # if type(lhs.typ) is not ArrayType and not c.checkType(lhs.typ, exp.typ):
            #     raise TypeMismatchInStatement(ast)
            if type(lhs.typ) is ArrayType and type(exp.typ) is ArrayType:
                if lhs.size != exp.size:
                    raise TypeMismatchInStatement(ast)
                if not c.checkType(lhs.eleType, exp.eleType):
                    raise TypeMismatchInStatement(ast)
        return

    def visitIf(self, ast, c):
        c = c[0] if type(c) is tuple else c
        expr, category = self.visit(ast.expr, c)
        if type(expr) is not BoolType:
            raise TypeMismatchInExpression(ast)
        self.visit(ast.thenStmt, c)
        self.visit(ast.elseStmt, c)

    def visitFor(self, ast, c):
        c = c[0] if type(c) is tuple else c
        scala, category_scala = self.visit(ast.id, c)
        expr1, category_expr1 = self.visit(ast.expr1, c)
        expr2, category_expr2 = self.visit(ast.expr2, c)
        expr3, category_expr3 = self.visit(ast.expr3, c)
        scala = scala.typ
        if category_scala == 'immutable':
            raise CannotAssignToConstant(ast)
        if type(expr1.typ) is not IntType or type(expr2.typ) is not IntType or type(expr3.typ) is not IntType:
            raise TypeMismatchInExpression(ast)
        self.visit(ast.loop, c)

    def visitId(self, ast, c):
        if c[2] == 'class':
            node = c[0].searchClass(ast.name)
            if node is None:
                raise Undeclared(Class(), ast.name)
            return node, None
        if c[2] == 'id':
            node = c[0].searchId(ast.name, c[0].current)
            if node is None:
                raise Undeclared(Identifier(), ast.name)
            # if found node -> return a (node, 'immutable/mutable')
            return node, node.isConst

    # object.fieldname
    def visitFieldAccess(self, ast, c):
        c = c[0] if type(c) is tuple else c
        obj = is_self = None
        if type(ast.obj) is Id:
            obj = c.searchObj(ast.obj.name, c.current)
            if obj is None:
                raise Undeclared(Identifier(), ast.obj.name)
        else:
            obj, is_self = self.visit(ast.obj, c)
        typ = obj if type(obj) is str else obj.typ
        # Obj must be class Type
        if type(typ) is not str:
            raise TypeMismatchInExpression(ast)
        # if there is no attribute -> raise
        node = c.searchAttr(ast.fieldname.name, typ)
        if node is None:
            raise Undeclared(Attribute(), ast.fieldname.name)
        # check Illegal Access Member
        if not c.checkIllegalAccess(obj, node, is_self):
            raise IllegalMemberAccess(ast)
        return node, node.isConst

    def visitCallStmt(self, ast, c):
        obj = is_self = None
        if type(ast.obj) is Id:
            obj = c.searchObj(ast.obj.name, c.current)
            if obj is None:
                raise Undeclared(Identifier(), ast.obj.name)
        else:
            obj, is_self = self.visit(ast.obj, c)
        # Type of object must be Class
        if type(obj.typ) is not str:
            raise TypeMismatchInStatement(ast)
        node = c.searchMethod(ast.method.name, obj.typ)
        # if there is no method (callee) exist -> raise
        if node is None:
            raise Undeclared(Method(), ast.method.name)
        # if object and method_name is not the same kind
        if not c.checkIllegalAccess(obj, node, is_self):
            raise IllegalMemberAccess(ast)
        # if member is method && member return type is Void => raise
        if node.tag == 'method' and type(node.typ) is not VoidType:
            raise TypeMismatchInStatement(ast)
        # Check type of params and arguments
        if node.tag == 'method':
            param = node.param
            args = [self.visit(element, c)[0].typ for element in ast.param]
            if len(param) < len(args):
                raise TypeMismatchInStatement(ast)
            for index in range(len(param)):
                if not c.checkType(param[index], args[index]):
                    raise TypeMismatchInStatement(ast)
        # return value
        return node, None

    def visitCallExpr(self, ast, c):
        c = c[0] if type(c) is tuple else c
        obj = is_self = None
        if type(ast.obj) is Id:
            obj = c.searchObj(ast.obj.name, c.current)
            if obj is None:
                raise Undeclared(Identifier(), ast.obj.name)
        else:
            node_obj, is_self = self.visit(ast.obj, c)
        # Type of object must be Class
        if type(obj.typ) is not str:
            raise TypeMismatchInExpression(ast)
        node = c.searchMethod(ast.method.name, obj.typ)
        # if there is no method (callee) exist -> raise
        if node is None:
            raise Undeclared(Method(), ast.method.name)
        # if object and method_name is not the same kind
        if not c.checkIllegalAccess(obj, node, is_self):
            raise IllegalMemberAccess(ast)
        # if member is method && member return type is Void => raise
        if node.tag == 'method' and type(node.typ) is VoidType:
            raise TypeMismatchInExpression(ast)
        # check type of params and arguments
        if node.tag == 'method':
            param = node.param
            args = [self.visit(element, c)[0].typ for element in ast.param]
            if len(param) < len(args):
                raise TypeMismatchInExpression(ast)
            for index in range(len(param)):
                if not c.checkType(param[index], args[index]):
                    raise TypeMismatchInExpression(ast)
        return node, None

    def visitNewExpr(self, ast, c):
        c = c[0] if type(c) is tuple else c
        class_name, category = self.visit(ast.classname, (c, None, 'class'))
        node = c.searchMethod('Constructor', class_name.name)
        if node is None:
            raise Undeclared(Method(), 'Constructor')

        if node.tag == 'method':
            param = node.param
            args = [self.visit(element, c)[0].typ for element in ast.param]
            if len(param) < len(args):
                raise TypeMismatchInExpression(ast)
            for index in range(len(param)):
                if not c.checkType(param[index], args[index]):
                    raise TypeMismatchInExpression(ast)
        return node, node.isConst

    def visitBinaryOp(self, ast: BinaryOp, c):
        c = c[0] if type(c) is tuple else c
        right, category = self.visit(ast.right, (c, None, 'id')) if type(ast.right) is Id else self.visit(ast.right, c)
        left, category = self.visit(ast.left, (c, None, 'id')) if type(ast.left) is Id else self.visit(ast.left, c)
        op = ast.op
        right = right.typ
        left = left.typ

        if op in ['+', '-', '*', '/']:
            if type(left) not in [IntType, FloatType] or type(right) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            if type(left) is IntType and type(right) is IntType:
                return Node(typ=IntType()), category
            return Node(typ=FloatType()), category
        elif op == '%':
            if type(left) is IntType and type(right) is IntType:
                return Node(typ=IntType()), category
            raise TypeMismatchInExpression(ast)
        elif op in ['&&', '||']:
            if type(left) is BoolType and type(right) is BoolType:
                return Node(typ=BoolType()), category
            raise TypeMismatchInExpression(ast)
        elif op in ['==.', '+.']:
            if type(left) is not StringType or type(right) is not StringType:
                raise TypeMismatchInExpression(ast)
            if op == '==.':
                return Node(typ=BoolType()), category
            return Node(typ=StringType()), category
        elif op in ['==', '!=']:
            if type(left) not in [BoolType, IntType] or type(right) not in [BoolType, IntType]:
                raise TypeMismatchInExpression(ast)
            return Node(typ=BoolType()), category
        elif op in ['<', '>', '<=', '>=']:
            if type(left) not in [FloatType, IntType] or type(right) not in [FloatType, IntType]:
                raise TypeMismatchInExpression(ast)
            return Node(typ=BoolType()), category

    def visitUnaryOp(self, ast: UnaryOp, c):
        c = c[0] if type(c) is tuple else c
        expr, category = self.visit(ast.body, (c, None, 'id'))[0].typ if type(ast.body) is Id else self.visit(ast.body,
                                                                                                              c)
        expr = expr.typ
        op = ast.op
        if op == '-':
            if type(expr) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            return (Node(typ=IntType()), category) if type(expr) is IntType else (Node(typ=FloatType()), category)
        if op in '!':
            if type(expr) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return Node(typ=BoolType()), category

    def visitArrayCell(self, ast, c):
        # array is a variable: ex a[5]
        node_array, category = self.visit(ast.arr, (c, None, 'id'))
        arr_type = node_array.typ
        idx_type = [self.visit(element, c)[0].typ for element in ast.idx]
        if type(arr_type) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        for element in idx_type:
            if type(element) is not IntType:
                raise TypeMismatchInExpression(ast)
        return node_array, category

    def visitReturn(self, ast, c):
        node = None
        if type(ast.expr) is Id:
            return_val, category = self.visit(ast.expr, (c, None, 'id'))
            return_val = return_val.typ if return_val.typ is not None else None
            node = c.searchId(ast.expr.name, c.current)
        else:
            return_val = VoidType() if ast.expr is None else self.visit(ast.expr, c)[0].typ
        if c.current.tag == 'method':
            c.current.typ = return_val
        return node, None

    def visitIntLiteral(self, ast, c):
        return Node(typ=IntType()), None

    def visitFloatLiteral(self, ast, c):
        return Node(typ=FloatType()), None

    def visitBooleanLiteral(self, ast, c):
        return Node(typ=BoolType()), None

    def visitNullLiteral(self, ast, c):
        return Node(typ=NullLiteral()), None

    def visitSelfLiteral(self, ast, c):
        c = c[0] if type(c) is tuple else c
        return c.Self, 'Self'

    def visitArrayLiteral(self, ast, c):
        c = c[0] if type(c) is tuple else c
        value_list = [self.visit(element, c)[0].typ for element in ast.value]
        check_value = value_list[0]
        for element in value_list:
            if not c.checkType(check_value, element):
                raise IllegalArrayLiteral(ast)
        ret_type = ArrayType(len(value_list), check_value)
        return Node(typ=ret_type), None

    def visitStringLiteral(self, ast, c):
        return Node(typ=StringType()), None

    # def visitArrayLiteral(self, ast, c):  # pass
    def visitIntType(self, ast, c):
        return Node(typ=IntType()), None

    def visitFloatType(self, ast, c):
        return Node(typ=FloatType()), None

    def visitBoolType(self, ast, c):
        return Node(typ=BoolType()), None

    def visitStringType(self, ast, c):
        return Node(typ=StringType()), None

    def visitClassType(self, ast, c):
        if type(c) is tuple:
            node = c[0].searchClass(ast.classname.name)
            if node is None:
                raise Undeclared(Class(), ast.classname.name)
            return Node(typ=node.name), None

        node = c.searchClass(ast.classname.name)
        if node is None:
            raise Undeclared(Class(), ast.classname.name)
        return Node(typ=node.name), None

    def visitVoidType(self, ast, c):
        return Node(typ=VoidType()), None

    def visitArrayType(self, ast, c):
        return Node(typ=ast), None
