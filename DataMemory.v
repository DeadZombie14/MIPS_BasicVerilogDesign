// Def I/O
module DataMemory(
    input [31:0]memAddr,memData,
    input memReadFlag, memWriteFlag,
	output reg [31:0]data
);
// Conexiones 

// Memoria ASYNC
reg [31:0]dataMemory[31:0]; // 32 espacios de 32 bit

// Cuerpo del modulo
always@*
begin
   if(memWriteFlag)
   begin
        dataMemory[memAddr] <= memData;
   end 

   if(memReadFlag)
   begin
        data <= dataMemory[memAddr];   
   end
end

endmodule
