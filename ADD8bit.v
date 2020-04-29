// Def I/O
module ADD8bit(
	input [7:0]a8bit, b8bit,
	input inputCarry8bit,
	output [7:0]sum8bit,
	output outputCarry8bit
);
// Conexiones
wire carry8bit;

// Cuerpo del modulo
ADD4bit FA_0(.a4bit(a8bit[3:0]),.b4bit(b8bit[3:0]),.inputCarry4bit(inputCarry8bit),.sum4bit(sum8bit[3:0]),.outputCarry4bit(carry8bit));
ADD4bit FA_1(.a4bit(a8bit[7:4]),.b4bit(b8bit[7:4]),.inputCarry4bit(carry8bit),.sum4bit(sum8bit[7:4]),.outputCarry4bit(outputCarry8bit));

endmodule
