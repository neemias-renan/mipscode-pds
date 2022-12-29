import { uInt } from '../../toolkit.js'

export default {
    addi: { 
        function: '001000', 
        type: 'a', 
        does: (rs, imm) => rs + imm
    },
    addiu: { 
        function: '001001', 
        type: 'a', 
        does: (rs, imm) => rs + uInt(imm)
    },
    andi: { 
        function: '001100', 
        type: 'a', 
        does: (rs, imm) => rs & imm },
    beq: { 
        function: '000100', 
        type: 'b', 
        does: null // (rs, rt) => if (rs === rt) jump(label)
    },
    bgez: { 
        function: '000001', 
        type: 'c', 
        does: null 
    },
    bgtz: { 
        function: '000111', 
        type: 'd', 
        does: null 
    },
    blez: { 
        function: '000110', 
        type: 'd', 
        does: null 
    },
    bltz: { 
        function: '000001', 
        type: 'd', 
        does: null 
    },
    bne: { 
        function: '000100', 
        type: 'b', 
        does: null // (rs, rt) => if (rs !== rt) jump(label)
    },

    /*
    lb	rt, imm(rs)	100000	
    lbu	rt, imm(rs)	100100	
    lh	rt, imm(rs)	100001	
    lhu	rt, imm(rs)	100101
    */

    lui: { 
        function: '001111', 
        type: 'f', 
        does: null 
    },

    lw: {
        function: '100011',
        type: 'e',
        does: null
    },
    /*
    lw	rt, imm(rs)	100011
    lwc1	rt, imm(rs)	110001
    */

    ori: { 
        function: '001101', 
        type: 'a', 
        does: (rs, imm) => rs | imm 
    },

    /*
    sb	rt, imm(rs)	101000	
    */

    slti: { 
        function: '001010', 
        type: 'a', 
        does: (rs, imm) => rs < imm ? 1 : 0 
    },
    sltiu: { 
        function: '001011', 
        type: 'a', 
        does: (rs, imm) => rs < uInt(imm) ? 1 : 0 
    },

    /*
    sh	rt, imm(rs)	101001	
    sw	rt, imm(rs)	101011	
    swc1  rt, imm(rs)	111001
    */
    
    xori: { 
        function: '001110', 
        type: 'a', 
        does: (rs, imm) => rs ^ imm 
    }
}
