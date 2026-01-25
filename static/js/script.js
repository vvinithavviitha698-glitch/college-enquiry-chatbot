function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    // SAFETY CHECK
    if (!input || !chatBox) {
        console.error("HTML element not found");
        return;
    }

    const message = input.value.trim();
    if (message === "") return;

    // Show user message
    chatBox.innerHTML += `<div class="user">${message}</div>`;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        chatBox.innerHTML += `<div class="bot">${data.reply}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(err => {
        console.error(err);
        chatBox.innerHTML += `<div class="bot">Error occurred</div>`;
    });

    input.value = "";
}

