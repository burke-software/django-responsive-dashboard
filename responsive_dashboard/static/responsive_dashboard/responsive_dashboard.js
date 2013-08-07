var ss_options = {
        enableDrag: false,
        gutterX: 20,
        gutterY: 20,
        paddingX: 20,
        paddingY: 20,
        align: "left",
        colWidth: 300,
        minColumns: 2,
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

function delete_dashlet(dashlet_id) {
    $.post(
        'ajax_delete/',
        {dashlet_id: dashlet_id},
        function(data){
            $('#save_status').html(data);
            $('#dashlet_'+dashlet_id).remove();
            $("#dashboard_container").trigger("ss-rearrange")
        }
    );
}

function customize_dashboard( element ){
    if ( $(element).data('is_customizing') == '1' ) {
        $(element).html('Customize Dashboard <img class="dashboard_gear" src="/static/responsive_dashboard/img/gear.svg"/>');
        $(element).data('is_customizing', '0');
        ss_options.enableDrag = false;
        $('#dashboard_container').shapeshift(ss_options);
        $('#dashlet_add_new').hide();
        $('.close_x').hide();
    } else {
        $(element).html('Stop Customizing <img class="dashboard_gear" src="/static/responsive_dashboard/img/gear.svg"/>');
        $(element).data('is_customizing', '1');
        ss_options.enableDrag = true;
        $('#dashboard_container').shapeshift(ss_options);
        $('#dashlet_add_new').show();
        $('.close_x').show();
    }
    $("#dashboard_container").trigger("ss-rearrange")
}
