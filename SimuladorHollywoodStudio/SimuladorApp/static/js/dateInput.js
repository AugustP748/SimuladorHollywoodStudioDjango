window.addEventListener("DOMContentLoaded", () => {
    const dateInput = document.getElementById('date-input');
    const decrementButton = document.getElementById('decrement-button');
    const incrementButton = document.getElementById('increment-button');

    if (dateInput.value === '01/07/2023') {
        decrementButton.disabled = true;
      }
    
    decrementButton.addEventListener('click', () => {
        decreaseDate();
    });

    incrementButton.addEventListener('click', () => {  
        increaseDate();
    });

    function decreaseDate() {
        let currentDate = new Date(dateInput.value);
        currentDate.setDate(currentDate.getDate() - 1)
        dateInput.value = formatDate(currentDate);
    }

    function increaseDate() {
        let currentDate = new Date(dateInput.value);
        currentDate.setDate(currentDate.getDate() + 1);
        dateInput.value = formatDate(currentDate);
    }

    function formatDate(date) {
        let day = String(date.getDate()).padStart(2, '0');
        let month = String(date.getMonth() + 1).padStart(2, '0');
        let year = date.getFullYear();
        return `${month}/${day}/${year}`;
    }


    // Agregar un escuchador de evento para verificar cada vez que el valor cambie
    dateInput.addEventListener('input', () => {
        if (dateInput.value === '07/01/2023') {
            decrementButton.disabled = true;
        } else {
            decrementButton.disabled = false;
        }
    });

}); 


