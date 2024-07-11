// Wait for DOM content to fully load
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form');
    if (form) {
        form.addEventListener('submit', mostrar_validacion_rut);
    } 
});

// Validar Rut
function validar_rut(rut) {
    // Limpiar el rut (sacar puntos y guiones)
    rut = rut.replace(/\./g, '').replace(/-/g, '');
    
    // Separar digito verificador
    const body = rut.slice(0, -1);
    let checkDigit = rut.slice(-1).toUpperCase();
    
    // Calcular la cantidad de digitos esperada
    let sum = 0;
    let multiplier = 2;
    
    for (let i = body.length - 1; i >= 0; i--) {
        sum += parseInt(body[i]) * multiplier;
        multiplier = multiplier === 7 ? 2 : multiplier + 1;
    }
    
    const remainder = sum % 11;
    let expectedCheckDigit = 11 - remainder;
    
    if (expectedCheckDigit === 11) {
        expectedCheckDigit = '0';
    } else if (expectedCheckDigit === 10) {
        expectedCheckDigit = 'K';
    } else {
        expectedCheckDigit = expectedCheckDigit.toString();
    }
    
    // Validar
    return checkDigit === expectedCheckDigit;
}

// Validar email
function validar_emails() {
    const email1 = document.getElementById('id_email').value;
    const email2 = document.getElementById('id_confirm_email').value;
    return email1 === email2;
}

// Mostrar modal
function showModal(title, message) {
    const modalTitle = document.querySelector('.modal-title');
    const modalBody = document.getElementById('modalBody');

    modalTitle.textContent = title;
    modalBody.textContent = message;

    // Show the modal
    const modal = new bootstrap.Modal(document.getElementById('modal_submit'));
    modal.show();
}

function mostrar_validacion_rut(event) {
    event.preventDefault(); // Prevent form submission

    const rutInput = document.getElementById('id_id_number').value;
    const rutValido = validar_rut(rutInput);
    const emailValido = validar_emails();

    if (!rutValido) {
        showModal('Error', 'Rut inválido');
    } else if (!emailValido) {
        showModal('Error', 'Los correos electrónicos no coinciden');
    } else {
        showModal('Correcto!', 'Registro completado exitosamente');
        // Retrasar envío para mostrar el modal
        setTimeout(() => {
            document.getElementById('form').submit();
        }, 2000);
    }
}

// Function sitio en construcción
function mostrarAlerta() {
    alert("SITIO EN CONSTRUCCIÓN!!!");
}
