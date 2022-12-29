// const addressArea = document.querySelector('.address')

export function mountView(instructions) {
    // instructions.forEach(instruction => {
    //     const line = createLine(instruction.address, instruction.code)
    //     // addressArea.appendChild(line)
    // });
}

function createLine(a, b) {
    const div = document.createElement('div')
    div.classList.add('address-line')
    const spanA = document.createElement('span')
    const spanB = document.createElement('span')
    spanA.innerText = a
    spanB.innerText = b
    div.appendChild(spanA)
    div.appendChild(spanB)
    return div
}

