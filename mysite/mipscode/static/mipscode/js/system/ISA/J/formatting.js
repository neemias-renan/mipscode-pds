import * as tools from "../toolkit.js";
import instructions from "./instructions.js";

const formatAddress = {
    op: '000000',
    target: '00000000000000000000000000'
};

export function organize(arr) {
    formatAddress.op = arr[0];
    formatAddress.target = arr[1];
    return Object.values(formatAddress).join('');
}

export function formatArrayElements(arr) {
    const cleanedElements = arr.map((element, index) => { // adaptar pro tipo j
        if (index === 0) return instructions[element].function;
        else return tools.convertDecimalToBin(
            Number(tools.cleanElement(element))
        );
    });

    return tools.completeElementsLength(cleanedElements);
}
