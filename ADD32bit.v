/* verilator lint_off PINCONNECTEMPTY */
// Def I/O
module ADD32bit(
	input [31:0]a32bit, b32bit,
	input inputCarry32bit,
	output [31:0]sum32bit
);
// Conexiones
wire carry32bit;

// Cuerpo del modulo
ADD16bit A16_0(.a16bit(a32bit[15:0]),.b16bit(b32bit[15:0]),.inputCarry16bit(inputCarry32bit),.sum16bit(sum32bit[15:0]),.outputCarry16bit(carry32bit));
ADD16bit A16_1(.a16bit(a32bit[31:16]),.b16bit(b32bit[31:16]),.inputCarry16bit(carry32bit),.sum16bit(sum32bit[31:16]),.outputCarry16bit());

endmodule
