// Def I/O
module BF1(
    input [31:0]dIn1_BF1,dIn2_BF1,dIn3_BF1,
    input [4:0]dIn4_BF1,
    input [4:0]dIn5_BF1,
    input [7:0]dIn6_BF1,
    input clk_BF1,
	output reg [31:0]data1BF1,data2BF1,functBF1,
    output reg [4:0]rdBF1,
    output reg [4:0]rtBF1,
    output reg [7:0]nextIns_BF1
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
end

endmodule
