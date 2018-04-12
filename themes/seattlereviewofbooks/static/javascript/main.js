jQuery(document).ready(function() {
    //HIDES TOO MANY BOOKS AND ALLOWS THEM TO BE SHOWN
    jQuery("abbr.timeago").timeago();
    $('.more-books').click(function() {
        event.preventDefault();
        var text = $(this).text();
        $(this).addClass('')
        $('.review-card .book + li + li + li').toggle('fast', function() {
            //get the text, find "show" and change it to "hide"
        });
        if (text.indexOf("show") >= 0) {
            text = text.replace('show', 'hide');
        } else {
            text = text.replace('hide', 'show');
        }
        $(this).text(text);
    });
    //MOBILE NAV EXPANSION
    $('.nav-expand').click(function() {
        $('.navbar-nav').toggle('swing');
        $(this).toggleClass('glyphicon-menu-down');
        $(this).toggleClass('glyphicon-menu-up')
    });
    //PAGINATION TWEAK
    $('.pagination-elipsis').click(function(e) {
            e.preventDefault();
        })
        //FORM MAILER AJAX HANDLER
    $(function() {
        var form = $('#ajax-contact');
        var formMessages = $('#form-messages');
        // Set up an event listener for the contact form.
        $(form).submit(function(e) {
            // Stop the browser from submitting the form.
            e.preventDefault();
            // Serialize the form data.
            var formData = $(form).serialize();
            // Submit the form using AJAX.
            $.ajax({
                type: 'POST',
                url: $(form).attr('action'),
                data: formData
            }).done(function(response) {
                // Make sure that the formMessages div has the 'success' class.
                $(formMessages).removeClass('error');
                $(formMessages).addClass('success');
                // Set the message text.
                $(formMessages).text(response);
                // Clear the form.
                $('#name').val('');
                $('#email').val('');
                $('#message').val('');
            }).fail(function(data) {
                // Make sure that the formMessages div has the 'error' class.
                $(formMessages).removeClass('success');
                $(formMessages).addClass('error');
                // Set the message text.
                if (data.responseText !== '') {
                    $(formMessages).text(data.responseText);
                } else {
                    $(formMessages).text('Oh snap, we\'re really sorry -- an error occured and your message could not be sent.');
                }
            });
        });
    });
    //Logic for selecting the correct rows on the sales page
    $('.reserved-checkbox').click(function() {
        $('tr.reserved').toggle();
    })
    $('.booked-checkbox').click(function() {
        $('tr.booked').toggle();
    })
    var dates = [];
    var rowcount = 0;
    var sellamount = 0;
    $('.row-select').click(function(e) {
        var row = $(this).parent().parent();
        var next = row.next();
        var prev = row.prev();
        var nextbox = next.find('input');
        var prevbox = prev.find('input');
        // if (rowcount == 4 && !row.hasClass('selected')) {
        //     alert('We\'re limiting sponsorships to four weeks total right now. Thank you for understanding');
        //     return false;
        //     e.preventDefault();
        // }
        if (row.hasClass('selected')) {
            rowcount--;
            var i = dates.indexOf($(this).attr('value'));
            dates.splice(i, 1);
            $('input#sponsored-weeks').attr('value', dates.toString());       
            sellamount -= Number( $(this).parent().next().next().next().attr('data-price') );
            //sellamount -= row('td .price').attr('data-price');            
            //the row is selected, so we are undoing
            // if (prev.hasClass('disabled')) {
            //     prevbox.attr('disabled', false);
            //     prev.removeClass('disabled');
            // }
            // if (next.hasClass('disabled')) {
            //     nextbox.attr('disabled', false);
            //     next.removeClass('disabled');
            // }
        } else {
            rowcount++;
            dates.push($(this).attr('value'));
            $('input#sponsored-weeks').attr('value', dates.toString());
           // alert( $(this).parent().next().next().next().attr('data-price'));            
            sellamount += Number( $(this).parent().next().next().next().attr('data-price') );            
            //the row is not selected, so we are doing
            // if (!prevbox.is('[disabled]')) {
            //     prevbox.attr('disabled', true);
            //     prev.addClass('disabled');
            // }
            // if (!nextbox.is('[disabled]')) {
            //     nextbox.attr('disabled', true);
            //     next.addClass('disabled');
            // }
        }
        row.toggleClass('selected');
        $('.total-amount').text(sellamount);
        if (rowcount == 0) {
            $('.payment-method').hide('fast');
            $('.payment-method-header').addClass('disabled');
        } else {
            $('.payment-method').show('fast');
            $('.payment-method-header').removeClass('disabled');
        }
    })
    $('.paybycheck').click(function() {
        if ($('.payonline').is('[disabled]')) {
            $('.payonline').attr('disabled', false);
            $('.payment-info').hide('fast');
            $('.payment-info-header').addClass('disabled');
        } else {
            $('.payonline').attr('disabled', true);
            $('.payment-info').show('fast');
            $('.payment-info-header').removeClass('disabled');
        }
        $('.payonline').parent().toggleClass('disabled');
    })
    $('.payonline').click(function() {
        if ($('.paybycheck').is('[disabled]')) {
            $('.paybycheck').attr('disabled', false);
            $('.payment-info').hide('fast');
            $('.payment-info-header').addClass('disabled');
        } else {
            $('.paybycheck').attr('disabled', true);
            $('.payment-info').show('fast');
            $('.payment-info-header').removeClass('disabled');
        }
        $('.paybycheck').parent().toggleClass('disabled');
    })
    $('input.terms').click(function() {
       if( $('.book-form-submit').is('[disabled]') ){
             $('.book-form-submit').attr('disabled', false);
       }else{
            $('.book-form-submit').attr('disabled', true);
       }
    })
    $('.book-form-submit').click(function(){
        $('#ajax-contact').hide('fast');
    })
    $(window).scroll(function() {
        if ( $(window).width() > 768 ) {            
            if ($(window).scrollTop() + $(window).height() > $(document).height() - 344) {
                $('.sponsor').addClass('fixed-bottom');
                $('.sponsor').css('margin-top', $(document).height() - (600 + $('.sponsor').height()));
            } else {
                $('.sponsor').removeClass('fixed-bottom');
                $('.sponsor').css('margin-top', 'inherit')
            }
        } else {
            return false;
        }
    });

//INITIALIZE TWITTER
twttr.widgets.load( $('.container'));

});