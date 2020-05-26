// Def I/O
module BancoRegistros(
    input [31:0]wrData,
	input [4:0]rAddr1, rAddr2, wAddr,
    input regWriteFlag,
	output reg [31:0]regData1,regData2
);
// Conexiones 
// Memoria ASYNC
reg [31:0]registerBank[31:0]; // 32 espacios de 32 bit

// Cuerpo del modulo
always@*
begin
   regData1 = registerBank[rAddr1];
   regData2 = registerBank[rAddr2];

   if(regWriteFlag)
   begin
       if(wAddr[0])
            registerBank[wAddr] = wrData;
   end 
end

endmodule
