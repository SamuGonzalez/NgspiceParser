# Generated from C:/Users/samug/PycharmProjects/NgspiceParser\NgspiceGrammar.g4 by ANTLR 4.8
from antlr4 import *

if __name__ is not None and "." in __name__:
    from gen.NgspiceGrammarParser import NgspiceGrammarParser
else:
    from gen.NgspiceGrammarParser import NgspiceGrammarParser


# This class defines a complete listener for a parse tree produced by NgspiceGrammarParser.
class NgspiceGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by NgspiceGrammarParser#code.
    def enterCode(self, ctx: NgspiceGrammarParser.CodeContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#code.
    def exitCode(self, ctx: NgspiceGrammarParser.CodeContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#linecode.
    def enterLinecode(self, ctx: NgspiceGrammarParser.LinecodeContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#linecode.
    def exitLinecode(self, ctx: NgspiceGrammarParser.LinecodeContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#device.
    def enterDevice(self, ctx: NgspiceGrammarParser.DeviceContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#device.
    def exitDevice(self, ctx: NgspiceGrammarParser.DeviceContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#resistance.
    def enterResistance(self, ctx: NgspiceGrammarParser.ResistanceContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#resistance.
    def exitResistance(self, ctx: NgspiceGrammarParser.ResistanceContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#capacitors.
    def enterCapacitors(self, ctx: NgspiceGrammarParser.CapacitorsContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#capacitors.
    def exitCapacitors(self, ctx: NgspiceGrammarParser.CapacitorsContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#inductors.
    def enterInductors(self, ctx: NgspiceGrammarParser.InductorsContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#inductors.
    def exitInductors(self, ctx: NgspiceGrammarParser.InductorsContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#switch.
    def enterSwitch(self, ctx: NgspiceGrammarParser.SwitchContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#switch.
    def exitSwitch(self, ctx: NgspiceGrammarParser.SwitchContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#voltage_source.
    def enterVoltage_source(self, ctx: NgspiceGrammarParser.Voltage_sourceContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#voltage_source.
    def exitVoltage_source(self, ctx: NgspiceGrammarParser.Voltage_sourceContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#current_source.
    def enterCurrent_source(self, ctx: NgspiceGrammarParser.Current_sourceContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#current_source.
    def exitCurrent_source(self, ctx: NgspiceGrammarParser.Current_sourceContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#lossless_line.
    def enterLossless_line(self, ctx: NgspiceGrammarParser.Lossless_lineContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#lossless_line.
    def exitLossless_line(self, ctx: NgspiceGrammarParser.Lossless_lineContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#lossy_line.
    def enterLossy_line(self, ctx: NgspiceGrammarParser.Lossy_lineContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#lossy_line.
    def exitLossy_line(self, ctx: NgspiceGrammarParser.Lossy_lineContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#rc_lines.
    def enterRc_lines(self, ctx: NgspiceGrammarParser.Rc_linesContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#rc_lines.
    def exitRc_lines(self, ctx: NgspiceGrammarParser.Rc_linesContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#diode.
    def enterDiode(self, ctx: NgspiceGrammarParser.DiodeContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#diode.
    def exitDiode(self, ctx: NgspiceGrammarParser.DiodeContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#bjt.
    def enterBjt(self, ctx: NgspiceGrammarParser.BjtContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#bjt.
    def exitBjt(self, ctx: NgspiceGrammarParser.BjtContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#jfet.
    def enterJfet(self, ctx: NgspiceGrammarParser.JfetContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#jfet.
    def exitJfet(self, ctx: NgspiceGrammarParser.JfetContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#mesfet.
    def enterMesfet(self, ctx: NgspiceGrammarParser.MesfetContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#mesfet.
    def exitMesfet(self, ctx: NgspiceGrammarParser.MesfetContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#mosfet.
    def enterMosfet(self, ctx: NgspiceGrammarParser.MosfetContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#mosfet.
    def exitMosfet(self, ctx: NgspiceGrammarParser.MosfetContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#twonodes.
    def enterTwonodes(self, ctx: NgspiceGrammarParser.TwonodesContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#twonodes.
    def exitTwonodes(self, ctx: NgspiceGrammarParser.TwonodesContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#threenodes.
    def enterThreenodes(self, ctx: NgspiceGrammarParser.ThreenodesContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#threenodes.
    def exitThreenodes(self, ctx: NgspiceGrammarParser.ThreenodesContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#fournodes.
    def enterFournodes(self, ctx: NgspiceGrammarParser.FournodesContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#fournodes.
    def exitFournodes(self, ctx: NgspiceGrammarParser.FournodesContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#command.
    def enterCommand(self, ctx: NgspiceGrammarParser.CommandContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#command.
    def exitCommand(self, ctx: NgspiceGrammarParser.CommandContext):
        pass

    # Enter a parse tree produced by NgspiceGrammarParser#values_params.
    def enterValues_params(self, ctx: NgspiceGrammarParser.Values_paramsContext):
        pass

    # Exit a parse tree produced by NgspiceGrammarParser#values_params.
    def exitValues_params(self, ctx: NgspiceGrammarParser.Values_paramsContext):
        pass


del NgspiceGrammarParser
