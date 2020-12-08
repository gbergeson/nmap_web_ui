$('#filter-box').click(function() {
    if($('#filter-box .allhosts').is(':checked')) {
        $('.col-10 .allhosts').prop('checked', true)
    } else if($('#filter-box .livehosts').is(':checked')) {
        $('.col-10 .livehosts').prop('checked', true)
    }

    if($('#filter-box .alloses').is(':checked')) {
        $('.col-10 .alloses').prop('checked', true)
    } else if($('#filter-box .windowshosts').is(':checked')) {
        $('.col-10 .windowshosts').prop('checked', true)
    } else if($('#filter-box .linuxhosts').is(':checked')) {
        $('.col-10 .linuxhosts').prop('checked', true)
    }
});