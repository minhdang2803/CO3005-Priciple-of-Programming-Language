"""
 * @author nhphung
"""
from StaticError import *
from Utils import Utils
from Visitor import *


# from src.main.d96.utils.Visitor import BaseVisitor

## TODO
## ClassType, IdType, FieldAccess, CallStm -> return (Node,kind)
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
                 tag=None, isConst = None):
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

    def redeclared_check(self, varName, node):
        for n in node.block:
            if n.name == varName:
                return False
        return True

    def addClass(self, className, parentName):
        if self.redeclared_check(className, self.current):
            new_node = Node(name=className, block=[], parent=self.current, inherit=parentName, tag='class')
            self.current.block.append(new_node)
            self.current = new_node
            return True
        return False

    def addAttribute(self, name, typ, data, kind, isConst):
        if self.redeclared_check(name, self.current):
            new_node = Node(name=name, typ=typ, data=data, kind=kind, tag='attr', isConst= isConst)
            self.current.block.append(new_node)
            return True
        return False

    def addMethod(self, name, kind):
        if self.redeclared_check(name, self.current):
            new_node = Node(name=name, kind=kind, block=[], parent=self.current, tag='method')
            self.current.block.append(new_node)
            self.current = new_node
            return True
        return False

    def assignParam(self, funcName, size, node):
        for n in node.parent.block:
            if n.name == funcName:
                n.param = [element for element in node.block][:size]

    def addVarOrConst(self, name, typ, data, kind,  isConst):
        if self.redeclared_check(name, self.current):
            new_node = Node(name=name, typ=typ, data=data, tag='id', isConst=isConst, kind=kind)
            self.current.block.append(new_node)
            return True
        return False

    def addBlock(self):
        new_node = Node(block=[], parent=self.current)
        self.current.block.append(new_node)
        self.current = new_node

    # Undeclared
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
                parent = self.searchClass(node.inherit)
                for element in parent.block:
                    if element.name == name and element.tag == 'attr':
                        return element
        return None

    def searchMethod(self, name, class_name):
        node = self.searchClass(class_name)
        if node is not None:
            for element in node.block:
                if element.name == name and element.tag == 'method':
                    return element
            if node.inherit:
                parent = self.searchClass(node.inherit)
                for element in parent.block:
                    if element.name == name and element.tag == 'method':
                        return element
        return None


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
            return
        else:
            raise Redeclared(Class(), ast.classname.name)

    def visitAttributeDecl(self, ast, c):
        name = typ = data = kind = category = None
        if type(ast.decl) is VarDecl:
            name = ast.decl.variable.name
            typ = self.visit(ast.decl.varType, c)
            data, category = self.visit(ast.decl.varInit, c) if ast.decl.varInit is not None else (None, None)
            kind = 'Instance' if type(ast.kind) is Instance else 'Static'
            category = 'mutable'
        if type(ast.decl) is ConstDecl:
            name = ast.decl.constant.name
            typ = self.visit(ast.decl.constType, c)
            data, category = self.visit(ast.decl.value, c) if ast.decl.value is not None else (None, None)
            kind = 'Instance' if type(ast.kind) is Instance else 'Static'
            category = 'immutable'
        if c.addAttribute(name, typ[0], data, kind, category):
            node = c.searchAttr(name, c.current.name)
            return node, category
        else:
            raise Redeclared(Attribute(), name)

    def visitMethodDecl(self, ast, c):
        kind = 'Instance' if type(ast.kind) is Instance else 'Static'
        name = ast.name.name
        if c.addMethod(name, kind):
            for element in ast.param:
                self.visit(element, (c, 'PARAM', 'id'))
            self.visit(ast.body, c)
            c.assignParam(name, len(ast.param), c.current)
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
        name = ast.variable.name
        typ = self.visit(ast.varType, c)
        data, category = self.visit(ast.varInit, c) if ast.varInit is not None else (None, None)
        kind = 'Static' if '$' in name else 'Instance'
        # Check if type of data is not type of assigned value
        if data is not None and type(typ[0]) is not str:
            if type(typ[0]) is not VoidType and type(typ[0]) is not type(data):
                raise TypeMismatchInStatement(ast)

        if c[0].addVarOrConst(name, typ[0], data, kind, 'mutable'):
            node = c[0].searchId(name, c[0].current)
            return node, 'mutable'
        ret_type = Variable() if c[1] == 'INST' else Parameter()
        raise Redeclared(ret_type, name)

    def visitConstDecl(self, ast, c):
        name = ast.constant.name
        kind = 'Static' if '$' in name else 'Instance'
        typ = self.visit(ast.constType, c)
        data, category = self.visit(ast.value, c) if ast.value is not None else (None, None)
        if data is None or category == 'mutable' or ExpUtils.isNotConst(data):
            raise IllegalConstantExpression(ast.value)
        if type(data) is not type(typ[0]):
            raise TypeMismatchInConstant(ast)

        if c[0].addVarOrConst(name, typ[0], data, kind,  'immutable'):
            node = c[0].searchId(name, c[0].current)
            return node, 'immutable'
        ret_type = Constant() if c[1] == 'INST' else Parameter()
        raise Redeclared(ret_type, name)

    def visitAssign(self, ast, c):
        # lhs is scala variable, c is a tuple
        if type(ast.lhs) is Id:
            lhs = self.visit(ast.lhs, (c, 'INST', 'id'))
            if lhs[1] == 'immutable': raise CannotAssignToConstant(ast)
            if type(lhs) is VoidType:
                raise TypeMismatchInStatement(ast)
        if type(ast.lhs) is FieldAccess:
            lhs = self.visit(ast.lhs, c)
            if lhs[1] == 'immutable': raise CannotAssignToConstant(ast)
            if type(lhs) is VoidType:
                raise TypeMismatchInStatement(ast)
        if type(ast.lhs) is ArrayCell:
            exp = self.visit(ast.exp, c)
            lhs = self.visit(ast.lhs, c)
            if type(lhs) is VoidType:
                raise TypeMismatchInStatement(ast)
            if type(lhs) is not ArrayType and type(exp) is not type(lhs):
                raise TypeMismatchInStatement(ast)
            if type(lhs) is ArrayType and type(exp) is ArrayType:
                if lhs.size != exp.size:
                    raise TypeMismatchInStatement(ast)
                if type(lhs.eleType) is FloatType and type(exp.eleType) not in [IntType, FloatType]:
                    raise TypeMismatchInStatement(ast)  # TODO Check type of each element
            if type(lhs) is FloatType and type(exp) not in [FloatType, IntType]:
                raise TypeMismatchInStatement(ast)
        return

    def visitId(self, ast, c):
        node = None
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
        node = obj = None
        if type(ast.obj) is Id:
            obj = self.visit(ast.obj, (c, 'INST', 'id'))  # find object, obj is VarDecl
            node = c.searchAttr(ast.fieldname.name, obj[0].typ)
            # if there is no attribute -> raise
            if node is None:
                raise Undeclared(Attribute(), ast.fieldname.name)
            # if type of obj is not class -> raise
            if type(obj[0].typ) is not str:
                raise TypeMismatchInExpression(ast)
            return node, node.isConst
        else:
            obj = self.visit(ast.obj, c)
            node = c.searchAttr(ast.fieldname.name, obj[0].typ)
            if type(obj[0].typ) is not str:
                raise TypeMismatchInExpression(ast)
            # if there is no attribute -> raise
            if node is None:
                raise Undeclared(Attribute(), ast.fieldname.name)
            if node.kind != obj[0].kind:
                raise IllegalMemberAccess(ast)
            return node, node.isConst

    def visitCallStmt(self, ast, c):
        node = obj = None
        if type(ast.obj) is Id:
            obj = self.visit(ast.obj, (c, None, 'id'))
        else:
            obj = self.visit(ast.obj, c)
        # if Object is not class type => raise
        if type(obj[0].typ) is not str:
            raise TypeMismatchInStatement(ast)
        node = c.searchMethod(ast.method.name, obj[0].typ)
        # if there is no method (callee) exist -> raise
        if node is None:
            raise Undeclared(Method(), ast.method.name)
        # if object and method_name is not the same kind
        if node.kind != obj[0].kind:
            raise IllegalMemberAccess(ast)
        # if member is method && member return type is Void => raise
        if node.tag == 'method' and type(node.typ) is not VoidType:
            raise TypeMismatchInStatement(ast)
        #
        # if node.tag == 'method':
        #     args = node.param
        #     param = [self.visit(element, c) for element in ast.param]
        #     if len(param) < len(args):
        #         raise TypeMismatchInStatement(ast)
        #     for index in range(len(param)):
        #         if type(param[index]) is not type(args[index]):
        #             if not (type(param[index]) is FloatType and type(args[index]) is IntType):
        #                 raise TypeMismatchInStatement(ast)
        # return value
        return node, None

    def visitCallExpr(self, ast, c):
        node = obj = None
        if type(ast.obj) is Id:
            obj = self.visit(ast.obj, (c, None, 'id'))
            # if Object is not class type => raise
            if type(obj[0].typ) is not str:
                raise TypeMismatchInExpression(ast)
            node = c.searchMethod(ast.method.name, obj[0].typ)
            # if there is no method (callee) exist -> raise
            if node is None:
                raise Undeclared(Method(), ast.method.name)
        # if object and method_name is not the same kind
        if node.kind != obj[0].kind:
            raise IllegalMemberAccess(ast)
        #
        # if member is method && member return type is Void => raise
        if node.tag == 'method' and node.typ is VoidType:
            raise TypeMismatchInExpression(ast)
        #
        # if node.tag == 'method':
        #     args = node.param
        #     param = [self.visit(element, c) for element in ast.param]
        #     if len(param) < len(args):
        #         raise TypeMismatchInExpression(ast)
        #     for index in range(len(param)):
        #         if type(param[index]) is not type(args[index]):
        #             if not (type(param[index]) is FloatType and type(args[index]) is IntType):
        #                 raise TypeMismatchInExpression(ast)
        return node, None

    def visitArrayCell(self, ast, c):
        # array is a variable: ex a[5]
        arrType = self.visit(ast.arr, (c, None, 'id'))
        idxType = [self.visit(element, c) for element in ast.idx]
        if type(arrType[0].typ) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        for element in idxType[0]:
            if type(element) is not IntType:
                raise TypeMismatchInExpression(ast)
        return arrType[0], None

    def visitReturn(self, ast, c):
        node = None
        if type(ast.expr) is Id:
            return_val, category = self.visit(ast.expr, (c, None, 'id'))
            node = c.searchId(ast.expr.name, c.current)
        else:
            return_val = VoidType() if ast.expr is None else self.visit(ast.expr, c)[0]
        if c.current.tag == 'method':
            c.current.typ = return_val.typ if type(ast.expr) is Id else return_val
        return node

    def visitIntLiteral(self, ast, c):
        return IntType(), None

    def visitFloatLiteral(self, ast, c):
        return FloatType(), None

    def visitBooleanLiteral(self, ast, c):
        return BoolType(), None

    def visitNullLiteral(self, ast, c):
        return NullLiteral(), None

    def visitSelfLiteral(self, ast, c):
        return SelfLiteral(), None

    # def visitArrayLiteral(self, ast, c):  # pass

    def visitIntType(self, ast, c):
        return IntType(), None

    def visitFloatType(self, ast, c):
        return FloatType(), None

    def visitBoolType(self, ast, c):
        return BoolType(), None

    def visitStringType(self, ast, c):
        return StringType(), None

    def visitClassType(self, ast, c):
        if type(c) is tuple:
            node = c[0].searchClass(ast.classname.name)
            if node is None:
                raise Undeclared(Class(), ast.classname.name)
            return node.name, None

        node = c.searchClass(ast.classname.name)
        if node is None:
            raise Undeclared(Class(), ast.classname.name)
        return node.name, None

    def visitArrayType(self, ast, c):
        return ast, None

    def visitVoidType(self, ast, c):
        return VoidType(), None

    def visitArrayType(self, ast, c):
        return ast, None

    # if objType == 'attr':  #     raise Undeclared(Attribute(), name)  #  # if objType == 'method':  #     raise Undeclared(Method(), name)  # Note: check hết mọi điều kiện rồi mới đến redeclared
