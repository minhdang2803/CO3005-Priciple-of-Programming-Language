# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u023b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\5\2\u00a4\n\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3,\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\3")
        buf.write("8\39\39\39\3:\3:\3:\3:\3:\5:\u0184\n:\3:\7:\u0187\n:\f")
        buf.write(":\16:\u018a\13:\5:\u018c\n:\3;\3;\3;\5;\u0191\n;\3;\7")
        buf.write(";\u0194\n;\f;\16;\u0197\13;\5;\u0199\n;\3<\3<\3<\3<\3")
        buf.write("<\5<\u01a0\n<\3<\7<\u01a3\n<\f<\16<\u01a6\13<\5<\u01a8")
        buf.write("\n<\3=\3=\3=\3=\5=\u01ae\n=\3=\7=\u01b1\n=\f=\16=\u01b4")
        buf.write("\13=\5=\u01b6\n=\3>\3>\3>\3>\5>\u01bc\n>\3>\3>\3?\3?\3")
        buf.write("?\7?\u01c3\n?\f?\16?\u01c6\13?\3?\5?\u01c9\n?\3@\3@\5")
        buf.write("@\u01cd\n@\3@\6@\u01d0\n@\r@\16@\u01d1\3A\3A\7A\u01d6")
        buf.write("\nA\fA\16A\u01d9\13A\3B\3B\3B\3B\3B\3B\5B\u01e1\nB\3B")
        buf.write("\3B\3B\5B\u01e6\nB\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\3E\5")
        buf.write("E\u01f3\nE\3F\3F\7F\u01f7\nF\fF\16F\u01fa\13F\3F\3F\3")
        buf.write("F\3G\3G\3G\3H\3H\3I\3I\3I\3J\3J\7J\u0209\nJ\fJ\16J\u020c")
        buf.write("\13J\3J\3J\3J\3J\3K\6K\u0213\nK\rK\16K\u0214\3K\3K\3L")
        buf.write("\3L\7L\u021b\nL\fL\16L\u021e\13L\3M\3M\6M\u0222\nM\rM")
        buf.write("\16M\u0223\3N\3N\7N\u0228\nN\fN\16N\u022b\13N\3N\3N\3")
        buf.write("O\3O\3O\3P\3P\7P\u0234\nP\fP\16P\u0237\13P\3P\3P\3P\3")
        buf.write("\u020a\2Q\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y\2[\2]._/a\60c\61e\62g\63i\64k\65")
        buf.write("m\66o\67q8s\2u\2w\2y\2{9}\2\177\2\u0081\2\u0083:\u0085")
        buf.write("\2\u0087\2\u0089\2\u008b;\u008d\2\u008f\2\u0091\2\u0093")
        buf.write("<\u0095=\u0097>\u0099?\u009b@\u009dA\u009fB\3\2\24\4\2")
        buf.write("DDdd\3\2\63\63\3\2\62\63\3\2\63;\3\2\62;\4\2ZZzz\4\2\63")
        buf.write(";CH\4\2\62;CH\3\2\639\3\2\629\4\2\62;aa\4\2GGgg\4\2--")
        buf.write("//\t\2))^^ddhhppttvv\6\2\n\f\16\17$$^^\5\2\n\f\16\17\"")
        buf.write("\"\5\2C\\aac|\6\2\62;C\\aac|\2\u024c\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2")
        buf.write("e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2")
        buf.write("\2o\3\2\2\2\2q\3\2\2\2\2{\3\2\2\2\2\u0083\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\3\u00a3\3\2\2\2\5\u00a5\3\2\2\2\7\u00ab\3\2\2")
        buf.write("\2\t\u00b4\3\2\2\2\13\u00b7\3\2\2\2\r\u00be\3\2\2\2\17")
        buf.write("\u00c3\3\2\2\2\21\u00cb\3\2\2\2\23\u00d1\3\2\2\2\25\u00d4")
        buf.write("\3\2\2\2\27\u00d8\3\2\2\2\31\u00de\3\2\2\2\33\u00e6\3")
        buf.write("\2\2\2\35\u00ed\3\2\2\2\37\u00f2\3\2\2\2!\u00f9\3\2\2")
        buf.write("\2#\u00ff\3\2\2\2%\u0103\3\2\2\2\'\u0107\3\2\2\2)\u0113")
        buf.write("\3\2\2\2+\u011e\3\2\2\2-\u0122\3\2\2\2/\u0125\3\2\2\2")
        buf.write("\61\u012a\3\2\2\2\63\u012f\3\2\2\2\65\u0135\3\2\2\2\67")
        buf.write("\u0137\3\2\2\29\u0139\3\2\2\2;\u013b\3\2\2\2=\u013d\3")
        buf.write("\2\2\2?\u013f\3\2\2\2A\u0141\3\2\2\2C\u0143\3\2\2\2E\u0146")
        buf.write("\3\2\2\2G\u0149\3\2\2\2I\u014b\3\2\2\2K\u014d\3\2\2\2")
        buf.write("M\u0150\3\2\2\2O\u0153\3\2\2\2Q\u0156\3\2\2\2S\u0159\3")
        buf.write("\2\2\2U\u015d\3\2\2\2W\u0160\3\2\2\2Y\u0163\3\2\2\2[\u0165")
        buf.write("\3\2\2\2]\u0167\3\2\2\2_\u0169\3\2\2\2a\u016b\3\2\2\2")
        buf.write("c\u016d\3\2\2\2e\u016f\3\2\2\2g\u0171\3\2\2\2i\u0173\3")
        buf.write("\2\2\2k\u0175\3\2\2\2m\u0177\3\2\2\2o\u0179\3\2\2\2q\u017b")
        buf.write("\3\2\2\2s\u017e\3\2\2\2u\u0198\3\2\2\2w\u019a\3\2\2\2")
        buf.write("y\u01a9\3\2\2\2{\u01bb\3\2\2\2}\u01c8\3\2\2\2\177\u01ca")
        buf.write("\3\2\2\2\u0081\u01d3\3\2\2\2\u0083\u01e5\3\2\2\2\u0085")
        buf.write("\u01e9\3\2\2\2\u0087\u01ec\3\2\2\2\u0089\u01f2\3\2\2\2")
        buf.write("\u008b\u01f4\3\2\2\2\u008d\u01fe\3\2\2\2\u008f\u0201\3")
        buf.write("\2\2\2\u0091\u0203\3\2\2\2\u0093\u0206\3\2\2\2\u0095\u0212")
        buf.write("\3\2\2\2\u0097\u0218\3\2\2\2\u0099\u021f\3\2\2\2\u009b")
        buf.write("\u0225\3\2\2\2\u009d\u022e\3\2\2\2\u009f\u0231\3\2\2\2")
        buf.write("\u00a1\u00a4\5\61\31\2\u00a2\u00a4\5\63\32\2\u00a3\u00a1")
        buf.write("\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\4\3\2\2\2\u00a5\u00a6")
        buf.write("\7D\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9")
        buf.write("\7c\2\2\u00a9\u00aa\7m\2\2\u00aa\6\3\2\2\2\u00ab\u00ac")
        buf.write("\7E\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af")
        buf.write("\7v\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2")
        buf.write("\7w\2\2\u00b2\u00b3\7g\2\2\u00b3\b\3\2\2\2\u00b4\u00b5")
        buf.write("\7K\2\2\u00b5\u00b6\7h\2\2\u00b6\n\3\2\2\2\u00b7\u00b8")
        buf.write("\7G\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba\7u\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd\7h\2\2\u00bd\f")
        buf.write("\3\2\2\2\u00be\u00bf\7G\2\2\u00bf\u00c0\7n\2\2\u00c0\u00c1")
        buf.write("\7u\2\2\u00c1\u00c2\7g\2\2\u00c2\16\3\2\2\2\u00c3\u00c4")
        buf.write("\7H\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7")
        buf.write("\7g\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9\7e\2\2\u00c9\u00ca")
        buf.write("\7j\2\2\u00ca\20\3\2\2\2\u00cb\u00cc\7C\2\2\u00cc\u00cd")
        buf.write("\7t\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0")
        buf.write("\7{\2\2\u00d0\22\3\2\2\2\u00d1\u00d2\7K\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\24\3\2\2\2\u00d4\u00d5\7K\2\2\u00d5\u00d6")
        buf.write("\7p\2\2\u00d6\u00d7\7v\2\2\u00d7\26\3\2\2\2\u00d8\u00d9")
        buf.write("\7H\2\2\u00d9\u00da\7n\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7c\2\2\u00dc\u00dd\7v\2\2\u00dd\30\3\2\2\2\u00de\u00df")
        buf.write("\7D\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7q\2\2\u00e1\u00e2")
        buf.write("\7n\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5")
        buf.write("\7p\2\2\u00e5\32\3\2\2\2\u00e6\u00e7\7U\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb")
        buf.write("\7p\2\2\u00eb\u00ec\7i\2\2\u00ec\34\3\2\2\2\u00ed\u00ee")
        buf.write("\7P\2\2\u00ee\u00ef\7w\2\2\u00ef\u00f0\7n\2\2\u00f0\u00f1")
        buf.write("\7n\2\2\u00f1\36\3\2\2\2\u00f2\u00f3\7T\2\2\u00f3\u00f4")
        buf.write("\7g\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6\7w\2\2\u00f6\u00f7")
        buf.write("\7t\2\2\u00f7\u00f8\7p\2\2\u00f8 \3\2\2\2\u00f9\u00fa")
        buf.write("\7E\2\2\u00fa\u00fb\7n\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd")
        buf.write("\7u\2\2\u00fd\u00fe\7u\2\2\u00fe\"\3\2\2\2\u00ff\u0100")
        buf.write("\7X\2\2\u0100\u0101\7c\2\2\u0101\u0102\7n\2\2\u0102$\3")
        buf.write("\2\2\2\u0103\u0104\7X\2\2\u0104\u0105\7c\2\2\u0105\u0106")
        buf.write("\7t\2\2\u0106&\3\2\2\2\u0107\u0108\7E\2\2\u0108\u0109")
        buf.write("\7q\2\2\u0109\u010a\7p\2\2\u010a\u010b\7u\2\2\u010b\u010c")
        buf.write("\7v\2\2\u010c\u010d\7t\2\2\u010d\u010e\7w\2\2\u010e\u010f")
        buf.write("\7e\2\2\u010f\u0110\7v\2\2\u0110\u0111\7q\2\2\u0111\u0112")
        buf.write("\7t\2\2\u0112(\3\2\2\2\u0113\u0114\7F\2\2\u0114\u0115")
        buf.write("\7g\2\2\u0115\u0116\7u\2\2\u0116\u0117\7v\2\2\u0117\u0118")
        buf.write("\7t\2\2\u0118\u0119\7w\2\2\u0119\u011a\7e\2\2\u011a\u011b")
        buf.write("\7v\2\2\u011b\u011c\7q\2\2\u011c\u011d\7t\2\2\u011d*\3")
        buf.write("\2\2\2\u011e\u011f\7P\2\2\u011f\u0120\7g\2\2\u0120\u0121")
        buf.write("\7y\2\2\u0121,\3\2\2\2\u0122\u0123\7D\2\2\u0123\u0124")
        buf.write("\7{\2\2\u0124.\3\2\2\2\u0125\u0126\7U\2\2\u0126\u0127")
        buf.write("\7g\2\2\u0127\u0128\7n\2\2\u0128\u0129\7h\2\2\u0129\60")
        buf.write("\3\2\2\2\u012a\u012b\7V\2\2\u012b\u012c\7t\2\2\u012c\u012d")
        buf.write("\7w\2\2\u012d\u012e\7g\2\2\u012e\62\3\2\2\2\u012f\u0130")
        buf.write("\7H\2\2\u0130\u0131\7c\2\2\u0131\u0132\7n\2\2\u0132\u0133")
        buf.write("\7u\2\2\u0133\u0134\7g\2\2\u0134\64\3\2\2\2\u0135\u0136")
        buf.write("\7-\2\2\u0136\66\3\2\2\2\u0137\u0138\7/\2\2\u01388\3\2")
        buf.write("\2\2\u0139\u013a\7,\2\2\u013a:\3\2\2\2\u013b\u013c\7\61")
        buf.write("\2\2\u013c<\3\2\2\2\u013d\u013e\7\'\2\2\u013e>\3\2\2\2")
        buf.write("\u013f\u0140\7#\2\2\u0140@\3\2\2\2\u0141\u0142\7?\2\2")
        buf.write("\u0142B\3\2\2\2\u0143\u0144\7(\2\2\u0144\u0145\7(\2\2")
        buf.write("\u0145D\3\2\2\2\u0146\u0147\7~\2\2\u0147\u0148\7~\2\2")
        buf.write("\u0148F\3\2\2\2\u0149\u014a\7>\2\2\u014aH\3\2\2\2\u014b")
        buf.write("\u014c\7@\2\2\u014cJ\3\2\2\2\u014d\u014e\7>\2\2\u014e")
        buf.write("\u014f\7?\2\2\u014fL\3\2\2\2\u0150\u0151\7@\2\2\u0151")
        buf.write("\u0152\7?\2\2\u0152N\3\2\2\2\u0153\u0154\7?\2\2\u0154")
        buf.write("\u0155\7?\2\2\u0155P\3\2\2\2\u0156\u0157\7#\2\2\u0157")
        buf.write("\u0158\7?\2\2\u0158R\3\2\2\2\u0159\u015a\7?\2\2\u015a")
        buf.write("\u015b\7?\2\2\u015b\u015c\7\60\2\2\u015cT\3\2\2\2\u015d")
        buf.write("\u015e\7-\2\2\u015e\u015f\7\60\2\2\u015fV\3\2\2\2\u0160")
        buf.write("\u0161\7<\2\2\u0161\u0162\7<\2\2\u0162X\3\2\2\2\u0163")
        buf.write("\u0164\7&\2\2\u0164Z\3\2\2\2\u0165\u0166\7$\2\2\u0166")
        buf.write("\\\3\2\2\2\u0167\u0168\7=\2\2\u0168^\3\2\2\2\u0169\u016a")
        buf.write("\7.\2\2\u016a`\3\2\2\2\u016b\u016c\7<\2\2\u016cb\3\2\2")
        buf.write("\2\u016d\u016e\7\60\2\2\u016ed\3\2\2\2\u016f\u0170\7*")
        buf.write("\2\2\u0170f\3\2\2\2\u0171\u0172\7+\2\2\u0172h\3\2\2\2")
        buf.write("\u0173\u0174\7]\2\2\u0174j\3\2\2\2\u0175\u0176\7_\2\2")
        buf.write("\u0176l\3\2\2\2\u0177\u0178\7}\2\2\u0178n\3\2\2\2\u0179")
        buf.write("\u017a\7\177\2\2\u017ap\3\2\2\2\u017b\u017c\7\60\2\2\u017c")
        buf.write("\u017d\7\60\2\2\u017dr\3\2\2\2\u017e\u017f\7\62\2\2\u017f")
        buf.write("\u018b\t\2\2\2\u0180\u018c\7\62\2\2\u0181\u0188\t\3\2")
        buf.write("\2\u0182\u0184\7a\2\2\u0183\u0182\3\2\2\2\u0183\u0184")
        buf.write("\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0187\t\4\2\2\u0186")
        buf.write("\u0183\3\2\2\2\u0187\u018a\3\2\2\2\u0188\u0186\3\2\2\2")
        buf.write("\u0188\u0189\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188\3")
        buf.write("\2\2\2\u018b\u0180\3\2\2\2\u018b\u0181\3\2\2\2\u018ct")
        buf.write("\3\2\2\2\u018d\u0199\7\62\2\2\u018e\u0195\t\5\2\2\u018f")
        buf.write("\u0191\7a\2\2\u0190\u018f\3\2\2\2\u0190\u0191\3\2\2\2")
        buf.write("\u0191\u0192\3\2\2\2\u0192\u0194\t\6\2\2\u0193\u0190\3")
        buf.write("\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196")
        buf.write("\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195\3\2\2\2\u0198")
        buf.write("\u018d\3\2\2\2\u0198\u018e\3\2\2\2\u0199v\3\2\2\2\u019a")
        buf.write("\u019b\7\62\2\2\u019b\u01a7\t\7\2\2\u019c\u01a8\7\62\2")
        buf.write("\2\u019d\u01a4\t\b\2\2\u019e\u01a0\7a\2\2\u019f\u019e")
        buf.write("\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1")
        buf.write("\u01a3\t\t\2\2\u01a2\u019f\3\2\2\2\u01a3\u01a6\3\2\2\2")
        buf.write("\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a8\3")
        buf.write("\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u019c\3\2\2\2\u01a7\u019d")
        buf.write("\3\2\2\2\u01a8x\3\2\2\2\u01a9\u01b5\7\62\2\2\u01aa\u01b6")
        buf.write("\7\62\2\2\u01ab\u01b2\t\n\2\2\u01ac\u01ae\7a\2\2\u01ad")
        buf.write("\u01ac\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af\3\2\2\2")
        buf.write("\u01af\u01b1\t\13\2\2\u01b0\u01ad\3\2\2\2\u01b1\u01b4")
        buf.write("\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01aa\3\2\2\2")
        buf.write("\u01b5\u01ab\3\2\2\2\u01b6z\3\2\2\2\u01b7\u01bc\5s:\2")
        buf.write("\u01b8\u01bc\5y=\2\u01b9\u01bc\5u;\2\u01ba\u01bc\5w<\2")
        buf.write("\u01bb\u01b7\3\2\2\2\u01bb\u01b8\3\2\2\2\u01bb\u01b9\3")
        buf.write("\2\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be")
        buf.write("\b>\2\2\u01be|\3\2\2\2\u01bf\u01c9\t\6\2\2\u01c0\u01c4")
        buf.write("\t\5\2\2\u01c1\u01c3\t\f\2\2\u01c2\u01c1\3\2\2\2\u01c3")
        buf.write("\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2")
        buf.write("\u01c5\u01c7\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c9\t")
        buf.write("\6\2\2\u01c8\u01bf\3\2\2\2\u01c8\u01c0\3\2\2\2\u01c9~")
        buf.write("\3\2\2\2\u01ca\u01cc\t\r\2\2\u01cb\u01cd\t\16\2\2\u01cc")
        buf.write("\u01cb\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01cf\3\2\2\2")
        buf.write("\u01ce\u01d0\t\6\2\2\u01cf\u01ce\3\2\2\2\u01d0\u01d1\3")
        buf.write("\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u0080")
        buf.write("\3\2\2\2\u01d3\u01d7\7\60\2\2\u01d4\u01d6\t\6\2\2\u01d5")
        buf.write("\u01d4\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d8\u0082\3\2\2\2\u01d9\u01d7\3")
        buf.write("\2\2\2\u01da\u01e0\5}?\2\u01db\u01e1\5\u0081A\2\u01dc")
        buf.write("\u01e1\5\177@\2\u01dd\u01de\5\u0081A\2\u01de\u01df\5\177")
        buf.write("@\2\u01df\u01e1\3\2\2\2\u01e0\u01db\3\2\2\2\u01e0\u01dc")
        buf.write("\3\2\2\2\u01e0\u01dd\3\2\2\2\u01e1\u01e6\3\2\2\2\u01e2")
        buf.write("\u01e3\5\u0081A\2\u01e3\u01e4\5\177@\2\u01e4\u01e6\3\2")
        buf.write("\2\2\u01e5\u01da\3\2\2\2\u01e5\u01e2\3\2\2\2\u01e6\u01e7")
        buf.write("\3\2\2\2\u01e7\u01e8\bB\3\2\u01e8\u0084\3\2\2\2\u01e9")
        buf.write("\u01ea\7)\2\2\u01ea\u01eb\7$\2\2\u01eb\u0086\3\2\2\2\u01ec")
        buf.write("\u01ed\7^\2\2\u01ed\u01ee\t\17\2\2\u01ee\u0088\3\2\2\2")
        buf.write("\u01ef\u01f3\5\u0087D\2\u01f0\u01f3\n\20\2\2\u01f1\u01f3")
        buf.write("\5\u0085C\2\u01f2\u01ef\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2")
        buf.write("\u01f1\3\2\2\2\u01f3\u008a\3\2\2\2\u01f4\u01f8\5[.\2\u01f5")
        buf.write("\u01f7\5\u0089E\2\u01f6\u01f5\3\2\2\2\u01f7\u01fa\3\2")
        buf.write("\2\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fb")
        buf.write("\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fb\u01fc\5[.\2\u01fc\u01fd")
        buf.write("\bF\4\2\u01fd\u008c\3\2\2\2\u01fe\u01ff\7^\2\2\u01ff\u0200")
        buf.write("\n\17\2\2\u0200\u008e\3\2\2\2\u0201\u0202\13\2\2\2\u0202")
        buf.write("\u0090\3\2\2\2\u0203\u0204\7%\2\2\u0204\u0205\7%\2\2\u0205")
        buf.write("\u0092\3\2\2\2\u0206\u020a\5\u0091I\2\u0207\u0209\5\u008f")
        buf.write("H\2\u0208\u0207\3\2\2\2\u0209\u020c\3\2\2\2\u020a\u020b")
        buf.write("\3\2\2\2\u020a\u0208\3\2\2\2\u020b\u020d\3\2\2\2\u020c")
        buf.write("\u020a\3\2\2\2\u020d\u020e\5\u0091I\2\u020e\u020f\3\2")
        buf.write("\2\2\u020f\u0210\bJ\5\2\u0210\u0094\3\2\2\2\u0211\u0213")
        buf.write("\t\21\2\2\u0212\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214")
        buf.write("\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0216\3\2\2\2")
        buf.write("\u0216\u0217\bK\5\2\u0217\u0096\3\2\2\2\u0218\u021c\t")
        buf.write("\22\2\2\u0219\u021b\t\23\2\2\u021a\u0219\3\2\2\2\u021b")
        buf.write("\u021e\3\2\2\2\u021c\u021a\3\2\2\2\u021c\u021d\3\2\2\2")
        buf.write("\u021d\u0098\3\2\2\2\u021e\u021c\3\2\2\2\u021f\u0221\5")
        buf.write("Y-\2\u0220\u0222\t\23\2\2\u0221\u0220\3\2\2\2\u0222\u0223")
        buf.write("\3\2\2\2\u0223\u0221\3\2\2\2\u0223\u0224\3\2\2\2\u0224")
        buf.write("\u009a\3\2\2\2\u0225\u0229\5[.\2\u0226\u0228\5\u0089E")
        buf.write("\2\u0227\u0226\3\2\2\2\u0228\u022b\3\2\2\2\u0229\u0227")
        buf.write("\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u022c\3\2\2\2\u022b")
        buf.write("\u0229\3\2\2\2\u022c\u022d\bN\6\2\u022d\u009c\3\2\2\2")
        buf.write("\u022e\u022f\13\2\2\2\u022f\u0230\bO\7\2\u0230\u009e\3")
        buf.write("\2\2\2\u0231\u0235\5[.\2\u0232\u0234\5\u0089E\2\u0233")
        buf.write("\u0232\3\2\2\2\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2")
        buf.write("\u0235\u0236\3\2\2\2\u0236\u0238\3\2\2\2\u0237\u0235\3")
        buf.write("\2\2\2\u0238\u0239\5\u008dG\2\u0239\u023a\bP\b\2\u023a")
        buf.write("\u00a0\3\2\2\2 \2\u00a3\u0183\u0188\u018b\u0190\u0195")
        buf.write("\u0198\u019f\u01a4\u01a7\u01ad\u01b2\u01b5\u01bb\u01c4")
        buf.write("\u01c8\u01cc\u01d1\u01d7\u01e0\u01e5\u01f2\u01f8\u020a")
        buf.write("\u0214\u021c\u0223\u0229\u0235\t\3>\2\3B\3\3F\4\b\2\2")
        buf.write("\3N\5\3O\6\3P\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOL_NUM = 1
    BREAK = 2
    CONTINUE = 3
    IF = 4
    ELSEIF = 5
    ELSE = 6
    FOREACH = 7
    ARRAY = 8
    IN = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    STR = 13
    NULL = 14
    RETURN = 15
    CLASS = 16
    VAL = 17
    VAR = 18
    CONSTRUCTOR = 19
    DESTRUCTOR = 20
    NEW = 21
    BY = 22
    SELF = 23
    TRUE = 24
    FALSE = 25
    ADD = 26
    MINUS = 27
    MULTIPLY = 28
    DEVIDE = 29
    MODULO = 30
    NOT = 31
    ASSIGN = 32
    AND = 33
    OR = 34
    LESS_THAN = 35
    LARGER_THAN = 36
    LESS_THAN_OR_EQUAL = 37
    LARGER_THAN_OR_EQUAL = 38
    EQUAL = 39
    DIFFRENCE = 40
    STR_CMP = 41
    STR_CONCAT = 42
    DOUBLE_COLON = 43
    SEMI = 44
    COMMA = 45
    COLON = 46
    DOT = 47
    LB = 48
    RB = 49
    LSB = 50
    RSB = 51
    LCB = 52
    RCB = 53
    DOUBLE_DOT = 54
    INT_NUM = 55
    FLOAT_NUM = 56
    STRING = 57
    COMMENT = 58
    WS = 59
    ID = 60
    STATIC_ID = 61
    UNCLOSE_STRING = 62
    ERROR_CHAR = 63
    ILLEGAL_ESCAPE = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
            "'Null'", "'Return'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'", "'Self'", "'True'", "'False'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'='", "'&&'", "'||'", 
            "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'==.'", "'+.'", 
            "'::'", "';'", "','", "':'", "'.'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "'..'" ]

    symbolicNames = [ "<INVALID>",
            "BOOL_NUM", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STR", "NULL", "RETURN", 
            "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", 
            "SELF", "TRUE", "FALSE", "ADD", "MINUS", "MULTIPLY", "DEVIDE", 
            "MODULO", "NOT", "ASSIGN", "AND", "OR", "LESS_THAN", "LARGER_THAN", 
            "LESS_THAN_OR_EQUAL", "LARGER_THAN_OR_EQUAL", "EQUAL", "DIFFRENCE", 
            "STR_CMP", "STR_CONCAT", "DOUBLE_COLON", "SEMI", "COMMA", "COLON", 
            "DOT", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOUBLE_DOT", 
            "INT_NUM", "FLOAT_NUM", "STRING", "COMMENT", "WS", "ID", "STATIC_ID", 
            "UNCLOSE_STRING", "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BOOL_NUM", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                  "FOREACH", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STR", 
                  "NULL", "RETURN", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                  "DESTRUCTOR", "NEW", "BY", "SELF", "TRUE", "FALSE", "ADD", 
                  "MINUS", "MULTIPLY", "DEVIDE", "MODULO", "NOT", "ASSIGN", 
                  "AND", "OR", "LESS_THAN", "LARGER_THAN", "LESS_THAN_OR_EQUAL", 
                  "LARGER_THAN_OR_EQUAL", "EQUAL", "DIFFRENCE", "STR_CMP", 
                  "STR_CONCAT", "DOUBLE_COLON", "STATIC", "DOUBLEQUOTE", 
                  "SEMI", "COMMA", "COLON", "DOT", "LB", "RB", "LSB", "RSB", 
                  "LCB", "RCB", "DOUBLE_DOT", "INT_BIN", "INT_DEC", "INT_HEX", 
                  "INT_OCT", "INT_NUM", "INT_PART", "FLOAT_EXP", "FLOAT_DEC", 
                  "FLOAT_NUM", "QUOTE_IN_STR", "ESC_SEQ", "CHAR_STRING", 
                  "STRING", "ESCAPE_ILLEGAL", "LEGAL_COMMENT_STRING", "COMMENT_SIGN", 
                  "COMMENT", "WS", "ID", "STATIC_ID", "UNCLOSE_STRING", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:
            raise UncloseString(result.text[1:])
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text[1:])
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        else:
            return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[60] = self.INT_NUM_action 
            actions[64] = self.FLOAT_NUM_action 
            actions[68] = self.STRING_action 
            actions[76] = self.UNCLOSE_STRING_action 
            actions[77] = self.ERROR_CHAR_action 
            actions[78] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_NUM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def FLOAT_NUM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text=self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    raise UncloseString(self.text[1:])
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    raise ErrorToken(self.text)
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                    raise IllegalEscape(self.text[1:])
                
     


