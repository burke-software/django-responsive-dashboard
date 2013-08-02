var ss_options = {
        enableDrag: false,
        gutterX: 20,
        gutterY: 20,
        paddingX: 20,
        paddingY: 20,
        align: "left"
    }

jQuery(document).ready(function($) {
    $container = $("#dashboard_container");
    $container.shapeshift(ss_options);
    $container.on("ss-rearranged", function(e, selected) {
        dashlet_id = $(selected).data('dashlet_id');
        $.post(
            'ajax_reposition/',
            {dashlet_id: dashlet_id, position: $(selected).index()},
            function(data){
                $('#save_status').html(data);
            }
        );
    });
});

function customize_dashboard(){
    ss_options.enableDrag = true;
    $('#dashboard_container').shapeshift(ss_options);
}
