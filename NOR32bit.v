// Def I/O
module NOR32bit(
	input [31:0]aNOR32bit, bNOR32bit,
	output [31:0]nor32bit
);
// Conexiones


// Cuerpo del modulo
assign nor32bit[31:0] = ~(aNOR32bit[31:0] | bNOR32bit[31:0]);

endmodule
