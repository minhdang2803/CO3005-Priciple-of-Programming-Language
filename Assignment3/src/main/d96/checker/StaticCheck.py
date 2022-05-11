"""
 * @author nhphung
"""
from StaticError import *
# from Utils import Utils
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
        return type(expType) in [CallExpr, ArrayCell, ArrayType]

    @staticmethod
    def isNotAccess(expType):
        return type(expType) not in [CallExpr, FieldAccess, CallStmt]


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
        self.InLoof = False
        self.in_func = None

    def redeclared_check(self, var_name, node):
        for n in node.block:
            if n.name == var_name:
                return False
        return True

    def redeclared_check_for_member(self, varname, node, flag):
        for n in node.block:
            if flag == 'attr':
                if n.name == varname and n.tag == 'attr':
                    return False
            elif flag == 'method':
                if n.name == varname and n.tag == 'method':
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
        if self.redeclared_check_for_member(name, self.current, 'attr'):
            new_node = Node(name=name, typ=typ, data=data, kind=kind, tag='attr', isConst=isConst)
            self.current.block.append(new_node)
            return True
        return False

    def addMethod(self, name, kind, class_type=None):
        if self.redeclared_check_for_member(name, self.current, 'method'):
            kind = 'Static' if name == 'main' and self.current.name == "Program" else kind
            mptype = class_type if ((name == 'Constructor' or name == 'Destructor') and self.current.tag == 'class') else VoidType()
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

    def searchMethod(self, name, class_name, size=None):
        node = self.searchClass(class_name)
        if size is not None and node is not None:
            for element in node.block:
                if element.name == name and element.tag == 'method' and len(element.param) == size:
                    return element
                if node.inherit:
                    return self.searchMethod(name, node.inherit, size)
        if size is None and node is not None:
            for element in node.block:
                if element.name == name and element.tag == 'method':
                    return element
            if node.inherit:
                return self.searchMethod(name, node.inherit, size)
        return None

    def checkType(self, type_decl, type_assign):
        if type(type_decl) is FloatType and type(type_assign) in [FloatType, IntType]:
            return True
        if type(type_decl) is ArrayType and type(type_assign) is ArrayType:
            if type(type_decl.eleType) is ArrayType and type(type_assign.eleType):
                return self.checkType(type_decl.eleType, type_assign.eleType)
            else:
                if type(type_decl.eleType) is not type(type_assign.eleType):
                    return False
                if type_decl.size != type_assign.size:
                    return False
        if type(type_decl) is str and type(type_assign) is str:
            if type_decl == type_assign:
                return True
            else:
                return False
        return type(type_decl) is type(type_assign)

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

    def checkEntryPoint(self):
        for node in self.head.block:
            if node.name == 'Program':
                for element in node.block:
                    if element.name == 'main' and element.tag == 'method' and element.kind == 'Static' and type(
                            element.typ) is VoidType and len(element.param) == 0:
                        return True
        return False


