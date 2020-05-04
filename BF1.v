// Def I/O
module _BF1(
    input [7:0]nextInst_BF1_IN,
    input [31:0]regData1_BF1_IN,regData2_BF1_IN,rdshfunct_BF1_IN,
    input [4:0]rd_BF1_IN,
    input [4:0]rt_BF1_IN,
    input [2:0]M_BF1_IN,EX_BF1_IN, //Señales de Unidad de control(M,EX)
    input [1:0]WB_BF1_IN, //Señales de unidad de control WB
    input clk_BF1,
    output reg [2:0]WB_BF1,M_BF1, //señales de la unidad de control que van hacia el BF2
    output reg ALUSrc_BF1,ALUOp_BF1,RegDst, //Señales de la unidad de control utilizadas en ID/EX
    output reg [7:0]nextInst_BF1,
	output reg [31:0]regData1_BF1,regData2_BF1,rdshfunct_BF1,
    output reg [4:0]rd_BF1,
    output reg [4:0]rt_BF1
);
// Conexiones 


// Cuerpo del modulo
always@(posedge clk_BF1)
begin
   // ==== Señales de control ===
   M_BF1 <= M_BF1_IN; //Señales M
   WB_BF1 <= WB_BF1_IN; //Señales WB

   RegDst <= EX_BF1_IN[2]; //señal que va al MUX2
   ALUOp_BF1 <= EX_BF1_IN[1]; //señal que va a la ALU control
   ALUSrc_BF1 <= EX_BF1_IN[0]; //Señal que va al MUX1
   // ===========================

   nextInst_BF1 <= nextInst_BF1_IN; //Instruccion de adder
   regData1_BF1 <= regData1_BF1_IN; //Va al ALU
   regData2_BF1 <= regData2_BF1_IN; //Va al Mux1 y al BF2
   rdshfunct_BF1 <= rdshfunct_BF1_IN; // Bits 15-0 con SignE
   rd_BF1 <= rd_BF1_IN; // rd van al MUX2
   rt_BF1 <= rt_BF1_IN; // rt van al MUX2
end

endmodule
