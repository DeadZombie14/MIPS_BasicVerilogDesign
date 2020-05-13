// Def I/O
module Mux3(
    input ctrlSignalmux3,
	input [31:0]input1_mux3, input2_mux3,
	output reg [31:0]output_mux3
);
// Conexiones


// Cuerpo del modulo
always@*
begin
	if(ctrlSignalmux3)
        begin
            output_mux3 = input1_mux3;
        end
    else
        begin
            output_mux3 = input2_mux3;
        end
end

endmodule
