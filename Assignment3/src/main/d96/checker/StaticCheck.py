"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *


# from src.main.d96.utils.Visitor import BaseVisitor


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


# var/const/attribute -> type, name, data
# method -> type name data param block,
# class -> classname, inherit, block
# Author of this structure: Le Thien An senpoi 🥺
class Node:
    def __init__(self, name=None, typ=None, data=None, param=None, block=None, inherit=None, parent=None, kind=None):
        self.name = name
        self.typ = typ
        self.data = data
        self.param = param
        self.block = block
        self.parent = parent
        self.inherit = inherit
        self.kind = kind

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
            new_node = Node(name=className, block=[], parent=self.current, inherit=parentName)
            self.current.block.append(new_node)
            self.current = new_node
            return True
        return False

    def addAttribute(self, ast):
        name = typ = data = None
        if type(ast.decl) is VarDecl:
            name = ast.decl.variable.name
            typ = ast.decl.varType
            data = ast.decl.varInit
        if type(ast.decl) is ConstDecl:
            name = ast.decl.constant.name
            typ = ast.decl.constType
            data = ast.decl.value
        kind = ast.kind
        new_node = Node(name=name, typ=typ, data=data, kind=kind)
        if self.redeclared_check(name, self.current):
            self.current.block.append(new_node)
            return True
        return False

    def addMethod(self, name, kind):
        if self.redeclared_check(name, self.current):
            new_node = Node(name=name, kind=kind, block=[], parent=self.current)
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
            new_node = Node(name=name, typ=typ, data=data, kind=kind)
            self.current.block.append(new_node)
            return True
        return False

    def addBlock(self):
        new_node = Node(block=[], parent=self.current)
        self.current.block.append(new_node)
        self.current = new_node

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
        if c.addAttribute(ast):
            return
        else:
            name = ast.decl.variable.name if type(ast.decl) is VarDecl else ast.decl.constant.name
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

    def visitVarDecl(self, ast, c):
        name = ast.variable.name
        typ = ast.varType
        data = ast.varInit
        if c[0].addVarOrConst(name, typ, data, kind=Instance()):
            return
        ret_type = Variable() if c[1] == 'INST' else Parameter()
        raise Redeclared(ret_type, name)

    def visitConstDecl(self, ast, c):
        name = ast.constant.name
        typ = ast.constType
        data = ast.value
        if c[0].addVarOrConst(name, typ, data, kind=Static()):
            return
        ret_type = Constant() if c[1] == 'INST' else Parameter()
        raise Redeclared(ret_type, name)
