// Def I/O
module ADD16bit(
	input [15:0]a16bit, b16bit,
	input inputCarry16bit,
	output [15:0]sum16bit,
	output outputCarry16bit
);
// Conexiones
wire carry16bit;

// Cuerpo del modulo
ADD8bit A8_0(.a8bit(a16bit[7:0]),.b8bit(b16bit[7:0]),.inputCarry8bit(inputCarry16bit),.sum8bit(sum16bit[7:0]),.outputCarry8bit(carry16bit));
ADD8bit A8_1(.a8bit(a16bit[15:8]),.b8bit(b16bit[15:8]),.inputCarry8bit(carry16bit),.sum8bit(sum16bit[15:8]),.outputCarry8bit(outputCarry16bit));

endmodule
