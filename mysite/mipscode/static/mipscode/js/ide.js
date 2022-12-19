window.onload = () => {
    const [input] = document.querySelectorAll(".codemirror-textarea");
    const editor = CodeMirror.fromTextArea(input, { lineNumbers: true, mode: { name: "gas", architecture: "ARMv6" } });
}
