const modal = document.querySelector(".help-modal-container")
const button = document.querySelector(".modal-button")

window.addEventListener("keyup", (e) => {
    if (e.key === "h") {
        modal.classList.toggle("hidden")
    } else if (e.key === "Escape") {
        modal.classList.add("hidden")
    }
})

button.addEventListener("click", () => {
    modal.classList.add("hidden")
})