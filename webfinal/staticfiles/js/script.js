// DOM - Document Object Model
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); 
            mostrar_validacion_rut(event); 
        });
    }

    
    const categoryDropdown = document.getElementById('categoryDropdown');
    if (categoryDropdown) {
        categoryDropdown.addEventListener('change', function() {
            const categoryId = this.value;
            const currentUrl = new URL(window.location.href);
            currentUrl.searchParams.set('category', categoryId);
            window.location.href = currentUrl.href;
        });
    }
});


function validar_rut(rut) {
    rut = rut.replace(/\./g, '').replace(/-/g, '');
    const body = rut.slice(0, -1);
    let checkDigit = rut.slice(-1).toUpperCase();
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
    
    return checkDigit === expectedCheckDigit;
}


function validar_emails() {
    const email1 = document.getElementById('id_email').value;
    const email2 = document.getElementById('id_confirm_email').value;
    return email1 === email2;
}


function showModal(title, message) {
    const modalTitle = document.getElementById('exampleModalLabel');
    const modalBody = document.getElementById('modal-body-content');

    if (modalTitle && modalBody) {
        modalTitle.textContent = title;
        modalBody.textContent = message;
        const myModal = new bootstrap.Modal(document.getElementById('myModal'));
        myModal.show();
    } else {
        console.error('Modal elements not found in the DOM.');
    }
}

function mostrar_validacion_rut(event) {
    event.preventDefault(); 

    const rutInput = document.getElementById('id_rut').value;
    const rutValido = validar_rut(rutInput);
    const emailValido = validar_emails();

    if (!rutValido) {
        showModal('Error', 'RUT inválido');
    } else if (!emailValido) {
        showModal('Error', 'Los correos electrónicos no coinciden');
    } else {
        
        
        setTimeout(() => {
            document.getElementById('form').submit();
        }, 2000);
    }
}
