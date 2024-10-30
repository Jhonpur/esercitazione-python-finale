// Data di inizio del triathlon (modifica questo valore con la data reale)
const startDate = new Date("2025-06-10T09:00:00").getTime();

// Funzione per aggiornare il timer ogni secondo
const timerInterval = setInterval(() => {
    const now = new Date().getTime();
    const timeRemaining = startDate - now;

    if (timeRemaining > 0) {
        const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

        // Mostra il tempo rimanente
        document.getElementById("timer").innerHTML = 
            `Il triathlon inizia tra ${days} giorni, ${hours} ore, ${minutes} minuti e ${seconds} secondi`;
    } else {
        clearInterval(timerInterval);
        document.getElementById("timer").innerHTML = "Il triathlon è iniziato!";
    }
}, 0);