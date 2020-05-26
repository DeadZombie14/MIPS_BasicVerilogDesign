/* verilator lint_off WIDTH */
/* verilator lint_off UNDRIVEN */
// Def I/O
module InstMemory(
	input [7:0]instAddr,
	output reg [31:0]instruction
);
// Conexiones 
// Memoria ASYNC
reg [7:0]instBank[0:127]; // 128 espacios de 8 bits = 32 instrucciones (4 bytes por inst)

// Cuerpo del modulo
always@*
begin
   instruction = {instBank[instAddr],instBank[instAddr + 1],instBank[instAddr + 2],instBank[instAddr + 3]};
end

endmodule
