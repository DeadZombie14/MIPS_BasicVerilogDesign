// Def I/O
module MUL32bit(
	input [31:0]aMul32bit, bMul32bit,
	output [31:0]mul32bit
);
// Conexiones


// Cuerpo del modulo
assign mul32bit[31:0] = aMul32bit[31:0] * bMul32bit[31:0];

endmodule
