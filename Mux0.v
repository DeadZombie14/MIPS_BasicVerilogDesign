// Def I/O
module Mux0(
    input ctrlSignalmux0,
	input [4:0]input1_mux0, input2_mux0,
	output reg [4:0]output_mux0
);
// Conexiones


// Cuerpo del modulo
always@*
begin
	if(ctrlSignalmux0)
        begin
            output_mux0 = input1_mux0;
        end
    else
        begin
            output_mux0 = input2_mux0;
        end
end

endmodule
