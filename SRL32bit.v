// Def I/O
module SRL32bit(
	input [31:0]aSRL32bit, bSRL32bit,
    input [4:0]rightShiftAmount,
	output [31:0]srl32bit
);
// Conexiones


// Cuerpo del modulo
assign srl32bit[31:0] = bSRL32bit[31:0] >> rightShiftAmount[4:0];

endmodule
