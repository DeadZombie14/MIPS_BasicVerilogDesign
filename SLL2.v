// Def I/O
module SLL2(
	input [31:0]inputSLL2,
	output reg[7:0]outputSll2
);
// Conexiones


// Cuerpo del modulo
always@*
begin
    outputSll2[7:0] = inputSLL2[5:0] << 2;
end

endmodule
