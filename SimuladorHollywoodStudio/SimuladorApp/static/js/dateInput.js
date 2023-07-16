
window.addEventListener("load", () => {
    const dateInput = document.getElementById('date-input');
    dateInput.value = '2023-07-01';
});

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
        verifyDate(currentDate);
    }

    function formatDate(date) {
        let day = String(date.getDate()).padStart(2, '0');
        let month = String(date.getMonth() + 1).padStart(2, '0');
        let year = date.getFullYear();
        return `-${day}/${month}/${year}`;
    }

    function verifyDate(date) {
        console.log(date);
        if (date == '01/07/2023') {
            decrementButton.disabled = true;
        } else {
            decrementButton.disabled = false;
        }

    }


}); 


