// Update Cart
$(document).on('click', '.update-cart', function(e){
    e.preventDefault();
    var productid = $(this).data('index');
    $.ajax({
        type: 'POST',
        url: cartUpdateUrl, // This variable should be set to the correct URL in your template
        data: {
            product_id: $(this).data('index'),
            product_qty: $('#select' + productid + ' option:selected').text(),
            csrfmiddlewaretoken: csrfToken, // This variable should be set to the CSRF token in your template
            action: 'post'
        },
        success: function(json){
            location.reload();
        },
        error: function(xhr, errmsg, err){
            console.log(errmsg);
        }
    });
});

// Delete Item From Cart
$(document).on('click', '.delete-product', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: cartDeleteUrl, // This variable should be set to the correct URL in your template
        data: {
            product_id: $(this).data('index'),
            csrfmiddlewaretoken: csrfToken, // This variable should be set to the CSRF token in your template
            action: 'post'
        },
        success: function(json){
            location.reload();
        },
        error: function(xhr, errmsg, err){
            console.log(errmsg);
        }
    });
});