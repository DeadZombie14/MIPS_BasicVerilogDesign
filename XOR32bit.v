// Def I/O
module XOR32bit(
	input [31:0]aXOR32bit, bXOR32bit,
	output [31:0]xor32bit
);
// Conexiones


// Cuerpo del modulo
assign xor32bit[31:0] = aXOR32bit[31:0] ^ bXOR32bit[31:0];

endmodule
