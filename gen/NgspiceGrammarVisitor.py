# Generated from C:/Users/samug/PycharmProjects/NgspiceParser\NgspiceGrammar.g4 by ANTLR 4.8
from antlr4 import *

if __name__ is not None and "." in __name__:
    from gen.NgspiceGrammarParser import NgspiceGrammarParser
else:
    from gen.NgspiceGrammarParser import NgspiceGrammarParser


# This class defines a complete generic visitor for a parse tree produced by NgspiceGrammarParser.

class NgspiceGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NgspiceGrammarParser#code.
    def visitCode(self, ctx: NgspiceGrammarParser.CodeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#linecode.
    def visitLinecode(self, ctx: NgspiceGrammarParser.LinecodeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#device.
    def visitDevice(self, ctx: NgspiceGrammarParser.DeviceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#resistance.
    def visitResistance(self, ctx: NgspiceGrammarParser.ResistanceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#capacitors.
    def visitCapacitors(self, ctx: NgspiceGrammarParser.CapacitorsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#inductors.
    def visitInductors(self, ctx: NgspiceGrammarParser.InductorsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#switch.
    def visitSwitch(self, ctx: NgspiceGrammarParser.SwitchContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#voltage_source.
    def visitVoltage_source(self, ctx: NgspiceGrammarParser.Voltage_sourceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#current_source.
    def visitCurrent_source(self, ctx: NgspiceGrammarParser.Current_sourceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#lossless_line.
    def visitLossless_line(self, ctx: NgspiceGrammarParser.Lossless_lineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#lossy_line.
    def visitLossy_line(self, ctx: NgspiceGrammarParser.Lossy_lineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#rc_lines.
    def visitRc_lines(self, ctx: NgspiceGrammarParser.Rc_linesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#diode.
    def visitDiode(self, ctx: NgspiceGrammarParser.DiodeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#bjt.
    def visitBjt(self, ctx: NgspiceGrammarParser.BjtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#jfet.
    def visitJfet(self, ctx: NgspiceGrammarParser.JfetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#mesfet.
    def visitMesfet(self, ctx: NgspiceGrammarParser.MesfetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#mosfet.
    def visitMosfet(self, ctx: NgspiceGrammarParser.MosfetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#twonodes.
    def visitTwonodes(self, ctx: NgspiceGrammarParser.TwonodesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#threenodes.
    def visitThreenodes(self, ctx: NgspiceGrammarParser.ThreenodesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#fournodes.
    def visitFournodes(self, ctx: NgspiceGrammarParser.FournodesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#command.
    def visitCommand(self, ctx: NgspiceGrammarParser.CommandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NgspiceGrammarParser#values_params.
    def visitValues_params(self, ctx: NgspiceGrammarParser.Values_paramsContext):
        return self.visitChildren(ctx)


del NgspiceGrammarParser
