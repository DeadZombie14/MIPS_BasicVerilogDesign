/* verilator lint_off UNUSED */
module ALU(
	input [31:0]x32bit, y32bit,
	input [3:0]sel,
	output reg [31:0]res32bit, 
	output reg zf
);
// Conexiones
wire [31:0]add32, sub32, mul32, div32, and32, or32, nor32, sll32, srl32, slt32, xor32, slti;

// Cuerpo
ADD32bit A32(.a32bit(x32bit[31:0]),.b32bit(y32bit[31:0]),.inputCarry32bit(1'b0),.sum32bit(add32[31:0]));
SUB32bit S32(.aSub32bit(x32bit[31:0]),.bSub32bit(y32bit[31:0]),.sub32bit(sub32[31:0]));
MUL32bit M32(.aMul32bit(x32bit[31:0]),.bMul32bit(y32bit[31:0]),.mul32bit(mul32[31:0]));
DIV32bit D32(.aDiv32bit(x32bit[31:0]),.bDiv32bit(y32bit[31:0]),.div32bit(div32[31:0]));
AND32bit AND32(.aAND32bit(x32bit[31:0]),.bAND32bit(y32bit[31:0]),.and32bit(and32[31:0]));
OR32bit	 OR32(.aOR32bit(x32bit[31:0]),.bOR32bit(y32bit[31:0]),.or32bit(or32[31:0]));	
NOR32bit NOR32(.aNOR32bit(x32bit[31:0]),.bNOR32bit(y32bit[31:0]),.nor32bit(nor32[31:0]));
SLT32bit SLT32(.aSLT32bit(x32bit[31:0]),.bSLT32bit(y32bit[31:0]),.slt32bit(slt32[31:0]));
XOR32bit XOR32(.aXOR32bit(x32bit[31:0]),.bXOR32bit(y32bit[31:0]),.xor32bit(xor32[31:0]));	
SLTi slti32(.aSLTi32bit(x32bit[31:0]),.bSLTi32bit(y32bit[31:0]),.slti32bit(slti[31:0]));

// Modulo always (multiplexor)
always@*
	begin		
		case(sel)
			4'b0000:
				begin
					res32bit[31:0] = add32[31:0]; // Suma
				end
			4'b0001:
				begin
					res32bit[31:0] = sub32[31:0]; // Resta
				end
			4'b0010:
				begin
					res32bit[31:0] = mul32[31:0]; // Multiplicación
				end
			4'b0011:
				begin
					res32bit[31:0] = div32[31:0]; // División
				end
			4'b0100:
				begin
					res32bit[31:0] = and32[31:0]; // AND
				end
			4'b0101:
				begin
					res32bit[31:0] = or32[31:0];  // OR
				end
			4'b0110:
				begin
					res32bit[31:0] = nor32[31:0];  // NOR
				end
			4'b0111:
				begin
					res32bit[31:0] = 32'b00000000000000000000000000000000; //Nop
				end
			4'b1001:
				begin
					res32bit[31:0] = slt32[31:0];  // Set On Less Than
				end
			4'b1010:
				begin
					res32bit[31:0] = xor32[31:0];  // XOR
				end
			4'b1011:
				begin
					res32bit[31:0] = slti[31:0]; //SLTI
				end 
			default:
				begin
					res32bit[31:0] = 32'b00000000000000000000000000000000;
				end
		endcase
		if(res32bit[0])
			zf = 1'b0;
		else
			zf = 1'b1;
	end
endmodule
