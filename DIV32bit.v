// Def I/O
module DIV32bit(
	input [31:0]aDiv32bit, bDiv32bit,
	output [31:0]div32bit
);
// Conexiones


// Cuerpo del modulo
assign div32bit[31:0] = aDiv32bit[31:0] / bDiv32bit[31:0];

endmodule
