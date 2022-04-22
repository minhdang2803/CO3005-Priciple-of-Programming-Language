# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u026a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\6\2\u0082\n\2\r\2")
        buf.write("\16\2\u0083\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4\u008f")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\5\5\u0096\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\7\6\u009e\n\6\f\6\16\6\u00a1\13\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\7\7\u00a9\n\7\f\7\16\7\u00ac\13\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\7\b\u00b4\n\b\f\b\16\b\u00b7\13\b\3\t")
        buf.write("\3\t\3\t\5\t\u00bc\n\t\3\n\3\n\3\n\5\n\u00c1\n\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u00cb\n\13\f")
        buf.write("\13\16\13\u00ce\13\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u00da\n\f\7\f\u00dc\n\f\f\f\16\f\u00df\13")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00e8\n\r\3\r\5\r\u00eb")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00f4\n\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00fe\n")
        buf.write("\17\3\20\3\20\3\20\3\20\5\20\u0104\n\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u010b\n\21\3\22\3\22\3\22\5\22\u0110\n")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0122\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\5\26\u012d\n\26")
        buf.write("\3\27\3\27\3\27\5\27\u0132\n\27\3\27\3\27\3\30\3\30\3")
        buf.write("\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u0144\n\31\3\32\3\32\3\32\3\32\3\32\3\33\3")
        buf.write("\33\3\33\3\33\5\33\u014f\n\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\5\35\u015a\n\35\3\36\3\36\3\36\3")
        buf.write("\36\3\36\5\36\u0161\n\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \5 \u016e\n \3 \3 \3 \3 \3!\3!\3!\3!")
        buf.write("\3!\3!\5!\u017a\n!\7!\u017c\n!\f!\16!\u017f\13!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\5%\u0199\n%\3&\3&\3&\3&\5&\u019f\n")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01a9\n\'\3(\3(")
        buf.write("\3(\5(\u01ae\n(\3(\3(\3)\3)\5)\u01b4\n)\3)\3)\3)\3)\5")
        buf.write(")\u01ba\n)\3)\5)\u01bd\n)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\5*\u01ca\n*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\5-\u01e0\n-\7-\u01e2\n-\f-\16-")
        buf.write("\u01e5\13-\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\5\61\u01fd")
        buf.write("\n\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u0206\n")
        buf.write("\62\3\63\3\63\3\63\5\63\u020b\n\63\3\63\3\63\3\63\5\63")
        buf.write("\u0210\n\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\7\66\u0226\n\66\f\66\16\66\u0229\13\66\3\66\3\66")
        buf.write("\5\66\u022d\n\66\3\67\3\67\3\67\38\38\38\39\39\59\u0237")
        buf.write("\n9\39\39\3:\3:\5:\u023d\n:\3:\3:\3;\3;\3;\3;\3;\3;\3")
        buf.write(";\3;\3;\5;\u024a\n;\3;\3;\3;\3<\3<\3<\3<\3<\5<\u0254\n")
        buf.write("<\3=\3=\3=\3=\3=\3=\5=\u025c\n=\3>\3>\3>\3>\3>\5>\u0263")
        buf.write("\n>\3?\3?\3?\3@\3@\3@\2\t\n\f\16\24\26@XA\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\2\t\3\2+,\3\2#$\3\2\34")
        buf.write("\35\3\2\36 \3\2\23\24\3\2>?\3\2%*\2\u027a\2\u0081\3\2")
        buf.write("\2\2\4\u0087\3\2\2\2\6\u008e\3\2\2\2\b\u0095\3\2\2\2\n")
        buf.write("\u0097\3\2\2\2\f\u00a2\3\2\2\2\16\u00ad\3\2\2\2\20\u00bb")
        buf.write("\3\2\2\2\22\u00c0\3\2\2\2\24\u00c2\3\2\2\2\26\u00cf\3")
        buf.write("\2\2\2\30\u00ea\3\2\2\2\32\u00f3\3\2\2\2\34\u00fd\3\2")
        buf.write("\2\2\36\u0103\3\2\2\2 \u010a\3\2\2\2\"\u010c\3\2\2\2$")
        buf.write("\u0113\3\2\2\2&\u0121\3\2\2\2(\u0123\3\2\2\2*\u012c\3")
        buf.write("\2\2\2,\u012e\3\2\2\2.\u0135\3\2\2\2\60\u0143\3\2\2\2")
        buf.write("\62\u0145\3\2\2\2\64\u014e\3\2\2\2\66\u0150\3\2\2\28\u0159")
        buf.write("\3\2\2\2:\u0160\3\2\2\2<\u0162\3\2\2\2>\u0169\3\2\2\2")
        buf.write("@\u0173\3\2\2\2B\u0180\3\2\2\2D\u0186\3\2\2\2F\u018b\3")
        buf.write("\2\2\2H\u0198\3\2\2\2J\u019e\3\2\2\2L\u01a8\3\2\2\2N\u01ad")
        buf.write("\3\2\2\2P\u01bc\3\2\2\2R\u01c9\3\2\2\2T\u01cb\3\2\2\2")
        buf.write("V\u01d1\3\2\2\2X\u01d5\3\2\2\2Z\u01e6\3\2\2\2\\\u01ed")
        buf.write("\3\2\2\2^\u01f1\3\2\2\2`\u01fc\3\2\2\2b\u0205\3\2\2\2")
        buf.write("d\u020f\3\2\2\2f\u0211\3\2\2\2h\u0215\3\2\2\2j\u021a\3")
        buf.write("\2\2\2l\u022e\3\2\2\2n\u0231\3\2\2\2p\u0234\3\2\2\2r\u023c")
        buf.write("\3\2\2\2t\u0240\3\2\2\2v\u0253\3\2\2\2x\u025b\3\2\2\2")
        buf.write("z\u0262\3\2\2\2|\u0264\3\2\2\2~\u0267\3\2\2\2\u0080\u0082")
        buf.write("\5> \2\u0081\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0081")
        buf.write("\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085\3\2\2\2\u0085")
        buf.write("\u0086\7\2\2\3\u0086\3\3\2\2\2\u0087\u0088\5\6\4\2\u0088")
        buf.write("\5\3\2\2\2\u0089\u008a\5\b\5\2\u008a\u008b\t\2\2\2\u008b")
        buf.write("\u008c\5\b\5\2\u008c\u008f\3\2\2\2\u008d\u008f\5\b\5\2")
        buf.write("\u008e\u0089\3\2\2\2\u008e\u008d\3\2\2\2\u008f\7\3\2\2")
        buf.write("\2\u0090\u0091\5\n\6\2\u0091\u0092\5~@\2\u0092\u0093\5")
        buf.write("\n\6\2\u0093\u0096\3\2\2\2\u0094\u0096\5\n\6\2\u0095\u0090")
        buf.write("\3\2\2\2\u0095\u0094\3\2\2\2\u0096\t\3\2\2\2\u0097\u0098")
        buf.write("\b\6\1\2\u0098\u0099\5\f\7\2\u0099\u009f\3\2\2\2\u009a")
        buf.write("\u009b\f\4\2\2\u009b\u009c\t\3\2\2\u009c\u009e\5\f\7\2")
        buf.write("\u009d\u009a\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3")
        buf.write("\2\2\2\u009f\u00a0\3\2\2\2\u00a0\13\3\2\2\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a2\u00a3\b\7\1\2\u00a3\u00a4\5\16\b\2\u00a4")
        buf.write("\u00aa\3\2\2\2\u00a5\u00a6\f\4\2\2\u00a6\u00a7\t\4\2\2")
        buf.write("\u00a7\u00a9\5\16\b\2\u00a8\u00a5\3\2\2\2\u00a9\u00ac")
        buf.write("\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab")
        buf.write("\r\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae\b\b\1\2\u00ae")
        buf.write("\u00af\5\20\t\2\u00af\u00b5\3\2\2\2\u00b0\u00b1\f\4\2")
        buf.write("\2\u00b1\u00b2\t\5\2\2\u00b2\u00b4\5\20\t\2\u00b3\u00b0")
        buf.write("\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5")
        buf.write("\u00b6\3\2\2\2\u00b6\17\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8")
        buf.write("\u00b9\7!\2\2\u00b9\u00bc\5\20\t\2\u00ba\u00bc\5\22\n")
        buf.write("\2\u00bb\u00b8\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\21\3")
        buf.write("\2\2\2\u00bd\u00be\7\35\2\2\u00be\u00c1\5\22\n\2\u00bf")
        buf.write("\u00c1\5\24\13\2\u00c0\u00bd\3\2\2\2\u00c0\u00bf\3\2\2")
        buf.write("\2\u00c1\23\3\2\2\2\u00c2\u00c3\b\13\1\2\u00c3\u00c4\5")
        buf.write("\26\f\2\u00c4\u00cc\3\2\2\2\u00c5\u00c6\f\4\2\2\u00c6")
        buf.write("\u00c7\7\64\2\2\u00c7\u00c8\5\4\3\2\u00c8\u00c9\7\65\2")
        buf.write("\2\u00c9\u00cb\3\2\2\2\u00ca\u00c5\3\2\2\2\u00cb\u00ce")
        buf.write("\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd")
        buf.write("\25\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0\b\f\1\2\u00d0")
        buf.write("\u00d1\5\30\r\2\u00d1\u00dd\3\2\2\2\u00d2\u00d3\f\4\2")
        buf.write("\2\u00d3\u00d4\7\61\2\2\u00d4\u00d9\7>\2\2\u00d5\u00d6")
        buf.write("\7\62\2\2\u00d6\u00d7\5\36\20\2\u00d7\u00d8\7\63\2\2\u00d8")
        buf.write("\u00da\3\2\2\2\u00d9\u00d5\3\2\2\2\u00d9\u00da\3\2\2\2")
        buf.write("\u00da\u00dc\3\2\2\2\u00db\u00d2\3\2\2\2\u00dc\u00df\3")
        buf.write("\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\27")
        buf.write("\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e1\7>\2\2\u00e1")
        buf.write("\u00e2\7-\2\2\u00e2\u00e7\7?\2\2\u00e3\u00e4\7\62\2\2")
        buf.write("\u00e4\u00e5\5\36\20\2\u00e5\u00e6\7\63\2\2\u00e6\u00e8")
        buf.write("\3\2\2\2\u00e7\u00e3\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8")
        buf.write("\u00eb\3\2\2\2\u00e9\u00eb\5\32\16\2\u00ea\u00e0\3\2\2")
        buf.write("\2\u00ea\u00e9\3\2\2\2\u00eb\31\3\2\2\2\u00ec\u00ed\7")
        buf.write("\27\2\2\u00ed\u00ee\5\32\16\2\u00ee\u00ef\7\62\2\2\u00ef")
        buf.write("\u00f0\5\36\20\2\u00f0\u00f1\7\63\2\2\u00f1\u00f4\3\2")
        buf.write("\2\2\u00f2\u00f4\5\34\17\2\u00f3\u00ec\3\2\2\2\u00f3\u00f2")
        buf.write("\3\2\2\2\u00f4\33\3\2\2\2\u00f5\u00f6\7\62\2\2\u00f6\u00f7")
        buf.write("\5\4\3\2\u00f7\u00f8\7\63\2\2\u00f8\u00fe\3\2\2\2\u00f9")
        buf.write("\u00fe\7>\2\2\u00fa\u00fe\7\31\2\2\u00fb\u00fe\5z>\2\u00fc")
        buf.write("\u00fe\7\20\2\2\u00fd\u00f5\3\2\2\2\u00fd\u00f9\3\2\2")
        buf.write("\2\u00fd\u00fa\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc")
        buf.write("\3\2\2\2\u00fe\35\3\2\2\2\u00ff\u0100\5\4\3\2\u0100\u0101")
        buf.write("\5 \21\2\u0101\u0104\3\2\2\2\u0102\u0104\3\2\2\2\u0103")
        buf.write("\u00ff\3\2\2\2\u0103\u0102\3\2\2\2\u0104\37\3\2\2\2\u0105")
        buf.write("\u0106\7/\2\2\u0106\u0107\5\4\3\2\u0107\u0108\5 \21\2")
        buf.write("\u0108\u010b\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u0105\3")
        buf.write("\2\2\2\u010a\u0109\3\2\2\2\u010b!\3\2\2\2\u010c\u010f")
        buf.write("\t\6\2\2\u010d\u0110\5(\25\2\u010e\u0110\5$\23\2\u010f")
        buf.write("\u010d\3\2\2\2\u010f\u010e\3\2\2\2\u0110\u0111\3\2\2\2")
        buf.write("\u0111\u0112\7.\2\2\u0112#\3\2\2\2\u0113\u0114\t\7\2\2")
        buf.write("\u0114\u0115\5&\24\2\u0115\u0116\5\4\3\2\u0116%\3\2\2")
        buf.write("\2\u0117\u0118\7/\2\2\u0118\u0119\t\7\2\2\u0119\u011a")
        buf.write("\5&\24\2\u011a\u011b\5\4\3\2\u011b\u011c\7/\2\2\u011c")
        buf.write("\u0122\3\2\2\2\u011d\u011e\7\60\2\2\u011e\u011f\5x=\2")
        buf.write("\u011f\u0120\7\"\2\2\u0120\u0122\3\2\2\2\u0121\u0117\3")
        buf.write("\2\2\2\u0121\u011d\3\2\2\2\u0122\'\3\2\2\2\u0123\u0124")
        buf.write("\t\7\2\2\u0124\u0125\5*\26\2\u0125\u0126\7\60\2\2\u0126")
        buf.write("\u0127\5x=\2\u0127)\3\2\2\2\u0128\u0129\7/\2\2\u0129\u012a")
        buf.write("\t\7\2\2\u012a\u012d\5*\26\2\u012b\u012d\3\2\2\2\u012c")
        buf.write("\u0128\3\2\2\2\u012c\u012b\3\2\2\2\u012d+\3\2\2\2\u012e")
        buf.write("\u0131\t\6\2\2\u012f\u0132\5\62\32\2\u0130\u0132\5.\30")
        buf.write("\2\u0131\u012f\3\2\2\2\u0131\u0130\3\2\2\2\u0132\u0133")
        buf.write("\3\2\2\2\u0133\u0134\7.\2\2\u0134-\3\2\2\2\u0135\u0136")
        buf.write("\7>\2\2\u0136\u0137\5\60\31\2\u0137\u0138\5\4\3\2\u0138")
        buf.write("/\3\2\2\2\u0139\u013a\7/\2\2\u013a\u013b\7>\2\2\u013b")
        buf.write("\u013c\5\60\31\2\u013c\u013d\5\4\3\2\u013d\u013e\7/\2")
        buf.write("\2\u013e\u0144\3\2\2\2\u013f\u0140\7\60\2\2\u0140\u0141")
        buf.write("\5x=\2\u0141\u0142\7\"\2\2\u0142\u0144\3\2\2\2\u0143\u0139")
        buf.write("\3\2\2\2\u0143\u013f\3\2\2\2\u0144\61\3\2\2\2\u0145\u0146")
        buf.write("\7>\2\2\u0146\u0147\5\64\33\2\u0147\u0148\7\60\2\2\u0148")
        buf.write("\u0149\5x=\2\u0149\63\3\2\2\2\u014a\u014b\7/\2\2\u014b")
        buf.write("\u014c\7>\2\2\u014c\u014f\5\64\33\2\u014d\u014f\3\2\2")
        buf.write("\2\u014e\u014a\3\2\2\2\u014e\u014d\3\2\2\2\u014f\65\3")
        buf.write("\2\2\2\u0150\u0151\7\n\2\2\u0151\u0152\7\62\2\2\u0152")
        buf.write("\u0153\58\35\2\u0153\u0154\7\63\2\2\u0154\67\3\2\2\2\u0155")
        buf.write("\u0156\5\4\3\2\u0156\u0157\5:\36\2\u0157\u015a\3\2\2\2")
        buf.write("\u0158\u015a\3\2\2\2\u0159\u0155\3\2\2\2\u0159\u0158\3")
        buf.write("\2\2\2\u015a9\3\2\2\2\u015b\u015c\7/\2\2\u015c\u015d\5")
        buf.write("\4\3\2\u015d\u015e\5:\36\2\u015e\u0161\3\2\2\2\u015f\u0161")
        buf.write("\3\2\2\2\u0160\u015b\3\2\2\2\u0160\u015f\3\2\2\2\u0161")
        buf.write(";\3\2\2\2\u0162\u0163\7\n\2\2\u0163\u0164\7\64\2\2\u0164")
        buf.write("\u0165\5v<\2\u0165\u0166\7/\2\2\u0166\u0167\5|?\2\u0167")
        buf.write("\u0168\7\65\2\2\u0168=\3\2\2\2\u0169\u016a\7\22\2\2\u016a")
        buf.write("\u016d\7>\2\2\u016b\u016c\7\60\2\2\u016c\u016e\7>\2\2")
        buf.write("\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\3")
        buf.write("\2\2\2\u016f\u0170\7\66\2\2\u0170\u0171\5@!\2\u0171\u0172")
        buf.write("\7\67\2\2\u0172?\3\2\2\2\u0173\u017d\b!\1\2\u0174\u0179")
        buf.write("\f\4\2\2\u0175\u017a\5B\"\2\u0176\u017a\5D#\2\u0177\u017a")
        buf.write("\5\"\22\2\u0178\u017a\5F$\2\u0179\u0175\3\2\2\2\u0179")
        buf.write("\u0176\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u0178\3\2\2\2")
        buf.write("\u017a\u017c\3\2\2\2\u017b\u0174\3\2\2\2\u017c\u017f\3")
        buf.write("\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017eA")
        buf.write("\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0181\7\25\2\2\u0181")
        buf.write("\u0182\7\62\2\2\u0182\u0183\5H%\2\u0183\u0184\7\63\2\2")
        buf.write("\u0184\u0185\5f\64\2\u0185C\3\2\2\2\u0186\u0187\7\26\2")
        buf.write("\2\u0187\u0188\7\62\2\2\u0188\u0189\7\63\2\2\u0189\u018a")
        buf.write("\5f\64\2\u018aE\3\2\2\2\u018b\u018c\t\7\2\2\u018c\u018d")
        buf.write("\7\62\2\2\u018d\u018e\5H%\2\u018e\u018f\7\63\2\2\u018f")
        buf.write("\u0190\5f\64\2\u0190G\3\2\2\2\u0191\u0192\7>\2\2\u0192")
        buf.write("\u0193\5J&\2\u0193\u0194\7\60\2\2\u0194\u0195\5x=\2\u0195")
        buf.write("\u0196\5L\'\2\u0196\u0199\3\2\2\2\u0197\u0199\3\2\2\2")
        buf.write("\u0198\u0191\3\2\2\2\u0198\u0197\3\2\2\2\u0199I\3\2\2")
        buf.write("\2\u019a\u019b\7/\2\2\u019b\u019c\7>\2\2\u019c\u019f\5")
        buf.write("J&\2\u019d\u019f\3\2\2\2\u019e\u019a\3\2\2\2\u019e\u019d")
        buf.write("\3\2\2\2\u019fK\3\2\2\2\u01a0\u01a1\7.\2\2\u01a1\u01a2")
        buf.write("\7>\2\2\u01a2\u01a3\5J&\2\u01a3\u01a4\7\60\2\2\u01a4\u01a5")
        buf.write("\5x=\2\u01a5\u01a6\5L\'\2\u01a6\u01a9\3\2\2\2\u01a7\u01a9")
        buf.write("\3\2\2\2\u01a8\u01a0\3\2\2\2\u01a8\u01a7\3\2\2\2\u01a9")
        buf.write("M\3\2\2\2\u01aa\u01ae\7>\2\2\u01ab\u01ae\5V,\2\u01ac\u01ae")
        buf.write("\5\\/\2\u01ad\u01aa\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad")
        buf.write("\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\5P)\2\u01b0")
        buf.write("O\3\2\2\2\u01b1\u01b3\7\64\2\2\u01b2\u01b4\5\4\3\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5\u01b6\7\65\2\2\u01b6\u01bd\5P)\2\u01b7\u01b9\7")
        buf.write("\64\2\2\u01b8\u01ba\5\4\3\2\u01b9\u01b8\3\2\2\2\u01b9")
        buf.write("\u01ba\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bd\7\65\2")
        buf.write("\2\u01bc\u01b1\3\2\2\2\u01bc\u01b7\3\2\2\2\u01bdQ\3\2")
        buf.write("\2\2\u01be\u01ca\5T+\2\u01bf\u01ca\7>\2\2\u01c0\u01ca")
        buf.write("\7\31\2\2\u01c1\u01ca\5\\/\2\u01c2\u01ca\5^\60\2\u01c3")
        buf.write("\u01ca\7\20\2\2\u01c4\u01c5\7\62\2\2\u01c5\u01c6\5\36")
        buf.write("\20\2\u01c6\u01c7\7\63\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01ca")
        buf.write("\5z>\2\u01c9\u01be\3\2\2\2\u01c9\u01bf\3\2\2\2\u01c9\u01c0")
        buf.write("\3\2\2\2\u01c9\u01c1\3\2\2\2\u01c9\u01c2\3\2\2\2\u01c9")
        buf.write("\u01c3\3\2\2\2\u01c9\u01c4\3\2\2\2\u01c9\u01c8\3\2\2\2")
        buf.write("\u01caS\3\2\2\2\u01cb\u01cc\7\27\2\2\u01cc\u01cd\7>\2")
        buf.write("\2\u01cd\u01ce\7\62\2\2\u01ce\u01cf\5\36\20\2\u01cf\u01d0")
        buf.write("\7\63\2\2\u01d0U\3\2\2\2\u01d1\u01d2\5X-\2\u01d2\u01d3")
        buf.write("\7\61\2\2\u01d3\u01d4\7>\2\2\u01d4W\3\2\2\2\u01d5\u01d6")
        buf.write("\b-\1\2\u01d6\u01d7\5R*\2\u01d7\u01e3\3\2\2\2\u01d8\u01d9")
        buf.write("\f\4\2\2\u01d9\u01da\7\61\2\2\u01da\u01df\7>\2\2\u01db")
        buf.write("\u01dc\7\62\2\2\u01dc\u01dd\5\36\20\2\u01dd\u01de\7\63")
        buf.write("\2\2\u01de\u01e0\3\2\2\2\u01df\u01db\3\2\2\2\u01df\u01e0")
        buf.write("\3\2\2\2\u01e0\u01e2\3\2\2\2\u01e1\u01d8\3\2\2\2\u01e2")
        buf.write("\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2")
        buf.write("\u01e4Y\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e7\5\26\f")
        buf.write("\2\u01e7\u01e8\7\61\2\2\u01e8\u01e9\7>\2\2\u01e9\u01ea")
        buf.write("\7\62\2\2\u01ea\u01eb\5\36\20\2\u01eb\u01ec\7\63\2\2\u01ec")
        buf.write("[\3\2\2\2\u01ed\u01ee\7>\2\2\u01ee\u01ef\7-\2\2\u01ef")
        buf.write("\u01f0\7?\2\2\u01f0]\3\2\2\2\u01f1\u01f2\7>\2\2\u01f2")
        buf.write("\u01f3\7-\2\2\u01f3\u01f4\7?\2\2\u01f4\u01f5\7\62\2\2")
        buf.write("\u01f5\u01f6\5\36\20\2\u01f6\u01f7\7\63\2\2\u01f7_\3\2")
        buf.write("\2\2\u01f8\u01fd\7>\2\2\u01f9\u01fd\5V,\2\u01fa\u01fd")
        buf.write("\5\\/\2\u01fb\u01fd\5N(\2\u01fc\u01f8\3\2\2\2\u01fc\u01f9")
        buf.write("\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc\u01fb\3\2\2\2\u01fd")
        buf.write("a\3\2\2\2\u01fe\u0206\5h\65\2\u01ff\u0206\5j\66\2\u0200")
        buf.write("\u0206\5r:\2\u0201\u0206\5l\67\2\u0202\u0206\5n8\2\u0203")
        buf.write("\u0206\5p9\2\u0204\u0206\5t;\2\u0205\u01fe\3\2\2\2\u0205")
        buf.write("\u01ff\3\2\2\2\u0205\u0200\3\2\2\2\u0205\u0201\3\2\2\2")
        buf.write("\u0205\u0202\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0204\3")
        buf.write("\2\2\2\u0206c\3\2\2\2\u0207\u020b\5b\62\2\u0208\u020b")
        buf.write("\5,\27\2\u0209\u020b\5f\64\2\u020a\u0207\3\2\2\2\u020a")
        buf.write("\u0208\3\2\2\2\u020a\u0209\3\2\2\2\u020b\u020c\3\2\2\2")
        buf.write("\u020c\u020d\5d\63\2\u020d\u0210\3\2\2\2\u020e\u0210\3")
        buf.write("\2\2\2\u020f\u020a\3\2\2\2\u020f\u020e\3\2\2\2\u0210e")
        buf.write("\3\2\2\2\u0211\u0212\7\66\2\2\u0212\u0213\5d\63\2\u0213")
        buf.write("\u0214\7\67\2\2\u0214g\3\2\2\2\u0215\u0216\5`\61\2\u0216")
        buf.write("\u0217\7\"\2\2\u0217\u0218\5\4\3\2\u0218\u0219\7.\2\2")
        buf.write("\u0219i\3\2\2\2\u021a\u021b\7\6\2\2\u021b\u021c\7\62\2")
        buf.write("\2\u021c\u021d\5\4\3\2\u021d\u021e\7\63\2\2\u021e\u0227")
        buf.write("\5f\64\2\u021f\u0220\7\7\2\2\u0220\u0221\7\62\2\2\u0221")
        buf.write("\u0222\5\4\3\2\u0222\u0223\7\63\2\2\u0223\u0224\5f\64")
        buf.write("\2\u0224\u0226\3\2\2\2\u0225\u021f\3\2\2\2\u0226\u0229")
        buf.write("\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228\3\2\2\2\u0228")
        buf.write("\u022c\3\2\2\2\u0229\u0227\3\2\2\2\u022a\u022b\7\b\2\2")
        buf.write("\u022b\u022d\5f\64\2\u022c\u022a\3\2\2\2\u022c\u022d\3")
        buf.write("\2\2\2\u022dk\3\2\2\2\u022e\u022f\7\4\2\2\u022f\u0230")
        buf.write("\7.\2\2\u0230m\3\2\2\2\u0231\u0232\7\5\2\2\u0232\u0233")
        buf.write("\7.\2\2\u0233o\3\2\2\2\u0234\u0236\7\21\2\2\u0235\u0237")
        buf.write("\5\4\3\2\u0236\u0235\3\2\2\2\u0236\u0237\3\2\2\2\u0237")
        buf.write("\u0238\3\2\2\2\u0238\u0239\7.\2\2\u0239q\3\2\2\2\u023a")
        buf.write("\u023d\5Z.\2\u023b\u023d\5^\60\2\u023c\u023a\3\2\2\2\u023c")
        buf.write("\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u023f\7.\2\2")
        buf.write("\u023fs\3\2\2\2\u0240\u0241\7\t\2\2\u0241\u0242\7\62\2")
        buf.write("\2\u0242\u0243\5\4\3\2\u0243\u0244\7\13\2\2\u0244\u0245")
        buf.write("\5\4\3\2\u0245\u0246\78\2\2\u0246\u0249\5\4\3\2\u0247")
        buf.write("\u0248\7\30\2\2\u0248\u024a\5\4\3\2\u0249\u0247\3\2\2")
        buf.write("\2\u0249\u024a\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u024c")
        buf.write("\7\63\2\2\u024c\u024d\5f\64\2\u024du\3\2\2\2\u024e\u0254")
        buf.write("\7\f\2\2\u024f\u0254\7\r\2\2\u0250\u0254\7\16\2\2\u0251")
        buf.write("\u0254\7\17\2\2\u0252\u0254\5<\37\2\u0253\u024e\3\2\2")
        buf.write("\2\u0253\u024f\3\2\2\2\u0253\u0250\3\2\2\2\u0253\u0251")
        buf.write("\3\2\2\2\u0253\u0252\3\2\2\2\u0254w\3\2\2\2\u0255\u025c")
        buf.write("\7\f\2\2\u0256\u025c\7\r\2\2\u0257\u025c\7\17\2\2\u0258")
        buf.write("\u025c\7\16\2\2\u0259\u025c\5<\37\2\u025a\u025c\7>\2\2")
        buf.write("\u025b\u0255\3\2\2\2\u025b\u0256\3\2\2\2\u025b\u0257\3")
        buf.write("\2\2\2\u025b\u0258\3\2\2\2\u025b\u0259\3\2\2\2\u025b\u025a")
        buf.write("\3\2\2\2\u025cy\3\2\2\2\u025d\u0263\79\2\2\u025e\u0263")
        buf.write("\7:\2\2\u025f\u0263\7;\2\2\u0260\u0263\7\3\2\2\u0261\u0263")
        buf.write("\5\66\34\2\u0262\u025d\3\2\2\2\u0262\u025e\3\2\2\2\u0262")
        buf.write("\u025f\3\2\2\2\u0262\u0260\3\2\2\2\u0262\u0261\3\2\2\2")
        buf.write("\u0263{\3\2\2\2\u0264\u0265\6?\t\2\u0265\u0266\79\2\2")
        buf.write("\u0266}\3\2\2\2\u0267\u0268\t\b\2\2\u0268\177\3\2\2\2")
        buf.write("\64\u0083\u008e\u0095\u009f\u00aa\u00b5\u00bb\u00c0\u00cc")
        buf.write("\u00d9\u00dd\u00e7\u00ea\u00f3\u00fd\u0103\u010a\u010f")
        buf.write("\u0121\u012c\u0131\u0143\u014e\u0159\u0160\u016d\u0179")
        buf.write("\u017d\u0198\u019e\u01a8\u01ad\u01b3\u01b9\u01bc\u01c9")
        buf.write("\u01df\u01e3\u01fc\u0205\u020a\u020f\u0227\u022c\u0236")
        buf.write("\u023c\u0249\u0253\u025b\u0262")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'Array'", 
                     "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "'Null'", "'Return'", "'Class'", "'Val'", "'Var'", 
                     "'Constructor'", "'Destructor'", "'New'", "'By'", "'Self'", 
                     "'True'", "'False'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'='", "'&&'", "'||'", "'<'", "'>'", "'<='", 
                     "'>='", "'=='", "'!='", "'==.'", "'+.'", "'::'", "';'", 
                     "','", "':'", "'.'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "'..'" ]

    symbolicNames = [ "<INVALID>", "BOOL_NUM", "BREAK", "CONTINUE", "IF", 
                      "ELSEIF", "ELSE", "FOREACH", "ARRAY", "IN", "INT", 
                      "FLOAT", "BOOLEAN", "STR", "NULL", "RETURN", "CLASS", 
                      "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
                      "BY", "SELF", "TRUE", "FALSE", "ADD", "MINUS", "MULTIPLY", 
                      "DEVIDE", "MODULO", "NOT", "ASSIGN", "AND", "OR", 
                      "LESS_THAN", "LARGER_THAN", "LESS_THAN_OR_EQUAL", 
                      "LARGER_THAN_OR_EQUAL", "EQUAL", "DIFFRENCE", "STR_CMP", 
                      "STR_CONCAT", "DOUBLE_COLON", "SEMI", "COMMA", "COLON", 
                      "DOT", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOUBLE_DOT", 
                      "INT_NUM", "FLOAT_NUM", "STRING", "COMMENT", "WS", 
                      "ID", "STATIC_ID", "UNCLOSE_STRING", "ERROR_CHAR", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_expr = 1
    RULE_expr0 = 2
    RULE_expr1 = 3
    RULE_expr2 = 4
    RULE_expr3 = 5
    RULE_expr4 = 6
    RULE_expr5 = 7
    RULE_expr6 = 8
    RULE_expr7 = 9
    RULE_expr8 = 10
    RULE_expr9 = 11
    RULE_expr10 = 12
    RULE_expr11 = 13
    RULE_listOfexpr = 14
    RULE_manyExpr = 15
    RULE_variableDecl = 16
    RULE_withASM = 17
    RULE_pair = 18
    RULE_withoutASM = 19
    RULE_manyVariable = 20
    RULE_variableDecl_func = 21
    RULE_withASM2 = 22
    RULE_pair2 = 23
    RULE_withoutASM2 = 24
    RULE_manyVariable2 = 25
    RULE_arrayLit = 26
    RULE_arrayAssignMember = 27
    RULE_arrayMemberList = 28
    RULE_arrayType = 29
    RULE_classDecl = 30
    RULE_classMember = 31
    RULE_constructorDecl = 32
    RULE_destructorDecl = 33
    RULE_methodDecl = 34
    RULE_parameterList = 35
    RULE_manyID = 36
    RULE_manyParam = 37
    RULE_expression_index = 38
    RULE_index_operator = 39
    RULE_scalar = 40
    RULE_instanceCreate = 41
    RULE_instanceAttr = 42
    RULE_exprInstanceAttr = 43
    RULE_instanceMethod = 44
    RULE_staticAttr = 45
    RULE_staticMethod = 46
    RULE_lhs = 47
    RULE_stmt = 48
    RULE_stmt_List = 49
    RULE_stmt_Block = 50
    RULE_stmt_Assignment = 51
    RULE_stmt_If = 52
    RULE_stmt_Break = 53
    RULE_stmt_Continue = 54
    RULE_stmt_Return = 55
    RULE_stmt_MethodInvocation = 56
    RULE_stmt_ForIn = 57
    RULE_typeDataPrimitive = 58
    RULE_mptype = 59
    RULE_literal = 60
    RULE_size = 61
    RULE_relational_op = 62

    ruleNames =  [ "program", "expr", "expr0", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "expr8", "expr9", 
                   "expr10", "expr11", "listOfexpr", "manyExpr", "variableDecl", 
                   "withASM", "pair", "withoutASM", "manyVariable", "variableDecl_func", 
                   "withASM2", "pair2", "withoutASM2", "manyVariable2", 
                   "arrayLit", "arrayAssignMember", "arrayMemberList", "arrayType", 
                   "classDecl", "classMember", "constructorDecl", "destructorDecl", 
                   "methodDecl", "parameterList", "manyID", "manyParam", 
                   "expression_index", "index_operator", "scalar", "instanceCreate", 
                   "instanceAttr", "exprInstanceAttr", "instanceMethod", 
                   "staticAttr", "staticMethod", "lhs", "stmt", "stmt_List", 
                   "stmt_Block", "stmt_Assignment", "stmt_If", "stmt_Break", 
                   "stmt_Continue", "stmt_Return", "stmt_MethodInvocation", 
                   "stmt_ForIn", "typeDataPrimitive", "mptype", "literal", 
                   "size", "relational_op" ]

    EOF = Token.EOF
    BOOL_NUM=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSEIF=5
    ELSE=6
    FOREACH=7
    ARRAY=8
    IN=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    STR=13
    NULL=14
    RETURN=15
    CLASS=16
    VAL=17
    VAR=18
    CONSTRUCTOR=19
    DESTRUCTOR=20
    NEW=21
    BY=22
    SELF=23
    TRUE=24
    FALSE=25
    ADD=26
    MINUS=27
    MULTIPLY=28
    DEVIDE=29
    MODULO=30
    NOT=31
    ASSIGN=32
    AND=33
    OR=34
    LESS_THAN=35
    LARGER_THAN=36
    LESS_THAN_OR_EQUAL=37
    LARGER_THAN_OR_EQUAL=38
    EQUAL=39
    DIFFRENCE=40
    STR_CMP=41
    STR_CONCAT=42
    DOUBLE_COLON=43
    SEMI=44
    COMMA=45
    COLON=46
    DOT=47
    LB=48
    RB=49
    LSB=50
    RSB=51
    LCB=52
    RCB=53
    DOUBLE_DOT=54
    INT_NUM=55
    FLOAT_NUM=56
    STRING=57
    COMMENT=58
    WS=59
    ID=60
    STATIC_ID=61
    UNCLOSE_STRING=62
    ERROR_CHAR=63
    ILLEGAL_ESCAPE=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



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



    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def classDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ClassDeclContext)
            else:
                return self.getTypedRuleContext(D96Parser.ClassDeclContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 126
                self.classDecl()
                self.state = 129 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 131
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr0(self):
            return self.getTypedRuleContext(D96Parser.Expr0Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.expr0()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr1Context,i)


        def STR_CONCAT(self):
            return self.getToken(D96Parser.STR_CONCAT, 0)

        def STR_CMP(self):
            return self.getToken(D96Parser.STR_CMP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr0" ):
                return visitor.visitExpr0(self)
            else:
                return visitor.visitChildren(self)




    def expr0(self):

        localctx = D96Parser.Expr0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr0)
        self._la = 0 # Token type
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.expr1()
                self.state = 136
                _la = self._input.LA(1)
                if not(_la==D96Parser.STR_CMP or _la==D96Parser.STR_CONCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 137
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr2Context,i)


        def relational_op(self):
            return self.getTypedRuleContext(D96Parser.Relational_opContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr1)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.expr2(0)
                self.state = 143
                self.relational_op()
                self.state = 144
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(D96Parser.Expr2Context,0)


        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 152
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 153
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 154
                    self.expr3(0) 
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 163
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 164
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 165
                    self.expr4(0) 
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def MULTIPLY(self):
            return self.getToken(D96Parser.MULTIPLY, 0)

        def DEVIDE(self):
            return self.getToken(D96Parser.DEVIDE, 0)

        def MODULO(self):
            return self.getToken(D96Parser.MODULO, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 174
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 175
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLY) | (1 << D96Parser.DEVIDE) | (1 << D96Parser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 176
                    self.expr5() 
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr5)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(D96Parser.NOT)
                self.state = 183
                self.expr5()
                pass
            elif token in [D96Parser.BOOL_NUM, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.LB, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expr6)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(D96Parser.MINUS)
                self.state = 188
                self.expr6()
                pass
            elif token in [D96Parser.BOOL_NUM, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.expr7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 202
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 195
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 196
                    self.match(D96Parser.LSB)
                    self.state = 197
                    self.expr()
                    self.state = 198
                    self.match(D96Parser.RSB) 
                self.state = 204
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def listOfexpr(self):
            return self.getTypedRuleContext(D96Parser.ListOfexprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 208
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 209
                    self.match(D96Parser.DOT)
                    self.state = 210
                    self.match(D96Parser.ID)
                    self.state = 215
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        self.state = 211
                        self.match(D96Parser.LB)
                        self.state = 212
                        self.listOfexpr()
                        self.state = 213
                        self.match(D96Parser.RB)

             
                self.state = 221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def listOfexpr(self):
            return self.getTypedRuleContext(D96Parser.ListOfexprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr9)
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.match(D96Parser.ID)
                self.state = 223
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 224
                self.match(D96Parser.STATIC_ID)
                self.state = 229
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 225
                    self.match(D96Parser.LB)
                    self.state = 226
                    self.listOfexpr()
                    self.state = 227
                    self.match(D96Parser.RB)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def listOfexpr(self):
            return self.getTypedRuleContext(D96Parser.ListOfexprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expr11(self):
            return self.getTypedRuleContext(D96Parser.Expr11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr10)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(D96Parser.NEW)
                self.state = 235
                self.expr10()
                self.state = 236
                self.match(D96Parser.LB)
                self.state = 237
                self.listOfexpr()
                self.state = 238
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOL_NUM, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.LB, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.expr11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = D96Parser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr11)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(D96Parser.LB)
                self.state = 244
                self.expr()
                self.state = 245
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.BOOL_NUM, D96Parser.ARRAY, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 249
                self.literal()
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 250
                self.match(D96Parser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListOfexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def manyExpr(self):
            return self.getTypedRuleContext(D96Parser.ManyExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_listOfexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListOfexpr" ):
                return visitor.visitListOfexpr(self)
            else:
                return visitor.visitChildren(self)




    def listOfexpr(self):

        localctx = D96Parser.ListOfexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listOfexpr)
        try:
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOL_NUM, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NOT, D96Parser.LB, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.expr()
                self.state = 254
                self.manyExpr()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def manyExpr(self):
            return self.getTypedRuleContext(D96Parser.ManyExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_manyExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManyExpr" ):
                return visitor.visitManyExpr(self)
            else:
                return visitor.visitChildren(self)




    def manyExpr(self):

        localctx = D96Parser.ManyExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_manyExpr)
        try:
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.match(D96Parser.COMMA)
                self.state = 260
                self.expr()
                self.state = 261
                self.manyExpr()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def withoutASM(self):
            return self.getTypedRuleContext(D96Parser.WithoutASMContext,0)


        def withASM(self):
            return self.getTypedRuleContext(D96Parser.WithASMContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variableDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDecl" ):
                return visitor.visitVariableDecl(self)
            else:
                return visitor.visitChildren(self)




    def variableDecl(self):

        localctx = D96Parser.VariableDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_variableDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 267
                self.withoutASM()
                pass

            elif la_ == 2:
                self.state = 268
                self.withASM()
                pass


            self.state = 271
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithASMContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self):
            return self.getTypedRuleContext(D96Parser.PairContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_withASM

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWithASM" ):
                return visitor.visitWithASM(self)
            else:
                return visitor.visitChildren(self)




    def withASM(self):

        localctx = D96Parser.WithASMContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_withASM)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.STATIC_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 274
            self.pair()
            self.state = 275
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def pair(self):
            return self.getTypedRuleContext(D96Parser.PairContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_pair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = D96Parser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_pair)
        self._la = 0 # Token type
        try:
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.match(D96Parser.COMMA)
                self.state = 278
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.STATIC_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 279
                self.pair()
                self.state = 280
                self.expr()
                self.state = 281
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.match(D96Parser.COLON)
                self.state = 284
                self.mptype()
                self.state = 285
                self.match(D96Parser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithoutASMContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def manyVariable(self):
            return self.getTypedRuleContext(D96Parser.ManyVariableContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_withoutASM

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWithoutASM" ):
                return visitor.visitWithoutASM(self)
            else:
                return visitor.visitChildren(self)




    def withoutASM(self):

        localctx = D96Parser.WithoutASMContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_withoutASM)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.STATIC_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 290
            self.manyVariable()
            self.state = 291
            self.match(D96Parser.COLON)
            self.state = 292
            self.mptype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def manyVariable(self):
            return self.getTypedRuleContext(D96Parser.ManyVariableContext,0)


        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_manyVariable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManyVariable" ):
                return visitor.visitManyVariable(self)
            else:
                return visitor.visitChildren(self)




    def manyVariable(self):

        localctx = D96Parser.ManyVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_manyVariable)
        self._la = 0 # Token type
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(D96Parser.COMMA)
                self.state = 295
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.STATIC_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 296
                self.manyVariable()
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDecl_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def withoutASM2(self):
            return self.getTypedRuleContext(D96Parser.WithoutASM2Context,0)


        def withASM2(self):
            return self.getTypedRuleContext(D96Parser.WithASM2Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variableDecl_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDecl_func" ):
                return visitor.visitVariableDecl_func(self)
            else:
                return visitor.visitChildren(self)




    def variableDecl_func(self):

        localctx = D96Parser.VariableDecl_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_variableDecl_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 301
                self.withoutASM2()
                pass

            elif la_ == 2:
                self.state = 302
                self.withASM2()
                pass


            self.state = 305
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithASM2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def pair2(self):
            return self.getTypedRuleContext(D96Parser.Pair2Context,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_withASM2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWithASM2" ):
                return visitor.visitWithASM2(self)
            else:
                return visitor.visitChildren(self)




    def withASM2(self):

        localctx = D96Parser.WithASM2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_withASM2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(D96Parser.ID)
            self.state = 308
            self.pair2()
            self.state = 309
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pair2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def pair2(self):
            return self.getTypedRuleContext(D96Parser.Pair2Context,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_pair2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair2" ):
                return visitor.visitPair2(self)
            else:
                return visitor.visitChildren(self)




    def pair2(self):

        localctx = D96Parser.Pair2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_pair2)
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(D96Parser.COMMA)
                self.state = 312
                self.match(D96Parser.ID)
                self.state = 313
                self.pair2()
                self.state = 314
                self.expr()
                self.state = 315
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.match(D96Parser.COLON)
                self.state = 318
                self.mptype()
                self.state = 319
                self.match(D96Parser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithoutASM2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def manyVariable2(self):
            return self.getTypedRuleContext(D96Parser.ManyVariable2Context,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_withoutASM2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWithoutASM2" ):
                return visitor.visitWithoutASM2(self)
            else:
                return visitor.visitChildren(self)




    def withoutASM2(self):

        localctx = D96Parser.WithoutASM2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_withoutASM2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(D96Parser.ID)
            self.state = 324
            self.manyVariable2()
            self.state = 325
            self.match(D96Parser.COLON)
            self.state = 326
            self.mptype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyVariable2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def manyVariable2(self):
            return self.getTypedRuleContext(D96Parser.ManyVariable2Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_manyVariable2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManyVariable2" ):
                return visitor.visitManyVariable2(self)
            else:
                return visitor.visitChildren(self)




    def manyVariable2(self):

        localctx = D96Parser.ManyVariable2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_manyVariable2)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.match(D96Parser.COMMA)
                self.state = 329
                self.match(D96Parser.ID)
                self.state = 330
                self.manyVariable2()
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def arrayAssignMember(self):
            return self.getTypedRuleContext(D96Parser.ArrayAssignMemberContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLit" ):
                return visitor.visitArrayLit(self)
            else:
                return visitor.visitChildren(self)




    def arrayLit(self):

        localctx = D96Parser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(D96Parser.ARRAY)
            self.state = 335
            self.match(D96Parser.LB)
            self.state = 336
            self.arrayAssignMember()
            self.state = 337
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAssignMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def arrayMemberList(self):
            return self.getTypedRuleContext(D96Parser.ArrayMemberListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arrayAssignMember

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAssignMember" ):
                return visitor.visitArrayAssignMember(self)
            else:
                return visitor.visitChildren(self)




    def arrayAssignMember(self):

        localctx = D96Parser.ArrayAssignMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_arrayAssignMember)
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOL_NUM, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NOT, D96Parser.LB, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.expr()
                self.state = 340
                self.arrayMemberList()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayMemberListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def arrayMemberList(self):
            return self.getTypedRuleContext(D96Parser.ArrayMemberListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arrayMemberList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayMemberList" ):
                return visitor.visitArrayMemberList(self)
            else:
                return visitor.visitChildren(self)




    def arrayMemberList(self):

        localctx = D96Parser.ArrayMemberListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_arrayMemberList)
        try:
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(D96Parser.COMMA)
                self.state = 346
                self.expr()
                self.state = 347
                self.arrayMemberList()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def typeDataPrimitive(self):
            return self.getTypedRuleContext(D96Parser.TypeDataPrimitiveContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def size(self):
            return self.getTypedRuleContext(D96Parser.SizeContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = D96Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(D96Parser.ARRAY)
            self.state = 353
            self.match(D96Parser.LSB)
            self.state = 354
            self.typeDataPrimitive()
            self.state = 355
            self.match(D96Parser.COMMA)
            self.state = 356
            self.size()
            self.state = 357
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def classMember(self):
            return self.getTypedRuleContext(D96Parser.ClassMemberContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = D96Parser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(D96Parser.CLASS)
            self.state = 360
            self.match(D96Parser.ID)
            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 361
                self.match(D96Parser.COLON)
                self.state = 362
                self.match(D96Parser.ID)


            self.state = 365
            self.match(D96Parser.LCB)
            self.state = 366
            self.classMember(0)
            self.state = 367
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classMember(self):
            return self.getTypedRuleContext(D96Parser.ClassMemberContext,0)


        def constructorDecl(self):
            return self.getTypedRuleContext(D96Parser.ConstructorDeclContext,0)


        def destructorDecl(self):
            return self.getTypedRuleContext(D96Parser.DestructorDeclContext,0)


        def variableDecl(self):
            return self.getTypedRuleContext(D96Parser.VariableDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(D96Parser.MethodDeclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classMember

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassMember" ):
                return visitor.visitClassMember(self)
            else:
                return visitor.visitChildren(self)



    def classMember(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.ClassMemberContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_classMember, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ClassMemberContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_classMember)
                    self.state = 370
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 375
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [D96Parser.CONSTRUCTOR]:
                        self.state = 371
                        self.constructorDecl()
                        pass
                    elif token in [D96Parser.DESTRUCTOR]:
                        self.state = 372
                        self.destructorDecl()
                        pass
                    elif token in [D96Parser.VAL, D96Parser.VAR]:
                        self.state = 373
                        self.variableDecl()
                        pass
                    elif token in [D96Parser.ID, D96Parser.STATIC_ID]:
                        self.state = 374
                        self.methodDecl()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConstructorDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def parameterList(self):
            return self.getTypedRuleContext(D96Parser.ParameterListContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt_Block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_BlockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructorDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructorDecl" ):
                return visitor.visitConstructorDecl(self)
            else:
                return visitor.visitChildren(self)




    def constructorDecl(self):

        localctx = D96Parser.ConstructorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_constructorDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 383
            self.match(D96Parser.LB)
            self.state = 384
            self.parameterList()
            self.state = 385
            self.match(D96Parser.RB)
            self.state = 386
            self.stmt_Block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt_Block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_BlockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructorDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructorDecl" ):
                return visitor.visitDestructorDecl(self)
            else:
                return visitor.visitChildren(self)




    def destructorDecl(self):

        localctx = D96Parser.DestructorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_destructorDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(D96Parser.DESTRUCTOR)
            self.state = 389
            self.match(D96Parser.LB)
            self.state = 390
            self.match(D96Parser.RB)
            self.state = 391
            self.stmt_Block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def parameterList(self):
            return self.getTypedRuleContext(D96Parser.ParameterListContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt_Block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_BlockContext,0)


        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_methodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = D96Parser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.STATIC_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 394
            self.match(D96Parser.LB)
            self.state = 395
            self.parameterList()
            self.state = 396
            self.match(D96Parser.RB)
            self.state = 397
            self.stmt_Block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def manyID(self):
            return self.getTypedRuleContext(D96Parser.ManyIDContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def manyParam(self):
            return self.getTypedRuleContext(D96Parser.ManyParamContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parameterList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = D96Parser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_parameterList)
        try:
            self.state = 406
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(D96Parser.ID)
                self.state = 400
                self.manyID()
                self.state = 401
                self.match(D96Parser.COLON)
                self.state = 402
                self.mptype()
                self.state = 403
                self.manyParam()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def manyID(self):
            return self.getTypedRuleContext(D96Parser.ManyIDContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_manyID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManyID" ):
                return visitor.visitManyID(self)
            else:
                return visitor.visitChildren(self)




    def manyID(self):

        localctx = D96Parser.ManyIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_manyID)
        try:
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.match(D96Parser.COMMA)
                self.state = 409
                self.match(D96Parser.ID)
                self.state = 410
                self.manyID()
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def manyID(self):
            return self.getTypedRuleContext(D96Parser.ManyIDContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def manyParam(self):
            return self.getTypedRuleContext(D96Parser.ManyParamContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_manyParam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManyParam" ):
                return visitor.visitManyParam(self)
            else:
                return visitor.visitChildren(self)




    def manyParam(self):

        localctx = D96Parser.ManyParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_manyParam)
        try:
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.match(D96Parser.SEMI)
                self.state = 415
                self.match(D96Parser.ID)
                self.state = 416
                self.manyID()
                self.state = 417
                self.match(D96Parser.COLON)
                self.state = 418
                self.mptype()
                self.state = 419
                self.manyParam()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def instanceAttr(self):
            return self.getTypedRuleContext(D96Parser.InstanceAttrContext,0)


        def staticAttr(self):
            return self.getTypedRuleContext(D96Parser.StaticAttrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_index" ):
                return visitor.visitExpression_index(self)
            else:
                return visitor.visitChildren(self)




    def expression_index(self):

        localctx = D96Parser.Expression_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expression_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 424
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 425
                self.instanceAttr()
                pass

            elif la_ == 3:
                self.state = 426
                self.staticAttr()
                pass


            self.state = 429
            self.index_operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = D96Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_index_operator)
        self._la = 0 # Token type
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.match(D96Parser.LSB)
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOL_NUM) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.INT_NUM) | (1 << D96Parser.FLOAT_NUM) | (1 << D96Parser.STRING) | (1 << D96Parser.ID))) != 0):
                    self.state = 432
                    self.expr()


                self.state = 435
                self.match(D96Parser.RSB)
                self.state = 436
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.match(D96Parser.LSB)
                self.state = 439
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOL_NUM) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.INT_NUM) | (1 << D96Parser.FLOAT_NUM) | (1 << D96Parser.STRING) | (1 << D96Parser.ID))) != 0):
                    self.state = 438
                    self.expr()


                self.state = 441
                self.match(D96Parser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instanceCreate(self):
            return self.getTypedRuleContext(D96Parser.InstanceCreateContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def staticAttr(self):
            return self.getTypedRuleContext(D96Parser.StaticAttrContext,0)


        def staticMethod(self):
            return self.getTypedRuleContext(D96Parser.StaticMethodContext,0)


        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def listOfexpr(self):
            return self.getTypedRuleContext(D96Parser.ListOfexprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_scalar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar" ):
                return visitor.visitScalar(self)
            else:
                return visitor.visitChildren(self)




    def scalar(self):

        localctx = D96Parser.ScalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_scalar)
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.instanceCreate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 446
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 447
                self.staticAttr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 448
                self.staticMethod()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 449
                self.match(D96Parser.NULL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 450
                self.match(D96Parser.LB)
                self.state = 451
                self.listOfexpr()
                self.state = 452
                self.match(D96Parser.RB)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 454
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceCreateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def listOfexpr(self):
            return self.getTypedRuleContext(D96Parser.ListOfexprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instanceCreate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceCreate" ):
                return visitor.visitInstanceCreate(self)
            else:
                return visitor.visitChildren(self)




    def instanceCreate(self):

        localctx = D96Parser.InstanceCreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_instanceCreate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(D96Parser.NEW)
            self.state = 458
            self.match(D96Parser.ID)
            self.state = 459
            self.match(D96Parser.LB)
            self.state = 460
            self.listOfexpr()
            self.state = 461
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceAttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprInstanceAttr(self):
            return self.getTypedRuleContext(D96Parser.ExprInstanceAttrContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instanceAttr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceAttr" ):
                return visitor.visitInstanceAttr(self)
            else:
                return visitor.visitChildren(self)




    def instanceAttr(self):

        localctx = D96Parser.InstanceAttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_instanceAttr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.exprInstanceAttr(0)
            self.state = 464
            self.match(D96Parser.DOT)
            self.state = 465
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprInstanceAttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar(self):
            return self.getTypedRuleContext(D96Parser.ScalarContext,0)


        def exprInstanceAttr(self):
            return self.getTypedRuleContext(D96Parser.ExprInstanceAttrContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def listOfexpr(self):
            return self.getTypedRuleContext(D96Parser.ListOfexprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exprInstanceAttr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprInstanceAttr" ):
                return visitor.visitExprInstanceAttr(self)
            else:
                return visitor.visitChildren(self)



    def exprInstanceAttr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.ExprInstanceAttrContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_exprInstanceAttr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.scalar()
            self._ctx.stop = self._input.LT(-1)
            self.state = 481
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ExprInstanceAttrContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprInstanceAttr)
                    self.state = 470
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 471
                    self.match(D96Parser.DOT)
                    self.state = 472
                    self.match(D96Parser.ID)
                    self.state = 477
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        self.state = 473
                        self.match(D96Parser.LB)
                        self.state = 474
                        self.listOfexpr()
                        self.state = 475
                        self.match(D96Parser.RB)

             
                self.state = 483
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class InstanceMethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def listOfexpr(self):
            return self.getTypedRuleContext(D96Parser.ListOfexprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instanceMethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceMethod" ):
                return visitor.visitInstanceMethod(self)
            else:
                return visitor.visitChildren(self)




    def instanceMethod(self):

        localctx = D96Parser.InstanceMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_instanceMethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.expr8(0)
            self.state = 485
            self.match(D96Parser.DOT)
            self.state = 486
            self.match(D96Parser.ID)
            self.state = 487
            self.match(D96Parser.LB)
            self.state = 488
            self.listOfexpr()
            self.state = 489
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticAttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_staticAttr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticAttr" ):
                return visitor.visitStaticAttr(self)
            else:
                return visitor.visitChildren(self)




    def staticAttr(self):

        localctx = D96Parser.StaticAttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_staticAttr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(D96Parser.ID)
            self.state = 492
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 493
            self.match(D96Parser.STATIC_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticMethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def listOfexpr(self):
            return self.getTypedRuleContext(D96Parser.ListOfexprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_staticMethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticMethod" ):
                return visitor.visitStaticMethod(self)
            else:
                return visitor.visitChildren(self)




    def staticMethod(self):

        localctx = D96Parser.StaticMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_staticMethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(D96Parser.ID)
            self.state = 496
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 497
            self.match(D96Parser.STATIC_ID)
            self.state = 498
            self.match(D96Parser.LB)
            self.state = 499
            self.listOfexpr()
            self.state = 500
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def instanceAttr(self):
            return self.getTypedRuleContext(D96Parser.InstanceAttrContext,0)


        def staticAttr(self):
            return self.getTypedRuleContext(D96Parser.StaticAttrContext,0)


        def expression_index(self):
            return self.getTypedRuleContext(D96Parser.Expression_indexContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_lhs)
        try:
            self.state = 506
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 502
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self.instanceAttr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 504
                self.staticAttr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 505
                self.expression_index()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_Assignment(self):
            return self.getTypedRuleContext(D96Parser.Stmt_AssignmentContext,0)


        def stmt_If(self):
            return self.getTypedRuleContext(D96Parser.Stmt_IfContext,0)


        def stmt_MethodInvocation(self):
            return self.getTypedRuleContext(D96Parser.Stmt_MethodInvocationContext,0)


        def stmt_Break(self):
            return self.getTypedRuleContext(D96Parser.Stmt_BreakContext,0)


        def stmt_Continue(self):
            return self.getTypedRuleContext(D96Parser.Stmt_ContinueContext,0)


        def stmt_Return(self):
            return self.getTypedRuleContext(D96Parser.Stmt_ReturnContext,0)


        def stmt_ForIn(self):
            return self.getTypedRuleContext(D96Parser.Stmt_ForInContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 508
                self.stmt_Assignment()
                pass

            elif la_ == 2:
                self.state = 509
                self.stmt_If()
                pass

            elif la_ == 3:
                self.state = 510
                self.stmt_MethodInvocation()
                pass

            elif la_ == 4:
                self.state = 511
                self.stmt_Break()
                pass

            elif la_ == 5:
                self.state = 512
                self.stmt_Continue()
                pass

            elif la_ == 6:
                self.state = 513
                self.stmt_Return()
                pass

            elif la_ == 7:
                self.state = 514
                self.stmt_ForIn()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_List(self):
            return self.getTypedRuleContext(D96Parser.Stmt_ListContext,0)


        def stmt(self):
            return self.getTypedRuleContext(D96Parser.StmtContext,0)


        def variableDecl_func(self):
            return self.getTypedRuleContext(D96Parser.VariableDecl_funcContext,0)


        def stmt_Block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_BlockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_List

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_List" ):
                return visitor.visitStmt_List(self)
            else:
                return visitor.visitChildren(self)




    def stmt_List(self):

        localctx = D96Parser.Stmt_ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_stmt_List)
        try:
            self.state = 525
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOL_NUM, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.NULL, D96Parser.RETURN, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.LCB, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 520
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOL_NUM, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.NULL, D96Parser.RETURN, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING, D96Parser.ID]:
                    self.state = 517
                    self.stmt()
                    pass
                elif token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 518
                    self.variableDecl_func()
                    pass
                elif token in [D96Parser.LCB]:
                    self.state = 519
                    self.stmt_Block()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 522
                self.stmt_List()
                pass
            elif token in [D96Parser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def stmt_List(self):
            return self.getTypedRuleContext(D96Parser.Stmt_ListContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_Block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_Block" ):
                return visitor.visitStmt_Block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_Block(self):

        localctx = D96Parser.Stmt_BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_stmt_Block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(D96Parser.LCB)
            self.state = 528
            self.stmt_List()
            self.state = 529
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_Assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_Assignment" ):
                return visitor.visitStmt_Assignment(self)
            else:
                return visitor.visitChildren(self)




    def stmt_Assignment(self):

        localctx = D96Parser.Stmt_AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_stmt_Assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.lhs()
            self.state = 532
            self.match(D96Parser.ASSIGN)
            self.state = 533
            self.expr()
            self.state = 534
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LB)
            else:
                return self.getToken(D96Parser.LB, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RB)
            else:
                return self.getToken(D96Parser.RB, i)

        def stmt_Block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Stmt_BlockContext)
            else:
                return self.getTypedRuleContext(D96Parser.Stmt_BlockContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ELSEIF)
            else:
                return self.getToken(D96Parser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_If

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_If" ):
                return visitor.visitStmt_If(self)
            else:
                return visitor.visitChildren(self)




    def stmt_If(self):

        localctx = D96Parser.Stmt_IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_stmt_If)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(D96Parser.IF)
            self.state = 537
            self.match(D96Parser.LB)
            self.state = 538
            self.expr()
            self.state = 539
            self.match(D96Parser.RB)
            self.state = 540
            self.stmt_Block()
            self.state = 549
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 541
                self.match(D96Parser.ELSEIF)
                self.state = 542
                self.match(D96Parser.LB)
                self.state = 543
                self.expr()
                self.state = 544
                self.match(D96Parser.RB)
                self.state = 545
                self.stmt_Block()
                self.state = 551
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 554
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 552
                self.match(D96Parser.ELSE)
                self.state = 553
                self.stmt_Block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_BreakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_Break

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_Break" ):
                return visitor.visitStmt_Break(self)
            else:
                return visitor.visitChildren(self)




    def stmt_Break(self):

        localctx = D96Parser.Stmt_BreakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_stmt_Break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.match(D96Parser.BREAK)
            self.state = 557
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ContinueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_Continue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_Continue" ):
                return visitor.visitStmt_Continue(self)
            else:
                return visitor.visitChildren(self)




    def stmt_Continue(self):

        localctx = D96Parser.Stmt_ContinueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_stmt_Continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(D96Parser.CONTINUE)
            self.state = 560
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_Return

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_Return" ):
                return visitor.visitStmt_Return(self)
            else:
                return visitor.visitChildren(self)




    def stmt_Return(self):

        localctx = D96Parser.Stmt_ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_stmt_Return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.match(D96Parser.RETURN)
            self.state = 564
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOL_NUM) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.INT_NUM) | (1 << D96Parser.FLOAT_NUM) | (1 << D96Parser.STRING) | (1 << D96Parser.ID))) != 0):
                self.state = 563
                self.expr()


            self.state = 566
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_MethodInvocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def instanceMethod(self):
            return self.getTypedRuleContext(D96Parser.InstanceMethodContext,0)


        def staticMethod(self):
            return self.getTypedRuleContext(D96Parser.StaticMethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_MethodInvocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_MethodInvocation" ):
                return visitor.visitStmt_MethodInvocation(self)
            else:
                return visitor.visitChildren(self)




    def stmt_MethodInvocation(self):

        localctx = D96Parser.Stmt_MethodInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_stmt_MethodInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 568
                self.instanceMethod()
                pass

            elif la_ == 2:
                self.state = 569
                self.staticMethod()
                pass


            self.state = 572
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ForInContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def DOUBLE_DOT(self):
            return self.getToken(D96Parser.DOUBLE_DOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt_Block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_BlockContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_ForIn

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_ForIn" ):
                return visitor.visitStmt_ForIn(self)
            else:
                return visitor.visitChildren(self)




    def stmt_ForIn(self):

        localctx = D96Parser.Stmt_ForInContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_stmt_ForIn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.match(D96Parser.FOREACH)
            self.state = 575
            self.match(D96Parser.LB)
            self.state = 576
            self.expr()
            self.state = 577
            self.match(D96Parser.IN)
            self.state = 578
            self.expr()
            self.state = 579
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 580
            self.expr()
            self.state = 583
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 581
                self.match(D96Parser.BY)
                self.state = 582
                self.expr()


            self.state = 585
            self.match(D96Parser.RB)
            self.state = 586
            self.stmt_Block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDataPrimitiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STR(self):
            return self.getToken(D96Parser.STR, 0)

        def arrayType(self):
            return self.getTypedRuleContext(D96Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_typeDataPrimitive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDataPrimitive" ):
                return visitor.visitTypeDataPrimitive(self)
            else:
                return visitor.visitChildren(self)




    def typeDataPrimitive(self):

        localctx = D96Parser.TypeDataPrimitiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_typeDataPrimitive)
        try:
            self.state = 593
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 588
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 589
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 590
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 591
                self.match(D96Parser.STR)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 592
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def STR(self):
            return self.getToken(D96Parser.STR, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def arrayType(self):
            return self.getTypedRuleContext(D96Parser.ArrayTypeContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mptype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMptype" ):
                return visitor.visitMptype(self)
            else:
                return visitor.visitChildren(self)




    def mptype(self):

        localctx = D96Parser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_mptype)
        try:
            self.state = 601
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 595
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 596
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.STR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 597
                self.match(D96Parser.STR)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 598
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 599
                self.arrayType()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 600
                self.match(D96Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_NUM(self):
            return self.getToken(D96Parser.INT_NUM, 0)

        def FLOAT_NUM(self):
            return self.getToken(D96Parser.FLOAT_NUM, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def BOOL_NUM(self):
            return self.getToken(D96Parser.BOOL_NUM, 0)

        def arrayLit(self):
            return self.getTypedRuleContext(D96Parser.ArrayLitContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_literal)
        try:
            self.state = 608
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_NUM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 603
                self.match(D96Parser.INT_NUM)
                pass
            elif token in [D96Parser.FLOAT_NUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 604
                self.match(D96Parser.FLOAT_NUM)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 605
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.BOOL_NUM]:
                self.enterOuterAlt(localctx, 4)
                self.state = 606
                self.match(D96Parser.BOOL_NUM)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 607
                self.arrayLit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_NUM(self):
            return self.getToken(D96Parser.INT_NUM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize" ):
                return visitor.visitSize(self)
            else:
                return visitor.visitChildren(self)




    def size(self):

        localctx = D96Parser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 610
            if not self.checkZero(self.getCurrentToken().text)!=1:
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self.checkZero(self.getCurrentToken().text)!=1")
            self.state = 611
            self.match(D96Parser.INT_NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS_THAN(self):
            return self.getToken(D96Parser.LESS_THAN, 0)

        def LARGER_THAN(self):
            return self.getToken(D96Parser.LARGER_THAN, 0)

        def LESS_THAN_OR_EQUAL(self):
            return self.getToken(D96Parser.LESS_THAN_OR_EQUAL, 0)

        def LARGER_THAN_OR_EQUAL(self):
            return self.getToken(D96Parser.LARGER_THAN_OR_EQUAL, 0)

        def DIFFRENCE(self):
            return self.getToken(D96Parser.DIFFRENCE, 0)

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_relational_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_op" ):
                return visitor.visitRelational_op(self)
            else:
                return visitor.visitChildren(self)




    def relational_op(self):

        localctx = D96Parser.Relational_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_relational_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 613
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LESS_THAN) | (1 << D96Parser.LARGER_THAN) | (1 << D96Parser.LESS_THAN_OR_EQUAL) | (1 << D96Parser.LARGER_THAN_OR_EQUAL) | (1 << D96Parser.EQUAL) | (1 << D96Parser.DIFFRENCE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr2_sempred
        self._predicates[5] = self.expr3_sempred
        self._predicates[6] = self.expr4_sempred
        self._predicates[9] = self.expr7_sempred
        self._predicates[10] = self.expr8_sempred
        self._predicates[31] = self.classMember_sempred
        self._predicates[43] = self.exprInstanceAttr_sempred
        self._predicates[61] = self.size_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def classMember_sempred(self, localctx:ClassMemberContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def exprInstanceAttr_sempred(self, localctx:ExprInstanceAttrContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def size_sempred(self, localctx:SizeContext, predIndex:int):
            if predIndex == 7:
                return self.checkZero(self.getCurrentToken().text)!=1
         




