// Def I/O
module Mux2(
    input ctrlSignalmux2,
	input [4:0]input1_mux2, input2_mux2,
	output reg [4:0]output_mux2
);
// Conexiones


// Cuerpo del modulo
always@*
begin
	if(ctrlSignalmux2)
        begin
            output_mux2 = input1_mux2;
        end
    else
        begin
            output_mux2 = input2_mux2;
        end
end

endmodule
