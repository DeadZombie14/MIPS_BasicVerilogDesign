// Def I/O
module BF1(
    input [5:0]op,
    output reg [2:0],EX,M,
    output reg [1:0]WB
);
// Conexiones 


// Cuerpo del modulo
always@*
    begin
        case(op)
            6'b000000:
                begin
                EX = 3'b110; //Señales de: RegDst, ALUSrc y ALUOp
                M = 3'b000; //Señales de: Branch, MemRead y MemWrite
                WB = 2'b10; //Señales de: RegWrite y MemtoReg
                end
        endcase
    end
endmodule