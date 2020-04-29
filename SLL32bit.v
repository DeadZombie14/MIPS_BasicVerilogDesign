// Def I/O
module SLL32bit(
	input [31:0]aSLL32bit, bSLL32bit,
    input [4:0]leftShiftAmount,
	output [31:0]sll32bit
);
// Conexiones


// Cuerpo del modulo
assign sll32bit[31:0] = bSLL32bit[31:0] << leftShiftAmount[4:0];

endmodule
