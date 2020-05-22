// Def I/O
module SLL2_J(
	input [25:0]inputSLL2_J,
	output reg[27:0]outputSll2_J
);
// Conexiones


// Cuerpo del modulo
always@*
begin
    outputSll2_J[27:0] = inputSLL2_J[25:0] << 2;
end

endmodule