// Def I/O
module Mux4(
    input jump_mux4,
	input [31:0]input1_mux4, 
    input [7:0]input2_mux4,
	output reg [7:0]output_mux4
);
// Conexiones


// Cuerpo del modulo
always@*
begin
	if(jump_mux4)
        begin
            output_mux4 = input1_mux4[7:0];
        end
    else
        begin
            output_mux4 = input2_mux4;
        end
end

endmodule