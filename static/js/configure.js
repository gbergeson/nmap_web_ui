$(document).ready(function(){

    function add_remove_option(opt, add_is_true) {
        // Add a space to maintain readability in command line
        opt += ' ';

        // Get options text, add or remove the option based on add_is_true param
        options = $('#options').text();
        options = add_is_true ? options + opt : options.replace(opt, '');
        $('#options').text(options);
    }

    $('#targets_specify').keyup(function(){
        $('#targets').text($(this).val());
    });

    $('#sL_option').click(function(){
        add_remove_option('-sL', $(this).prop('checked'));
    });

    $('#sn_option').click(function(){
        add_remove_option('-sn', $(this).prop('checked'));
    });

    $('#Pn_option').click(function(){
        add_remove_option('-Pn', $(this).prop('checked'));
    });

    $('#sV_option').click(function(){
        add_remove_option('-sV', $(this).prop('checked'));
    });

    $('#O_option').click(function(){
        add_remove_option('-O', $(this).prop('checked'));
    });

    $('#A_option').click(function(){
        add_remove_option('-A', $(this).prop('checked'));
    });
});