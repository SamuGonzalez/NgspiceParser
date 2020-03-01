grammar NgspiceGrammar ;

//We parse line by line
code: linecode NL ;

//Define what types of line codes we parse
linecode: device
        | command
        | Commentline
        ;
//Device lines parse
//We identify the device in first place
device: resistance
      | capacitors
      | inductors
      | switch
      | voltage_source
      | current_source
      | lossless_line
      | lossy_line
      | rc_lines
      | diode
      | bjt
      | jfet
      | mesfet
      | mosfet
      ;

//We identify the ID and how many nodes have the device in second place
resistance: RID WS twonodes RVALUE values_params
          | RID WS twonodes RESISTANCE RVALUE values_params
          ;
capacitors: CID WS twonodes CVALUE values_params
          | CID WS twonodes values_params
          ;
inductors: LID WS twonodes LVALUE
         | LID WS twonodes values_params
         ;
switch: SWSID WS fournodes
      | SWWID WS twonodes ;
voltage_source: VID WS twonodes ;
current_source: IID WS twonodes ;
lossless_line: TID WS fournodes ;
lossy_line: OID WS fournodes ;
rc_lines: UID WS threenodes;
diode: DID WS twonodes;
bjt: QID WS threenodes
   | QID WS fournodes ;
jfet: JID WS fournodes ;
mesfet: ZID WS fournodes ;
mosfet: MID WS fournodes ;

//We identify the nodes in third place
twonodes: NODE WS NODE ;
threenodes: NODE WS NODE WS NODE ;
fournodes: NODE WS NODE WS NODE WS NODE ;

//We catch up the device name and node names in fourth place
RID: [rR] [a-zA-Z0-9]+ ;
CID: [cC] [a-zA-Z0-9]+ ;
LID: [lL] [a-zA-Z0-9]+ ;
SWSID: [sS] [a-zA-Z0-9]+ ;
SWWID: [wW] [a-zA-Z0-9]+ ;
VID: [vV] [a-zA-Z0-9]+ ;
IID: [iI] [a-zA-Z0-9]+ ;
TID: [tT] [a-zA-Z0-9]+ ;
OID: [oO] [a-zA-Z0-9]+ ;
UID: [uU] [a-zA-Z0-9]+ ;
DID: [dD] [a-zA-Z0-9]+ ;
QID: [qQ] [a-zA-Z0-9]+ ;
JID: [jJ] [a-zA-Z0-9]+ ;
ZID: [zZ] [a-zA-Z0-9]+ ;
MID: [mM] [a-zA-Z0-9]+ ;

NODE: [a-zA-Z0-9]+ ;

RVALUE: [0-9]+ ([fFpPnNuUmMkKgGtT]|([mM][eE][gG])|([mM][iI][lL]))? ;
RESISTANCE: [rR] WS+? '=' WS+?
          | [rR][eE][sS][iI][sS][tT][aA][nN][cC][eE] WS+? '=' WS+?
          ;
CVALUE: [0-9]+ ([fFpPnNuUmMkKgGtT]|([mM][eE][gG])|([mM][iI][lL]))? ;
LVALUE: [0-9]+ ([fFpPnNuUmMkKgGtT]|([mM][eE][gG])|([mM][iI][lL]))? ;

//We identify what command it is (including models and subcircuits)
command: '.' MODEL values_params
       | '.' SUBCKT values_params
       | '.' SUBCKT values_params '.' ENDS
       ;

values_params:
             | VALUES_CONTENTS
             | VALUES_CONTENTS '+' WS? '\n' values_params
             ;
VALUES_CONTENTS: [a-zA-Z0-9 \t=!<>+\-*/^.(){}[\]]+ ;

//model : MODEL resistor_model
//      | MODEL capacitor_model
//      | MODEL inductor_model
//      | MODEL vswitch_model
//      | MODEL cswitch_model
//      | MODEL rc_line_model
//      | MODEL lossy_line_model
//      | MODEL diode_model
//      | MODEL npn_bjt_model
//      | MODEL pnp_bjt_model
//      | MODEL njf_jfet_model
//      | MODEL pjf_jfet_model
//      | MODEL nmf_mesfet_model
//      | MODEL pmf_mesfet_model
//      | MODEL vdmos_powermos_model
//      | MODEL nmos_mosfet_model
//      | MODEL pmos_mosfet_model
//      ;

//subcircuit : SUBCKT ;

MODEL : [mM][oO][dD][eE][lL] ;
SUBCKT : [sS][uU][bB][cC][kK][tT] ;
ENDS : [eE][nN][dD][sS] ;

Commentline: '*' [a-zA-Z0-9 ]+
           | '$' [a-zA-Z0-9 ]+
           | '\\' [a-zA-Z0-9 ]+ ;


WS: [ \t]+ -> skip ;
NL: '\r'? '\n' ;