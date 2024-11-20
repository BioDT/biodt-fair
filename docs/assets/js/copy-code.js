document.addEventListener("DOMContentLoaded", function () {
    // Add copy button to each code block
    document.querySelectorAll("pre").forEach(function (codeBlock) {
        // Create copy button
        var copyButton = document.createElement("button");
        copyButton.className = "copy-code-button";
        copyButton.type = "button";
        copyButton.innerText = "Copy";

        // Add button to code block
        codeBlock.style.position = "relative";
        codeBlock.insertBefore(copyButton, codeBlock.firstChild);

        // Add click event
        copyButton.addEventListener("click", function () {
            var code = codeBlock.querySelector("code");
            var text = code ? code.innerText : codeBlock.innerText;

            // Copy text
            navigator.clipboard
                .writeText(text)
                .then(function () {
                    // Visual feedback
                    copyButton.innerText = "Copied!";
                    setTimeout(function () {
                        copyButton.innerText = "Copy";
                    }, 2000);
                })
                .catch(function (error) {
                    console.error("Failed to copy: ", error);
                });
        });
    });
});
