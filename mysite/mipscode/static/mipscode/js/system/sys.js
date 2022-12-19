import memory from "./memory.js";
// import view from "./viewRegisters.js";
import { convertDecimalToAddressHex, formatAddress, convertHexToDecimal } from "./toolkit.js";
import { executeTypeI } from './ISA/I/execution.js'
import { executeTypeR } from './ISA/R/execution.js'
//import { executeTypeJ } from './ISA/J/execution.js'

import * as Console from './console.js'

const sys = { 
    regs: {
        $0: 0, $1: 0, $2: 0, $3: 0, $4: 0, $5: 0, $6: 0, $7: 0, $8: 0, $9: 0,
        $10: 0, $11: 0, $12: 0, $13: 0, $14: 0, $15: 0, $16: 0, $17: 0, $18: 0, $19: 0,
        $20: 0, $21: 0, $22: 0, $23: 0, $24: 0, $25: 0, $26: 0, $27: 0, $28: 0, $29: 0,
        $30: 0, $31: 0, pc: 0, hi: 0, lo: 0
    },
    memory,
    addressCount: 0,
    instructions: [],
    regsStackTimeline: [],
    viewInformations: [],
    lastInstructionExecuted: 0,
    initialAssembly: true
}

Object.prototype.Data = () => {}

Object.prototype.Text = () => {}

Object.prototype.Word = () => {}

Object.prototype.ToOutput = (data) => {}

Object.prototype.SetValueInViewRegister = (value, register) => {
    const reg = document.querySelector(`input[name="${register}"]`)
    reg.value = value
}

Object.prototype.Call = () => {
    if (sys.regs.$2 === 1) { // integer to print
        Console.dataOut(sys.regs.$4, 'value', '')
        return
    }

    else if (sys.regs.$2 === 2) console.log(sys.regs.$4.toFixed(2)); // float to print
    else if (sys.regs.$2 === 3) console.log(sys.regs.$4.toFixed(1)); // double to print
    else if (sys.regs.$2 === 5) {
        sys.regs.$2 = parseInt(prompt());
        sys.SetValueInViewRegister(sys.regs.$2, '$2')
    } // $2 contains integer read
    else if (sys.regs.$2 === 6) sys.regs.$2 = parseFloat(prompt()); // $2 contains float read
    else if (sys.regs.$2 === 7) sys.regs.$2 = parseFloat(prompt()); // $2 contains double read
    else if (sys.regs.$2 === 8) sys.regs.$2 = prompt(); // $2 contains string read
    // else if (sys.regs.$2 === 9) // allocate heap regs
    else if (sys.regs.$2 === 10) {
        Console.dataOut(null, 'exit', 'Programa finalizado!')
        sys.Clean();
    };

    // TODO: Completar chamada do sistema
}

Object.prototype.Clean = () => {
    sys.regs = {
        $0: 0, $1: 0, $2: 0, $3: 0, $4: 0, $5: 0, $6: 0, $7: 0, $8: 0, $9: 0,
        $10: 0, $11: 0, $12: 0, $13: 0, $14: 0, $15: 0, $16: 0, $17: 0, $18: 0, $19: 0,
        $20: 0, $21: 0, $22: 0, $23: 0, $24: 0, $25: 0, $26: 0, $27: 0, $28: 0, $29: 0,
        $30: 0, $31: 0, pc: 0, hi: 0, lo: 0
    }
    sys.addressCount = 0
    sys.instructions = []
    sys.regsStackTimeline = []
    sys.viewInformations = []
    sys.lastInstructionExecuted = 0
}

Object.prototype.OnlyLabel = (instruction, regsSpace) => {
    return {
        address: formatAddress(regsSpace), // 0x00000004
        onlyLabel: true,
        label: instruction.label
    }
}

Object.prototype.SetNextOnPc = () => {
    sys.regs.pc = convertHexToDecimal(sys.instructions[sys.lastInstructionExecuted].address)
}

Object.prototype.Execute = () => {
    //console.log('Execute()');
    const instruction = sys.instructions.find( instruction => instruction.address === convertDecimalToAddressHex( sys.regs.pc ) )
    //console.log(validAddress);
    //const instruction = sys.instructions.find( instruction => instruction.address === validAddress.address )
    //console.log(instruction);

    if (instruction.onlyLabel) {

    }

    if (instruction.does || instruction.syscall) { // instruction.does || instruction.syscall
        if (instruction.typing.type === "i") {
            return executeTypeI(instruction, sys)
        }
    
        if (instruction.typing.type === "r") {
            return executeTypeR(instruction, sys)
        }
    
        if (instruction.typing.type === "j") {
            // return executeTypeJ(instruction, sys)
        }

        //if ()
    }
}

Object.prototype.Branch = (instruction, op) => {
    if (op === 'j') 
        sys.regs.pc = convertHexToDecimal(instruction.address)

    
}

export default sys;
