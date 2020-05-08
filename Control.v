// Def I/O
module Control(
    input [5:0]op,
    output reg [2:0]EX,M,
    output reg [1:0]WB
);
// Conexiones 


// Cuerpo del modulo
always@*
    begin
        case(op)
            6'b000000:
                begin
                EX = {1'b1, // RegDst
                      1'b1, // ALUOp
                      1'b0  // ALUSrc
                    };
                M =  {1'b0, // Branch
                      1'b0, // MemRead
                      1'b0  // MemWrite
                    };
                WB = {1'b1, // RegWrite
                      1'b0  // MemtoReg
                    };
                end
        endcase
    end
endmodule