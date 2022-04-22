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
        buf.write("\u027c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\3\2")
        buf.write("\6\2\u0088\n\2\r\2\16\2\u0089\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\5\4\u0095\n\4\3\5\3\5\3\5\3\5\3\5\5\5\u009c")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u00a4\n\6\f\6\16\6\u00a7")
        buf.write("\13\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u00af\n\7\f\7\16\7\u00b2")
        buf.write("\13\7\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00ba\n\b\f\b\16\b\u00bd")
        buf.write("\13\b\3\t\3\t\3\t\5\t\u00c2\n\t\3\n\3\n\3\n\5\n\u00c7")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\7\13\u00ce\n\13\f\13\16")
        buf.write("\13\u00d1\13\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u00dd\n\f\7\f\u00df\n\f\f\f\16\f\u00e2\13\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00eb\n\r\3\r\5\r\u00ee\n")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00f7\n\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u00fe\n\17\3\20\3\20\3")
        buf.write("\20\3\20\5\20\u0104\n\20\3\21\3\21\3\21\3\21\5\21\u010a")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u0111\n\22\3\23\3")
        buf.write("\23\3\23\5\23\u0116\n\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u0128\n\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\5")
        buf.write("\27\u0132\n\27\3\30\3\30\3\30\5\30\u0137\n\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u0149\n\32\3\33\3\33\3\33\3\33\3")
        buf.write("\34\3\34\3\34\3\34\5\34\u0153\n\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\5\36\u015e\n\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\5\37\u0165\n\37\3 \3 \3 \3 \3 \3 \3 \3!")
        buf.write("\3!\3!\3!\5!\u0172\n!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\7\"")
        buf.write("\u017c\n\"\f\"\16\"\u017f\13\"\3#\3#\3#\3#\3#\3#\3$\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\5&\u0198")
        buf.write("\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01a1\n\'\3(\3(\3")
        buf.write("(\3(\5(\u01a7\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\5)\u01b6\n)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u01c3")
        buf.write("\n*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u01d0\n+\3,\3")
        buf.write(",\3,\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\5.\u01e6\n.\7.\u01e8\n.\f.\16.\u01eb\13.\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\5\64\u0211")
        buf.write("\n\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u021b")
        buf.write("\n\65\3\66\3\66\7\66\u021f\n\66\f\66\16\66\u0222\13\66")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\38\38\39\39\39\39\39\39")
        buf.write("\39\39\39\39\39\79\u0238\n9\f9\169\u023b\139\39\39\59")
        buf.write("\u023f\n9\3:\3:\3:\3;\3;\3;\3<\3<\5<\u0249\n<\3<\3<\3")
        buf.write("=\3=\5=\u024f\n=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3>\5>\u025c")
        buf.write("\n>\3>\3>\3>\3?\3?\3?\3?\3?\5?\u0266\n?\3@\3@\3@\3@\3")
        buf.write("@\3@\5@\u026e\n@\3A\3A\3A\3A\3A\5A\u0275\nA\3B\3B\3B\3")
        buf.write("C\3C\3C\2\b\n\f\16\24\26ZD\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnprtvxz|~\u0080\u0082\u0084\2\t\3\2+,\3\2#$\3")
        buf.write("\2\34\35\3\2\36 \3\2\23\24\3\2>?\3\2%*\2\u028e\2\u0087")
        buf.write("\3\2\2\2\4\u008d\3\2\2\2\6\u0094\3\2\2\2\b\u009b\3\2\2")
        buf.write("\2\n\u009d\3\2\2\2\f\u00a8\3\2\2\2\16\u00b3\3\2\2\2\20")
        buf.write("\u00c1\3\2\2\2\22\u00c6\3\2\2\2\24\u00c8\3\2\2\2\26\u00d2")
        buf.write("\3\2\2\2\30\u00ed\3\2\2\2\32\u00f6\3\2\2\2\34\u00fd\3")
        buf.write("\2\2\2\36\u0103\3\2\2\2 \u0109\3\2\2\2\"\u0110\3\2\2\2")
        buf.write("$\u0112\3\2\2\2&\u0119\3\2\2\2(\u0127\3\2\2\2*\u0129\3")
        buf.write("\2\2\2,\u0131\3\2\2\2.\u0133\3\2\2\2\60\u013a\3\2\2\2")
        buf.write("\62\u0148\3\2\2\2\64\u014a\3\2\2\2\66\u0152\3\2\2\28\u0154")
        buf.write("\3\2\2\2:\u015d\3\2\2\2<\u0164\3\2\2\2>\u0166\3\2\2\2")
        buf.write("@\u016d\3\2\2\2B\u017d\3\2\2\2D\u0180\3\2\2\2F\u0186\3")
        buf.write("\2\2\2H\u018b\3\2\2\2J\u0197\3\2\2\2L\u01a0\3\2\2\2N\u01a6")
        buf.write("\3\2\2\2P\u01b5\3\2\2\2R\u01c2\3\2\2\2T\u01cf\3\2\2\2")
        buf.write("V\u01d1\3\2\2\2X\u01d7\3\2\2\2Z\u01db\3\2\2\2\\\u01ec")
        buf.write("\3\2\2\2^\u01f3\3\2\2\2`\u01fa\3\2\2\2b\u01fe\3\2\2\2")
        buf.write("d\u0205\3\2\2\2f\u0210\3\2\2\2h\u021a\3\2\2\2j\u0220\3")
        buf.write("\2\2\2l\u0223\3\2\2\2n\u0227\3\2\2\2p\u022c\3\2\2\2r\u0240")
        buf.write("\3\2\2\2t\u0243\3\2\2\2v\u0246\3\2\2\2x\u024e\3\2\2\2")
        buf.write("z\u0252\3\2\2\2|\u0265\3\2\2\2~\u026d\3\2\2\2\u0080\u0274")
        buf.write("\3\2\2\2\u0082\u0276\3\2\2\2\u0084\u0279\3\2\2\2\u0086")
        buf.write("\u0088\5@!\2\u0087\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089")
        buf.write("\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\3\2\2\2")
        buf.write("\u008b\u008c\7\2\2\3\u008c\3\3\2\2\2\u008d\u008e\5\6\4")
        buf.write("\2\u008e\5\3\2\2\2\u008f\u0090\5\b\5\2\u0090\u0091\t\2")
        buf.write("\2\2\u0091\u0092\5\b\5\2\u0092\u0095\3\2\2\2\u0093\u0095")
        buf.write("\5\b\5\2\u0094\u008f\3\2\2\2\u0094\u0093\3\2\2\2\u0095")
        buf.write("\7\3\2\2\2\u0096\u0097\5\n\6\2\u0097\u0098\5\u0084C\2")
        buf.write("\u0098\u0099\5\n\6\2\u0099\u009c\3\2\2\2\u009a\u009c\5")
        buf.write("\n\6\2\u009b\u0096\3\2\2\2\u009b\u009a\3\2\2\2\u009c\t")
        buf.write("\3\2\2\2\u009d\u009e\b\6\1\2\u009e\u009f\5\f\7\2\u009f")
        buf.write("\u00a5\3\2\2\2\u00a0\u00a1\f\4\2\2\u00a1\u00a2\t\3\2\2")
        buf.write("\u00a2\u00a4\5\f\7\2\u00a3\u00a0\3\2\2\2\u00a4\u00a7\3")
        buf.write("\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\13")
        buf.write("\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\b\7\1\2\u00a9")
        buf.write("\u00aa\5\16\b\2\u00aa\u00b0\3\2\2\2\u00ab\u00ac\f\4\2")
        buf.write("\2\u00ac\u00ad\t\4\2\2\u00ad\u00af\5\16\b\2\u00ae\u00ab")
        buf.write("\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\r\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3")
        buf.write("\u00b4\b\b\1\2\u00b4\u00b5\5\20\t\2\u00b5\u00bb\3\2\2")
        buf.write("\2\u00b6\u00b7\f\4\2\2\u00b7\u00b8\t\5\2\2\u00b8\u00ba")
        buf.write("\5\20\t\2\u00b9\u00b6\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\17\3\2\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00be\u00bf\7!\2\2\u00bf\u00c2\5\20\t\2")
        buf.write("\u00c0\u00c2\5\22\n\2\u00c1\u00be\3\2\2\2\u00c1\u00c0")
        buf.write("\3\2\2\2\u00c2\21\3\2\2\2\u00c3\u00c4\7\35\2\2\u00c4\u00c7")
        buf.write("\5\22\n\2\u00c5\u00c7\5\24\13\2\u00c6\u00c3\3\2\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c7\23\3\2\2\2\u00c8\u00c9\b\13\1\2\u00c9")
        buf.write("\u00ca\5\26\f\2\u00ca\u00cf\3\2\2\2\u00cb\u00cc\f\4\2")
        buf.write("\2\u00cc\u00ce\5R*\2\u00cd\u00cb\3\2\2\2\u00ce\u00d1\3")
        buf.write("\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\25")
        buf.write("\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d3\b\f\1\2\u00d3")
        buf.write("\u00d4\5\30\r\2\u00d4\u00e0\3\2\2\2\u00d5\u00d6\f\4\2")
        buf.write("\2\u00d6\u00d7\7\61\2\2\u00d7\u00dc\7>\2\2\u00d8\u00d9")
        buf.write("\7\62\2\2\u00d9\u00da\5 \21\2\u00da\u00db\7\63\2\2\u00db")
        buf.write("\u00dd\3\2\2\2\u00dc\u00d8\3\2\2\2\u00dc\u00dd\3\2\2\2")
        buf.write("\u00dd\u00df\3\2\2\2\u00de\u00d5\3\2\2\2\u00df\u00e2\3")
        buf.write("\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\27")
        buf.write("\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e4\7>\2\2\u00e4")
        buf.write("\u00e5\7-\2\2\u00e5\u00ea\7?\2\2\u00e6\u00e7\7\62\2\2")
        buf.write("\u00e7\u00e8\5 \21\2\u00e8\u00e9\7\63\2\2\u00e9\u00eb")
        buf.write("\3\2\2\2\u00ea\u00e6\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb")
        buf.write("\u00ee\3\2\2\2\u00ec\u00ee\5\32\16\2\u00ed\u00e3\3\2\2")
        buf.write("\2\u00ed\u00ec\3\2\2\2\u00ee\31\3\2\2\2\u00ef\u00f0\7")
        buf.write("\27\2\2\u00f0\u00f1\5\32\16\2\u00f1\u00f2\7\62\2\2\u00f2")
        buf.write("\u00f3\5 \21\2\u00f3\u00f4\7\63\2\2\u00f4\u00f7\3\2\2")
        buf.write("\2\u00f5\u00f7\5\34\17\2\u00f6\u00ef\3\2\2\2\u00f6\u00f5")
        buf.write("\3\2\2\2\u00f7\33\3\2\2\2\u00f8\u00f9\7\62\2\2\u00f9\u00fa")
        buf.write("\5\4\3\2\u00fa\u00fb\7\63\2\2\u00fb\u00fe\3\2\2\2\u00fc")
        buf.write("\u00fe\5\36\20\2\u00fd\u00f8\3\2\2\2\u00fd\u00fc\3\2\2")
        buf.write("\2\u00fe\35\3\2\2\2\u00ff\u0104\7>\2\2\u0100\u0104\7\31")
        buf.write("\2\2\u0101\u0104\5\u0080A\2\u0102\u0104\7\20\2\2\u0103")
        buf.write("\u00ff\3\2\2\2\u0103\u0100\3\2\2\2\u0103\u0101\3\2\2\2")
        buf.write("\u0103\u0102\3\2\2\2\u0104\37\3\2\2\2\u0105\u0106\5\4")
        buf.write("\3\2\u0106\u0107\5\"\22\2\u0107\u010a\3\2\2\2\u0108\u010a")
        buf.write("\3\2\2\2\u0109\u0105\3\2\2\2\u0109\u0108\3\2\2\2\u010a")
        buf.write("!\3\2\2\2\u010b\u010c\7/\2\2\u010c\u010d\5\4\3\2\u010d")
        buf.write("\u010e\5\"\22\2\u010e\u0111\3\2\2\2\u010f\u0111\3\2\2")
        buf.write("\2\u0110\u010b\3\2\2\2\u0110\u010f\3\2\2\2\u0111#\3\2")
        buf.write("\2\2\u0112\u0115\t\6\2\2\u0113\u0116\5*\26\2\u0114\u0116")
        buf.write("\5&\24\2\u0115\u0113\3\2\2\2\u0115\u0114\3\2\2\2\u0116")
        buf.write("\u0117\3\2\2\2\u0117\u0118\7.\2\2\u0118%\3\2\2\2\u0119")
        buf.write("\u011a\t\7\2\2\u011a\u011b\5(\25\2\u011b\u011c\5\4\3\2")
        buf.write("\u011c\'\3\2\2\2\u011d\u011e\7/\2\2\u011e\u011f\t\7\2")
        buf.write("\2\u011f\u0120\5(\25\2\u0120\u0121\5\4\3\2\u0121\u0122")
        buf.write("\7/\2\2\u0122\u0128\3\2\2\2\u0123\u0124\7\60\2\2\u0124")
        buf.write("\u0125\5~@\2\u0125\u0126\7\"\2\2\u0126\u0128\3\2\2\2\u0127")
        buf.write("\u011d\3\2\2\2\u0127\u0123\3\2\2\2\u0128)\3\2\2\2\u0129")
        buf.write("\u012a\5,\27\2\u012a\u012b\7\60\2\2\u012b\u012c\5~@\2")
        buf.write("\u012c+\3\2\2\2\u012d\u0132\t\7\2\2\u012e\u012f\t\7\2")
        buf.write("\2\u012f\u0130\7/\2\2\u0130\u0132\5,\27\2\u0131\u012d")
        buf.write("\3\2\2\2\u0131\u012e\3\2\2\2\u0132-\3\2\2\2\u0133\u0136")
        buf.write("\t\6\2\2\u0134\u0137\5\64\33\2\u0135\u0137\5\60\31\2\u0136")
        buf.write("\u0134\3\2\2\2\u0136\u0135\3\2\2\2\u0137\u0138\3\2\2\2")
        buf.write("\u0138\u0139\7.\2\2\u0139/\3\2\2\2\u013a\u013b\7>\2\2")
        buf.write("\u013b\u013c\5\62\32\2\u013c\u013d\5\4\3\2\u013d\61\3")
        buf.write("\2\2\2\u013e\u013f\7/\2\2\u013f\u0140\7>\2\2\u0140\u0141")
        buf.write("\5\62\32\2\u0141\u0142\5\4\3\2\u0142\u0143\7/\2\2\u0143")
        buf.write("\u0149\3\2\2\2\u0144\u0145\7\60\2\2\u0145\u0146\5~@\2")
        buf.write("\u0146\u0147\7\"\2\2\u0147\u0149\3\2\2\2\u0148\u013e\3")
        buf.write("\2\2\2\u0148\u0144\3\2\2\2\u0149\63\3\2\2\2\u014a\u014b")
        buf.write("\5\66\34\2\u014b\u014c\7\60\2\2\u014c\u014d\5~@\2\u014d")
        buf.write("\65\3\2\2\2\u014e\u0153\7>\2\2\u014f\u0150\7>\2\2\u0150")
        buf.write("\u0151\7/\2\2\u0151\u0153\5\66\34\2\u0152\u014e\3\2\2")
        buf.write("\2\u0152\u014f\3\2\2\2\u0153\67\3\2\2\2\u0154\u0155\7")
        buf.write("\n\2\2\u0155\u0156\7\62\2\2\u0156\u0157\5:\36\2\u0157")
        buf.write("\u0158\7\63\2\2\u01589\3\2\2\2\u0159\u015a\5\4\3\2\u015a")
        buf.write("\u015b\5<\37\2\u015b\u015e\3\2\2\2\u015c\u015e\3\2\2\2")
        buf.write("\u015d\u0159\3\2\2\2\u015d\u015c\3\2\2\2\u015e;\3\2\2")
        buf.write("\2\u015f\u0160\7/\2\2\u0160\u0161\5\4\3\2\u0161\u0162")
        buf.write("\5<\37\2\u0162\u0165\3\2\2\2\u0163\u0165\3\2\2\2\u0164")
        buf.write("\u015f\3\2\2\2\u0164\u0163\3\2\2\2\u0165=\3\2\2\2\u0166")
        buf.write("\u0167\7\n\2\2\u0167\u0168\7\64\2\2\u0168\u0169\5|?\2")
        buf.write("\u0169\u016a\7/\2\2\u016a\u016b\5\u0082B\2\u016b\u016c")
        buf.write("\7\65\2\2\u016c?\3\2\2\2\u016d\u016e\7\22\2\2\u016e\u0171")
        buf.write("\7>\2\2\u016f\u0170\7\60\2\2\u0170\u0172\7>\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173\u0174\7\66\2\2\u0174\u0175\5B\"\2\u0175\u0176\7")
        buf.write("\67\2\2\u0176A\3\2\2\2\u0177\u017c\5D#\2\u0178\u017c\5")
        buf.write("F$\2\u0179\u017c\5$\23\2\u017a\u017c\5H%\2\u017b\u0177")
        buf.write("\3\2\2\2\u017b\u0178\3\2\2\2\u017b\u0179\3\2\2\2\u017b")
        buf.write("\u017a\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2")
        buf.write("\u017d\u017e\3\2\2\2\u017eC\3\2\2\2\u017f\u017d\3\2\2")
        buf.write("\2\u0180\u0181\7\25\2\2\u0181\u0182\7\62\2\2\u0182\u0183")
        buf.write("\5J&\2\u0183\u0184\7\63\2\2\u0184\u0185\5l\67\2\u0185")
        buf.write("E\3\2\2\2\u0186\u0187\7\26\2\2\u0187\u0188\7\62\2\2\u0188")
        buf.write("\u0189\7\63\2\2\u0189\u018a\5l\67\2\u018aG\3\2\2\2\u018b")
        buf.write("\u018c\t\7\2\2\u018c\u018d\7\62\2\2\u018d\u018e\5J&\2")
        buf.write("\u018e\u018f\7\63\2\2\u018f\u0190\5l\67\2\u0190I\3\2\2")
        buf.write("\2\u0191\u0192\5N(\2\u0192\u0193\7\60\2\2\u0193\u0194")
        buf.write("\5~@\2\u0194\u0195\5L\'\2\u0195\u0198\3\2\2\2\u0196\u0198")
        buf.write("\3\2\2\2\u0197\u0191\3\2\2\2\u0197\u0196\3\2\2\2\u0198")
        buf.write("K\3\2\2\2\u0199\u019a\7.\2\2\u019a\u019b\5N(\2\u019b\u019c")
        buf.write("\7\60\2\2\u019c\u019d\5~@\2\u019d\u019e\5L\'\2\u019e\u01a1")
        buf.write("\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u0199\3\2\2\2\u01a0")
        buf.write("\u019f\3\2\2\2\u01a1M\3\2\2\2\u01a2\u01a7\7>\2\2\u01a3")
        buf.write("\u01a4\7>\2\2\u01a4\u01a5\7/\2\2\u01a5\u01a7\5N(\2\u01a6")
        buf.write("\u01a2\3\2\2\2\u01a6\u01a3\3\2\2\2\u01a7O\3\2\2\2\u01a8")
        buf.write("\u01b6\7>\2\2\u01a9\u01b6\5X-\2\u01aa\u01b6\5`\61\2\u01ab")
        buf.write("\u01b6\5^\60\2\u01ac\u01b6\5d\63\2\u01ad\u01b6\5V,\2\u01ae")
        buf.write("\u01af\7\62\2\2\u01af\u01b0\5\4\3\2\u01b0\u01b1\7\63\2")
        buf.write("\2\u01b1\u01b6\3\2\2\2\u01b2\u01b6\7\20\2\2\u01b3\u01b6")
        buf.write("\5\u0080A\2\u01b4\u01b6\7\31\2\2\u01b5\u01a8\3\2\2\2\u01b5")
        buf.write("\u01a9\3\2\2\2\u01b5\u01aa\3\2\2\2\u01b5\u01ab\3\2\2\2")
        buf.write("\u01b5\u01ac\3\2\2\2\u01b5\u01ad\3\2\2\2\u01b5\u01ae\3")
        buf.write("\2\2\2\u01b5\u01b2\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b4")
        buf.write("\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\5R*\2\u01b8Q")
        buf.write("\3\2\2\2\u01b9\u01ba\7\64\2\2\u01ba\u01bb\5\4\3\2\u01bb")
        buf.write("\u01bc\7\65\2\2\u01bc\u01bd\5R*\2\u01bd\u01c3\3\2\2\2")
        buf.write("\u01be\u01bf\7\64\2\2\u01bf\u01c0\5\4\3\2\u01c0\u01c1")
        buf.write("\7\65\2\2\u01c1\u01c3\3\2\2\2\u01c2\u01b9\3\2\2\2\u01c2")
        buf.write("\u01be\3\2\2\2\u01c3S\3\2\2\2\u01c4\u01d0\5V,\2\u01c5")
        buf.write("\u01d0\7>\2\2\u01c6\u01d0\7\31\2\2\u01c7\u01d0\5`\61\2")
        buf.write("\u01c8\u01d0\5d\63\2\u01c9\u01d0\7\20\2\2\u01ca\u01cb")
        buf.write("\7\62\2\2\u01cb\u01cc\5\4\3\2\u01cc\u01cd\7\63\2\2\u01cd")
        buf.write("\u01d0\3\2\2\2\u01ce\u01d0\5\u0080A\2\u01cf\u01c4\3\2")
        buf.write("\2\2\u01cf\u01c5\3\2\2\2\u01cf\u01c6\3\2\2\2\u01cf\u01c7")
        buf.write("\3\2\2\2\u01cf\u01c8\3\2\2\2\u01cf\u01c9\3\2\2\2\u01cf")
        buf.write("\u01ca\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0U\3\2\2\2\u01d1")
        buf.write("\u01d2\7\27\2\2\u01d2\u01d3\7>\2\2\u01d3\u01d4\7\62\2")
        buf.write("\2\u01d4\u01d5\5 \21\2\u01d5\u01d6\7\63\2\2\u01d6W\3\2")
        buf.write("\2\2\u01d7\u01d8\5Z.\2\u01d8\u01d9\7\61\2\2\u01d9\u01da")
        buf.write("\7>\2\2\u01daY\3\2\2\2\u01db\u01dc\b.\1\2\u01dc\u01dd")
        buf.write("\5T+\2\u01dd\u01e9\3\2\2\2\u01de\u01df\f\4\2\2\u01df\u01e0")
        buf.write("\7\61\2\2\u01e0\u01e5\7>\2\2\u01e1\u01e2\7\62\2\2\u01e2")
        buf.write("\u01e3\5 \21\2\u01e3\u01e4\7\63\2\2\u01e4\u01e6\3\2\2")
        buf.write("\2\u01e5\u01e1\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e8")
        buf.write("\3\2\2\2\u01e7\u01de\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9")
        buf.write("\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea[\3\2\2\2\u01eb")
        buf.write("\u01e9\3\2\2\2\u01ec\u01ed\5Z.\2\u01ed\u01ee\7\61\2\2")
        buf.write("\u01ee\u01ef\7>\2\2\u01ef\u01f0\7\62\2\2\u01f0\u01f1\5")
        buf.write(" \21\2\u01f1\u01f2\7\63\2\2\u01f2]\3\2\2\2\u01f3\u01f4")
        buf.write("\5Z.\2\u01f4\u01f5\7\61\2\2\u01f5\u01f6\7>\2\2\u01f6\u01f7")
        buf.write("\7\62\2\2\u01f7\u01f8\5 \21\2\u01f8\u01f9\7\63\2\2\u01f9")
        buf.write("_\3\2\2\2\u01fa\u01fb\7>\2\2\u01fb\u01fc\7-\2\2\u01fc")
        buf.write("\u01fd\7?\2\2\u01fda\3\2\2\2\u01fe\u01ff\7>\2\2\u01ff")
        buf.write("\u0200\7-\2\2\u0200\u0201\7?\2\2\u0201\u0202\7\62\2\2")
        buf.write("\u0202\u0203\5 \21\2\u0203\u0204\7\63\2\2\u0204c\3\2\2")
        buf.write("\2\u0205\u0206\7>\2\2\u0206\u0207\7-\2\2\u0207\u0208\7")
        buf.write("?\2\2\u0208\u0209\7\62\2\2\u0209\u020a\5 \21\2\u020a\u020b")
        buf.write("\7\63\2\2\u020be\3\2\2\2\u020c\u0211\7>\2\2\u020d\u0211")
        buf.write("\5X-\2\u020e\u0211\5`\61\2\u020f\u0211\5P)\2\u0210\u020c")
        buf.write("\3\2\2\2\u0210\u020d\3\2\2\2\u0210\u020e\3\2\2\2\u0210")
        buf.write("\u020f\3\2\2\2\u0211g\3\2\2\2\u0212\u021b\5n8\2\u0213")
        buf.write("\u021b\5p9\2\u0214\u021b\5x=\2\u0215\u021b\5r:\2\u0216")
        buf.write("\u021b\5t;\2\u0217\u021b\5v<\2\u0218\u021b\5z>\2\u0219")
        buf.write("\u021b\5l\67\2\u021a\u0212\3\2\2\2\u021a\u0213\3\2\2\2")
        buf.write("\u021a\u0214\3\2\2\2\u021a\u0215\3\2\2\2\u021a\u0216\3")
        buf.write("\2\2\2\u021a\u0217\3\2\2\2\u021a\u0218\3\2\2\2\u021a\u0219")
        buf.write("\3\2\2\2\u021bi\3\2\2\2\u021c\u021f\5h\65\2\u021d\u021f")
        buf.write("\5.\30\2\u021e\u021c\3\2\2\2\u021e\u021d\3\2\2\2\u021f")
        buf.write("\u0222\3\2\2\2\u0220\u021e\3\2\2\2\u0220\u0221\3\2\2\2")
        buf.write("\u0221k\3\2\2\2\u0222\u0220\3\2\2\2\u0223\u0224\7\66\2")
        buf.write("\2\u0224\u0225\5j\66\2\u0225\u0226\7\67\2\2\u0226m\3\2")
        buf.write("\2\2\u0227\u0228\5f\64\2\u0228\u0229\7\"\2\2\u0229\u022a")
        buf.write("\5\4\3\2\u022a\u022b\7.\2\2\u022bo\3\2\2\2\u022c\u022d")
        buf.write("\7\6\2\2\u022d\u022e\7\62\2\2\u022e\u022f\5\4\3\2\u022f")
        buf.write("\u0230\7\63\2\2\u0230\u0239\5l\67\2\u0231\u0232\7\7\2")
        buf.write("\2\u0232\u0233\7\62\2\2\u0233\u0234\5\4\3\2\u0234\u0235")
        buf.write("\7\63\2\2\u0235\u0236\5l\67\2\u0236\u0238\3\2\2\2\u0237")
        buf.write("\u0231\3\2\2\2\u0238\u023b\3\2\2\2\u0239\u0237\3\2\2\2")
        buf.write("\u0239\u023a\3\2\2\2\u023a\u023e\3\2\2\2\u023b\u0239\3")
        buf.write("\2\2\2\u023c\u023d\7\b\2\2\u023d\u023f\5l\67\2\u023e\u023c")
        buf.write("\3\2\2\2\u023e\u023f\3\2\2\2\u023fq\3\2\2\2\u0240\u0241")
        buf.write("\7\4\2\2\u0241\u0242\7.\2\2\u0242s\3\2\2\2\u0243\u0244")
        buf.write("\7\5\2\2\u0244\u0245\7.\2\2\u0245u\3\2\2\2\u0246\u0248")
        buf.write("\7\21\2\2\u0247\u0249\5\4\3\2\u0248\u0247\3\2\2\2\u0248")
        buf.write("\u0249\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u024b\7.\2\2")
        buf.write("\u024bw\3\2\2\2\u024c\u024f\5\\/\2\u024d\u024f\5b\62\2")
        buf.write("\u024e\u024c\3\2\2\2\u024e\u024d\3\2\2\2\u024f\u0250\3")
        buf.write("\2\2\2\u0250\u0251\7.\2\2\u0251y\3\2\2\2\u0252\u0253\7")
        buf.write("\t\2\2\u0253\u0254\7\62\2\2\u0254\u0255\7>\2\2\u0255\u0256")
        buf.write("\7\13\2\2\u0256\u0257\5\4\3\2\u0257\u0258\78\2\2\u0258")
        buf.write("\u025b\5\4\3\2\u0259\u025a\7\30\2\2\u025a\u025c\5\4\3")
        buf.write("\2\u025b\u0259\3\2\2\2\u025b\u025c\3\2\2\2\u025c\u025d")
        buf.write("\3\2\2\2\u025d\u025e\7\63\2\2\u025e\u025f\5l\67\2\u025f")
        buf.write("{\3\2\2\2\u0260\u0266\7\f\2\2\u0261\u0266\7\r\2\2\u0262")
        buf.write("\u0266\7\16\2\2\u0263\u0266\7\17\2\2\u0264\u0266\5> \2")
        buf.write("\u0265\u0260\3\2\2\2\u0265\u0261\3\2\2\2\u0265\u0262\3")
        buf.write("\2\2\2\u0265\u0263\3\2\2\2\u0265\u0264\3\2\2\2\u0266}")
        buf.write("\3\2\2\2\u0267\u026e\7\f\2\2\u0268\u026e\7\r\2\2\u0269")
        buf.write("\u026e\7\17\2\2\u026a\u026e\7\16\2\2\u026b\u026e\5> \2")
        buf.write("\u026c\u026e\7>\2\2\u026d\u0267\3\2\2\2\u026d\u0268\3")
        buf.write("\2\2\2\u026d\u0269\3\2\2\2\u026d\u026a\3\2\2\2\u026d\u026b")
        buf.write("\3\2\2\2\u026d\u026c\3\2\2\2\u026e\177\3\2\2\2\u026f\u0275")
        buf.write("\79\2\2\u0270\u0275\7:\2\2\u0271\u0275\7;\2\2\u0272\u0275")
        buf.write("\7\3\2\2\u0273\u0275\58\35\2\u0274\u026f\3\2\2\2\u0274")
        buf.write("\u0270\3\2\2\2\u0274\u0271\3\2\2\2\u0274\u0272\3\2\2\2")
        buf.write("\u0274\u0273\3\2\2\2\u0275\u0081\3\2\2\2\u0276\u0277\6")
        buf.write("B\b\2\u0277\u0278\79\2\2\u0278\u0083\3\2\2\2\u0279\u027a")
        buf.write("\t\b\2\2\u027a\u0085\3\2\2\2\63\u0089\u0094\u009b\u00a5")
        buf.write("\u00b0\u00bb\u00c1\u00c6\u00cf\u00dc\u00e0\u00ea\u00ed")
        buf.write("\u00f6\u00fd\u0103\u0109\u0110\u0115\u0127\u0131\u0136")
        buf.write("\u0148\u0152\u015d\u0164\u0171\u017b\u017d\u0197\u01a0")
        buf.write("\u01a6\u01b5\u01c2\u01cf\u01e5\u01e9\u0210\u021a\u021e")
        buf.write("\u0220\u0239\u023e\u0248\u024e\u025b\u0265\u026d\u0274")
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
    RULE_operand = 14
    RULE_listOfexpr = 15
    RULE_manyExpr = 16
    RULE_variableDecl = 17
    RULE_withASM = 18
    RULE_pair = 19
    RULE_withoutASM = 20
    RULE_manyVariable = 21
    RULE_variableDecl_func = 22
    RULE_withASM2 = 23
    RULE_pair2 = 24
    RULE_withoutASM2 = 25
    RULE_manyVariable2 = 26
    RULE_arrayLit = 27
    RULE_arrayAssignMember = 28
    RULE_arrayMemberList = 29
    RULE_arrayType = 30
    RULE_classDecl = 31
    RULE_classMember = 32
    RULE_constructorDecl = 33
    RULE_destructorDecl = 34
    RULE_methodDecl = 35
    RULE_parameterList = 36
    RULE_manyParam = 37
    RULE_manyID = 38
    RULE_expression_index = 39
    RULE_index_operator = 40
    RULE_scalar = 41
    RULE_instanceCreate = 42
    RULE_instanceAttr = 43
    RULE_exprInstanceAttr = 44
    RULE_instanceMethod = 45
    RULE_stmInstanceMethod = 46
    RULE_staticAttr = 47
    RULE_staticMethod = 48
    RULE_stmStaticMethod = 49
    RULE_lhs = 50
    RULE_stmt = 51
    RULE_stmt_List = 52
    RULE_stmt_block = 53
    RULE_stmt_Assignment = 54
    RULE_stmt_If = 55
    RULE_stmt_Break = 56
    RULE_stmt_Continue = 57
    RULE_stmt_Return = 58
    RULE_stmt_MethodInvocation = 59
    RULE_stmt_ForIn = 60
    RULE_typeDataPrimitive = 61
    RULE_mptype = 62
    RULE_literal = 63
    RULE_size = 64
    RULE_relational_op = 65

    ruleNames =  [ "program", "expr", "expr0", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "expr8", "expr9", 
                   "expr10", "expr11", "operand", "listOfexpr", "manyExpr", 
                   "variableDecl", "withASM", "pair", "withoutASM", "manyVariable", 
                   "variableDecl_func", "withASM2", "pair2", "withoutASM2", 
                   "manyVariable2", "arrayLit", "arrayAssignMember", "arrayMemberList", 
                   "arrayType", "classDecl", "classMember", "constructorDecl", 
                   "destructorDecl", "methodDecl", "parameterList", "manyParam", 
                   "manyID", "expression_index", "index_operator", "scalar", 
                   "instanceCreate", "instanceAttr", "exprInstanceAttr", 
                   "instanceMethod", "stmInstanceMethod", "staticAttr", 
                   "staticMethod", "stmStaticMethod", "lhs", "stmt", "stmt_List", 
                   "stmt_block", "stmt_Assignment", "stmt_If", "stmt_Break", 
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
            self.state = 133 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 132
                self.classDecl()
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 137
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
            self.state = 139
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
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.expr1()
                self.state = 142
                _la = self._input.LA(1)
                if not(_la==D96Parser.STR_CMP or _la==D96Parser.STR_CONCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 143
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
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
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.expr2(0)
                self.state = 149
                self.relational_op()
                self.state = 150
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
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
            self.state = 156
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 163
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 158
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 159
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 160
                    self.expr3(0) 
                self.state = 165
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
            self.state = 167
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 169
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 170
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 171
                    self.expr4(0) 
                self.state = 176
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
            self.state = 178
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 180
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 181
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLY) | (1 << D96Parser.DEVIDE) | (1 << D96Parser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 182
                    self.expr5() 
                self.state = 187
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
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(D96Parser.NOT)
                self.state = 189
                self.expr5()
                pass
            elif token in [D96Parser.BOOL_NUM, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.LB, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
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
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(D96Parser.MINUS)
                self.state = 194
                self.expr6()
                pass
            elif token in [D96Parser.BOOL_NUM, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
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


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


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
            self.state = 199
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 201
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 202
                    self.index_operator() 
                self.state = 207
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
            self.state = 209
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 211
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 212
                    self.match(D96Parser.DOT)
                    self.state = 213
                    self.match(D96Parser.ID)
                    self.state = 218
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        self.state = 214
                        self.match(D96Parser.LB)
                        self.state = 215
                        self.listOfexpr()
                        self.state = 216
                        self.match(D96Parser.RB)

             
                self.state = 224
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
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(D96Parser.ID)
                self.state = 226
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 227
                self.match(D96Parser.STATIC_ID)
                self.state = 232
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 228
                    self.match(D96Parser.LB)
                    self.state = 229
                    self.listOfexpr()
                    self.state = 230
                    self.match(D96Parser.RB)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
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
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(D96Parser.NEW)
                self.state = 238
                self.expr10()
                self.state = 239
                self.match(D96Parser.LB)
                self.state = 240
                self.listOfexpr()
                self.state = 241
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOL_NUM, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.LB, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
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

        def operand(self):
            return self.getTypedRuleContext(D96Parser.OperandContext,0)


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
                self.state = 246
                self.match(D96Parser.LB)
                self.state = 247
                self.expr()
                self.state = 248
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOL_NUM, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.operand()
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


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = D96Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_operand)
        try:
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.BOOL_NUM, D96Parser.ARRAY, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 255
                self.literal()
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 256
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
        self.enterRule(localctx, 30, self.RULE_listOfexpr)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOL_NUM, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NOT, D96Parser.LB, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.expr()
                self.state = 260
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
        self.enterRule(localctx, 32, self.RULE_manyExpr)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(D96Parser.COMMA)
                self.state = 266
                self.expr()
                self.state = 267
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
        self.enterRule(localctx, 34, self.RULE_variableDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 273
                self.withoutASM()
                pass

            elif la_ == 2:
                self.state = 274
                self.withASM()
                pass


            self.state = 277
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
        self.enterRule(localctx, 36, self.RULE_withASM)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.STATIC_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 280
            self.pair()
            self.state = 281
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
        self.enterRule(localctx, 38, self.RULE_pair)
        self._la = 0 # Token type
        try:
            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(D96Parser.COMMA)
                self.state = 284
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.STATIC_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 285
                self.pair()
                self.state = 286
                self.expr()
                self.state = 287
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.match(D96Parser.COLON)
                self.state = 290
                self.mptype()
                self.state = 291
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


        def getRuleIndex(self):
            return D96Parser.RULE_withoutASM

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWithoutASM" ):
                return visitor.visitWithoutASM(self)
            else:
                return visitor.visitChildren(self)




    def withoutASM(self):

        localctx = D96Parser.WithoutASMContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_withoutASM)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.manyVariable()
            self.state = 296
            self.match(D96Parser.COLON)
            self.state = 297
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

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def manyVariable(self):
            return self.getTypedRuleContext(D96Parser.ManyVariableContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_manyVariable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManyVariable" ):
                return visitor.visitManyVariable(self)
            else:
                return visitor.visitChildren(self)




    def manyVariable(self):

        localctx = D96Parser.ManyVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_manyVariable)
        self._la = 0 # Token type
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.STATIC_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.STATIC_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 301
                self.match(D96Parser.COMMA)
                self.state = 302
                self.manyVariable()
                pass


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
        self.enterRule(localctx, 44, self.RULE_variableDecl_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 306
                self.withoutASM2()
                pass

            elif la_ == 2:
                self.state = 307
                self.withASM2()
                pass


            self.state = 310
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
        self.enterRule(localctx, 46, self.RULE_withASM2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(D96Parser.ID)
            self.state = 313
            self.pair2()
            self.state = 314
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
        self.enterRule(localctx, 48, self.RULE_pair2)
        try:
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(D96Parser.COMMA)
                self.state = 317
                self.match(D96Parser.ID)
                self.state = 318
                self.pair2()
                self.state = 319
                self.expr()
                self.state = 320
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.match(D96Parser.COLON)
                self.state = 323
                self.mptype()
                self.state = 324
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
        self.enterRule(localctx, 50, self.RULE_withoutASM2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.manyVariable2()
            self.state = 329
            self.match(D96Parser.COLON)
            self.state = 330
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

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
        self.enterRule(localctx, 52, self.RULE_manyVariable2)
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.match(D96Parser.ID)
                self.state = 334
                self.match(D96Parser.COMMA)
                self.state = 335
                self.manyVariable2()
                pass


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
        self.enterRule(localctx, 54, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(D96Parser.ARRAY)
            self.state = 339
            self.match(D96Parser.LB)
            self.state = 340
            self.arrayAssignMember()
            self.state = 341
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
        self.enterRule(localctx, 56, self.RULE_arrayAssignMember)
        try:
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOL_NUM, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NOT, D96Parser.LB, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.expr()
                self.state = 344
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
        self.enterRule(localctx, 58, self.RULE_arrayMemberList)
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.match(D96Parser.COMMA)
                self.state = 350
                self.expr()
                self.state = 351
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
        self.enterRule(localctx, 60, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(D96Parser.ARRAY)
            self.state = 357
            self.match(D96Parser.LSB)
            self.state = 358
            self.typeDataPrimitive()
            self.state = 359
            self.match(D96Parser.COMMA)
            self.state = 360
            self.size()
            self.state = 361
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
        self.enterRule(localctx, 62, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(D96Parser.CLASS)
            self.state = 364
            self.match(D96Parser.ID)
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 365
                self.match(D96Parser.COLON)
                self.state = 366
                self.match(D96Parser.ID)


            self.state = 369
            self.match(D96Parser.LCB)
            self.state = 370
            self.classMember()
            self.state = 371
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

        def constructorDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ConstructorDeclContext)
            else:
                return self.getTypedRuleContext(D96Parser.ConstructorDeclContext,i)


        def destructorDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.DestructorDeclContext)
            else:
                return self.getTypedRuleContext(D96Parser.DestructorDeclContext,i)


        def variableDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.VariableDeclContext)
            else:
                return self.getTypedRuleContext(D96Parser.VariableDeclContext,i)


        def methodDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.MethodDeclContext)
            else:
                return self.getTypedRuleContext(D96Parser.MethodDeclContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_classMember

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassMember" ):
                return visitor.visitClassMember(self)
            else:
                return visitor.visitChildren(self)




    def classMember(self):

        localctx = D96Parser.ClassMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_classMember)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.STATIC_ID))) != 0):
                self.state = 377
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.CONSTRUCTOR]:
                    self.state = 373
                    self.constructorDecl()
                    pass
                elif token in [D96Parser.DESTRUCTOR]:
                    self.state = 374
                    self.destructorDecl()
                    pass
                elif token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 375
                    self.variableDecl()
                    pass
                elif token in [D96Parser.ID, D96Parser.STATIC_ID]:
                    self.state = 376
                    self.methodDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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

        def stmt_block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructorDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructorDecl" ):
                return visitor.visitConstructorDecl(self)
            else:
                return visitor.visitChildren(self)




    def constructorDecl(self):

        localctx = D96Parser.ConstructorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_constructorDecl)
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
            self.stmt_block()
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

        def stmt_block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructorDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructorDecl" ):
                return visitor.visitDestructorDecl(self)
            else:
                return visitor.visitChildren(self)




    def destructorDecl(self):

        localctx = D96Parser.DestructorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_destructorDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(D96Parser.DESTRUCTOR)
            self.state = 389
            self.match(D96Parser.LB)
            self.state = 390
            self.match(D96Parser.RB)
            self.state = 391
            self.stmt_block()
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

        def stmt_block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_blockContext,0)


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
        self.enterRule(localctx, 70, self.RULE_methodDecl)
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
            self.stmt_block()
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
        self.enterRule(localctx, 72, self.RULE_parameterList)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.manyID()
                self.state = 400
                self.match(D96Parser.COLON)
                self.state = 401
                self.mptype()
                self.state = 402
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


    class ManyParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

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
            self.state = 414
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(D96Parser.SEMI)
                self.state = 408
                self.manyID()
                self.state = 409
                self.match(D96Parser.COLON)
                self.state = 410
                self.mptype()
                self.state = 411
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

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
        self.enterRule(localctx, 76, self.RULE_manyID)
        try:
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.match(D96Parser.ID)
                self.state = 418
                self.match(D96Parser.COMMA)
                self.state = 419
                self.manyID()
                pass


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


        def stmInstanceMethod(self):
            return self.getTypedRuleContext(D96Parser.StmInstanceMethodContext,0)


        def stmStaticMethod(self):
            return self.getTypedRuleContext(D96Parser.StmStaticMethodContext,0)


        def instanceCreate(self):
            return self.getTypedRuleContext(D96Parser.InstanceCreateContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_index" ):
                return visitor.visitExpression_index(self)
            else:
                return visitor.visitChildren(self)




    def expression_index(self):

        localctx = D96Parser.Expression_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expression_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 422
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 423
                self.instanceAttr()
                pass

            elif la_ == 3:
                self.state = 424
                self.staticAttr()
                pass

            elif la_ == 4:
                self.state = 425
                self.stmInstanceMethod()
                pass

            elif la_ == 5:
                self.state = 426
                self.stmStaticMethod()
                pass

            elif la_ == 6:
                self.state = 427
                self.instanceCreate()
                pass

            elif la_ == 7:
                self.state = 428
                self.match(D96Parser.LB)
                self.state = 429
                self.expr()
                self.state = 430
                self.match(D96Parser.RB)
                pass

            elif la_ == 8:
                self.state = 432
                self.match(D96Parser.NULL)
                pass

            elif la_ == 9:
                self.state = 433
                self.literal()
                pass

            elif la_ == 10:
                self.state = 434
                self.match(D96Parser.SELF)
                pass


            self.state = 437
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

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = D96Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_index_operator)
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.match(D96Parser.LSB)
                self.state = 440
                self.expr()
                self.state = 441
                self.match(D96Parser.RSB)
                self.state = 442
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.match(D96Parser.LSB)
                self.state = 445
                self.expr()
                self.state = 446
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


        def stmStaticMethod(self):
            return self.getTypedRuleContext(D96Parser.StmStaticMethodContext,0)


        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


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
        self.enterRule(localctx, 82, self.RULE_scalar)
        try:
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.instanceCreate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 452
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 453
                self.staticAttr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 454
                self.stmStaticMethod()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 455
                self.match(D96Parser.NULL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 456
                self.match(D96Parser.LB)
                self.state = 457
                self.expr()
                self.state = 458
                self.match(D96Parser.RB)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 460
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
        self.enterRule(localctx, 84, self.RULE_instanceCreate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(D96Parser.NEW)
            self.state = 464
            self.match(D96Parser.ID)
            self.state = 465
            self.match(D96Parser.LB)
            self.state = 466
            self.listOfexpr()
            self.state = 467
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
        self.enterRule(localctx, 86, self.RULE_instanceAttr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.exprInstanceAttr(0)
            self.state = 470
            self.match(D96Parser.DOT)
            self.state = 471
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
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_exprInstanceAttr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.scalar()
            self._ctx.stop = self._input.LT(-1)
            self.state = 487
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ExprInstanceAttrContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprInstanceAttr)
                    self.state = 476
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 477
                    self.match(D96Parser.DOT)
                    self.state = 478
                    self.match(D96Parser.ID)
                    self.state = 483
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        self.state = 479
                        self.match(D96Parser.LB)
                        self.state = 480
                        self.listOfexpr()
                        self.state = 481
                        self.match(D96Parser.RB)

             
                self.state = 489
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
            return D96Parser.RULE_instanceMethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceMethod" ):
                return visitor.visitInstanceMethod(self)
            else:
                return visitor.visitChildren(self)




    def instanceMethod(self):

        localctx = D96Parser.InstanceMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_instanceMethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.exprInstanceAttr(0)
            self.state = 491
            self.match(D96Parser.DOT)
            self.state = 492
            self.match(D96Parser.ID)
            self.state = 493
            self.match(D96Parser.LB)
            self.state = 494
            self.listOfexpr()
            self.state = 495
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmInstanceMethodContext(ParserRuleContext):
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

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def listOfexpr(self):
            return self.getTypedRuleContext(D96Parser.ListOfexprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmInstanceMethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmInstanceMethod" ):
                return visitor.visitStmInstanceMethod(self)
            else:
                return visitor.visitChildren(self)




    def stmInstanceMethod(self):

        localctx = D96Parser.StmInstanceMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stmInstanceMethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.exprInstanceAttr(0)
            self.state = 498
            self.match(D96Parser.DOT)
            self.state = 499
            self.match(D96Parser.ID)
            self.state = 500
            self.match(D96Parser.LB)
            self.state = 501
            self.listOfexpr()
            self.state = 502
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
        self.enterRule(localctx, 94, self.RULE_staticAttr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(D96Parser.ID)
            self.state = 505
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 506
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
        self.enterRule(localctx, 96, self.RULE_staticMethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(D96Parser.ID)
            self.state = 509
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 510
            self.match(D96Parser.STATIC_ID)
            self.state = 511
            self.match(D96Parser.LB)
            self.state = 512
            self.listOfexpr()
            self.state = 513
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmStaticMethodContext(ParserRuleContext):
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
            return D96Parser.RULE_stmStaticMethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmStaticMethod" ):
                return visitor.visitStmStaticMethod(self)
            else:
                return visitor.visitChildren(self)




    def stmStaticMethod(self):

        localctx = D96Parser.StmStaticMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_stmStaticMethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(D96Parser.ID)
            self.state = 516
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 517
            self.match(D96Parser.STATIC_ID)
            self.state = 518
            self.match(D96Parser.LB)
            self.state = 519
            self.listOfexpr()
            self.state = 520
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
        self.enterRule(localctx, 100, self.RULE_lhs)
        try:
            self.state = 526
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 522
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 523
                self.instanceAttr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 524
                self.staticAttr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 525
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


        def stmt_block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 528
                self.stmt_Assignment()
                pass

            elif la_ == 2:
                self.state = 529
                self.stmt_If()
                pass

            elif la_ == 3:
                self.state = 530
                self.stmt_MethodInvocation()
                pass

            elif la_ == 4:
                self.state = 531
                self.stmt_Break()
                pass

            elif la_ == 5:
                self.state = 532
                self.stmt_Continue()
                pass

            elif la_ == 6:
                self.state = 533
                self.stmt_Return()
                pass

            elif la_ == 7:
                self.state = 534
                self.stmt_ForIn()
                pass

            elif la_ == 8:
                self.state = 535
                self.stmt_block()
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

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtContext,i)


        def variableDecl_func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.VariableDecl_funcContext)
            else:
                return self.getTypedRuleContext(D96Parser.VariableDecl_funcContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_List

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_List" ):
                return visitor.visitStmt_List(self)
            else:
                return visitor.visitChildren(self)




    def stmt_List(self):

        localctx = D96Parser.Stmt_ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_stmt_List)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOL_NUM) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.RETURN) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.LCB) | (1 << D96Parser.INT_NUM) | (1 << D96Parser.FLOAT_NUM) | (1 << D96Parser.STRING) | (1 << D96Parser.ID))) != 0):
                self.state = 540
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOL_NUM, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.NULL, D96Parser.RETURN, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.LCB, D96Parser.INT_NUM, D96Parser.FLOAT_NUM, D96Parser.STRING, D96Parser.ID]:
                    self.state = 538
                    self.stmt()
                    pass
                elif token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 539
                    self.variableDecl_func()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 544
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_blockContext(ParserRuleContext):
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
            return D96Parser.RULE_stmt_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_block" ):
                return visitor.visitStmt_block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_block(self):

        localctx = D96Parser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_stmt_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.match(D96Parser.LCB)
            self.state = 546
            self.stmt_List()
            self.state = 547
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
        self.enterRule(localctx, 108, self.RULE_stmt_Assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.lhs()
            self.state = 550
            self.match(D96Parser.ASSIGN)
            self.state = 551
            self.expr()
            self.state = 552
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

        def stmt_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Stmt_blockContext)
            else:
                return self.getTypedRuleContext(D96Parser.Stmt_blockContext,i)


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
        self.enterRule(localctx, 110, self.RULE_stmt_If)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.match(D96Parser.IF)
            self.state = 555
            self.match(D96Parser.LB)
            self.state = 556
            self.expr()
            self.state = 557
            self.match(D96Parser.RB)
            self.state = 558
            self.stmt_block()
            self.state = 567
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 559
                self.match(D96Parser.ELSEIF)
                self.state = 560
                self.match(D96Parser.LB)
                self.state = 561
                self.expr()
                self.state = 562
                self.match(D96Parser.RB)
                self.state = 563
                self.stmt_block()
                self.state = 569
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 572
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 570
                self.match(D96Parser.ELSE)
                self.state = 571
                self.stmt_block()


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
        self.enterRule(localctx, 112, self.RULE_stmt_Break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.match(D96Parser.BREAK)
            self.state = 575
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
        self.enterRule(localctx, 114, self.RULE_stmt_Continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            self.match(D96Parser.CONTINUE)
            self.state = 578
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
        self.enterRule(localctx, 116, self.RULE_stmt_Return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self.match(D96Parser.RETURN)
            self.state = 582
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOL_NUM) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUS) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.INT_NUM) | (1 << D96Parser.FLOAT_NUM) | (1 << D96Parser.STRING) | (1 << D96Parser.ID))) != 0):
                self.state = 581
                self.expr()


            self.state = 584
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
        self.enterRule(localctx, 118, self.RULE_stmt_MethodInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 586
                self.instanceMethod()
                pass

            elif la_ == 2:
                self.state = 587
                self.staticMethod()
                pass


            self.state = 590
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def DOUBLE_DOT(self):
            return self.getToken(D96Parser.DOUBLE_DOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_blockContext,0)


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
        self.enterRule(localctx, 120, self.RULE_stmt_ForIn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(D96Parser.FOREACH)
            self.state = 593
            self.match(D96Parser.LB)
            self.state = 594
            self.match(D96Parser.ID)
            self.state = 595
            self.match(D96Parser.IN)
            self.state = 596
            self.expr()
            self.state = 597
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 598
            self.expr()
            self.state = 601
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 599
                self.match(D96Parser.BY)
                self.state = 600
                self.expr()


            self.state = 603
            self.match(D96Parser.RB)
            self.state = 604
            self.stmt_block()
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
        self.enterRule(localctx, 122, self.RULE_typeDataPrimitive)
        try:
            self.state = 611
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 606
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 607
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 608
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 609
                self.match(D96Parser.STR)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 610
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
        self.enterRule(localctx, 124, self.RULE_mptype)
        try:
            self.state = 619
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 613
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 614
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.STR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 615
                self.match(D96Parser.STR)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 616
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 617
                self.arrayType()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 618
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
        self.enterRule(localctx, 126, self.RULE_literal)
        try:
            self.state = 626
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_NUM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 621
                self.match(D96Parser.INT_NUM)
                pass
            elif token in [D96Parser.FLOAT_NUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 622
                self.match(D96Parser.FLOAT_NUM)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 623
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.BOOL_NUM]:
                self.enterOuterAlt(localctx, 4)
                self.state = 624
                self.match(D96Parser.BOOL_NUM)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 625
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
        self.enterRule(localctx, 128, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 628
            if not self.checkZero(self.getCurrentToken().text)!=1:
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self.checkZero(self.getCurrentToken().text)!=1")
            self.state = 629
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
        self.enterRule(localctx, 130, self.RULE_relational_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
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
        self._predicates[44] = self.exprInstanceAttr_sempred
        self._predicates[64] = self.size_sempred
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
         

    def exprInstanceAttr_sempred(self, localctx:ExprInstanceAttrContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def size_sempred(self, localctx:SizeContext, predIndex:int):
            if predIndex == 6:
                return self.checkZero(self.getCurrentToken().text)!=1
         




