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
    @ staticmethod
    def isNaNType(expType):
        return type(expType) not in [IntType, FloatType]

    @ staticmethod
    def isNotConst(expType):
        return type(expType) in [CallExpr, NewExpr, ArrayCell, ArrayType]

    @ staticmethod
    def isNotAccess(expType):
        return type(expType) not in [CallExpr, FieldAccess, CallStmt]

# var/const/attribute -> type, name, data
# method -> type name data param block,
# class -> classname, inherit, block
# Author of this structure: Le Thien An senpoi 🥺
class Node:
    def __init__(self, name=None, typ=None, data=None, param=None, block=None, inherit=None, parent=None, kind=None,
                 tag=None):
        self.name = name
        self.typ = typ
        self.data = data
        self.param = param
        self.block = block
        self.parent = parent
        self.inherit = inherit
        self.kind = kind
        self.tag = tag


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

    def addAttribute(self, name, typ, data, kind):
        if self.redeclared_check(name, self.current):
            new_node = Node(name=name, typ=typ, data=data, kind=kind, tag='attr')
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
                node.param = [element for element in node.block][:size]

    def addVarOrConst(self, name, typ, data, kind):
        if self.redeclared_check(name, self.current):
            new_node = Node(name=name, typ=typ, data=data, kind=kind, tag='id')
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

    def searchClass(self,name):
        for element in self.head.block:
            if element.name == name:
                return element
        return None

    def searchAttr(self,name,class_name):
        node = self.searchClass(class_name)
        if node is not None:
            for element in node.block:
                if element.name == name and element.tag == 'attr':
                    return element
        return None

    def searchMethod(self,name,class_name):
        node = self.searchClass(class_name)
        if node is not None:
            for element in node.block:
                if element.name == name and element.tag =='method':
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
        if c.addClass(ast.classname.name, None if ast.parentname is None else ast.parentname.name):
            for member in ast.memlist:
                self.visit(member, c)
            c.current = c.current.parent
            return
        else:
            raise Redeclared(Class(), ast.classname.name)

    def visitAttributeDecl(self, ast, c):
        name = typ = data = kind = None
        if type(ast.decl) is VarDecl:
            name = ast.decl.variable.name
            typ = ast.decl.varType
            data = ast.decl.varInit
            kind = 'mutable'
        if type(ast.decl) is ConstDecl:
            name = ast.decl.constant.name
            typ = self.visit(ast.decl.constType, c)
            data = self.visit(ast.decl.value, c)
            kind = 'immutable'
        if c.addAttribute(name, typ, data, kind):
            return
        else:
            raise Redeclared(Attribute(), name)

    def visitMethodDecl(self, ast, c):
        kind = ast.kind
        name = ast.name.name
        if c.addMethod(name, kind):
            for element in ast.param:
                self.visit(element, (c, 'PARAM'))
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
                self.visit(element, (c, 'INST'))

    # return (kind,name,'mutable',type)
    def visitVarDecl(self, ast, c):
        name = ast.variable.name
        typ = self.visit(ast.varType, c)
        data = self.visit(ast.varInit, c) if ast.varInit is not None else None
        if c[0].addVarOrConst(name, typ[0], data, kind='Instance'):
            node = c[0].searchId(name, c[0].current)
            return node, 'mutable'
        ret_type = Variable() if c[1] == 'INST' else Parameter()
        raise Redeclared(ret_type, name)

    # return (kind,name,'mutable',type)
    # c is tuple (c,instruction)
    def visitConstDecl(self, ast, c):
        name = ast.constant.name
        typ = self.visit(ast.constType, c)
        data = self.visit(ast.value, c) if ast.value is not None else None
        if data is None or data[1] == 'mutable' or ExpUtils.isNotConst(data):
            raise IllegalConstantExpression(ast.value)
        if type(data[0]) is not type(typ[0]):
            raise TypeMismatchInConstant(ast)

        if c[0].addVarOrConst(name, typ[0], data, kind='Static'):
            node = c[0].searchId(name, c[0].current)
            return node, 'immutable'
        ret_type = Constant() if c[1] == 'INST' else Parameter()
        raise Redeclared(ret_type, name)

    # def visitBinaryOp(self, ast, c):
    #     pass

    def visitAssign(self, ast, c):
        # lhs is scala variable, c is a tuple
        # check undefinded,
        lhs = self.visit(ast.lhs, c)
        exp = self.visit(ast.exp, c)
        if type(ast.lhs) is Id:
            if lhs[1] == 'mutable': raise CannotAssignToConstant(ast)
        return



    def visitId(self, ast, c):
        # if not found node -> raise undeclared
        node = c[0].searchId(ast.name, c[0].current)
        if node is None:
            raise Undeclared(Identifier(), ast.name)
        # if found node -> return a (node, 'immutable/mutable')
        if node.kind == 'Static':
            return node, 'immutable'
        if node.kind == 'Instance':
            return node, 'mutable'

    def visitFieldAccess(self, ast, c):
        obj = self.visit(ast.obj,c) #object can be an ID
        node = c[0].searchAttr(ast.fieldname.name, obj[0].typ)
        if node is None:
            raise Undeclared(Attribute(), ast.fieldname.name)
        if node.kind == 'Static':
            return node, 'immutable'
        if node.kind == 'Instance':
            return node, 'mutable'

    def visitCallStmt(self,ast,c):
        obj = self.visit(ast.obj,c)
        node = c[0].searchMethod(ast.method.name, obj[0].typ)
        if node is None:
            raise Undeclared(Method(), ast.method.name)
        return node, None

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
        node = c[0].searchClass(ast.classname.name)
        if node is None:
            raise Undeclared(Class(), ast.classname.name)
        return node.name, None

    def visitVoidType(self, ast, c):
        return VoidType(), None

    # if objType == 'attr':  #     raise Undeclared(Attribute(), name)  #  # if objType == 'method':  #     raise Undeclared(Method(), name)  # Note: check hết mọi điều kiện rồi mới đến redeclared
