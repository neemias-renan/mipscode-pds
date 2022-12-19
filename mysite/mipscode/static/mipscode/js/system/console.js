const dataInAndOut = document.querySelector('.console')

export const dataOut = (data, type, msg) => {
    if (type === 'error') {}

    if (type === 'value') {
        const output = document.createElement('div')
        // const value = document.createElement('p')
        // const message = document.createElement('p')

        // value.innerText = data
        // message.innerText = msg

        // output.appendChild(value)
        // output.appendChild(message)

        output.innerHTML = `<p>${data}</p> <br></p>`

        //console.log(output);

        dataInAndOut.appendChild(output)
    }

    if (type === 'exit') {
        const output = document.createElement('div')
        output.innerHTML = `<br> <p>--- ${msg} ---</p>`
        dataInAndOut.appendChild(output)
    }

    if (type === 'log') {}

    if (type === 'comment') {}
}

export const dataIn = () => {}

export const clean = () => {
    dataInAndOut.innerHTML = ''
}
