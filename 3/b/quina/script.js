const btn = document.querySelector("#btn");
const box = document.querySelector("#box");

btn.addEventListener("click", () => {
    const currentPosition = box.getBoundingClientRect();
    const newPosition = {
        top: currentPosition.top + 90,
        left: currentPosition.left + 16,
        bottom: currentPosition.bottom + 90,
        right: currentPosition.right + 16,
    };
    if (newPosition.right <= window.innerWidth && newPosition.bottom <= window.innerHeight)
        box.style.transform = `translate(${newPosition.left}px, ${newPosition.top}px)`;
});
