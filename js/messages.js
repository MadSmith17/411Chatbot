document.addEventListener("DOMContentLoaded", (event) => {
  const form = document.getElementById("messageForm");
  const input = document.getElementById("messageInput");
  const chatBox = document.getElementById("chatBox");

  if (!form || !input || !chatBox) {
    console.error("One or more elements are missing:", {
      form,
      input,
      chatBox,
    });
    return;
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    console.log("Form submitted");

    const message = input.value.trim();
    if (message) {
      console.log("User message:", message);
      addMessageToChatBox("User", message);
      input.value = "";
      setTimeout(() => {
        console.log("Bot response:", ` ${message}`);
        addMessageToChatBox("Bot", ` ${message}`);
      }, 500);
    }
  });

  function addMessageToChatBox(sender, message) {
    console.log("Adding message to chat box:", { sender, message });
    const messageElement = document.createElement("div");
    messageElement.classList.add("message");
    messageElement.classList.add("bubble");
    messageElement.innerHTML = `<strong>${sender}: </strong> ${message}`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
  }
});