class StaticChecker(BaseVisitor):
    global_envi = [Symbol("getInt", MType([], IntType())), Symbol("putIntLn", MType([IntType()], VoidType()))]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        c = Tree()
        for decl in ast.decl:
            self.visit(decl, c)
        if not c.checkEntryPoint():
            raise NoEntryPoint()
        return ""

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
        name, typ, data, kind, category = self.visit(ast.decl, (c, 'Attribute', None))
        kind = 'Instance' if type(ast.kind) is Instance else 'Static'
        if c.addAttribute(name, typ, data, kind, category):
            return
        else:
            raise Redeclared(Attribute(), name)

    def visitMethodDecl(self, ast, c):
        kind = 'Instance' if type(ast.kind) is Instance else 'Static'
        name = ast.name.name
        in_program = False
        if c.current.name == 'Program' and name == 'main':
            in_program = True
        class_name = None
        if name == 'Constructor' or name == 'Destructor':
            if c.current.tag == 'class':
                class_name = c.current.name
        if c.addMethod(name, kind, class_name):
            c.in_func = c.current
            for element in ast.param:
                self.visit(element, (c, 'PARAM', 'id'))
            c.in_func.param = [element.typ for element in c.current.block][:len(ast.param)]
            self.visit(ast.body, c)
            if in_program is True and len(c.current.param) == 0 and type(c.current.typ) is not VoidType:
                raise TypeMismatchInStatement(ast)
            c.current = c.current.parent
            c.in_func = None
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
        return

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
            if not c[0].checkType(typ, data):
                raise TypeMismatchInStatement(ast)
        if data is not None and type(typ) is str:
            if type(data) is not NullLiteral:
                if not c[0].checkType(typ, data):
                    raise TypeMismatchInStatement(ast)
        # Adding the identifier
        if c[1] == 'Attribute':
            return name, typ, data, kind, 'mutable'
        if c[0].addVarOrConst(name, typ, data, kind, 'mutable'):
            return
        ret_type = Variable() if c[1] == 'INST' else Parameter()
        raise Redeclared(ret_type, name)

    def visitConstDecl(self, ast, c):
        name = ast.constant.name
        kind = 'Static' if '$' in name else 'Instance'
        typ = self.visit(ast.constType, c)[0].typ
        node_data = category = None
        if type(ast.value) is FieldAccess:
            node_data, category = self.visit(ast.value, (c[0], 'Const')) if ast.value is not None else (None, None)
        else:
            node_data, category = self.visit(ast.value, c) if ast.value is not None else (None, None)
        data = node_data.typ if node_data is not None else node_data
        if data is None or category == 'mutable' or ExpUtils.isNotConst(ast.value):
            raise IllegalConstantExpression(ast.value)
        if data is not None and type(typ) is not str:
            if not c[0].checkType(typ, data):
                raise TypeMismatchInConstant(ast)
        # Adding the identifier
        if c[1] == 'Attribute':
            return name, typ, data, kind, 'immutable'
        if c[0].addVarOrConst(name, typ, data, kind, 'immutable'):
            return
        ret_type = Constant() if c[1] == 'INST' else Parameter()
        raise Redeclared(ret_type, name)

    def visitAssign(self, ast, c):
        c = c[0] if type(c) is tuple else c
        # lhs is scala variable, c is a tuple
        expr, expr_category = self.visit(ast.exp, c) if type(ast.exp) is not Id else self.visit(ast.exp,
                                                                                                (c, None, 'id'))
        lhs, category = self.visit(ast.lhs, (c, 'INST', 'id')) if type(ast.lhs) is Id else self.visit(ast.lhs, c)

        if category == 'immutable':
            raise CannotAssignToConstant(ast)
        if type(lhs.typ) is VoidType and expr.typ is not None:
            raise TypeMismatchInStatement(ast)
        if type(lhs.typ) is not ArrayType and not c.checkType(lhs.typ, expr.typ):
            raise TypeMismatchInStatement(ast)
        if type(lhs.typ) is ArrayType and type(expr.typ) is not ArrayType:
            if not c.checkType(lhs.typ.eleType, expr.typ):
                raise TypeMismatchInStatement(ast)
        if type(lhs.typ) is ArrayType and type(expr.typ) is ArrayType:
            if lhs.typ.size != expr.typ.size:
                raise TypeMismatchInStatement(ast)
            if not c.checkType(lhs.typ.eleType, expr.typ.eleType):
                raise TypeMismatchInStatement(ast)
        return

    def visitIf(self, ast, c):
        c = c[0] if type(c) is tuple else c
        expr, category = self.visit(ast.expr, (c, None, 'id')) if type(ast.expr) is Id else self.visit(ast.expr, c)
        if type(expr.typ) is not BoolType:
            raise TypeMismatchInStatement(ast)
        c.addBlock()
        self.visit(ast.thenStmt, c)
        c.current = c.current.parent
        if ast.elseStmt:
            c.addBlock()
            self.visit(ast.elseStmt, c)
            c.current = c.current.parent
        return

    def visitFor(self, ast, c):
        c = c[0] if type(c) is tuple else c
        scala, category_scala = self.visit(ast.id, (c, None, 'id'))
        scala = scala.typ
        expr1, category_expr1 = self.visit(ast.expr1, c) if type(ast.expr1) is not Id else self.visit(ast.expr1,
                                                                                                      (c, None, 'id'))
        expr2, category_expr2 = self.visit(ast.expr2, c) if type(ast.expr2) is not Id else self.visit(ast.expr2,
                                                                                                      (c, None, 'id'))
        if category_scala == 'immutable':
            raise CannotAssignToConstant(ast)
        if type(expr1.typ) is not IntType or type(expr2.typ) is not IntType or type(scala) is not IntType:
            raise TypeMismatchInStatement(ast)
        c.InLoof = True
        c.addBlock()
        self.visit(ast.loop, c)
        c.current = c.current.parent
        c.InLoof = False
        return

    def visitBreak(self, ast, c):
        if c.InLoof is False:
            raise MustInLoop(ast)
        return

    def visitContinue(self, ast, c):
        if c.InLoof is False:
            raise MustInLoop(ast)
        return

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
        is_val = None
        if type(c) is tuple:
            is_val = c[1]
            c = c[0]
        # c = c[0] if type(c) is tuple else c
        obj = is_self = category = None
        if type(ast.obj) is Id:
            is_id = c.searchId(ast.obj.name, c.current)
            is_class = c.searchClass(ast.obj.name)
            if is_id is None and is_class is None:
                if '$' not in ast.fieldname.name:
                    raise Undeclared(Identifier(), ast.obj.name)
                else:
                    raise Undeclared(Class(), ast.obj.name)
            elif is_id is None:
                obj = is_class
            elif is_class is None:
                obj = is_id
            else:
                if '$' in ast.fieldname.name:
                    obj = is_class
                else:
                    obj = is_id
        elif type(ast.obj) is SelfLiteral:
            obj, is_self = self.visit(ast.obj, c)
        else:
            obj, category = self.visit(ast.obj, c)
        typ = obj if type(obj) is str else obj.typ
        # Obj must be class Type
        if type(typ) is not str:
            raise TypeMismatchInExpression(ast)
        # if there is no attribute -> raise
        node = c.searchAttr(ast.fieldname.name, typ)
        if node is None:
            raise Undeclared(Attribute(), ast.fieldname.name)
        # check if immutable for Constdecl:
        if is_val == 'Const':
            if category == 'mutable':
                raise IllegalConstantExpression(ast)
        # check Illegal Access Member
        if not c.checkIllegalAccess(obj, node, is_self):
            raise IllegalMemberAccess(ast)
        return node, node.isConst

    def visitCallStmt(self, ast, c):
        obj = is_self = category = None
        if type(ast.obj) is Id:
            is_id = c.searchId(ast.obj.name, c.current)
            is_class = c.searchClass(ast.obj.name)
            if is_id is None and is_class is None:
                if '$' not in ast.method.name:
                    raise Undeclared(Identifier(), ast.obj.name)
                else:
                    raise Undeclared(Class(), ast.obj.name)
            elif is_id is None:
                obj = is_class
            elif is_class is None:
                obj = is_id
            else:
                if '$' in ast.method.name:
                    obj = is_class
                else:
                    obj = is_id
        elif type(ast.obj) is SelfLiteral:
            obj, is_self = self.visit(ast.obj, c)
        else:
            obj, category = self.visit(ast.obj, c)
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
        obj = is_self = category = None
        if type(ast.obj) is Id:
            is_id = c.searchId(ast.obj.name, c.current)
            is_class = c.searchClass(ast.obj.name)
            if is_id is None and is_class is None:
                if '$' not in ast.method.name:
                    raise Undeclared(Identifier(), ast.obj.name)
                else:
                    raise Undeclared(Class(), ast.obj.name)
            elif is_id is None:
                obj = is_class
            elif is_class is None:
                obj = is_id
            else:
                if '$' in ast.method.name:
                    obj = is_class
                else:
                    obj = is_id
        elif type(ast.obj) is SelfLiteral:
            obj, is_self = self.visit(ast.obj, c)
        else:
            obj, category = self.visit(ast.obj, c)
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
        return node, node.isConst

    def visitNewExpr(self, ast, c):
        c = c[0] if type(c) is tuple else c
        class_name, category = self.visit(ast.classname, (c, None, 'class'))
        node = None
        if len(ast.param) == 0:
            node = c.searchMethod('Constructor', class_name.name)
            if node is None:
                return Node(typ=class_name.name), 'immutable'
            if len(node.param) > 0:
                raise TypeMismatchInExpression(ast)
        if len(ast.param) > 0:
            node = c.searchMethod('Constructor', class_name.name, len(ast.param))
            if node is None:
                # raise Undeclared(Method(), 'Constructor')
                raise TypeMismatchInExpression(ast)
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
        category = None
        right, category_right = self.visit(ast.right, (c, None, 'id')) if type(ast.right) is Id else self.visit(
            ast.right, c)
        left, category_left = self.visit(ast.left, (c, None, 'id')) if type(ast.left) is Id else self.visit(ast.left, c)
        if category_left is None and category_right is not None:
            category = category_right
        if category_right is None and category_left is not None:
            category = category_left
        if category_left is None and category_right is None:
            category = None
        if category_left == category_right:
            category = category_left
        if category_right == 'mutable':
            if category_left == 'immutable':
                category = 'mutable'
        if category_right == 'immutable':
            if category_left == 'mutable':
                category = 'mutable'
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
            elif type(left) is not type(right):
                raise TypeMismatchInExpression(ast)
            return Node(typ=BoolType()), category
        elif op in ['<', '>', '<=', '>=']:
            if type(left) not in [FloatType, IntType] or type(right) not in [FloatType, IntType]:
                raise TypeMismatchInExpression(ast)
            return Node(typ=BoolType()), category

    def visitUnaryOp(self, ast: UnaryOp, c):
        c = c[0] if type(c) is tuple else c
        expr, category = self.visit(ast.body, (c, None, 'id')) if type(ast.body) is Id else self.visit(ast.body, c)
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
        idx_type = [self.visit(element, c)[0].typ for element in ast.idx]
        check = arr_type = node_array.typ
        #Check type of id
        if type(arr_type) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        #Check Dimension
        number_dim = 1
        while type(check.eleType) is ArrayType:
            number_dim = number_dim + 1
            check = check.eleType
        if number_dim < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        #check type of Index
        for element in idx_type:
            if type(element) is not IntType:
                raise TypeMismatchInExpression(ast)
        target_element, target_category = self.visit(arr_type.eleType, c)
        length = range(len(ast.idx)-1)
        for element in length:
            if type(target_element.typ) is ArrayType:
                target_element, target_category = self.visit(target_element.typ.eleType, c)
        return target_element, category

    def visitReturn(self, ast, c):
        node = category = None
        if type(ast.expr) is Id:
            return_val, category = self.visit(ast.expr, (c, None, 'id'))
            return_val = return_val.typ if return_val.typ is not None else None
            node = c.searchId(ast.expr.name, c.current)
        else:
            return_val, category = (VoidType(), None) if ast.expr is None else self.visit(ast.expr, c)
            return_val = return_val.typ if type(return_val) is Node else return_val
        if c.in_func.tag == 'method':
            c.in_func.typ = return_val
            c.in_func.isConst = category
        if c.in_func.name == 'main' and len(c.in_func.param) == 0 and c.in_func.parent.name == "Program":
            raise TypeMismatchInStatement(ast)
        if c.in_func.name == 'Constructor':
            raise TypeMismatchInStatement(ast)
        return node, category

    def visitIntLiteral(self, ast, c):
        return Node(data=ast.value, typ=IntType(), isConst='immutable'), 'immutable'

    def visitFloatLiteral(self, ast, c):
        return Node(data=ast.value, typ=FloatType(), isConst='immutable'), 'immutable'

    def visitBooleanLiteral(self, ast, c):
        return Node(data=ast.value, typ=BoolType(), isConst='immutable'), 'immutable'

    def visitNullLiteral(self, ast, c):
        return Node(typ=NullLiteral(), isConst='immutable'), 'immutable'

    def visitSelfLiteral(self, ast, c):
        c = c[0] if type(c) is tuple else c
        return c.Self, 'Self'

    def visitArrayLiteral(self, ast, c):
        c = c[0] if type(c) is tuple else c
        ret_type, category = self.visitArrayLiteral2(ast, c)
        if not ret_type:
            raise IllegalArrayLiteral(ast)
        return ret_type, None

    def visitArrayLiteral2(self, ast, c):
        if len(ast.value) == 0:
            return False
        temp, category = self.visit(ast.value[0], c) if type(
            ast.value[0]) is not ArrayLiteral else self.visitArrayLiteral2(ast.value[0], c)
        if temp is False:
            return False, None
        for element in ast.value:
            type_ele, ele_cate = self.visit(element, c) if type(
                ast.value[0]) is not ArrayLiteral else self.visitArrayLiteral2(element, c)
            if type_ele is False:
                return False, None
            elif type(temp.typ) is ArrayType and type(type_ele.typ) is ArrayType:
                if not (temp.typ.size == type_ele.typ.size and type(temp.typ.eleType) is type(type_ele.typ.eleType)):
                    return False, None
            elif type(temp.typ) is not type(type_ele.typ):
                return False, None
        return Node(typ=ArrayType(len(ast.value), temp.typ)), None

    def visitStringLiteral(self, ast, c):
        return Node(data=ast.value, typ=StringType()), None

    def visitIntType(self, ast, c):
        return Node(typ=IntType()), None

    def visitFloatType(self, ast, c):
        return Node(typ=FloatType()), None

    def visitBoolType(self, ast, c):
        return Node(typ=BoolType()), None

    def visitStringType(self, ast, c):
        return Node(typ=StringType()), None

    def visitClassType(self, ast, c):
        c = c[0] if type(c) is tuple else c
        node = c.searchClass(ast.classname.name)
        if node is None:
            raise Undeclared(Class(), ast.classname.name)
        return Node(typ=node.name), None

    def visitVoidType(self, ast, c):
        return Node(typ=VoidType()), None

    def visitArrayType(self, ast, c):
        return Node(typ=ast), None
