const add = document.getElementById("add");
const remove = document.getElementById("remove");
const quantity = document.getElementById("quantity");

add.addEventListener("click", () => {
    quantity.value = parseInt(quantity.value) + 1;
});

remove.addEventListener("click", () => {
    if (parseInt(quantity.value) !== 1) {
        quantity.value = parseInt(quantity.value) - 1;
    }
});