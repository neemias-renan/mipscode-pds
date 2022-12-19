export default {
    j: {
        op: '000010',
        // target: '', // coded address of label
        does: (instruction, sys) => sys.Jump(instruction, 'j') // (label) => { //a full 32-bit jump target address }
    },
    jal: {
        op: '000011',
        // target: '', // coded address of label
        does: null // (label) => { //a full 32-bit jump target address }
    }
}
