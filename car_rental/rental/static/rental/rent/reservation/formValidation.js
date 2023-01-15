var numberRegex = /^\d{9}$/;

function validateReservation() {
    var form = document.getElementById("reservationForm");
    var errorText = "";
    var valid = true;

    // Check if the user has entered a date
    if (form.name.value == "") {
        errorText += "Please enter a name. <br>";
        valid = false;
        document.getElementById("name").style.borderColor = "red";
    }

    // Check if the user has entered a time
    if (form.surname.value == "") {
        errorText += "Please enter a surname. <br>";
        valid = false;
        document.getElementById("surname").style.borderColor = "red";
    }

    // Check if the user has entered a duration
    if (form.phone.value == "" || !numberRegex.test(form.phone.value)) {
        errorText += "Please enter a phone number. <br>";
        valid = false;
        document.getElementById("phone").style.borderColor = "red";
    }

    if(!dateValid(form)) {
        errorText += "Start date cannot be after end date! <br>";
        valid = false;
    }

    // Display the error message
    document.getElementById('error').innerHTML = errorText;

    // Return the validation result
    return valid;
}

function dateValid(form) {
    var endDate = Date.parse(form.id_end_date_day.value + "-" +
        form.id_end_date_month.value + "-" + form.id_end_date_year.value);

    var startDate = Date.parse(form.id_start_date_day.value + "-" +
        form.id_start_date_month.value + "-" + form.id_start_date_year.value);

    if (startDate > endDate) {
        return false;
    }
    return true;
}