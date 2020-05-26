/* verilator lint_off UNOPTFLAT */
// Def I/O
module ADD4bit(
	input [3:0]a4bit, b4bit,
	input inputCarry4bit,
	output [3:0]sum4bit,
	output outputCarry4bit
);
// Conexiones
wire [2:0]carry4bit;

// Cuerpo del modulo
FullAdder FA_0(.aBit(a4bit[0]),.bBit(b4bit[0]),.inputCarry(inputCarry4bit),.sumBit(sum4bit[0]),.outputCarry(carry4bit[0]));
FullAdder FA_1(.aBit(a4bit[1]),.bBit(b4bit[1]),.inputCarry(carry4bit[0]),.sumBit(sum4bit[1]),.outputCarry(carry4bit[1]));
FullAdder FA_2(.aBit(a4bit[2]),.bBit(b4bit[2]),.inputCarry(carry4bit[1]),.sumBit(sum4bit[2]),.outputCarry(carry4bit[2]));
FullAdder FA_3(.aBit(a4bit[3]),.bBit(b4bit[3]),.inputCarry(carry4bit[2]),.sumBit(sum4bit[3]),.outputCarry(outputCarry4bit));

endmodule
