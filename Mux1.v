// Def I/O
module Mux1(
    input ctrlSignalmux1,
	input [31:0]input1_mux1, input2_mux1,
	output reg [31:0]output_mux1
);
// Conexiones


// Cuerpo del modulo
always@*
begin
	if(ctrlSignalmux1)
        begin
            output_mux1 = input1_mux1;
        end
    else
        begin
            output_mux1 = input2_mux1;
        end
end

endmodule
