// Def I/O
module FullAdder(
	input aBit,bBit,inputCarry,
	output sumBit,outputCarry
);
// Conexiones
wire FAsum;
wire FAcarry1;
wire FAcarry2;

// Cuerpo del modulo
HalfAdder HA_1(.a(aBit),.b(bBit),.sum(FAsum),.carry(FAcarry1));
HalfAdder HA_2(.a(FAsum),.b(inputCarry),.sum(sumBit),.carry(FAcarry2));
assign outputCarry = FAcarry2 | FAcarry1;

endmodule
