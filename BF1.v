// Def I/O
module BF1(
    input [31:0]dIn1_BF1,dIn2_BF1,dIn3_BF1,
    input [4:0]dIn4_BF1,
    input [4:0]dIn5_BF1,
    input [7:0]dIn6_BF1,
    input [2:0]dIn8_BF1,dIn9_BF1, //Señales de Unidad de control(M,EX)
    input [1:0]dIn7_BF1, //Señales de unidad de control WB
    input clk_BF1,
	output reg [31:0]data1BF1,data2BF1,functBF1,
    output reg [4:0]rdBF1,
    output reg [4:0]rtBF1,
    output reg [7:0]nextIns_BF1,
    output reg [2:0]wbBF1,mBF1, //señales de la unidad de control que van hacia el BF2
    output reg ALUSrcBF1,ALUOpBF1,RegDst //Señales de la unidad de control utilizadas en ID/EX
);
// Conexiones 


// Cuerpo del modulo
always@(posedge clk_BF1)
begin
   data1BF1 <= dIn1_BF1; //Van al MUX1
   data2BF1 <= dIn2_BF1; //Van al MUX1
   functBF1 <= dIn3_BF1; // Funct con bits de SignE
   rdBF1 <= dIn4_BF1; // rd van al MUX2
   rtBF1 <= dIn5_BF1; // rt van al MUX2
   nextIns_BF1 <= dIn6_BF1; //Instruccion de adder
   wbBF1 <= dIn7_BF1; //señales WB
   mBF1 <= dIn8_BF1; //Señales M
   ALUSrcBF1 <= dIn9_BF1[0]; //Señal que va al MUX1
   ALUOpBF1 <= dIn9_BF1[1]; //señal que va a la ALU control
   RegDst <= dIn9_BF1[2]; //señal que va al MUX2
end

endmodule
