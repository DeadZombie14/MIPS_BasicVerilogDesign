// Def I/O
module HalfAdder(
	input a,b,
	output sum,carry
);
// Conexiones

// Cuerpo del modulo
assign sum = a ^ b; // XOR
assign carry = a & b; // AND

endmodule
