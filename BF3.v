// Def I/O
module BF3(
    input [31:0]data_BF3_IN,resALU_BF3_IN,
    input [4:0]mux2Output_BF3_IN,
    input [4:0]WB_BF3_IN,
    input clk_BF3,
	output reg [31:0]data_BF3,resALU_BF3,
    output reg [4:0]mux2Output_BF3_IN,
    output reg [4:0]WB_BF3,
    output reg RegWrite_BF3,MemtoReg_BF3 //Señales de la unidad de control utilizadas en ID/EX
);
// Conexiones 


// Cuerpo del modulo
always@(posedge clk_BF3)
begin
   data_BF3 <= data_BF3_IN[31:0]; //
   resALU_BF3 <= resALU_BF3_IN[31:0]; //
   mux2Output_BF3 <= mux2Output_BF3_IN[4:0]; //
   
   RegWrite_BF3 <= WB_BF3_IN[1]; //RegWrite
   MemtoReg_BF3 <= WB_BF3_IN[0]; //MemtoReg
end

endmodule
